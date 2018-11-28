import urllib.request
import urllib.parse
import requests
import json
import base64
import xmltodict

class HttpClient:
    def __init__(self):
        self.baseUrl = 'https://demo.groupsession.jp/gsession'

        user = "kanri"
        password = "pass"
        dataString = (user + ":" + password)
        dataBytes = dataString.encode("utf-8")
        dataEncoded = base64.b64encode(dataBytes).decode('utf-8')
        self.dataEncoded = dataEncoded

        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': "Basic " + self.dataEncoded
        }

    def getSelf(self):
        requestPath = '/api/user/whoami.do?'
        requestUrl = self.baseUrl + requestPath
        data = {}

        req = urllib.request.Request(requestUrl, json.dumps(data).encode(), self.headers)
        with urllib.request.urlopen(req) as res:
            body = res.read()
            # print(body)

        responseDist = xmltodict.parse(body)
        # print(responseDist)
        responseJson = json.dumps(responseDist)
        # print(responseJson)
        return responseDist

    def getUser(self, usrSid):
        requestPath = '/api/user/inf.do?'
        requestUrl = self.baseUrl + requestPath
        data = {
            'usrSid': usrSid
        }

        parsedData = urllib.parse.urlencode(data)

        req = urllib.request.Request(requestUrl, parsedData.encode(), self.headers, method='POST')
        with urllib.request.urlopen(req) as res:
            body = res.read()
            print(body)

        responseDist = xmltodict.parse(body)
        # print(responseDist)
        # responseJson = json.dumps(responseDist)
        # print(responseJson)
        return responseDist

    def getShortMailAccountList(self):
        requestPath = '/api/smail/account/list.do'
        requestUrl = self.baseUrl + requestPath
        data = {
            # 'usrSid': sid
        }

        parsedData = urllib.parse.urlencode(data)

        req = urllib.request.Request(requestUrl, parsedData.encode(), self.headers, method='POST')
        with urllib.request.urlopen(req) as res:
            body = res.read()
            # print(body)

        responseDist = xmltodict.parse(body)
        # print(responseDist)
        # responseJson = json.dumps(responseDist)
        # print(responseJson)
        return responseDist

    def getShortMailUser(self, sid = -1):
        requestPath = '/api/smail/account/defaultinput.do'
        requestUrl = self.baseUrl + requestPath
        data = {
            'usrSid': sid
        }

        parsedData = urllib.parse.urlencode(data)

        req = urllib.request.Request(requestUrl, parsedData.encode(), self.headers, method='POST')
        with urllib.request.urlopen(req) as res:
            body = res.read()
            # print(body)

        responseDist = xmltodict.parse(body)
        # print(responseDist)
        # responseJson = json.dumps(responseDist)
        # print(responseJson)
        return responseDist

    def sendShortMail(self):
        # ショートメールを送る
        requestPath = '/api/smail/mail/send.do'
        requestUrl = self.baseUrl + requestPath

        # header
        headers = {
            # 'Content-Type': 'multipart/form-data',
            'Authorization': "Basic " + self.dataEncoded
        }

        # file
        fileDataBinary = open("file/j006-00-003.csv", 'rb').read()
        files = {'tmpFile1': ("j006-00-003.csv", fileDataBinary, "text/csv")}
        file = {'tmpFile1': open("file/j006-00-003.csv", 'rb')}

        # data
        data = {
            'sacSid': 2,
            'sendTo': 2,
            'title': "テストタイトル",
            'body': "テスト本文",
            'procMode': 0
        }
        # parsedData = urllib.parse.urlencode(data)
        # print(parsedData.encode())
        #
        # req = urllib.request.Request(requestUrl, parsedData.encode(), self.headers, method='POST')
        # with urllib.request.urlopen(req) as res:
        #     body = res.read()
        #     print(body)

        # csv = open('file/j006-00-003.csv', 'rb')
        # files = {'param_name': ('filename.jpg', csv, 'image/jpeg')}
        # data = {'another_key': 'another_value'}
        # r = requests.post(requestUrl,headers=headers, files=files, data=data)
        print(requestUrl)
        print(headers)
        print(data)
        r = requests.post(requestUrl,headers=headers, files=file, data=data)
        print(r.text)

        # responseDist = xmltodict.parse(body)
        # print(responseDist)
        # responseJson = json.dumps(responseDist)
        # print(responseJson)
        # return responseDist
