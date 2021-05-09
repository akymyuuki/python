#辞書を使用して解いた。
n = int(input())
dict = {}
for i in range(n):
    S = input().split()
    if S[0] == "insert":
        dict[S[1]] = "1" 
    else:
        if S[1] in dict:
            print("yes")
        else:
            print("no") 