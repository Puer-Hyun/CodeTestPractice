'''
문제정의 
1. 우선 올바른 괄호인지를 판단한다. 
2. 한 쌍이 채워졌을 때, 앞에 남아 있는 괄호가 몇개냐? 
'''

'''def is_right(data):
    result = []
    value = []
    for i in data:
        print(result)
        if len(result)==0:
            result.append(i)
        else:
            last = result[-1]
            if (last == '(' and i == ')'):
                result.pop(-1)
                value.append([2,len(result)])
            elif ((last == '[' and i == ']')):
                result.pop(-1)
                value.append([3,len(result)])
            else:
                result.append(i)
    if len(result)==0:
        print(1, value)
    else:
        print(0)

data = input()
print("This is data", data)
is_right(data)'''

data = list(input())

stack = []
answer = 0
tmp = 1

for i in range(len(data)):

    if data[i] == "(":
        stack.append(data[i])
        tmp *= 2

    elif data[i] == "[":
        stack.append(data[i])
        tmp *= 3

    elif data[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if data[i-1] == "(":
            answer += tmp
        stack.pop()
        tmp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if data[i-1] == "[":
            answer += tmp
        stack.pop()
        tmp //= 3

if stack:
    print(0)
else:
    print(answer)
