#!/usr/bin/env python

import MySQLdb



db=MySQLdb.connect("localhost","root","raspberry","clientinfo")

class data:
	 
	
	def inserti(self,clientmac,signalstrength,connectiontime):
		
		cursor=db.cursor()
		sql="insert into client(clientmac,signalstrength,connectiontime) values('%s','%d','%s');"%(clientmac,signalstrength,connectiontime)
		try:
			cursor.execute(sql)
			db.commit()
		except:
			db.rollback()
		return
	
	
		db.close()



#x=data()
#x.inserti()
