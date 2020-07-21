from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json

accessKeyId = '********'
accessSecret = '******'
regionid = 'cn-hangzhou'
SignName = '强仔浅谈'
TemplateCode = 'SMS_193508720'


class AliyunSMS(object):
    '''阿里云短信服务'''

    def __init__(self):
        self.client = AcsClient(accessKeyId, accessSecret, regionid)

    def _create_request(self, to: str, code: str):
        '''封装短信请求'''
        self.request = CommonRequest()
        self.request.set_accept_format('json')
        self.request.set_domain('dysmsapi.aliyuncs.com')
        self.request.set_method('POST')
        self.request.set_protocol_type('https')  # https | http
        self.request.set_version('2017-05-25')
        self.request.set_action_name('SendSms')

        self.request.add_query_param('RegionId', regionid)
        self.request.add_query_param('PhoneNumbers', to)
        self.request.add_query_param('SignName', SignName)
        self.request.add_query_param('TemplateCode', TemplateCode)
        self.request.add_query_param('TemplateParam', "{\"code\":\"%s\"}" % code)

    def sen_msg(self, to: str, code: str):
        self._create_request(to, code)
        response = self.client.do_action_with_exception(self.request).decode()
        result = json.loads(response).get('Code')
        if result == 'OK':
            return True
        else:
            return False


if __name__ == '__main__':
    aliyun_sms = AliyunSMS()
    result = aliyun_sms.sen_msg('13014666851', '1314')
    print(result)
