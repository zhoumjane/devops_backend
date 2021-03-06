# Generated by Django 2.2.1 on 2021-06-09 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.CharField(db_index=True, help_text='镜像名', max_length=128, verbose_name='镜像名')),
                ('commit_id', models.CharField(db_index=True, help_text='commit_id', max_length=32, verbose_name='commit_id')),
                ('owner', models.CharField(db_index=True, help_text='代码提交者', max_length=32, verbose_name='代码提交者')),
                ('commit_time', models.DateTimeField(auto_now=True, help_text='上传时间', verbose_name='上传时间')),
            ],
            options={
                'ordering': ['-commit_time'],
            },
        ),
    ]
