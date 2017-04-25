import xml.etree.cElementTree as ET
import urllib2

Query = raw_input("What are you looking for? (Space Separated)")
Qcity = raw_input("What City?")
Qstate = raw_input("What State?")
Query=Query.replace(' ','+')



xmlurl='http://api.indeed.com/ads/apisearch?publisher=6768328719336877&q='+Query+'&l='+Qcity+'%2C%20'+Qstate+'&sort=&radius=&st=&jt=&start=&limit=&fromage=&filter=&latlong=1&co=us&chnl=&userip=1.2.3.4&useragent=Mozilla%2F%2F4.0(Firefox)&v=2'
tree = ET.ElementTree(file=urllib2.urlopen(xmlurl))
root = tree.getroot()
root.tag, root.attrib
results = root.find('results')
#total=root.find('totalresults').text

#print total
print '\n'
for result in results.findall('result'):
    jobtitle=result.find('jobtitle').text
    company=result.find('company').text
    city=result.find('city').text
    state=result.find('state').text
    url=result.find('url').text
    print jobtitle,'\n', company,"\n",city,'\n',state, '\n',url
    print '\n'
    

