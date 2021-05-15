c = "ᳶ"
acc = ""
size = int((2 ** 16) * 1)
split_by = 2 ** 10
with open(".\\r.txt", 'w', encoding='utf-16') as f:
    for i in range(size // split_by):
        acc += c * split_by
        acc += "\n"
    acc += c * (size % split_by)
    f.write(acc)
