from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import json
import paramiko
# 解决前端post请求 csrf问题
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def testapi(request):
    global true
    global false
    false = False
    true = True
    if request.method == "GET":
        resp = {'message': "error"}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    else:
        print(request.POST)
        print(request.body)
        str1 = str(request.body, encoding="utf-8")
        data = eval(str1)
        print(data)
        resp = {'ip': data['ip'], 'account': data['account'], 'password': data['password']}
        if ssh_success(data['ip'], 22, data['account'], data['password']):
            return HttpResponse(True)
        else:
            return HttpResponse(False)


def ssh_success(ip, ssh_port, ssh_username, ssh_password):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        client.connect(hostname=ip, port=ssh_port, username=ssh_username, password=ssh_password, timeout=10,
                       look_for_keys=False, allow_agent=False)
        return True
    except Exception as err:
        print(err)
        return False
    finally:
        client.close()
