def get_char_freq(file_path):
    data = None
    try:
        with open(file_path, "r") as fh:
            data = fh.read()
    except Exception:
        return None
    freq_map = {}
    for char in data:
        freq_map[char] = freq_map.get(char, 0) + 1
    return freq_map
