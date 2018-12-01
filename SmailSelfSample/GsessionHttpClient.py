import configparser
import os
import sys
import urllib.request
import urllib.parse
import requests
import json
import base64
import xmltodict

class GsessionHttpClient:
    def __init__(self):
        self._ini = configparser.ConfigParser()
        if os.path.exists("./config.ini"):
            self._ini.read("./config.ini")
        else:
            sys.stderr.write('config.ini is not found.')
            sys.exit(2)

        self.baseUrl = self._ini['login']['url']
        user = self._ini['login']['username']
        password = self._ini['login']['password']
        dataString = (user + ":" + password)
        dataBytes = dataString.encode("utf-8")
        dataEncoded = base64.b64encode(dataBytes).decode('utf-8')
        self.dataEncoded = dataEncoded

        self.headers = {
            'Authorization': "Basic " + self.dataEncoded
        }

    def getSelf(self):
        requestPath = '/api/user/whoami.do?'
        requestUrl = self.baseUrl + requestPath
        data = {}

        req = urllib.request.Request(requestUrl, json.dumps(data).encode(), self.headers)
        with urllib.request.urlopen(req) as res:
            body = res.read()

        responseDist = xmltodict.parse(body)
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

        responseDist = xmltodict.parse(body)
        return responseDist

    def sendShortMail(self, sId):
        # ショートメールを送る
        requestPath = '/api/smail/mail/send.do'
        requestUrl = self.baseUrl + requestPath

        # header
        headers = {
            'Authorization': "Basic " + self.dataEncoded
        }

        # file
        file = {
            'tmpFile1': open(self._ini['tmp']['tmpFile1'], 'rb'),
            'tmpFile2': open(self._ini['tmp']['tmpFile2'], 'rb')
        }

        # data
        data = {
            'sacSid': sId,
            'sendTo': sId,
            'title': "テストタイトル",
            'body': "テスト本文",
            'procMode': 0
        }

        res = requests.post(requestUrl,headers=headers, files=file, data=data)
        print(res.text)
        responseDist = xmltodict.parse(res.text)
        return responseDist['Result']['#text']

