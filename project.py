#!/usr/bin/env python

import sys,MySQLdb
import schedule
from scapy.all import *

def banner():
	print "##################################"
	print " Finding AP and mac"
	print "####################################"


apmac=set()
clientmac=set()
def handler(pkt):
	if pkt.haslayer(Dot11ProbeReq):
		if pkt.info:
			value=pkt.addr2+"---"+pkt.info
			if value not in clientmac:
				clientmac.add(value)
				
				#print "client MAC "+pkt.addr2 +"   "+"SSID :"+pkt.info

				currenttime=time.ctime()
                                conn_time=re.findall(r'([0-9]{2}\:[0-9]{2}\:[0-9]{2})',currenttime)
                                connectiontime=str(conn_time[0])
				db=MySQLdb.connect("localhost","root","raspberry","Probrequest")
				cursor=db.cursor()
				db=MySQLdb.connect("localhost","root","raspberry","Probrequest")
				cursor=db.cursor()
                                x=pkt.notdecoded
                                try:
                                        signalstrength=struct.unpack('>b',x[-2:-1])[0]    # RSSI bit 16 of radiotapheader
					sql1="insert into clientinfo(clientmac,signalstrengthdbm,connectiontime,SSID) values('%s','%d','%s','%s');"%(pkt.addr2,signalstrength,currenttime,pkt.info)
					cursor.execute(sql1)
					db.commit()
						
					print "client MAC "+pkt.addr2 +"   "+"SSID :"+pkt.info
                                        print connectiontime+"        "+str(signalstrength)+ "dbm"
                                except IndexError:
                                        	print " Index error out of range"

				db.close()

def read():
	db=MySQLdb.connect("localhost","root","raspberry","Probrequest")
	cursor=db.cursor()
	sql="select clientmac,SSID from clientinfo;"
        cursor.execute(sql)
        results=cursor.fetchall() #reading from databases
        if not results:
        	print " Databases is empty"
        else:
		print " *****************************"
               	for row in results:
                	client=row[0]
                        ssid=row[1]
			data=client+"---"+ssid
			if data not in apmac:                
                        	apmac.add(data)
				print data
                                                #print data
	db.close()

		







banner()
read()
#sniff(iface="mon0",count=int(sys.argv[1]),prn=handler)

sniff(iface="mon0",count=5000,prn=handler)
		
