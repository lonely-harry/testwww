#coding:utf-8
import requests
import logging
import json
import pytest

class Testwww(object):
    logging.basicConfig(level=logging.INFO)
    url='https://testservice.tencloudnet.com/api.php'
    def test_login(self):
        d ={
            "username":"admin",
            "password":"angyunding"}
        r=requests.post(url=Testwww.url+'/Index/login',data=d)
        #logging.info(json.dumps(r.json(),indent=2,ensure_ascii=False))
        uid=r.json()["data"]["uid"]
        token=r.json()["data"]["token"]
        assert r.json()["message"] == "登录成功"
        print(uid,token)

    #def test_onepage(self):

