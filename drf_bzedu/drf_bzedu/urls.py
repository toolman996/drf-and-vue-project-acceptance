"""drf_bzedu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import path,re_path,include
from django.views.static import serve
#使用xadmin
import xadmin
from xadmin.plugins import xversion
xversion.register_models()

urlpatterns = [
    # 富文本编辑器的路由
    path("ckeditor/", include("ckeditor_uploader.urls")),
    path('xadmin/', xadmin.site.urls),
    path('home/', include('home.urls')),
    path('user/', include('user.urls')),
    path("course/", include("course.urls")),
    path("shoppingcart/", include("shoppingCart.urls")),
    path("order/", include("order.urls")),
    path("payoff/", include("payoff.urls")),
    re_path(r'media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}),
]
