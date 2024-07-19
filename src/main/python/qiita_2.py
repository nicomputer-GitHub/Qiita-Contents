my_list = [5, 2, 3]
print(my_list)
my_list[0] = 1
print(my_list)

my_tuple = (5, 2, 3)
print(my_tuple)
my_tuple[0] = 1
print(my_tuple)

numbers = [1, 2, 3]
total = 0
for number in numbers:
    total = total + number    
print(total)

for n in 'nicomputer🍃':
    print(n)

for n in range(10, 15):
    print(n)
  
d = {'nicomputer🍃': 10, "Python💻": 2}
print(d["nicomputer🍃"])
print(d["Python💻"])

d = {'nicomputer🍃': 10, "Python💻": 2}
print(d)
d["学習"] = 1
print(d)

d = {"nicomputer🍃": 10,"Python💻": 2,"学習": 1}
print(d)
del d["Python💻"]
print(d)

d = {"nicomputer🍃": 10,"Python💻": 2,"学習": 1}
print(len(d))

d = {"nicomputer🍃": 10,"Python💻": 2,"学習": 1}
x = input("文字列を入力してください：")
if x in d:
    print("辞書にあります〇")
else:
    print("辞書にありません×")

d = {"nicomputer": 10,"Python": 2,"学習": 1}
for key in d.keys():
    print(key)

d = {"nicomputer": 10,"Python": 2,"学習": 1}
for value in d.values():
    print(value)

import math
math.sqrt(4)

!pip install streamlit
import streamlit as st









