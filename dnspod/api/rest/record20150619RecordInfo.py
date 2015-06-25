'''
Created by minqiang.feng on 2015.06.19
'''
from dnspod.api.base import RestApi
class record20150619RecordInfo(RestApi):
	def __init__(self,domain='dnsapi.cn',port=443):
		RestApi.__init__(self,domain, port)
		self.domain_id = None
		self.record_id = None
		
	def getapiname(self):
		return 'Record.Info'
