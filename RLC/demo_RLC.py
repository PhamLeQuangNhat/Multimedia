from .RunLengthCoding import RLC
import os
import pickle
import time

def encode(textPaths, base_encode, time_exe_encode, compression_ratio):
    stt = 0 
    path_ratio_rlc = 'Result/RLC/ratio_rlc.txt'
    for textPath in textPaths:

        textPath = 'Data/' + textPath
        with open(textPath,'r') as f:
            string = f.read()

        #store_path = 'Result/LZW/store.txt'
        output_path = base_encode +'output' + str(stt) + '.txt'

        start_time = time.time()

        rlc = RLC()
        values = rlc.Compress(string)

        end_time = time.time()

        #print("[INFO] The value encoded: {}".format(values))
        diff_time = (end_time - start_time) * 1000
        print("==========================================================")
        print('[INFO] Total run-time: {} ms'.format(diff_time))

        with open(time_exe_encode, 'a+') as f:
            f.write(str(diff_time)+'\n')
    
        with open(output_path, 'w+') as f:
            f.write(values)

        # Number of bits before compressing 
        uncompressed_size = os.stat(textPath).st_size*8
        #print('[INFO] Uncompressed size: {} bits'.format(uncompressed_size))

        # Number of bits after compressing 
        compressed_size = os.stat(output_path).st_size*8
        #print('[INFO] Compressed size: {} bits'.format(compressed_size))

        # Calculate compression ratio 
        print('[INFO] Compression ratio = {0} / {1} = {2:.3f}'.format(
                            uncompressed_size, compressed_size,
                            uncompressed_size / compressed_size))
        print("==========================================================")
        with open(compression_ratio, 'a+') as f:
            f.write(str(uncompressed_size / compressed_size)+'\n')

        with open(path_ratio_rlc, 'a+') as f:
            f.write(str(uncompressed_size / compressed_size)+'\n')

        stt += 1

def decode(base_encode, base_decode, time_exe_decode):
    inputPaths = os.listdir(base_encode)
    stt = 0

    for inputPath in inputPaths:
        inputPath = base_encode + inputPath
        outputPath = base_decode + 'output'+ str(stt) + '.txt'

        with open(inputPath, 'r') as f:
            data = f.read()

        start_time = time.time()

        rlc = RLC()
        result = rlc.Decompress(data)

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