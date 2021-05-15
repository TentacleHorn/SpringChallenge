import os


def walk_files(p, topdown=True):
    for parent, dirs, files in os.walk(p, topdown=topdown):
        for file in files:
            current = os.path.join(parent, file)
            diff_p = os.path.relpath(current, p)
            yield diff_p
