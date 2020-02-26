import markdown2
import os
cwd = os.getcwd()
cwd = os.path.abspath(cwd)
for root, dirs, files in os.walk(cwd):
    for name in files:
        if name.endswith(".md"):
            filename = os.path.join(root, name)
            html = markdown2.markdown_path(filename)
            filename = os.path.join(root, name.replace(".md", ".html"))
            if not os.path.exists(os.path.dirname(filename)):
                try:
                    os.makedirs(os.path.dirname(filename))
                except OSError as exc: # Guard against race condition
                    if exc.errno != errno.EEXIST:
                        raise
            Html_file = open(filename, "w")
            Html_file.write(html)
            Html_file.close()


