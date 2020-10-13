from rest_framework.serializers import ModelSerializer

from user.models import MyUser


class UserSerializers(ModelSerializer):
    class Meta:
        model=MyUser
        fields=('username',)
