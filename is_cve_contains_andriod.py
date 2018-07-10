import requests
from lxml import html
str1=input("Enter start number:")
str2=input("Enter   end number:")
url='http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-'
print "start number:"+str(str1)
print "end number:"+str(str2)
for num in range(str1,str2+1):
	url1=url+str(num)
	page=requests.Session().get(url1) 
	tree=html.fromstring(page.text) 
	result=str(tree.xpath('//td[@colspan="2"]/text()'))
	if "for Android" in result:
		continue		
		#print'number'+str(num)+' contains android'
	else:
		print'number'+str(num)+' not contains android'
