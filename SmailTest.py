import base64
import urllib.request
import urllib.parse

# access param setting
requestUrl = 'https://demo.groupsession.jp/gsession/api/smail/mail/send.do'
user = "kanri"
password = "pass"

# request header setting
dataString = (user + ":" + password)
dataBytes = dataString.encode("utf-8")
dataEncoded = base64.b64encode(dataBytes).decode('utf-8')
header = {
    'Content-Type': 'application/x-www-form-urlencoded',
    'Authorization': "Basic " + dataEncoded
}

# request data setting
data = {
    'sacSid': 2,
    'sendTo': [2],  # 配列で指定するとGS 管理者に送信される。 'sendTo': 2 だと正しく自分に送信できる
    'title': "テストタイトル",
    'body': "テスト本文",
    'procMode': 0
}
parsedData = urllib.parse.urlencode(data)

# send short mail
req = urllib.request.Request(requestUrl, parsedData.encode(), header, method='POST')
with urllib.request.urlopen(req) as res:
    body = res.read()
print(body)