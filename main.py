import math, queue
from collections import Counter

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    ## This function is done.
    ## Given any file name, this function reads line by line to count the frequency per character. 
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return(dict(C.most_common()))

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        # TODO
        left = p.get()
        right = p.get()
        p.put(TreeNode(left, right, (left.data[0] + right.data[0], "")))
    # return root of the tree
    return p.get()

# perform a traversal on the prefix code tree to collect all encodings
def get_code(node, prefix="", code={}):
    # TODO - perform a tree traversal and collect encodings for leaves in code
    # if both left & right nodes are empty, then it just updates the prefix with the data at index 1
    if ((node.left == None) and (node.right == None)):
        code[node.data[1]] = prefix
    # if the left node isn't empty, then it calls the get_code function recursively and adds '0' to the prefix
    if (node.left != None):
        get_code(node.left, prefix + "0", code)
    # if the right node isn't empty, then it calls the get_code function recursively and adds '1' to the prefix
    if (node.right != None):
        get_code(node.right, prefix + "1", code)
        
    return code

# given an alphabet and frequencies, compute the cost of a fixed length encoding
def fixed_length_cost(f):
    # TODO
    # cost of string is length of string * cost of every char (should be the same)
    # math.ceil(log2(3)) to calculate number of bits needed for every char
    bits = math.ceil(math.log2(len(f.keys())))
    total_cost = 0
    # uses for loop to add all of the calculations together
    for i in f.keys():
        total_cost += (bits * f[i])
    return total_cost

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    # TODO
    # number of each character * cost for the character
    # cost of every char is the depth of the char in the tree
    # every leaf will correspond to every char you're encoding
    # generate a dict that maps from cost to char by traversing tree and add char whenever you get to a leaf along w the depth of the char in the tree
    # length of encoding from get_code is the cost
    # loop to calculate number of bits in each char, then multiply by the frequency
    total_cost = 0
    for i in f.keys():
        total_cost += (len(C[i]) * f[i])
    return total_cost

file_list = ['f1.txt', 'alice29.txt', 'asyoulik.txt', 'grammar.lsp', 'fields.c']

for filename in file_list:
    f = get_frequencies(filename)
    print("Fixed-length cost:  %d" % fixed_length_cost(f))
    
    T = make_huffman_tree(f)
    C = get_code(T)
    print("Huffman cost:  %d" % huffman_cost(C, f))
    
    huffman_fixed_ratio = fixed_length_cost(f) / huffman_cost(C, f)
    print("Huffman vs. fixed-length ratio: %f" % huffman_fixed_ratio)