from django.db import models


class Image(models.Model):

    image_name = models.CharField('镜像名', max_length=128, db_index=True, help_text=u'镜像名')
    commit_id = models.CharField('commit_id', max_length=32, db_index=True, help_text=u'commit_id')
    owner = models.CharField('代码提交者', max_length=32, db_index=True, help_text=u'代码提交者')
    commit_time = models.DateTimeField("上传时间", auto_now=True, help_text=u'上传时间')
    status_choices = (
        ("success", u'成功'),
        ("failed", u'失败'),
        ("uploading", u'上传中')
    )
    status = models.CharField(u'状态', max_length=10, default='uploading', choices=status_choices, help_text=u'状态')
    record = models.FileField(upload_to='images/%Y/%m/%d/%H', verbose_name=u'构建详情',
                                       help_text=u'构建详情', null=True, blank=True)
    url = models.URLField(u'gitlab代码仓库地址', max_length=64, help_text=u'gitlab代码仓库地址', null=True, blank=True)
    branch = models.CharField(u'分支名', max_length=32, help_text=u'分支名', null=True, blank=True)

    def __str__(self):
        return self.image_name

    class Meta:
        ordering = ["-commit_time"]