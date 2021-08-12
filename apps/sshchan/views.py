from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, HttpResponse
from utils.tools.tools import unique
from devops_backend.settings import TMP_DIR
from rest_framework import viewsets, filters, mixins, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from servers.models import Server

import os


# def index(request):
#     return render(request, 'index.html')
class IndexViewSet(viewsets.ViewSet, mixins.ListModelMixin):

    permission_classes = (IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        try:
            ip_addr = self.request.query_params['ip']
        except:
            return Response({"permission": False}, status=status.HTTP_403_FORBIDDEN)
        permission_str = 'servers.login_' + ip_addr
        if not (self.request.user.has_perm('servers.login_server') or self.request.user.has_perm(permission_str)):
            return Response({"permission": False}, status=status.HTTP_403_FORBIDDEN)
        try:
            print(ip_addr)
            Server.objects.filter(ip=ip_addr)
        except Exception as e:
            return Response({"permission": False}, status=status.HTTP_400_BAD_REQUEST)
        try:
            port = self.request.query_params['port']
        except Exception as e:
            port = '22'
        try:
            user = self.request.query_params['user']
        except Exception as e:
            user = 'root'
        content = {
            'host': ip_addr,
            'port': port,
            'user': user
        }
        return render(request, 'index.html', content)

def upload_ssh_key(request):
    if request.method == 'POST':
        pkey = request.FILES.get('pkey')
        ssh_key = pkey.read().decode('utf-8')

        while True:
            filename = unique()
            ssh_key_path = os.path.join(TMP_DIR, filename)
            if not os.path.isfile(ssh_key_path):
                with open(ssh_key_path, 'w+') as f:
                    f.write(ssh_key)
                break
            else:
                continue
        return HttpResponse(filename)