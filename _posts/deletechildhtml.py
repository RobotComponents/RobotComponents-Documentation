import os
cwd = os.getcwd()
cwd = os.path.abspath(cwd)
for root, dirs, files in os.walk(cwd):
    for name in files:
        if name.endswith(".html"):
            filename = os.path.join(root, name)
            os.remove(filename)


