
# -*- coding: utf-8 -*-

import sys
from wikipedia2vec.dictionary import Dictionary
from wikipedia2vec.mention_db import MentionDB

dic = Dictionary.load(sys.argv[1])
db = MentionDB.load(sys.argv[2], dic)
words = set()