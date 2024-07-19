print("ここに表示したい文字列を入力します")
print("Pythonを学びましょう💻")

print(10 + 2)

print('筆者の名前は{}🍃、学習中の言語は{}です💻'.format("nicomputer", "Python"))

input("ここに表示したい文字列を入力してください：")

-10 + 2 # -8
-10.0 + 2 # -8

2 - 10 # -8
2.0 - 10 # -8

2 - 10 # -8
2.0 - 10 # -8

10 / 2 # 5
10.0 / 2 # 5

2 // 10 # 0
2.0 // 10 # 0

10 % 3 # 1
10.0 % 3 # 1

10 ** 2 # 100
10.0 ** 2 # 100

print("Pythonを" + "学びましょう💻")
print("Python" * 3)

print(2 + "2")

print(2 + int("2"))

print(type("Pythonを学びましょう!!"))

name = "nicomputer🍃"
print(name)

tate = 10 
yoko = 2 
area = tate * yoko 
print(area)

print(10 == 10) 
print(10 == 2) 

True and False

temperature = int(input("気温を入力してください："))
if 25 < temperature:
    print('暖かいので走りに行きましょう🏃')
elif temperature < 0:
    print('寒いのでゲームをしましょう🎮')
else:
    print('Pythonを学びましょう💻')

x = int(input("数を入力してください："))
total = 0
i = 1
while i <= x:
    total = total + i
    i = i + 1
print(total)

while True:
    number = input('数を入力してください：')
    print(number)
    if number == '0':
        break
print(number)

print('3人の大学生の50m走のタイムを入力してください🏃')
total = 0
i = 0
while i < 3:
    time = float(input('タイムを入力してください⏱：'))
    if time < 0:
        print('0以上の数で入力してください')
        continue
    total = total + time
    i = i + 1
print('平均タイム：', total / 3)

abs(-2)

x = input("数を入力してください：")
y = input("数を入力してください：")
ans = max(int(x), int(y))
print(ans)

x = input("数を入力してください：")
y = input("数を入力してください：")
ans = min(int(x), int(y))
print(ans)

def python_learning():
    print('Pythonを学びましょう💻')
print('print関数によって表示されます')
python_learning()

def print_number():
    number = '2'
    print(number)
print_number()
print(number)

def area(tate, yoko):
    return tate * yoko
result = area(2, 10)
print(result)

word = input("文字列を入力してください：")
ans = input("文字列を入力してください：")
print(word.count(ans))

text = 'I am nicomputer.🍃'
print(text.replace('nicomputer', 'not nicomputer'))
print(text)

number = ["1", "2", "3", "4", "5"]
print(number)
print(number[0])
print(number[-1])

text = "nicomputer🍃"
print(text[0:2])
print(text[:2])
print(text[2:])

numbers = [1, 2, 4]
print(numbers[2])
numbers[2] = 3
print(numbers)

numbers = [1, 2, 3]
print(numbers)
del numbers[2]
print(numbers)

print(list(range(10)))
print(list(range(10,15)))

numbers = [1, 2, 3]
print(len(numbers))

numbers = [1, 2, 3]
i = 0
total = 0
while i < len(numbers): 
    total = total + numbers[i]
    i = i + 1 
print(total)

numbers = [1, 2, 3]
print(numbers)
numbers.append(4)
print(numbers)

numbers = [1, 3, 4]
print(numbers)
numbers.insert(1, 2)
print(numbers)

numbers = [1, 2, 3]
print(numbers)
numbers.remove(3)
print(numbers)

numbers = [1, 2, 3]
x = int(input("数を入力してください："))
if x in numbers:
    print("リストにあります〇")
else:
    print("リストにありません×")

































