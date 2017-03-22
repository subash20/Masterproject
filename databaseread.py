#!/usr/bin/env python

import sys,MySQLdb
import schedule
from scapy.all import *

def banner():
	print "##################################"
	print " Reading from database Probrequest"
	print "####################################"


apmac=set()
clientmac=set()

def read():
	db=MySQLdb.connect("localhost","root","raspberry","Probrequest")
	cursor=db.cursor()
	sql="select clientmac,SSID from clientinfo;"
        cursor.execute(sql)
        results=cursor.fetchall() #reading from databases
        if not results:
        	print " Databases is empty"
        else:
		print "********************************************"	
                print " In Every one  minutes reading from databases"
		print "********************************************"                #data=client+"---"+if client  not in apmac:
               	for row in results:
                	client=row[0]
                        ssid=row[1]

                        if client not in apmac:          #data=client+"---"+if client  not in apmac:
                        	apmac.add(client)
                        	print " Achtung new client"+"   "+client
                                                #print "No new client"
                                        #else:
                                                #print " No new client"
                                        #print "New Client:"+pkt.addr2+"--sending probrequest-->>"+pkt.info
                                        #print client+"   " +ssid
                                        #if pkt.addr2==client and pkt.info==ssid:
                                        #       print "No new client"
                                                #print "Old client:"+client +"----->>>>"+ssid
                                        #else:
                                        #       print "New Client:"+pkt.addr2+"--sending probrequest-->>"+pkt.infdb.close()
	db.close()

		







banner()
#read()
#sniff(iface="mon0",count=int(sys.argv[1]),prn=handler)

#sniff(iface="mon0",count=5000,prn=handler)
schedule.every(1).minutes.do(read)
#schedule.every(2).minutes.do(sniff(iface="mon0",count=int(sys.argv[1]),prn=handler))
while True:
	schedule.run_pending()
	time.sleep(1)
		
