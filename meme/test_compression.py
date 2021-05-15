# -*- coding: iso-8859-1 -*-

p = r"C:\Users\User\PycharmProjects\ShellGhost\out\copy.py"

with open(p, 'rb') as f:
    original_data = f.read()

encoding = 'iso-8859-1'

n_token = "baaaaaaaaaaaa"
r_token = "cbbbbbbbbbbbb"
b_token = "dcccccccccccc"
import zlib


def encode(data):
    """has some randomness to it due to gzip.compress"""
    zipped = zlib.compress(data)
    as_str = zipped.decode(encoding)
    as_str = as_str.replace("\n", n_token)
    as_str = as_str.replace("\r", r_token)
    return as_str


def decode(data):
    data = data.replace(n_token, "\n")
    data = data.replace(r_token, "\r")
    data = data.encode(encoding)
    return zlib.decompress(data)


limit = 90 * 1000
original_data = original_data[:limit]
as_str = encode(original_data)
decoded = decode(as_str)
assert decoded == original_data

write_path = "test_compression.py"
token = "#comm"
token += "ent="
writing = True
# writing = False

with open(write_path, 'a', encoding=encoding) as f:
    data = as_str
    if writing:
        f.write("# -*- coding: iso-8859-1 -*-\n")
        f.write(token)
        f.write(data)

with open(write_path, encoding=encoding) as f:
    # data = f.readlines()[1]
    data = f.read()
    ind = data.find(token)
    if ind == -1:
        raise ValueError("encoded data not found")
    data = data[ind + len(token):]
    print(ind, len(data))
    decoded2 = decode(data)
    print(len(decoded2))
    assert decoded == decoded2