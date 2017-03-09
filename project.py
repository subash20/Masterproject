#!/usr/bin/env python

import sys,re
import MySQLdb
from bs4 import BeautifulSoup
from database import data

#db=MySQLdb.connect("localhost","root","raspberry","clientinfo")

def banner():
	print " ################################"
	print "     WiFI Packet Parser     "
	print	"##############################"


def parser():
	count=1
	html=open(sys.argv[1],'r').read()
	soup=BeautifulSoup(html)
	#for time in soup.find_all("wireless-client"):
	#	print "Time of connection:"+time.get("last-time")
	for link in soup.find_all('wireless-client'):
		#print "Time of connection:"+link.get("last-time")
		time=link.get("last-time")
		
		conn_time=re.findall(r'([0-9]{2}\:[0-9]{2}\:[0-9]{2})',time)
		connectiontime= str(conn_time[0])
		print connectiontime
		clientmac= link.find("client-mac").text
		signalstrength=link.find("max_signal_dbm").text
		print clientmac + " "+ signalstrength
		sigstr=int(signalstrength)
		data().inserti(clientmac,sigstr,connectiontime)
		
		#cursor=db.cursor()
		
		#try:			
		#	cursor.execute("insert into client(clientmac,signalstrength,connectiontime) values('%s','%d','%s');",%(clientmac,sigstr,connectiontime))
		#	db.commit()
		#except MySQLdb.InterfaceError,e :
		#	print "error in database"
		#	raise e
		#	db.rollback()
	#db.close()	

banner()
parser()
