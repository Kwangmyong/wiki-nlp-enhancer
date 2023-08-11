
# -*- coding: utf-8 -*-

import sys
import Levenshtein
from collections import Counter
from wikipedia2vec.dump_db import DumpDB

dump_db = DumpDB(sys.argv[1])
pair_counter = Counter()

for (title1, title2) in dump_db.redirects():
    ops = Levenshtein.editops(title1.lower(), title2.lower())
    if len(ops) == 1:
        (op, p1, p2) = ops[0]