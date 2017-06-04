#!/usr/bin/env python

import sys,MySQLdb
import schedule
from scapy.all import *
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as md
import dateutil,sys

def banner():
	print "##################################"
	print " Reading from database Probrequest"
	print "####################################"


apmac=set()
clientmac=set()
sig=[]
time=[]
def read():
	db=MySQLdb.connect("localhost","root","raspberry","Probrequest")
	cursor=db.cursor()
	#sql="select signalstrengthdbm,connectiontime from clientinfo where clientmac='str(sys.argv[1])' ;"
	sql="select signalstrengthdbm,connectiontime from clientinfo where id between 11645 and 11651 ;"
        cursor.execute(sql)
        results=cursor.fetchall() #reading from databases
        if not results:
        	print " Databases is empty"
        else:
		print "###########################################"
                print " In Every one  minute reading from databases"
		print "############################################"                #data=client+"---"+if client  not in apmac:
               	for row in results:
                	sig.append(row[0])
                        connectiontime=row[1]
			conn_time=re.findall(r'([0-9]{2}\:[0-9]{2}\:[0-9]{2})',connectiontime)
			#ax=plt.gca()
			#ax.set_xticks(dates)
			time.append(connectiontime)
			dates =[dateutil.parser.parse(s) for s in time]
			
	
			ax=plt.gca()
			ax.set_xticks(dates)
        		xfmt = md.DateFormatter('%H:%M:%S')
			ax.xaxis.set_major_formatter(xfmt)
        	#	plt.subplots_adjust(bottom=0.2)
		#	plt.xticks( rotation=25 )         

			plt.title("Matplotlib demo")
			plt.xlabel("x axis caption")
			plt.ylabel("y axis caption")
	
			plt.plot(dates,sig,"-b")
	
			plt.show()			


		
	db.close()

		







banner()
read()

		
