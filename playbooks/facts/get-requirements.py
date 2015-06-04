#!/bin/env python
# -*- coding: utf-8 -*-


import json
import sys
import os
import re


project_dir = sys.argv[1]
requirements_file = os.path.join(project_dir, 'requirements.txt')
if not os.path.exists(requirements_file):
    print json.dumps([])

with open(requirements_file) as f:
    p = re.compile('[\w.-]+')
    for line in f:
      line = line.strip()
      if line and not line.startswith('#'):
          out = p.search(line.strip()).group(0)
          if out:
              print out
