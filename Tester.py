
import os
import sys

N = 10

if len(sys.argv) > 2:
    classNames = [sys.argv[1], sys.argv[2]]
else:
    print("Error arguments : Tester.py <player_BLACK.py> <player_WHITE.py> [N : number of games]")
    exit(1)

if len(sys.argv) > 3:
    N = int(sys.argv[3])

os.system("echo -n "" > Tester_logs.txt")

for game in range(N):
    os.system("python3 namedGame.py " + " ".join(sys.argv[1:3]) + " > Tester_tmp.txt")
    os.system("tail -1 Tester_tmp.txt >> Tester_logs.txt")
    print("Game", game+1, "finished\r", end="")

result_file = open("Tester_logs.txt", 'r')
lines = result_file.readlines()
result_file.close()


wins_white = 0
wins_black = 0
wins_deuce = 0

for i in range(len(lines)):
    line = lines[i]
    line = line.strip('\n')
    line = line.strip('Winner:')
    line = line.strip(' ')
    
    if line == 'WHITE':
        wins_white += 1
    elif line == 'BLACK':
        wins_black += 1
    else:
        wins_deuce += 1

print("WHITE ({}) won : {} times".format(classNames[1], wins_white))
print("BLACK ({}) won : {} times".format(classNames[0], wins_black))
print("Number of DEUCE :", wins_deuce)