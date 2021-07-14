import subprocess
import re
import logging
from celery import shared_task
from .models import Image
import time
import json
import requests
from devops_backend.settings import IMAGE_PUSH_HOST, DIR_PATH
from devops_backend.celery import app as celery_app
from utils.send_email import send_mail


def image_pull_cmd(image_url):

    cmd = "docker pull " + image_url
    return cmd


def docker_save_cmd(image_name, image_url, dir_path):

    cmd = "docker save -o " + dir_path + image_name  + " " + image_url
    return cmd


def get_scp_cmd(image_name, host, dir_path):
    cmd = "scp " + dir_path + image_name  + " " + host + ":/" + dir_path
    return cmd

def get_push_url(image_push_host):
    url = "http://" + image_push_host + "/"
    return url


def shell_command(cmd):
    res = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    res.wait()
    result = res.communicate()
    return result


# pull image
def download_image(image_url):

    cmd = image_pull_cmd(image_url)
    result = shell_command(cmd)
    logging.info("pull image: {}----{}".format(result[0].decode(), image_url))
    str_t_sec = str(int(round(time.time() * 1000)))
    image_name = str_t_sec + ".tar"
    cmd = docker_save_cmd(image_name, image_url, DIR_PATH)
    subprocess.call(cmd, shell=True)
    cmd = get_scp_cmd(image_name, IMAGE_PUSH_HOST, DIR_PATH)
    subprocess.call(cmd, shell=True)
    data = {"image_url": image_url, "image_tar_name": image_name}
    json_data = json.dumps(data)
    url = get_push_url(IMAGE_PUSH_HOST)
    r = requests.post(url=url, json=json_data)
    if r.status_code == 200:
       pass
    else:
       return False
    if re.findall("not found", result[0].decode()):
        logging.error("image not found: {}---{}".format(result[0].decode(), image_url))
        return False
    return True

@shared_task
def sync_image(image_url, id):

    download_image_res = download_image(image_url)
    if download_image_res:
        obj = Image.objects.get(pk=id)
        obj.status = 'success'
        obj.save()
        commit_time = obj.commit_time
        commit_id = obj.commit_id
        owner = obj.owner
        message = """<html><body><a href="http://devops.eig.yunpan.com/images/list">镜像构建成功、同步到瑞云环境成功!请前往devops平台查看http://devops.eig.yunpan.com/images/list</a>
                     <p>镜像地址: {}</p>
                     <p>代码提交者: {}</p>
                     <p>commit_id: {}</p>
                     <p>提交时间: {}</p></body></html>
                    """.format(image_url, owner, commit_id, commit_time)
        send_mail(message, image_url)
    else:
        obj = Image.objects.get(pk=id)
        obj.status = 'failed'
        obj.save()
        send_mail('<html><body><a href="http://devops.eig.yunpan.com/images/list">镜像build成功,镜像地址为: {}, 同步到瑞云环境失败!</a></body></html>'.format(image_url))
    return obj.image_name, obj.status

@shared_task(bind=True)
def auto_sc(self):
    try:
        time.sleep(20)
        logging.info("sc test")
    except Exception as e:
        self.retry(exc=e, countdown=3)

