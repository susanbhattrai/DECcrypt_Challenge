#!/usr/bin/python

MESSAGE = "84909104909101909112909979091159091159091199091119091149091009091059091159091009091019099990999909111909110909118909101909114909116"

PLAINTEXT = ""

DECIMALS_LIST = MESSAGE.split('909')
print DECIMALS_LIST

for DECIMAL in DECIMALS_LIST:
     DECIMAL = int(DECIMAL)
     PLAINTEXT = PLAINTEXT + chr(DECIMAL)

print "Plaintext: " + PLAINTEXT
