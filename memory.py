import os

textPaths = os.listdir("Data")

memory_path = 'memory.txt'

for textPath in textPaths:
    textPath = 'Data/' + textPath
    Size = os.stat(textPath).st_size

    with open(memory_path,'a+') as f:
        f.write(str(Size)+'\n')