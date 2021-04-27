from django.shortcuts import HttpResponse
from django.contrib.auth.decorators import login_required
from requests import get, HTTPError
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import logging

logger = logging.getLogger(__name__)


@login_required
def search(request, room_id, stock):
    try:
        api_response = get('https://stooq.com/q/l/?s={}&f=sd2t2ohlcv&h&e=csv'.format(stock))
        symbol, stock_price = parse_csv(api_response.content)
        message = "{} quote is ${:.2f} per share".format(symbol, float(stock_price))
    except HTTPError:
        message = "Connection with FinApi Failed. Please try later."
    except ValueError:
        message = "Stock: {} does not exist or FinApi could not get a correct value.".format(stock)
    except Exception as e:
        message = "There was an error with FinApi. Please try later."
        logger.error(str(e))

    channel_layer = get_channel_layer()
    async_to_sync(channel_layer.group_send)(
        'chat_{}'.format(room_id),
        {"type": "chat_message",
         "message": message,
         "user": "FinBot"},
    )
    return HttpResponse("OK")


def parse_csv(text):
    data = text.decode('utf-8').splitlines()
    lines = [row.split(',') for row in data]
    price_idx = lines[0].index('Close')
    symbol_idx = lines[0].index('Symbol')
    return lines[1][symbol_idx], lines[1][price_idx]
