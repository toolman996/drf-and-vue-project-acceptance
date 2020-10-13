from django.urls import path

from home import views

urlpatterns=[
    path('bancom/',views.MyBanner.as_view()),
    path('navcom/',views.MyNavbarShow.as_view()),
]