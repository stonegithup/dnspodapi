'''
Created by minqiang.feng on 2015.06.19
'''
from dnspod.api.base import RestApi
class domain20150619DomainList(RestApi):
	def __init__(self,domain='dnsapi.cn',port=443):
		RestApi.__init__(self,domain, port)
		self.type = None
		self.offset = None
		self.length = None
		self.group_id = None
		self.keyword = None

	def getapiname(self):
		return 'Domain.List'
