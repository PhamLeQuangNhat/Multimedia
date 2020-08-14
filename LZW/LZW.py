class LZWCoding:
    def Compress(self, data):
        
        dictionary_table = { chr(c):c for c in range(0,5000) }
        key_list = dictionary_table.keys()
        code = 255
        code_list = []
        len_string = len(data)
        index = 0
        
        c = data[index]
        
        while(index < len_string - 1):
            
            s = data[index + 1]
            if c + s not in key_list:
                
                code += 1
                dictionary_table[c + s] = code
                code_list.append(dictionary_table[c])
                index += 1
                c = s
            
            else:
                
                c = c + s
                index += 1
                
        code_list.append(dictionary_table[c])   
        
        return code_list
    
    def Decompress(self, codes):
        
        dictionary_table = {c: chr(c) for c in range(0, 256)}
        code = 255
        
        s = ""
        entries = []
        Str = ""
        
        for k in codes:
            
            entry = dictionary_table.get(k, "")
            
            if entry is "":
                entry = s + s[0]
            Str += entry
            
            if s is not "":
                code += 1
                dictionary_table[code] = s + entry[0]
            s = entry
            
        return Str