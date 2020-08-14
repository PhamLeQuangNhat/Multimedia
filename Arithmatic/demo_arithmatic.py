from .Arithmatic import ArithmaticCoding
import os
import pickle
import argparse
import time 
import collections

TERMINATOR = "$"

def probability_table(data):

    length_input = len(data)
    low_prob = 0.
    freq = collections.Counter(data)
    table = dict()

    for key, value in freq.items():
        _range = value / length_input
        table[key] = (low_prob, low_prob + _range)
        low_prob = low_prob + _range

    return table

def calculate_size(binary, output_file):
    num = len(binary)
    compressed_size = os.stat(output_file).st_size*8
    compressed_size = num + compressed_size
    return compressed_size

def encode(textPaths, base_encode, time_exe_encode, compression_ratio):
    stt = 0
    path_ratio_arith = 'Result/Arithmatic/ratio_arith.txt'
    for textPath in textPaths:
        #print(textPath)
        textPath = 'Data/' + textPath
        with open(textPath,'r') as f:
            string = f.read()
            string += TERMINATOR
        
        store_path = 'Result/Arithmatic/store.txt'
        output_path = base_encode +'output' + str(stt) + '.txt'

        start_time = time.time()

        table = probability_table(string)

        # Encode information source 
        ArthCode = ArithmaticCoding(table, "$")
        (value, binary) = ArthCode.Compress(string)

        end_time = time.time()
        diff_time = (end_time - start_time) * 1000

        #print("[INFO] The value encoded: {}".format(value))
        #print("[INFO] The binary representation: {}".format(binary))

        print("==========================================================")
        print('[INFO] Total run-time: {} ms'.format(diff_time))

        with open(time_exe_encode, 'a+') as f:
            f.write(str(diff_time)+'\n')

        with open(store_path, 'wb') as f:
            pickle.dump(table, f)
    
        with open(output_path, 'wb') as f:
            pickle.dump((binary, table), f)

        # Number of bits before compressing 
        uncompressed_size = os.stat(textPath).st_size*8
        #print('[INFO] Uncompressed size: {} bits'.format(uncompressed_size))

        # Number of bits after compressing 
        compressed_size = calculate_size(binary, store_path)
        #print('[INFO] Compressed size: {} bits'.format(compressed_size))

        # Calculate compression ratio 
        print('[INFO] Compression ratio = {0} / {1} = {2:.3f}'.format(
                            uncompressed_size, compressed_size,
                            uncompressed_size / compressed_size))
        print("==========================================================")

        with open(compression_ratio, 'a+') as f:
            f.write(str(uncompressed_size / compressed_size)+'\n')

        with open(path_ratio_arith, 'a+') as f:
            f.write(str(uncompressed_size / compressed_size)+'\n')

        stt += 1

def decode(base_encode, base_decode,time_exe_decode):
    inputPaths = os.listdir(base_encode)
    stt = 0

    for inputPath in inputPaths:
        inputPath = base_encode + inputPath
        outputPath = base_decode + 'output'+ str(stt) + '.txt'

        with open(inputPath, 'rb') as f:
            (code, table) = pickle.load(f)

        start_time = time.time()
        
        ArthCode = ArithmaticCoding(table, "$")
        result = ArthCode.Decompress(code)

        end_time = time.time()
        diff_time = (end_time - start_time) * 1000

        print("[INFO] The encoded binary: {}".format(code))
        print("[INFO] Result decode: {}".format(result))
        print('[INFO] Total run-time: {} ms'.format(diff_time))

        with open(time_exe_decode, 'a+') as f:
            f.write(str(diff_time)+'\n')

        # write result file 
        with open(outputPath, 'w+') as f:
            f.write(result)
        stt += 1
