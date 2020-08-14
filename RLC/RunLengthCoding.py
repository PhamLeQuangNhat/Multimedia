class RLC:
    def __init__(self):
        self.encode = ''
        self.decode = ''
    def Compress(self,string):
        length = len(string)
        i = 0
        while i < length:
            begin = i
            dem = 0
            if begin < length:
                pass
            else:
                begin = i
            for j in range(begin,length):
                if string[begin] != string[j]:
                    break
                else:
                    dem += 1
                i += 1
            self.encode = self.encode + string[begin]
            self.encode = self.encode + str(dem)
        
        return self.encode
       
    def Decompress(self, string):
        num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        index = 0
        char = ""
        num = ""
        flag = True
        len_string = len(string)
        while index < len_string:
            if string[index] not in num_list:
                if flag:
                    char = string[index]
                    flag = False
                else:
                    len_st = int(num)
                    for i in range(len_st):
                        self.decode += char
                    char = string[index]
                    num =""
            else:
                num += string[index]
            index += 1
        len_st = int(num)
        for i in range(len_st):
            self.decode += char
        return self.decode