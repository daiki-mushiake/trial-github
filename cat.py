import sys

#cnt = 0

for line in sys.stdin:
    file_data = open(line.rstrip('\n'), "r")
    cnt = 0

    for character in file_data:
        print(str(cnt) + " "  + character, end="")
        cnt += 1

