'''
Created by minqiang.feng on 2015.06.19
'''
from dnspod.api.base import RestApi
class record20150619RecordList(RestApi):
	def __init__(self,domain='dnsapi.cn',port=443):
		RestApi.__init__(self,domain, port)
		self.domain_id = None
		self.offset = None
		self.length = None
		self.sub_domain = None
		self.keyword = None
		
	def getapiname(self):
		return 'Record.List'
