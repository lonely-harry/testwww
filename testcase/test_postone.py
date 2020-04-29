#coding:utf-8
import requests
import logging
import json
import pytest

class Testnew(object):
    logging.basicConfig(level=logging.INFO)
    def test_post(self):
        url='http://new1.tencloudnet.com/api.php'
        d ={
            "username":"admin",
            "password":"angyunding"}
        r=requests.post(url=url+'/Index/login',data=d)
        logging.info(json.dumps(r.json(),indent=2))

