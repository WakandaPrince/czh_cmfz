import requests

from czh_cmfz.settings import API_KEY


class YunPian():

    def __init__(self, api_key):
        self.api_key = api_key
        self.single_send_url = 'https://sms.yunpian.com/v2/sms/single_send.json'

    def send_msg(self, phone, code):
        params = {
            'apikey': self.api_key,
            'mobile': phone,
            'text': f"【陈泽昊test】您的验证码是{code}。如非本人操作，请忽略本短信"
        }

        resp = requests.post(self.single_send_url, data=params)
        print(resp)


if __name__ == '__main__':
    yun_pian = YunPian(API_KEY)
    yun_pian.send_msg('15210352577', '123456')
