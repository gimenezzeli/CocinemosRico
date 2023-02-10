from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path

from users.views import register, update_user, LoginView

urlpatterns=[
    path('login/', LoginView, name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html')),
    path('signup/', register, name='register'),
    path('update/', update_user, name='update_user'),
]