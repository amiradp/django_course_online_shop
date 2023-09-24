from django.urls import path

from . import views


urlpatterns = [
    path('aboutus/', views.AboutUsPageView.as_view(), name='aboutus'),
    path('contactus/', views.ContactUsView.as_view(), name='contactus'),
]
