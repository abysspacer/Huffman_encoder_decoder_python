from utils import get_char_freq
import argparse

class Node:

    right = None
    left = None

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq

# create parser
parser = argparse.ArgumentParser(description="Huffman encoder decoder")

# add flags
parser.add_argument("file_path", type=str, nargs="+", help="specify target file(s)")

# parse flags
args = parser.parse_args()

for f in args.file_path:
    char_freq_map = get_char_freq(f)
    freq_sorted_list = sorted([Node(char, freq) for (char, freq) in char_freq_map.items()], key=lambda x: x.freq, reverse=True) 
    while len(freq_sorted_list) >= 2:
        node1 = freq_sorted_list.pop()
        node2 = freq_sorted_list.pop()
        new_node = Node(None, node1.freq + node2.freq)
        new_node.right = node1
        new_node.left = node2
        freq_sorted_list.append(new_node)
    tree = None
    if len(freq_sorted_list):
        tree = freq_sorted_list[0]
