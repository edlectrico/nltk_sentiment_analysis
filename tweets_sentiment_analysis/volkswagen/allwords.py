import pandas as pd
import os
import sys

input_csv = pd.read_csv('output/vw_clean_en_rechecked.csv')
input_df = pd.DataFrame(data=input_csv)

# df = input_df['text']

f = open('output/all_words.txt', 'w')

for index, row in input_df.iterrows():
  try:
    row_words = str(row['text'])
    words = row_words.split(' ')
    for word in words:
      f.write(word + '\n')
  except KeyboardInterrupt:
    print 'Exiting...'
    sys.exit()
