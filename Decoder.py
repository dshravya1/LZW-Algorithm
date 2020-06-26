import sys
from sys import argv
import string
import struct

# Readin of command line arguments
File_Name=sys.argv[1]
BIT_LENGTH=sys.argv[2]
# Input file readin
ip_filename=open(File_Name,"rb")
# Initialization of variables, list and dictionary
MAXIMUM_TABLE_SIZE=pow(2,int(BIT_LENGTH))
TABLE_SIZE=256
INPUT_CODE=[]
DECODED_DATA=[]
NEW_STRING=""
STRING=""
# Input file readin of 2 bytes at a time
while True:
    Bytes_data=ip_filename.read(2)
    if len(Bytes_data)!=2:
        break
    (INT_DATA, )=struct.unpack(">H",Bytes_data)
    INPUT_CODE.append(INT_DATA)
print(INPUT_CODE)
TABLE={i:chr(i)for i in range (TABLE_SIZE)}
#LZW Decoding algorithm
for code in INPUT_CODE:
    if TABLE.get(code)==None:
        TABLE[code]=STRING+(STRING[0])
    NEW_STRING=NEW_STRING+TABLE[code]
    if not (len(STRING)==0):
        TABLE[TABLE_SIZE]=STRING+TABLE[code][0]
        TABLE_SIZE+=1
    STRING=TABLE[code]
print(NEW_STRING)
# Exporting the decoded file in .txt format
op_file=File_Name.split(".")[0]+"_decoded.txt"
exported_file=open(op_file,'w')
for x in NEW_STRING:
  exported_file.write(x)
exported_file.close()
ip_filename.close()