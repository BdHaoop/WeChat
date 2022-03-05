import time
import requests
import json
import math
import random
class WeChat:

    def __init__(self):
        self.CORPID = 'wwb3abceb034b00d03'  # 企业ID，在管理后台获取
        self.CORPSECRET = 'NPVo1df6HbRhOInn4UOyiklKaSsV02KVujia3ujPU18'  # 自建应用的Secret，每个自建应用里都有单独的secret
        self.AGENTID = '1000002'  # 应用ID，在后台应用中获取
        self.TOUSER = "WeiJieGuang"  # 接收者用户名,多个用户用|分割@all
        self.TOKENS=""


    def get_access_token(self):
        #发起请求,获取access_token
        res = requests.get("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}".format(self.CORPID,self.CORPSECRET))
        print(res.text)

    def get_url_use(self):
        #13500001234时间戳
        _meg_signatur  ="FQWEXZCVAQFAS"
        _timestamp = math.ceil(time.time()*10)#时间戳
        _nonces = int(random.random()*1000000000)
        _echostrs = "sadasd213sdasd"
        # dev_msg_signature = sorted(self.TOKENS,_timestamp,_nonces,_meg_signatur)
        print("http://api.3dept.com/?msg_signature={}&timestamp={}&nonce={}&echostr={}".format(_meg_signatur,_timestamp,_nonces,_echostrs))
        res = requests.get("http://api.3dept.com/?msg_signature={}&timestamp={}&nonce={}&echostr={}".format(_meg_signatur,_timestamp,_nonces,_echostrs))
        print(res.text)

if __name__ == '__main__':
    wx = WeChat()
    # wx.get_access_token()
    wx.get_url_use()