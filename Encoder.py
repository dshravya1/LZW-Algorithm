import sys
from sys import argv
import string
import struct 

# Readin of Command line arguments
File_Name=sys.argv[1]
BIT_LENGTH=int(sys.argv[2])
# Input File readin 
ip_file=open(File_Name)
# Initialization of variables, list and dictionary
MAXIMUM_TABLE_SIZE=pow(2,BIT_LENGTH)
TABLE_SIZE=256
TABLE={chr(i):i for  i in range(TABLE_SIZE)}
STRING=""
OUTPUT_CODE=[]
# LZW Encoding algorithm
for SYMBOL in (ip_file.read()):
    STRING_SYMBOL=STRING+SYMBOL
    if STRING_SYMBOL in TABLE:
        STRING=STRING_SYMBOL
    else:
         OUTPUT_CODE.append(TABLE[STRING])
         if len(TABLE)<=MAXIMUM_TABLE_SIZE:
            TABLE[STRING_SYMBOL]=TABLE_SIZE
            TABLE_SIZE+=1
         STRING=SYMBOL

if STRING in TABLE:
    OUTPUT_CODE.append(TABLE[STRING])
print(OUTPUT_CODE)
# Exporting the encoded data in .lzw format
op_file=File_Name.split(".")[0]
op_filename=op_file+".lzw"
exported_file=open(op_filename,"wb")
for x in OUTPUT_CODE:
    exported_file.write(struct.pack(">H",x))
exported_file.close()
ip_file.close()