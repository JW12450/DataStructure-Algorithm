
import sys
from collections import defaultdict

input = sys.stdin.readline
trees = defaultdict(int)
n = 0

while True:
    tree = input().rstrip()
    if not tree:
        break
    trees[tree] += 1
    n += 1

treelist = list(trees.keys())
treelist.sort()
for tree in treelist:
    print('%s %.4f' %(tree, trees[tree]/n*100))




