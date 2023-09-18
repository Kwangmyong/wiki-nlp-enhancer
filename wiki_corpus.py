
# -*- coding: utf-8 -*-

import bz2
import sys
from rdflib import Graph

def read_ttl(f):
  lines = []
  for line in f:
    lines.append(line.decode('utf-8').rstrip())
    if len(lines) == 1000: #1000行をまとめて処理
      for triple in parse_lines(lines):
        yield triple
      lines = []
  if lines:
    for triple in parse_lines(lines):
      yield triple

def parse_lines(lines):