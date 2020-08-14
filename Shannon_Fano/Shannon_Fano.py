import os
import string

class Shannon_Fano:
    
    def __init__(self):
        self.Tree = []
        self.encode = ''
        self.decode = ''
        #self.freq = frequencies

    def Compress(self,string):
       
        Tree = []
        l = len(string)
        i = 0
        while self.Sum(Tree) < l:
            while string[i] in [row[0] for row in Tree]:
                i = i+1
            Tree.append([string[i],string.count(string[i])])
            i = i+1

        # Sort
        Tree.sort(key=lambda Tree: Tree[1],reverse=1)

        # Build Tree 
        len_l = len(Tree)
        self.Build_Tree(Tree,0,len_l-1)

        # Convert list to dictionary
        dic = {}
        for i in range(len_l):
            dic[Tree[i][0]] = Tree[i][1:]
        self.Tree = dic
        #print('Shannon Fano Tree',self.Tree)

        # Covert code for Shannon Fano
        for i in range(l):
            temp_str = ''
            for char in self.Tree[string[i]][1:]:
                temp_str = temp_str + str(char)
            self.encode = self.encode + temp_str

        return (self.encode ,self.Tree)

    def Decompress(self,encode,Tree):
        
        low = 0 
        high = 1
        len_code = len(encode)
        Region_Find = []
        for key in Tree.keys():
            temp = ''
            for char in Tree[key][1:]:
                temp = temp + str(char)
            Region_Find.append(temp)
        
        while low < len_code:
            while encode[low:high] not in Region_Find :
                
                if high >= len_code:
                    return self.decode
                high += 1
            
            for key in Tree.keys():
                temp = ''
                for char in Tree[key][1:]:
                    temp = temp + str(char)
                if temp != encode[low:high]:
                    continue
                else:
                   
                    self.decode = self.decode + key
                    break
            low = high
            high += 1
        
        
        return self.decode

    def Build_Tree(self,list,begin,end):

        i = begin 
        if begin <  end:
            while self.Sum_List(list,begin,i) < self.Sum_List(list,i+1,end):
                i += 1
        
            # add code 
            for j in range(begin,i+1):
                list[j].append(0)
            for j in range(i+1,end+1):
                list[j].append(1)

            # Split list 
            return self.Build_Tree(list,begin,i), self.Build_Tree(list,i+1, end)
        else:
            return list

    def Sum_List(self,list,begin,end):
    
        s = list[begin][1]
        for i in range(begin+1,end+1):
            s += list[i][1]
        return s
        
    def Sum(self,Tree):
        s = 0 
        for i in Tree:
            s += i[1]
        return s
    