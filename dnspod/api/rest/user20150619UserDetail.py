'''
Created by minqiang.feng on 2015.06.19
'''
from dnspod.api.base import RestApi
class user20150619UserDetail(RestApi):
	def __init__(self,domain='dnsapi.cn',port=443):
		RestApi.__init__(self,domain, port)

	def getapiname(self):
		return 'User.Detail'
