import subprocess
import os
import shutil
import argparse

# params:
from pprint import pprint

from utils.comments_and_strings import remove_comments_and_docstrings

remove_file_description = True
remove_pyminifier_comment = True

"""
currently remove_file_description is mandatory because pyminifier on (networkx\\release.py) don't work properly with 
file comment.
this is also why we read write before pyminifier and after... (pyminifier also read+write) 
this could be massively improved :)
"""


def minify(i, o):
    os.makedirs(os.path.dirname(o), exist_ok=True)
    try:
        if not os.stat(i).st_size:
            shutil.copy(i, o)
            return
        with open(i, "r", encoding="utf-8") as f:
            data = f.read()
            data = remove_comments_and_docstrings(data)
        if remove_file_description:
            multi_comment = "\"\"\""
            if data[:3] == multi_comment:
                end = data[3:].index(multi_comment)
                data = data[end + len(multi_comment) * 2:]
        with open(o, "w", encoding="utf-8") as f:
            f.write(data)
        subprocess.check_call(f"pyminifier -o {o} {o}")
        with open(o, "r+", encoding="utf-8") as f:
            data = f.read()
            original_data = data
            if remove_pyminifier_comment:
                data = data.replace(r"# Created by pyminifier (https://github.com/liftoff/pyminifier)", '')
            if len(data) < len(original_data):
                f.seek(0)
                f.write(data)
                f.truncate()
    except Exception as e:
        print(f"file {i} failed with {e}")  # TODO: print stacktrace
        shutil.copy(i, o)


if __name__ == '__main__':
    dest = r"C:\Users\User\PycharmProjects\ShellGhost\out"
    site_path = "C:\\Users\\User\\PycharmProjects\\ShellGhost\\venv\\lib\\site-packages\\"

    from modulefinder import ModuleFinder

    finder = ModuleFinder()
    finder.run_script("..\\meme\\meme1.py")
    for k, v in finder.modules.items():
        p = v.__file__
        if p:
            m_p = p.replace(site_path, "")
            dirname = m_p.split(os.sep)[0]
            if dirname in ["networkx"]:
                o = os.path.join(dest, m_p)
                minify(p, o)