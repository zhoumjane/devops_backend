from django.db import models
from django.contrib.auth.models import User


class Server(models.Model):

    ip = models.GenericIPAddressField('管理ip', max_length=15, db_index=True, help_text=u'IP地址')
    hostname = models.CharField('主机名', max_length=32, db_index=True, help_text=u'主机名')
    cpu = models.CharField("CPU", max_length=256, help_text=u'cpu型号')
    cpu_core = models.IntegerField(verbose_name=u"cpu核数", help_text=u'cpu核数')
    memory = models.CharField("内存", max_length=32, help_text=u'内存')
    disk = models.CharField('磁盘', max_length=200, help_text=u'磁盘')
    os = models.CharField("操作系统", max_length=50, help_text=u'系统版本')
    model_name = models.CharField(verbose_name="服务器型号", max_length=32, null=True, blank=True, help_text=u'服务器型号')
    rmt_card_ip = models.CharField("管理卡IP", max_length=15, db_index=True, null=True, blank=True, help_text=u'管理卡IP')
    idc = models.CharField(verbose_name="所在机房", max_length=32, null=True, blank=True, help_text=u'所在机房')
    cabinet = models.CharField(null=True, verbose_name="所在机柜", max_length=32, blank=True, help_text=u'所在机柜')
    cabinet_position = models.CharField("机柜内位置", null=True, max_length=20, help_text=u'机柜内位置')
    server_type_choices = (
                      ("Physical", u'物理机'),
                      ("Opencloud", u'opencloud'),
                      ("Ruiyun", u'瑞云'),
                      ("Aliyun", u'阿里云')
                      )
    server_type = models.CharField(u'服务器类型', max_length=32, default='Physical', choices=server_type_choices,
                                   help_text=u'服务器类型')
    last_check = models.DateTimeField("上次检测时间", auto_now=True, help_text=u'上次检测时间')
    remark = models.CharField("备注", max_length=200, null=True, help_text=u'备注')
    status_choices = (
                      ("disable", u'不可用'),
                      ("enable", u'可用')
                      )
    status = models.CharField(u'状态', max_length=10, default='enable', choices=status_choices, help_text=u'状态')
    owner = models.ManyToManyField(User, related_name='owner', verbose_name=u'服务器负责人', null=True, blank=True,
                                   help_text=u'服务器负责人')
    gpu_type = models.CharField(max_length=32, verbose_name=u'GPU类型', null=True, blank=True,
                                help_text=u'GPU类型')
    borrow = models.CharField(max_length=256, verbose_name=u'借用', null=True, blank=True, help_text=u'是否借用')

    project = models.CharField(max_length=256, verbose_name=u'项目/产品', null=True, blank=True, help_text=u'产品线')

    asset = models.CharField(max_length=256, verbose_name=u'资产号', null=True, blank=True, help_text=u'资产')

    zone = models.CharField(max_length=256, verbose_name=u'区域', null=True, blank=True, help_text=u'区域')

    last_time = models.DateTimeField('服务器到期时间', null=True, blank=True, help_text=u'服务器到期时间')

    def __str__(self):
        return self.ip

    class Meta:
        ordering = ["-last_check"]
