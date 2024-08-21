from utils import get_char_freq
import argparse

parser = argparse.ArgumentParser(description="Huffman encoder decoder")

parser.add_argument("file_path", type=str, nargs="+", help="specify target file(s)")

args = parser.parse_args()

for f in args.file_path:
    char_freq_map = get_char_freq(f)
