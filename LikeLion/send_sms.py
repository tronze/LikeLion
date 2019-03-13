from urllib import parse, request

from django.conf import settings


def send_sms(receiver, msg):
    data = {
        'key': settings.SMS_KEY,
        'user_id': settings.SMS_ID,
        'sender': settings.SMS_PHONE_NUM,
        'receiver': receiver,
        'msg': msg,
        'testmode_yn': settings.SMS_TEST_MODE,
    }
    wrapper = parse.urlencode(data).encode('UTF-8')
    url = request.Request("https://apis.aligo.in/send/", wrapper)
    response = request.urlopen(url).read().decode("UTF-8")
    print(msg)
    print(response)
