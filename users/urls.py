from django.urls import path
from users import views


urlpatterns = [
    path(
        route='signup/',
        view=views.UsersSignUpView.as_view(),
        name='signup'
    ),
    path(
        route='login/',
        view=views.UsersLoginView.as_view(),
        name='login'
    )
]
