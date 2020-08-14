class ArithmaticCoding:
    def __init__(self, table, terminator):
        self.table = table
        self.terminator = terminator 

    def __GetBinaryFractionValue(self, binaryFraction):
        value = 0
        power = 1
        
        # Git the fraction bits after "."
        fraction = binaryFraction.split('.')[1]

        # Compute the formula value
        
        for i in fraction:
            value += ((2 ** (-power)) * int(i))
            power += 1
        return (value, fraction)
        #return value

    def value_to_bin(self,low,high):
        val = 0
        check = 0
        bins = ""
        print("Low = {}".format(low))
        whole, decimal = str(low).split(".")
        decimal = int(decimal)
        print("whole = {}, decimal = {}".format(low,decimal))
        for j in range(1,32):
            check = val + 2**(-j)
            if check >= high :
                bins += "0"
            else:
                bins += "1"
                val = check 
            if low < val < high:
                break
        #print("BIN = {}".format(bins))
        return (val,bins)

    def binary_to_float(self, code):
        # Git the fraction bits after "."
        whole, decimal = code.split(".")
        value = 0
        k = -1
        for digit in decimal:
            value += int(digit) * 2**k
            k -= 1
        return value
    
    def Compress(self, word):
        lowOld = 0.
        highOld = 1.
        _range = 1.
        
        # Iterate through the word to find the final range.
        for c in word:
            low  = lowOld + _range * self.table[c][0]
            high = lowOld + _range * self.table[c][1]
            _range = high - low

            # Updete old low & hihh
            lowOld = low#round(low,100000)
            highOld = high#round(high,100000)#10000000000000000)
        
        # Generating code word for encoder.
        code = ["0", "."] # Binary fractional number
        k = 2             # kth binary fraction bit
        #result = self.value_to_bin(low,high)
        #(value, fraction) = self.__GetBinaryFractionValue("".join(code))
        #temp = 2
        #epi = 0.0000000000001
        #high = high - epi 
        #print(epi)
        value = 0
        #print("Low = {}, High = {}".format(low,high))
        while(value < low):
            # Assign 1 to the kth binary fraction bit
            code.append('1')
            (value,fraction) = self.__GetBinaryFractionValue("".join(code))
            #value = value - 0.000000001
            if value > high :
                # Replace the kth bit by 0
                code[k] = '0'
            (value,fraction) = self.__GetBinaryFractionValue("".join(code))
            k += 1
        
        """
        if value == high :
            code[k-1] = '0'
            (value,fraction) = self.__GetBinaryFractionValue("".join(code))
            while value < low:
                code.append('1')
                (value,fraction) = self.__GetBinaryFractionValue("".join(code))
                if value > high :
                # Replace the kth bit by 0
                    code[k] = '0'
                (value,fraction) = self.__GetBinaryFractionValue("".join(code))
                k += 1
            #code[k] = '1'
            #code.append('1')
        #(value,fraction) = self.__GetBinaryFractionValue("".join(code))
        print("value = {}".format(value))
        """
        #(value,fraction) = self.value_to_bin(low,high)        
        string = "0."+fraction
        #value = self.__GetBinaryFractionValue(string)
        return (value,string)
    
    def Decompress(self, code):
        value = self.binary_to_float(code)
        
        s = "" # flag to stop the while loop
        result = ""
        while (s != self.terminator):
            # find the key which has low <= code and high > code
            for key, t in self.table.items():
                if (value >= self.table[key][0] and value < self.table[key][1]):
                    result += key 
                    # update low, high, code
                    low = self.table[key][0]
                    high = self.table[key][1]
                    _range = high - low
                    value = (value - low)/_range
                    # chech for the terminator
                    
                    if (key == self.terminator):
                        s = key
                        break
                    
        return result
        
        
        
         
