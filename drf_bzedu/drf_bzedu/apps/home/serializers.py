from rest_framework.serializers import ModelSerializer

from home.models import Banner, Navber


#轮播图序列化
class BannerModelSerializer(ModelSerializer):
    class Meta:
        model=Banner
        fields=('img','link')

#导航栏序列化
class NavberModelSerializer(ModelSerializer):
    class Meta:
        model=Navber
        fields = ("title", 'link','position','is_site')