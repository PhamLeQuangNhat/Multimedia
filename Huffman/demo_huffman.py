from .Huffman import Huffman
import os
import collections
import pickle
import time 


def calculate_size(binary, output_file):
    num = len(binary)
    compressed_size = os.stat(output_file).st_size*8
    compressed_size = num + compressed_size
    return compressed_size

def encode(textPaths, base_encode, time_exe_encode, compression_ratio, compression_ratio_not_freq):
    
    stt = 0
    path_ratio_huff = 'Result/Huffman/ratio_huff.txt'

    for textPath in textPaths:
        #print(textPath)
        textPath = 'Data/' + textPath
        with open(textPath,'r') as f:
            string = f.read()

        store_path = 'Result/Huffman/store.txt'
        output_path = base_encode +'output' + str(stt) + '.txt'

        start_time = time.time()

        # Get frequency table from data
        freq = collections.Counter(string)
        huff = Huffman(freq)
        binary = huff.Compress(string)
        
        end_time = time.time()

        #print("[INFO] The binary representation: {}".format(binary))

        diff_time = (end_time - start_time) * 1000
        print("==========================================================")
        print('[INFO] Total run-time: {} ms'.format(diff_time))
        
        with open(time_exe_encode, 'a+') as f:
            f.write(str(diff_time)+'\n')

        with open(store_path, 'wb') as f:
            pickle.dump(freq, f)
    
        with open(output_path, 'wb') as f:
            pickle.dump((binary, freq), f)
        
        # Number of bits before compressing 
        uncompressed_size = os.stat(textPath).st_size*8
        #print('[INFO] Uncompressed size: {} bits'.format(uncompressed_size))

        # Number of bits after compressing 
        compressed_size = calculate_size(binary, store_path)
        compressed_size_1 = len(binary)
        #print('[INFO] Compressed size: {} bits'.format(compressed_size))

        # Calculate compression ratio 
        print('[INFO] Compression ratio = {0} / {1} = {2:.3f}'.format(
                            uncompressed_size, compressed_size,
                            uncompressed_size / compressed_size))
        print("==========================================================")
        
        with open(compression_ratio, 'a+') as f:
            f.write(str(uncompressed_size / compressed_size)+'\n')

        with open(path_ratio_huff, 'a+') as f:
            f.write(str(uncompressed_size / compressed_size)+'\n')
    
        with open(compression_ratio_not_freq, 'a+') as f:
            f.write(str(uncompressed_size / compressed_size_1)+'\n')
        stt += 1

def decode(base_encode, base_decode, time_exe_decode):
    inputPaths = os.listdir(base_encode)
    stt = 0

    for inputPath in inputPaths:
        inputPath = base_encode + inputPath
        outputPath = base_decode + 'output'+ str(stt) + '.txt'

        with open(inputPath, 'rb') as f:
            (code, freq) = pickle.load(f)
            
        start_time = time.time()

        huff = Huffman(freq)
        result = huff.Decompress(code)

        end_time = time.time()
        diff_time = (end_time - start_time) * 1000
        print("==========================================================")
        #print("[INFO] The encoded binary: {}".format(code))
        #print("[INFO] Result decode: {}".format(result))
        print('[INFO] Total run-time: {} ms'.format(diff_time))
        print("==========================================================")

        with open(time_exe_decode, 'a+') as f:
            f.write(str(diff_time)+'\n')

        # write result file 
        with open(outputPath, 'w+') as f:
            f.write(result)
        stt += 1
