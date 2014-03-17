#!/usr/bin/env python
import os
import sys

pwf = open(sys.argv[1])

li = 0
for line in pwf:
   litem = ''
   li = li + 1
   litem = line.split(":")
   sfi = open(sys.argv[2])
   for l in sfi:
      if litem[0] in l:
         lv = ''
         lv = l.split(":")
			#print "User: %s Password: %s" % (lv[0], litem[1].strip())
         print litem[1].strip()
			
         #if lv[6].strip() != "Disabled":
			#	print "User: %s" % lv[0]
			#	print "User: %s Password: %s" % (lv[0], litem[1].strip())
			#	print "User: %s Password: %s Hash: %s" % (lv[0], litem[1].strip(), litem[0])
			#print "Username: %s" % (lv[6])
			#print "Passwd: %s" % (litem[1].strip())
	sfi.close()
pwf.close()
