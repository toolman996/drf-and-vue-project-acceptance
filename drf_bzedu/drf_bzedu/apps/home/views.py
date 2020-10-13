from django.shortcuts import render
from rest_framework.generics import ListAPIView

from home.models import Banner, Navber
from home.serializers import BannerModelSerializer, NavberModelSerializer


class MyBanner(ListAPIView):
    queryset = Banner.objects.filter(is_show=True,is_delete=False)
    serializer_class = BannerModelSerializer

# 导航栏类视图
class MyNavbarShow(ListAPIView):
    queryset = Navber.objects.filter(is_show=True,is_delete=False).order_by('-orders')
    serializer_class = NavberModelSerializer