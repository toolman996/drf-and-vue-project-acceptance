from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from user import views

urlpatterns=[
    path('login/',obtain_jwt_token),
    path('captcha/',views.Captcha.as_view()),
    path('register/',views.Register.as_view()),
    path('phone/<str:phone_id>',views.CheckPhoneId.as_view()),
    path('send/<str:mobile>',views.SmsAPIView.as_view()),
    path('get_sms/<str:mobile>',views.SendLogin.as_view()),
    path('sms_login/',views.SmsLogin.as_view({'post': 'sms_login'})),
    path('check_user/<str:phone_id>',views.SmsLoginCheckPhoneId.as_view()),
]