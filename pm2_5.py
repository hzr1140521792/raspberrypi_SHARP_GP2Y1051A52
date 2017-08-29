# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
#encoding=utf-8
import serial  
import time
import   struct
from struct import *
# import sqlite3
# 打开串口  
print "Opening Serial Port...",
ser = serial.Serial("/dev/ttyAMA0", 2400)  
print "Done"
def main():
    while True:  
        # 获得接收缓冲区字符  
        count = ser.inWaiting()   
        # 读取内容并回显  
        recv_start = ser.read(1)
        if hexShow(recv_start)=="ff":
            print '-'*20 
            recv=ser.read(7)
            sum=int(hexShow(recv[1]),16)+int(hexShow(recv[2]),16)+int(hexShow(recv[3]),16)+int(hexShow(recv[4]),16)
            checkbyte=int(hexShow(recv[5]),16)
            if sum==checkbyte:
                print "check data ok!"
                Vout=(int(hexShow(recv[1]),16)*256+int(hexShow(recv[2]),16))/1024*5.0
                print 'Vout:'+str(Vout)
                pm25=Vout*500
                print 'PM2.5:'+str(pm25)
            print "sum:"+str(sum)
            print "checkdata:"+str(checkbyte)
            print '-'*20
            ser.flushInput()  
        # 必要的软件延时  
        time.sleep(0.1)
        # time.sleep(10)

#十六进制显示串口数据
def hexShow(argv):  
    result = ''  
    hLen = len(argv)  
    for i in xrange(hLen):  
        hvol = ord(argv[i])  
        hhex = '%02x'%hvol  
        # result += hhex+' '  
        result += hhex
    # print 'hexShow:',result
    return result



if __name__ == '__main__':  
    try:  
        main()  
    except KeyboardInterrupt:  
        if ser != None:  
            ser.close()  