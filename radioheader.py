import sys
from scapy.all import *

def banner():
	print " ##########################"
	print "  Radio Tap Header Field"
	print "###########################"



#def __init__(self, interface):
    # Radiotap field specification
 #   self.radiotap_formats = {"TSFT":"Q", "Flags":"B", "Rate":"B","Channel":"HH", "FHSS":"BB", "dBm_AntSignal":"b", "dBm_AntNoise":"b","Lock_Quality":"H", "TX_Attenuation":"H", "dB_TX_Attenuation":"H","dBm_TX_Power":"b", "Antenna":"B",  "dB_AntSignal":"B",
     # "dB_AntNoise":"B", "b14":"H", "b15":"B", "b16":"B", "b17":"B", "b18":"B",
     # "b19":"BBB", "b20":"LHBB", "b21":"HBBBBBH", "b22":"B", "b23":"B",
     # "b24":"B", "b25":"B", "b26":"B", "b27":"B", "b28":"B", "b29":"B","b30":"B", "Ext":"B"}





def parsePacket(pkt):
	radiotap_formats = {"TSFT":"Q", "Flags":"B", "Rate":"B",
      				"Channel":"HH", "FHSS":"BB", "dBm_AntSignal":"b", "dBm_AntNoise":"b",
      				"Lock_Quality":"H", "TX_Attenuation":"H", "dB_TX_Attenuation":"H",
      				"dBm_TX_Power":"b", "Antenna":"B",  "dB_AntSignal":"B",
      				"dB_AntNoise":"B", "b14":"H", "b15":"B", "b16":"B", "b17":"B", "b18":"B",
      				"b19":"BBB", "b20":"LHBB", "b21":"HBBBBBH", "b22":"B", "b23":"B",
      				"b24":"B", "b25":"B", "b26":"B", "b27":"B", "b28":"B", "b29":"B",
      				"b30":"B", "Ext":"B"}
	#radiotap_formats = {"TSFT":"Q", "Flags":"B", "Rate":"B","Channel":"HH", "FHSS":"BB", "dBm_AntSignal":"b", "dBm_AntNoise":"b","Lock_Quality":"H", "TX_Attenuation":"H", "dB_TX_Attenuation":"H","dBm_TX_Power":"b", "Antenna":"B",  "dB_AntSignal":"B","dB_AntNoise":"B","b14":"H","b15":"B","b16":"B","b17":"B","b18":"B","b19":"BBB", "b20":"LHBB", "b21":"HBBBBBH", "b22":"B", "b23":"B","b24":"B", "b25":"B", "b26":"B", "b27":"B", "b28":"B", "b29":"B","b30":"B", "Ext":"B"}
	
	if pkt.haslayer(Dot11):
		#count=0
     		if pkt.addr2 is not None:
        # check available Radiotap fields
        		field, val = pkt.getfield_and_val("present")
        		names = [field.names[i][0] for i in range(len(field.names)) if (1 << i) & val != 0]
        # check if we measured signal strength
        		if "dBm_AntSignal" in names:
          # decode radiotap header
          			fmt = "<"
          			rssipos = 0
          			for name in names:
            # some fields consist of more than one value
            				if name == "dBm_AntSignal":
              # correct for little endian format sign
              					rssipos = len(fmt)-1
            				fmt = fmt + radiotap_formats[name]
          # unfortunately not all platforms work equally well and on my arm
          # platform notdecoded was padded with a ton of zeros without
          # indicating more fields in pkt.len and/or padding in pkt.pad
          			decoded = struct.unpack(fmt, pkt.notdecoded[:struct.calcsize(fmt)])
				
				print decoded
          					#return pkt.addr2, decoded[rssipos]
				#count=count+1




banner()
sniff(iface=sys.argv[1],count=int(sys.argv[2]),prn=parsePacket)
