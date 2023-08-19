from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.signupUpView.as_view(), name='signup'),
]