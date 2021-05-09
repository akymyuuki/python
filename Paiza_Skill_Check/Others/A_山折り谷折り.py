import copy
n = int(input())

paper = list()
paper_c = list()
while n > 0:
    paper_c.clear()
    paper_c = paper.copy()
    paper.clear()

    # 折り目の最初は必ず０
    paper.append(0)
    for i in range(len(paper_c)):
        # 一回前の折り目のコピー
        paper.append(paper_c[i])
        # 一回前の折り目に対して交互に0と1を挿入していく
        if i % 2 == 0:
            paper.append(1)
        else:
            paper.append(0)
    n -= 1

print("".join(map(str, paper)))
