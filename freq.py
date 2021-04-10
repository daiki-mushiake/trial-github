import sys
from collections import Counter

word_array = []
i = 0

#標準入力から開くファイル名を指定しファイルを開く
fh = open(sys.argv[1],'r')


#ファイルから一行ごとにデータを読み込む
line_data = fh.readlines()
#print(line_data)

#一行ごとのデータを単語ごとに分割する
for line in line_data:
    for data in line.rsplit(' '):
        #print(data)
        word = data.rstrip('\n')
        #print(word)
        word_array.insert(i,word)
        i += 1
        
#print(word_array)

#現れた単語の回数をカウントする
#for char in word_array:
 #   print(char)
a = Counter(word_array)

#カウント数と単語を出力する
#for result in Counter:   
print(a)
