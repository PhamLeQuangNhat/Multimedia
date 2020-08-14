from .node import Node
from queue import PriorityQueue
from .utility import *
class Huffman:
    def __init__(self, frequencies):
        self.freq = frequencies

    def priority_queue(self, a = 0):
        q = PriorityQueue()
        for k, v in self.freq.items():
            n = Node(k, v)
            q.put((n.freq, n))
        return q
    
    def build_tree(self, a = 0):
        # Build Huffman tree and return its root 
        q = self.priority_queue(self.freq)
        
        while q.qsize() > 1:
            left = q.get()[1]
            right = q.get()[1]

            new_node = Node('', left.freq + right.freq, left, right)
            q.put((new_node.freq, new_node))

        root = q.get()[1]
        return root
    
    def Compress(self, data):
        root = self.build_tree(self.freq)
        encoded_str = get_encoded_str(root, data)
        return encoded_str

    def Decompress(self, code):
        root = self.build_tree(self.freq)
        decoded_str = get_decoded_str(root, code)
        return decoded_str


