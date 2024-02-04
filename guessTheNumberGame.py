import random

n = int(input('１つ目の数字を入力してください：'))
m = int(input('２つ目の数字を入力してください：'))

# 最小値がn, 最大値がmになるようにする
if n > m:
    o = n
    n = m
    m = o

randomInt = random.randint(n, m)

answer = int(input('数字を予想してください：'))

def checkAnswer(answer):
    if answer == randomInt:
        return '正解です！！'
    else:
        answer = int(input('不正解です。もう一度予想を入力してください：'))
        return checkAnswer(answer)

print(checkAnswer(answer))