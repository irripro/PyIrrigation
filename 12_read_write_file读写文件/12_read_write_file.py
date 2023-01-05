# read file读文件
f=open("funny.txt","r")
for line in f:
    print(line)
f.close()

# readlines()读一行
f=open("funny.txt","r")
lines = f.readlines()
print(lines)

# write file写文件
f=open("love.txt","w")
f.write("I love python")
f.close()

# same file when you write i love javascript the previous line goes away 同样的文件，当你写 I love javascript时，前一行就消失了
f=open("love.txt","w")
f.write("I love javascript")
f.close()

# You can use append mode to stop having previous lines overwritten 您可以使用追加模式来停止覆盖先前的行
f=open("love.txt","a")
f.write("I love javascript")
f.close()

# show a picture of file open modes 显示文件打开模式的图片 

# writelines 写入一行
f=open("love.txt","w")
f.writelines(["I love C++\n","I love scala"])
f.close()

# with statement   with 语句
with open("funny.txt","r") as f:
    for line in f:
        print(line)

#
player_scores = {}
with open("scores.csv","r") as f:
    for line in f:
        tokens = line.split(',')
        player = tokens[0]
        score = int(tokens[1])
        if player in player_scores:
            player_scores[player].append(score)
        else:
            player_scores[player] = [score]

print(player_scores)

for player, score_list in player_scores.items():
    min_score=min(score_list)
    max_score=max(score_list)
    avg_score=sum(score_list)/len(score_list)

    print(f"{player}==>Min:{min_score}, Max:{max_score}, Avg:{avg_score}")
