# Generated by Django 2.2 on 2021-06-23 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servers', '0004_auto_20210622_1127'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='server',
            options={'ordering': ['-last_check'], 'permissions': (('login_server', '登录服务器'), ('login_10.5.42.117', '登录10.5.42.117'), ('login_10.5.42.118', '登录10.5.42.118'), ('login_10.5.42.120', '登录10.5.42.120'), ('login_10.5.42.121', '登录10.5.42.121'), ('login_172.20.23.147', '登录172.20.23.147'), ('login_10.151.5.151', '登录10.151.5.151'), ('login_10.198.22.191', '登录10.198.22.191'), ('login_172.20.23.217', '登录172.20.23.217'), ('login_172.20.23.218', '登录172.20.23.218'), ('login_10.9.244.231', '登录10.9.244.231'), ('login_172.20.1.241', '登录172.20.1.241'), ('login_10.112.63.39', '登录10.112.63.39'), ('login_172.20.23.43', '登录172.20.23.43'), ('login_172.20.52.46', '登录172.20.52.46'), ('login_10.9.244.54', '登录10.9.244.54'), ('login_10.9.244.56', '登录10.9.244.56'), ('login_10.9.244.57', '登录10.9.244.57'), ('login_172.20.52.55', '登录172.20.52.55'), ('login_10.198.22.83', '登录10.198.22.83'))},
        ),
    ]
