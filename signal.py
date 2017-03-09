#!/usr/bin/env python

import sys
from scapy.all import *
import time,struct
import MySQLdb


#db=MySQLdb.connect("localhost","root","raspberry","Probrequest")
def banner():
	print "########################"
	print "    Welcome to Scapy radiotap header"
	print "###############################"

client=set()

def handler(pkt):
	#cursor=db.cursor()
	if pkt.haslayer(RadioTap) and pkt.haslayer(Dot11ProbeReq):
		if(pkt.info>0):
			previous=pkt.addr2+ "---"+pkt.addr3+"---"+pkt.info
			#if previous not in client and pkt.addr3=="d4:63:fe:13:7c:09": #  AP mac address ( router point)
			
			if previous not in client:
				client.add(previous)
				
				print "New client Probe Request:"+" "+pkt.addr2+" "+pkt.addr3+" "+pkt.info 
				currenttime=time.ctime()
				conn_time=re.findall(r'([0-9]{2}\:[0-9]{2}\:[0-9]{2})',currenttime)
				connectiontime=str(conn_time[0])
				
				x=pkt.notdecoded
				#print x
				signalstrength=struct.unpack('>b',x[16])    # RSSI bit 16 of radiotapheader
				print connectiontime+"        "+str(signalstrength[0])
				db=MySQLdb.connect("localhost","root","raspberry","Probrequest")
				cursor=db.cursor()
				
				sql="insert into clientinfo(clientmac,signalstrength,connectiontime) values('%s','%d','%s');"%(pkt.addr2,signalstrength[0],connectiontime)
				try:
					cursor.execute(sql)
					db.commit()
				except:
					db.rollback()
				db.close()


banner()
sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=handler)
