#! /usr/bin/env python3

import xml.etree.ElementTree as ET
import sys
import base64
import os
PREFIX="data:image/png;base64,"
ATTR="{http://www.w3.org/1999/xlink}href"
DEFAULT_NS="http://www.w3.org/2000/svg"
with open(sys.argv[1]) as f:
    root = ET.parse(f)
    file_id = 1
    base_name = os.path.splitext(sys.argv[1])[0]
    for e in root.findall(".//{%s}image" % DEFAULT_NS):
        href = e.get(ATTR)
        if href and href.startswith(PREFIX):
            n_file_name = "%s%d.png" % (base_name, file_id)
            with open(n_file_name, "wb") as f2:
                f2.write(base64.b64decode(href[len(PREFIX):]))
                file_id += 1
                e.set(ATTR, os.path.basename(n_file_name))

root.write(sys.argv[1])