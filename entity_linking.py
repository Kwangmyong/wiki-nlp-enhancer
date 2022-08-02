# -*- coding: utf-8 -*-

import sys
from wikipedia2vec.dictionary import Dictionary
from wikipedia2vec.mention_db import MentionDB
from wikipedia2vec.utils.tokenizer.mecab_tokenizer import MeCabTokenizer

dic = Dictionary.load(sys.argv[2])
db = MentionDB.load(sys.argv[3], dic)
with o