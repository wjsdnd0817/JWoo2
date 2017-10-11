# JWoo2

import turtle as t

t.speed(0) # 거북이 최고 속도

t.penup()
t.goto(-200,0)
t.pendown()

#바닥만들기

t.color("#CD8F49") # 바닥의 색넣기
t.pensize(2)  # 선의 굵기를 2로 조정

t.fd(30)
for x in range(30):
    t.rt(90)
    t.fd(30)
    t.rt(90)
    t.fd(30)
    t.rt(90)
    t.fd(30)
    t.rt(90)
    t.fd(60)
t.rt(90)
t.fd(30)
t.rt(90)
t.fd(30)
t.fd(900)


for x in range(5):
    t.rt(90)
    t.fd(15)
    t.rt(90)
    t.fd(30)
    for x in range(30):
        t.rt(90)
        t.fd(30)
        t.rt(90)
        t.fd(30)
        t.rt(90)
        t.fd(30)
        t.rt(90)
        t.fd(60)
    t.rt(90)
    t.fd(30)
    t.rt(90)
    t.fd(30)
    t.fd(900)
t.penup()
t.goto(0,0)
t.rt(180)
t.pendown()




# 외형 만들기

# 1층 왼쪽 기둥

t.color("#646464")

t.lt(90)
t.fd(150)
t.rt(60)
t.fd(40)
t.rt(120)
t.fd(170) # 150+40*sin60 =170
# 1층 가운데
t.rt(90)
t.fd(34.64) # 40*cos30 = 34.63
t.rt(180)
t.fd(200)
t.lt(90)
t.fd(170)
t.lt(90)
t.fd(165.36) # 150-34.64= 115.36

 # 2층쌓기

t.rt(90)
t.fd(80)
for x in range(5): # 2층 벽돌모양 만들기
    t.rt(90)
    t.fd(15)
    t.rt(90)
    t.fd(15)
    t.lt(90)
    t.fd(15)
    t.lt(90)
    t.fd(15)

 # 1층의 오른쪽부분 만들기
    
t.rt(90)   
t.fd(15)
t.rt(90)
t.fd(80)
t.lt(60)
t.fd(40)
t.rt(60)
t.fd(150)
t.rt(90)
t.fd(34.64)

# 시계탑 쌓기

t.color("#CD853F")

t.rt(90)
t.penup() # 선 그리지않고 움직이기위해
t.fd(235)
t.lt(90)
t.fd(52.5)
t.rt(90)
t.pendown() # 다시 선그리기 시작
t.fd(120)
t.lt(30)
# 시계탑 지붕 (삼각형) 그리기

t.color("#FF0000")

for x in range(7):
    t.fd(10*x)
    t.lt(120)
    t.fd(10*x)
    t.lt(120)
    t.fd(10*x)
    t.lt(120)
# 깃발 만들기

t.color("#282828")
t.penup()
t.fd(60)
t.pendown()
t.rt(30)
t.fd(50)
for x in range(3):
    t.rt(120)
    t.fd(30)
t.lt(180)
t.fd(50)
t.penup()
t.rt(30)
t.fd(60)
t.pendown() # 시계탑의 왼쪽면을 그리기 위해서
t.color("#CD853F")
t.lt(30)
t.fd(120)

# 2층 창문 만들기

t.color("#282828")
t.penup() # 창문위치로 이동
t.fd(11.25)
t.lt(90)
t.fd(12.5)
t.pendown()
for x in range(4): # 창문틀 만들기
    t.fd(35)
    t.rt(90)
# 창문의 엑스표시 만들기
t.rt(45)
t.fd(49.49)
t.lt(135)
t.fd(35)
t.lt(135)
t.fd(49.49)

# 시계탑의 시계만들기
t.rt(135) # 시계의 위치로 이동
t.penup()
t.fd(120)
t.rt(90)
t.fd(18)
t.pendown() # 시계 그리기
t.circle(15)

# 1층 문 만들기
t.penup()
t.goto(0,0) # 시작위치로가기
t.fd(137.68)
t.lt(90)
t.pendown()
t.fd(90)
t.circle(15,180)
t.fd(90)

# 나무만들기

# 나무 위치로 이동
t.penup()
t.lt(90)
t.fd(350)
a=t.xcor()
b=t.ycor()
# 나무 기둥 만들기
t.color("#8B4513")
t.pendown()
t.lt(85)
t.fd(80)
t.goto(a,b)
t.rt(85)
t.fd(40)
t.lt(95)
t.fd(80)
# 나무 오른쪽잎 만들기
t.color("#329632")
t.rt(150)
t.circle(80,180)
t.goto(a,b+350)
# 나무 왼쪽잎 만들기
t.penup()
t.goto(a,b)
t.rt(40)
t.fd(80)
t.pendown()
t.lt(80)
t.penup()
t.fd(140)
t.pendown()
t.lt(90)
# 반원을 먼저 그리기
t.circle(70,180)
t.lt(90)
t.penup()
t.fd(140)
t.pendown()

t.goto(a,b+350)
