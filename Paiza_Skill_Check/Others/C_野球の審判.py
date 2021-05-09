n = int(input())
cntStrike = 0
cntBall = 0

for i in range(n):
    s = input()
    if s[0] == 's':
        cntStrike += 1
        if cntStrike < 3:
            print('strike!')
        else:
            print('out!')
            break
    if s[0] == 'b':
        cntBall += 1
        if cntBall < 4:
            print('ball!')
        else:
            print('fourball!')
