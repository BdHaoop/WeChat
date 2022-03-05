import time
import requests
import json

# def main():
class WeChat:
    def __init__(self):
        self.CORPID = 'wwb3abceb034b00d03'  # 企业ID，在管理后台获取
        self.CORPSECRET = '0sslis_dlQWnmyOzGgmQuX-5eEzJ3wENS11Friti9tc'  # 自建应用的Secret，每个自建应用里都有单独的secret
        self.AGENTID = '1000005'  # 应用ID，在后台应用中获取
        self.TOUSER = "@all"  # 接收者用户名,多个用户用|分割@all

    def _get_access_token(self):
        url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken'
        values = {'corpid': self.CORPID,
                  'corpsecret': self.CORPSECRET,
                  }
        req = requests.post(url, params=values)
        # print(req.text)
        data = json.loads(req.text)
        print(data['access_token'])
        return data["access_token"]

    def get_access_token(self):
        try:
            with open('D:\\tmp\\access_token.conf', 'r') as f:
                t, access_token = f.read().split()
                # print(t)
                # print(time.time())
        except:
            with open('D:\\tmp\\access_token.conf', 'w') as f:
                access_token = self._get_access_token()
                cur_time = time.time()
                f.write('\t'.join([str(cur_time), access_token]))
                return access_token
        else:
            cur_time = time.time()
            if 0 < cur_time - float(t) < 7260:
                return access_token
            else:
                with open('D:\\tmp\\access_token.conf', 'w') as f:
                    access_token = self._get_access_token()
                    f.write('\t'.join([str(cur_time), access_token]))
                    return access_token
    #
    # 发送消息-------------------------------------------------------------------------------------
    def send_data(self, message):
        send_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=' + self.get_access_token()
        send_values = {
            "touser": self.TOUSER,
            "msgtype": "text",
            "agentid": self.AGENTID,
            "text": {
                "content": message
            },
            "safe": "0"
        }
        send_msges = (bytes(json.dumps(send_values), 'utf-8'))
        respone = requests.post(send_url, send_msges)
        respone = respone.json()  # 当返回的数据是json串的时候直接用.json即可将respone转换成字典
        return respone["errmsg"]

    # # 发送文件------------------------------------------------------------------------------------------
    # def _upload_file(self, file):
    #     """
    #     先将文件上传到临时媒体库
    #     """
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token={self.get_access_token()}&type=file"
    #     data = {"file": open(file, "rb")}
    #     res = requests.post(url, files=data)
    #     return res.json()['media_id']
    #
    # def send_file(self, file):
    #     """
    #     发送文件
    #     """
    #     media_id = self._upload_file(file)  # 先将文件上传至临时媒体库
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={self.get_access_token()}"
    #     send_values = {
    #         "touser": self.TOUSER,
    #         "msgtype": "file",
    #         "agentid": self.AGENTID,
    #         "file": {
    #             "media_id": media_id
    #         },
    #     }
    #     send_message = (bytes(json.dumps(send_values), 'utf-8'))
    #     res = requests.post(url, send_message)
    #     return res.json()['errmsg']
    #
    # # 发送图片-----------------------------------------------------------------------------------------------
    # def get_media_url(self, path):  ##上传到图片素材  图片url
    #     # Gtoken = self.__get_token(self.corpID, self.secret)
    #     # img_url = "https://qyapi.weixin.qq.com/cgi-bin/media/uploadimg?access_token={}".format(Gtoken)
    #     img_url = f"https://qyapi.weixin.qq.com/cgi-bin/media/uploadimg?access_token={self.get_access_token()}"
    #     files = {'media': open(path, 'rb')}
    #     r = requests.post(img_url, files=files)
    #     re = json.loads(r.text)
    #     # print("media_id: " + re['media_id'])
    #     return re['url']
    #
    # def send_pic(self, pic_path):
    #     img_url = self.get_media_url(pic_path)
    #     # url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(
    #     # 	self.__get_token(self.corpID, self.secret))
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={self.get_access_token()}"
    #     data = {
    #         "touser": self.TOUSER,
    #         "msgtype": "text",
    #         "agentid": self.AGENTID,
    #         "text": {
    #             "content": img_url
    #         },
    #         "safe": "0"
    #     }
    #     result = requests.post(url=url, data=json.dumps(data))
    #     return result.text
    #
    # def send_violence_warning(self, pic_path):
    #     img_url = self.get_media_url(pic_path)
    #     # url = "https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(
    #     # 	self.__get_token(self.corpID, self.secret))
    #     url = f"https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={self.get_access_token()}"
    #     data = {
    #         "touser": self.TOUSER,
    #         "msgtype": "text",
    #         "agentid": self.AGENTID,
    #         "text": {
    #             "content": '我是DJ李淳罡>>' + img_url
    #         },
    #         "safe": "0"
    #     }
    #     result = requests.post(url=url, data=json.dumps(data))
    #     return result.text

if __name__ == '__main__':
    # 调用类
    wx = WeChat()
    wx.send_data("你好。你很好。")






    # 消息内容
    #wx.send_data("天不生我李淳罡，剑道万古如长夜！")
    #wx.send_file(r"F:\企业微信API开发\测试数据\1.xlsx")
    #wx.send_pic(r'F:\企业微信API开发\测试数据\1.jpg')
    #wx.send_violence_warning(r'F:\企业微信API开发\测试数据\2.jpg')
    # 抛出参数
    # return True
