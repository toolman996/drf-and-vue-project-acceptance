from django.db import models


class BaseModel(models.Model):
    """基础表"""
    is_show = models.BooleanField(default=False, verbose_name="是否展示")
    orders = models.IntegerField(default=1, verbose_name="排序")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    update_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")

    class Meta:
        abstract = True


class Banner(models.Model):
    """轮播图模型"""
    img = models.ImageField(upload_to='banner', max_length=255, verbose_name="轮播图图片",null=True)
    title = models.CharField(max_length=200, verbose_name="标题")
    link = models.CharField(max_length=400, verbose_name="图片链接")
    is_show = models.BooleanField(default=False, verbose_name="是否展示图片")
    orders = models.IntegerField(default=1, verbose_name="排序")
    is_delete = models.BooleanField(default=False, verbose_name="是否删除")

    class Meta:
        db_table = "tb_banner"
        verbose_name = "轮播图"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class Navber(BaseModel):
    """导航栏"""
    POSITION_OPTION = (
        (1, "顶部导航"),
        (2, "底部导航"),
    )

    title = models.CharField(max_length=200, verbose_name="标题")
    link = models.CharField(max_length=400, verbose_name="图片链接")
    position = models.IntegerField(choices=POSITION_OPTION, default=1)
    is_site = models.BooleanField(default=False, verbose_name="是否是外部网址")

    class Meta:
        db_table = "tb_navber"
        verbose_name = "导航栏"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title