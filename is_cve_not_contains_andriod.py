import requests
from lxml import html
str1=input("Enter start number:")
str2=input("Enter   end number:")
url='http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2014-'
print "start number:"+str(str1)
print "end number:"+str(str2)
while str1-str2 >=0:
	url1=url+str(str1)
	page=requests.Session().get(url1) 
	tree=html.fromstring(page.text) 
	result=str(tree.xpath('//td[@colspan="2"]/text()'))
	str1=str1-1
	if "for Android" in result or "for\\nAndroid" in result:
		continue		
		#print'number'+str(str1+1)+' contains android'
	else:
		#continue		
		print'number'+str(str1+1)+' not contains android'
print "----END-----"
