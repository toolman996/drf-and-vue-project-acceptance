# 定义了jwt的返回值
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q

from user.models import MyUser
from user.serializers import UserSerializers


def jwt_response(token, user=None, request=None):
    # print(user.password,type(user.password))
    return {
        'token': token,
        'username': user.username,
        # 'request':{'request':request}
    }

# def jwt_response(token, user=None, request=None):
#     return {
#         'token': token,
#         'user': UserSerializers(user, context={'request': request}).data
#     }

def fun(args):
    try:
        result = MyUser.objects.filter(Q(username=args) | Q(phone=args) | Q(email=args)).first()

    except MyUser.DoesNotExist:
        return None
    else:
        return result

#多条件查询自定义认证方式
class UserAuth(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        #多条件查询满足其一就可
        bt=fun(username)
        if bt and bt.check_password(password) and bt.is_authenticated:
            return bt
        else:
            return None


