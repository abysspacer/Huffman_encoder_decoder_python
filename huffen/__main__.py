from utils import get_char_freq
import argparse

def get_huffman_tree(char_freq_map):
    freq_sorted_list = sorted([Node(char, freq) for (char, freq) in char_freq_map.items()], key=lambda x: x.freq, reverse=True) 
    while len(freq_sorted_list) >= 2:
        node1 = freq_sorted_list.pop()
        node2 = freq_sorted_list.pop()
        new_node = Node(None, node1.freq + node2.freq)
        new_node.right = node1
        new_node.left = node2
        freq_sorted_list.append(new_node)
        freq_sorted_list.sort(key=lambda x: x.freq, reverse=True)
    if len(freq_sorted_list):
        return freq_sorted_list[0]
    return None

def get_prefix_code_map(node, prefix_code, prefix_map):
    if not node:
        return
    if node.char:
        prefix_map[node.char] = prefix_code
    get_prefix_code_map(node.right, prefix_code + "1", prefix_map)
    get_prefix_code_map(node.left, prefix_code + "0", prefix_map)
    return prefix_map

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
    tree = get_huffman_tree(char_freq_map)
    prefix_code_map = get_prefix_code_map(tree, "", {})
    for (k, v) in prefix_code_map.items():
        print(f"{k}: {v}\n")
