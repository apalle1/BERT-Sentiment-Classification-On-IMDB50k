# -*- coding: utf-8 -*-
"""config.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DECo1MhWIwGYodYKIIgorJfYWnW3zZ3S
"""

import transformers

MAX_LEN = 512
TRAIN_BATCH_SIZE = 8
VALID_BATCH_SIZE = 4
EPOCHS = 10
DIR_INPUT = '/content/gdrive/My Drive/Jigsaw/IMDB'
BERT_PATH = f'{DIR_INPUT}/input/bert_base_uncased/' 
MODEL_PATH = f'{DIR_INPUT}/model.bin' 
TRAINING_FILE = f'{DIR_INPUT}/input/imdb.csv' 
TOKENIZER = transformers.BertTokenizer.from_pretrained(
    BERT_PATH,
    do_lower_case=True
)