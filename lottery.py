from random import randint

balls = set()
while len(balls) < 7 :
    red_ball = randint(1, 36)
    balls.add(red_ball)
print(balls)
s = list(balls)
s.sort()
print(s)