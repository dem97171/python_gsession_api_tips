import sys

import SmailSelfSample.GsessionHttpClient

# init
httpClient = SmailSelfSample.GsessionHttpClient.GsessionHttpClient()

# get self info
loginUser = httpClient.getSelf()
print(loginUser)
myUserId = loginUser['ResultSet']['Result']['Usid']

# get smail info
smailUserInfo = httpClient.getShortMailUser(myUserId)
sId = smailUserInfo['ResultSet']['Result']['sacSid']
print(sId)

# send smail to self
result = httpClient.sendShortMail(sId)
print(result)
if result == 'OK':
    sys.exit()
else:
    sys.exit(1) # error