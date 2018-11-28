import HttpClient

httpClient = HttpClient.HttpClient()

# get login user info
loginUser = httpClient.getSelf()
print(loginUser)
loginSid = loginUser['ResultSet']['Result']['Usid']
print("login info:")
print(loginSid)

# get shotmail info
smailUserInfo = httpClient.getShortMailUser(loginSid)
sId = smailUserInfo['ResultSet']['Result']
print("smail info")
print(sId)

print(httpClient.sendShortMail())