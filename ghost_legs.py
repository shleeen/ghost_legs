import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

w, h = [int(i) for i in input().split()]

print(w, h)
answer = {}

# number of T and B =>
cols = 0
for i in range(w):
    if i%3 == 0:
        cols += 1

print("cols", cols)

print("starting loop")
for i in range(h):
    if i==0:
        line = input() # gets one entire line :) heck yeah that makes life a lot easier
        print(line)
        
        for item in line:
            # if a letter then follow path
            if item != " ":
                
                answer[item] = 0


    # elif i==(h-1):
    #     number = input()
    #     print(number)
    # else:
    #     line = input()

    # if '|'
    #     if '-'
    #         // go to next row


    # print(input())

print("end loop")
    

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

# output the answer
print("--------------")
for i in range(len(answer)):
    print(str(list(answer.keys())[i])+str(list(answer.values())[i]))
    # print("\n")
