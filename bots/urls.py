from django.urls import path
from bots import views


urlpatterns = [
    path(
        route='search/<str:room_id>/<str:stock>/',
        view=views.search,
        name='bot_search'
    )
]
