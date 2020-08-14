import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import argparse

def option():
    ap = argparse.ArgumentParser(description="The algorithm")

    ap.add_argument("-i", "--input", required=True,
                    help="Input file txt")

    ap.add_argument("-n", "--name", required=True,
                    help="Name pyplot",
                    choices=['1','2','3','4'])
    ap.add_argument("-o", "--output", required=True,
                    help="output path pyplot")

    args = vars(ap.parse_args())
    return args

def main():
    args = option()

    plt.style.use('seaborn')
    sns.set(style="darkgrid")
    plt.ylim([0,100])
    with open(args['input'],'r') as infile:
        f = [float(x) for x in infile.read().split()]

    arr = np.array(f)
    arr = arr.reshape(-1,134).transpose()

    name = ['RLC','Shannon_Fano','Huffman','Arithmatic','LZW']

    if args['name'] == '1':

        name_pyplot = 'Compare Time Execute Encode'
        name_y      = 'Time excute (ms)'

    elif args['name'] == '2':

        name_pyplot = 'Compare Time Execute Decode'
        name_y      = 'Time excute (ms)'

    elif args['name'] == '3':

        name_pyplot = 'Compare Compression Ratio Encode'
        name_y      = 'Compression ratio'
    
    elif args['name'] == '4':

        name_pyplot = 'Compare Compression Ratio Encode Not Save Frequency Table'
        name_y      = 'Compression ratio'

    plt.boxplot(arr,labels=name)
    plt.ylabel(name_y)
    plt.title(name_pyplot)
    plt.savefig(args['output'], dpi=300, bbox_inches='tight')
    #plt.show()

if __name__ == "__main__":
    main()