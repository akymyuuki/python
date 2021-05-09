import math


def dijkstra(A, stations):

    # 自分の位置と現在値を格納するキュー
    queue = []

    # スタート地点, スタート時の値0をキューに格納
    queue.append([0, 0])

    # スタート地点が0だと戻ってきてしまうので-1を入れておく
    stations[0] = -1

    # キューが空になるまで
    while len(queue) > 0:
        # キューから次の位置と値を取り出す
        y, v = map(int, queue.pop(0))
        for i in range(len(stations)):

            # 辺の値が入っており、かつ駅に記録された値より現在地+移動コストが低い　
            # もしくは　辺の値が入っていて、駅に値が記録されていない場合
            if (A[y][i] > 0 and stations[i] > v + A[y][i]) \
                    or (A[y][i] > 0 and stations[i] == 0):

                # 移動先の駅に　現在地＋移動コスト　の値を記録する
                stations[i] = v + A[y][i]

                # 移動先の駅の位置と、現在の値を求める
                queue.append([i, (v + A[y][i])])


E, V, T = map(int, input().split())

# 最小コストを記録するため、駅の数だけ配列を作る
stations = [0 for i in range(V)]

# 辺の情報からグラフを作成
A = [[0 for i in range(V)] for j in range(V)]

for i in range(E):
    s, e, v = map(int, input().split())
    # 辺の情報を記録する
    A[s][e] = v
    A[e][s] = v

# ダイクストラ法で駅の最小移動コストを求める
dijkstra(A, stations)

# 目的の駅までのコストを表示
print(stations[T])
