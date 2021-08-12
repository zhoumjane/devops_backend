# -*- coding: utf-8 -*-
from django.urls import path
from utils.tools.channel import websocket


websocket_urlpatterns = [
    path('webssh/', websocket.WebSSH),
]

