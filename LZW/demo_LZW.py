from LZW import LZWCoding
import os
import collections
import pickle
import time 

def encode(textPaths, base_encode, time_exe_encode, compression_ratio):
    stt = 0
    path_ratio_LZW = 'Result/LZW/ratio_LZW.txt'

    #print(len(textPaths))
    for textPath in textPaths:
       
        textPath = 'Data/' + textPath
        with open(textPath,'r') as f:
            string = f.read()
        #print("[INFO] Path = {}".format(textPath))
        store_path = 'Result/LZW/store.txt'
        output_path = base_encode +'output' + str(stt) + '.txt'

        start_time = time.time()

        lzw = LZWCoding()
        values = lzw.Compress(string)

        end_time = time.time()
        
        #print("[INFO] The value encoded: {}".format(values))
        diff_time = (end_time - start_time) * 1000
        print("==========================================================")
        print('[INFO] Total run-time: {} ms'.format(diff_time))

        with open(time_exe_encode, 'a+') as f:
            f.write(str(diff_time)+'\n')

        with open(store_path, 'wb') as f:
            pickle.dump(values, f)
    
        with open(output_path, 'wb') as f:
            pickle.dump(values, f)

        # Number of bits before compressing 
        uncompressed_size = os.stat(textPath).st_size*8
        #print('[INFO] Uncompressed size: {} bits'.format(uncompressed_size))

        # Number of bits after compressing 
        compressed_size = os.stat(store_path).st_size*8
        #print('[INFO] Compressed size: {} bits'.format(compressed_size))

        # Calculate compression ratio 
        print('[INFO] Compression ratio = {0} / {1} = {2:.3f}'.format(
                            uncompressed_size, compressed_size,
                            uncompressed_size / compressed_size))
        print("==========================================================")

        with open(compression_ratio, 'a+') as f:
            f.write(str(uncompressed_size / compressed_size)+'\n')

        with open(path_ratio_LZW, 'a+') as f:
            f.write(str(uncompressed_size / compressed_size)+'\n')
        
        stt += 1

def decode(base_encode, base_decode, time_exe_decode):
    inputPaths = os.listdir(base_encode)
    stt = 0

    for inputPath in inputPaths:
        inputPath = base_encode + inputPath
        outputPath = base_decode + 'output'+ str(stt) + '.txt'

        with open(inputPath, 'rb') as f:
            data = pickle.load(f)

        start_time = time.time()

        lzw = LZWCoding()
        result = lzw.Decompress(data)

        end_time = time.time()
        diff_time = (end_time - start_time) * 1000

        print("[INFO] Result decode: {}".format(result))
        print('[INFO] Total run-time: {} ms'.format(diff_time))

        with open(time_exe_decode, 'a+') as f:
            f.write(str(diff_time)+'\n')

        # write result file 
        with open(outputPath, 'w+') as f:
            f.write(result)
        stt += 1
    