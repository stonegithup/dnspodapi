'''
Created by minqiang.feng on 2015.06.19
'''
from dnspod.api.base import RestApi
class domain20150619DomainCreate(RestApi):
	def __init__(self,domain='dnsapi.cn',port=443):
		RestApi.__init__(self,domain, port)
		self.domain = None

	def getapiname(self):
		return 'Domain.Create'
