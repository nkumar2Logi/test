import requests # http://pypi.python.org/pypi/requests
import time
#import datetime
import json

######################
PostalCodes = []
RoviURL='http://api.rovicorp.com/TVlistings/v9/listings/services/postalcode/%s/info?countrycode=US&apikey=sz7xwh32bppm6jhseat4ma8h&sig=739e43cd-9b5f-4a76-a76c-a8fd7c7f0938'
OutputFile = open('/home/nkumar2/Script/Python/RoviSPAllPostCode.csv','w')
for PostalCode in PostalCodes:
	print(PostalCode)
	if len(str(PostalCode))<5:
			PostalCode=str('0'*(5-int(len(str(PostalCode)))))+str(PostalCode)
	RoviResponse = requests.get(RoviURL %(PostalCode)).json()
	if RoviResponse["ServicesResult"]["Services"]:
		for ServiceProvider in RoviResponse["ServicesResult"]["Services"]["Service"]:
				if ServiceProvider.get('TimeZones'):
						if ServiceProvider['TimeZones'][0].get("StartDateTime"):
								StartTime=ServiceProvider['TimeZones'][0].get("StartDateTime")
						else:
								StartTime=None
						if ServiceProvider['TimeZones'][0].get("EndDateTime"):
								EndTime=ServiceProvider['TimeZones'][0]["EndDateTime"]
						else:
								EndTime=None
						if ServiceProvider['TimeZones'][0].get("Offset"):
								Offset=ServiceProvider['TimeZones'][0]["Offset"]
						else:
								Offset=None
				else:
						StartTime=EndTime=Offset=None

				OutputFile.write(
						str(PostalCode)+str("|")+\
						str(ServiceProvider.get("ServiceClass"))+str("|")+\
						str(ServiceProvider.get("ServiceId"))+str("|")+\
					  	str(ServiceProvider.get('Name'))+str("|")+\
						str(ServiceProvider.get('City'))+str("|")+\
						str(ServiceProvider.get('Type'))+str("|")+\
					  	str(ServiceProvider.get('MSO'))+str("|")+\
						str(ServiceProvider.get('MSOID'))+str("|")+\
						str(ServiceProvider.get('SystemName'))+str("|")+\
					  	str(ServiceProvider['TimeZones'][0]["StartDateTime"])+str("|")+\
						str(ServiceProvider['TimeZones'][0]["EndDateTime"])+str("|")+\
					  	str(ServiceProvider['TimeZones'][0]["Offset"]+str("\n"))
				)
		time.sleep(.8)
OutputFile.close()
