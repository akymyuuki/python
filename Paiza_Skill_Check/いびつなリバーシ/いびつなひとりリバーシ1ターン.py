class Point:
    def __init__(self, x, y, s):
        self.x = x
        self.y = y
        self.s = s

    # ポイントに情報をセットする
    def setData(self, input_data):
        self.s = input_data

    # ポイントの情報を返す
    def getData(self):
        return self.s


class Map:
    # ある向きで前に進んだ移動に対応する配列　北、東、南、西
    move_x = {'N': 0, 'NE': -1, 'E': 1, 'ES': 1,
              'S': 0, 'SW': -1, 'W': -1, 'WN': 1}
    move_y = {'N': -1, 'NE': -1, 'E': 0, 'ES': 1,
              'S': 1, 'SW': 1, 'W': 0, 'WN': -1}

    # 上下左右に1マスずつ広いマップを作成
    field = []

    def __init__(self, h, w):
        # 石と違う文字にして壁の判定に使用する
        self.field = [[Point(i+1, j+1, '#') for i in range(h+2)]
                      for j in range(w+2)]

    def getPoint(self, x, y):
        return self.field[x+1][y+1].getData()

    def setPoint(self, x, y, input_data):
        return self.field[x+1][y+1].setData(input_data)

    def setPointLoop(self, x, y, direction):
        while self.getPoint(x + self.move_x[direction], y + self.move_y[direction]) == '.':
            x += self.move_x[direction]
            y += self.move_y[direction]
            self.setPoint(x, y, '*')

    def checkThereStone(self, x, y, direction):
        while self.getPoint(x + self.move_x[direction], y + self.move_y[direction]) == '.':
            x += self.move_x[direction]
            y += self.move_y[direction]
            if self.getPoint(x + self.move_x[direction], y + self.move_y[direction]) == '*':
                return True
        return False


h, w = map(int, input().split())

field = Map(h, w)
directions = ['N', 'NE', 'E', 'ES', 'S', 'SW', 'W', 'WN']

sx, sy = 0, 0

for i in range(h):
    line = input()
    for j in range(w):
        if line[j] == '!':
            sx = j
            sy = i
        field.setPoint(j, i, line[j])

field.setPoint(sx, sy, '*')
for i in range(len(directions)):
    if field.checkThereStone(sx, sy, directions[i]) == True:
        field.setPointLoop(sx, sy, directions[i])


for i in range(h):
    list = []
    for j in range(w):
        list.append(str(field.getPoint(j, i)))
    print(''.join(list))
