import io
import os
import tokenize


def remove_comments_and_docstrings(source):
    io_obj = io.StringIO(source)
    out = ""
    prev_toktype = tokenize.INDENT
    last_lineno = -1
    last_col = 0

    is_doc_string = False
    for tok in tokenize.generate_tokens(io_obj.readline):
        token_type = tok[0]
        token_string = tok[1]
        start_line, start_col = tok[2]
        end_line, end_col = tok[3]
        ltext = tok[4]
        if start_line > last_lineno:
            last_col = 0
        if start_col > last_col:
            out += (" " * (start_col - last_col))
        if token_type == tokenize.COMMENT:
            pass
        elif token_type == tokenize.STRING:
            if prev_toktype not in [tokenize.INDENT, tokenize.NEWLINE] and start_col > 0:
                out += token_string
            else:
                out += "pass"
                # out += "_______ = None"
        else:
            out += token_string
        prev_toktype = token_type
        last_col = end_col
        last_lineno = end_line
    out = '\n'.join(l for l in out.splitlines() if l.strip())
    return out


def main(i_path, o_path):
    extension_filter = ['.py']

    def for_file(p, o):
        with open(p) as f:
            result = remove_comments_and_docstrings(f.read())
        os.makedirs(os.path.dirname(o), exist_ok=True)
        with open(o, 'w') as f:
            f.write(result)

    if os.path.isdir(i_path):
        os.makedirs(o_path, exist_ok=True)
        for parent_p, dirs, files in os.walk(i_path):
            for file in files:
                name, ext = os.path.splitext(file)
                if ext not in extension_filter:
                    continue
                current_p = os.path.join(parent_p, file)
                diff_p = os.path.relpath(current_p, i_path)
                o = os.path.join(o_path, diff_p)
                for_file(current_p, o)
    else:
        for_file(i_path, o_path)


def parse():
    pass


if __name__ == '__main__':
    f = r"C:\Users\User\PycharmProjects\ShellGhost\venv\Lib\site-packages\networkx\algorithms\chordal.py"
    # main("..\\app", "out\\")
    main(f, "out/meme.py")
