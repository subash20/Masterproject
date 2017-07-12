#!/usr/bin/env python

import sys,MySQLdb
#import schedule
from scapy.all import *
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.dates as md
import dateutil,sys

def banner():
	print "##################################"
	print " Plotting signalstrength in db versus time"
	print "####################################"


apmac=set()
#client=sys.argv[1]
sig=[]
#x=[]
def read():
	db=MySQLdb.connect("localhost","root","raspberry","Probrequest")
	cursor=db.cursor()
	#sql="select signalstrengthdbm,connectiontime from clientinfo where clientmac='%s' and id between 11806 and 12000 "%(str(sys.argv[1]))
          
	sql="select signalstrengthdbm from clientinfo where clientmac='%s'"%(str(sys.argv[1]))
	#sql="select signalstrengthdbm from clientinfo "
        cursor.execute(sql)
        results=cursor.fetchall() #reading from databases
        if not results:
        	print " Databases is empty"
        else:
		print "###########################################"
                print " Graph show"
		print "############################################"                #data=client+"---"+if client  not in apmac:
               	for row in results:
                	sig.append(row[0])
			
                        #connectiontime=row[1]
			#conn_time=re.findall(r'([0-9]{2}\:[0-9]{2}\:[0-9]{2})',connectiontime)
			#ax=plt.gca()
			#ax.set_xticks(dates)
			#time.append(connectiontime)
			#dates =[dateutil.parser.parse(s) for s in time]
			
	
		#ax=plt.gca()
		#ax.set_xticks(dates)
		#ax.set_xticklabels(x)
        	#xfmt = md.DateFormatter('%H:%M:%S')
		#ax.xaxis.set_major_formatter(xfmt)
        	#plt.subplots_adjust(bottom=0.2)
		#plt.xticks( rotation=90 )         
		
		x=range(1,len(sig)+1)		
		plt.title("Data Analysis")
		plt.xlabel("time of signal generation")
		plt.ylabel("signal strength (dbm)")
	
		plt.plot(x,sig,"-b")
		plt.axis([0,len(sig),-100,0])
		plt.xticks(x,rotation=90)
			
		#ax.set_xticklabels(x)
		plt.show()			


		
	db.close()

		







banner()
read()

		
