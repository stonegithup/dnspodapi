'''
Created by minqiang.feng on 2015.06.19
'''
from dnspod.api.base import RestApi
class record20150619RecordCreate(RestApi):
	def __init__(self,domain='dnsapi.cn',port=443):
		RestApi.__init__(self,domain, port)
		self.domain_id = None
		self.sub_domain = None
		self.record_type = None
		self.record_line = None
		self.value = None
		self.mx = None
		self.ttl = None
		self.status = None
		
	def getapiname(self):
		return 'Record.Create'
