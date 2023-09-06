
# -*- coding: utf-8 -*-

import bz2
import sys
from rdflib import Graph

def read_ttl(f):
  lines = []
  for line in f:
    lines.append(line.decode('utf-8').rstrip())