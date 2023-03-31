x,y,w,h = map(int, input().split())
print(min(map(abs,[x,w-x,y,h-y])))