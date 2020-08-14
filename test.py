import os
import argparse

from Arithmatic import demo_arithmatic 
from LZW import demo_LZW
from Huffman import demo_huffman
from RLC import demo_RLC
from Shannon_Fano import demo_shannon

textPaths = os.listdir("Data")
time_exe_encode = 'time_exe_encode.txt'
time_exe_decode = 'time_exe_decode.txt'
compression_ratio = 'compression_ratio.txt'
compression_ratio_not_freq = 'compression_ratio_not_freq.txt'

def option():
    ap = argparse.ArgumentParser(description="The algorithm")
    ap.add_argument("-a", "--algorithm", required=True,
                    choices=['Arithmatic','Huffman','LZW','RLC','Shannon'])
    ap.add_argument("-t", "--type", required=True,
                    choices=['encode', 'decode'],
                    help="Choice Encode or Decode")

    args = vars(ap.parse_args())
    return args

def main():
    args = option()
    if args['algorithm'] == 'Arithmatic':

        base_encode = 'Result/Arithmatic/Output_encode/'
        base_decode = 'Result/Arithmatic/Output_decode/'

        if args['type'] == 'encode':

            demo_arithmatic.encode(textPaths,base_encode,time_exe_encode, compression_ratio, compression_ratio_not_freq)
                
        if args['type'] == 'decode':

            demo_arithmatic.decode(base_encode, base_decode,time_exe_decode)
            
    if args['algorithm'] == 'Huffman':

        base_encode = 'Result/Huffman/Output_encode/'
        base_decode = 'Result/Huffman/Output_decode/'

        if args['type'] == 'encode':

            demo_huffman.encode(textPaths,base_encode,time_exe_encode, compression_ratio,compression_ratio_not_freq)

        if args['type'] == 'decode':

            demo_huffman.decode(base_encode, base_decode,time_exe_decode)

            
    if args['algorithm'] == 'LZW':

        base_encode = 'Result/LZW/Output_encode/'
        base_decode = 'Result/LZW/Output_decode/'

        if args['type'] == 'encode':

            demo_LZW.encode(textPaths,base_encode,time_exe_encode, compression_ratio,compression_ratio_not_freq)
            
        if args['type'] == 'decode':

            demo_LZW.decode(base_encode, base_decode,time_exe_decode)
    
    if args['algorithm'] == 'RLC':

        base_encode = 'Result/RLC/Output_encode/'
        base_decode = 'Result/RLC/Output_decode/'

        if args['type'] == 'encode':

            demo_RLC.encode(textPaths,base_encode,time_exe_encode, compression_ratio,compression_ratio_not_freq)
            
        if args['type'] == 'decode':

            demo_RLC.decode(base_encode, base_decode,time_exe_decode)

    if args['algorithm'] == 'Shannon':

        base_encode = 'Result/Shannon_Fano/Output_encode/'
        base_decode = 'Result/Shannon_Fano/Output_decode/'

        if args['type'] == 'encode':

            demo_shannon.encode(textPaths,base_encode,time_exe_encode, compression_ratio,compression_ratio_not_freq)
            
        if args['type'] == 'decode':

            demo_shannon.decode(base_encode, base_decode,time_exe_decode)

if __name__ == "__main__":
    main()

    
        
            


