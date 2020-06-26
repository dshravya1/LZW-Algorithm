# LZW-Algorithm
Lempel–Ziv–Welch (LZW) algorithm is a lossless data compression algorithm.This is implemented in python version 3.7.3 and compiler version Clang 11.0.0
 
This algorithm has two steps: 1. Encoding/Compressing
			      2. Decoding/Decompressing

Encoding/Compressing:

Source code for LZW Encoding is Encoder.py. Input File Name( in the .txt format) and bit length is provided in command line argument. Maximum bit size is taken as 2 power of bit length.A dictionary named Table of size 256 is initialized with character as key and its ASCII as value.

Following is the pseudocode (taken from Project1.pdf provided on canvas)used for Encoding :

STRING = null
while there are still input symbols:
SYMBOL = get input symbol
if STRING + SYMBOL is in TABLE:
STRING = STRING + SYMBOL else:
output the code for STRING
If TABLE.size < MAX_TABLE_SIZE:
                              // if table is not full
add STRING + SYMBOL to TABLE // STRING + SYMBOL now has a code
STRING = SYMBOL output the code for STRING

Encoded data is stored in the list OUTPUT_CODE. Output file is exported is in the form of .lzw format.

Decoding/Decompressing:

Source code for LZW Encoding is Decoder.py. Input File Name (the .lzw file obtained as output from Encoding) and bit length is provided in command line argument. Maximum bit size is taken as 2 power of bit length.A dictionary Table of size 256 is initialized with ASCII as key and the character as value.

Following is the pseudocode (taken from Project1.pdf provided on canvas) for Decoding is:

CODE = read next code from encoder
STRING = TABLE[CODE]
output STRING
while there are still codes to receive:
CODE = read next code from encoder if TABLE[CODE] is not defined:
// needed because sometimes the NEW_STRING = STRING + STRING[0] // decoder may not yet have code!
else:
NEW_STRING = TABLE[CODE]
output NEW_STRING
if TABLE.size < MAX_TABLE_SIZE:
add STRING + NEW_STRING[0] to TABLE STRING = NEW_STRING

Decoded data is stored in the list DECODED_DATA. Output file after decoding is exported in .txt format.


Procedure to run the source code:

Open the command window in IDE.Place the input file to be encoded in the current directory chosen for IDE.To run the encoding source code, type the input in the format python Encoder.py <Input_file_name> <Bit_Length> in the python terminal Ex: python Encoder.py Input.txt 9. Output file is created in the current directory as Input_file_name.lzw. To run the decoding source code, type the input in the format python Decoder.py <Input_file_name> <Bit_Length> in the python terminal Ex: python Decoder.py Input.lzw 9. Input file name here is the output of the Encoder.Output is created in the current directory as Input_file_name_decoded.txt
