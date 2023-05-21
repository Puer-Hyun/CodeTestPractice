N, row, column = map(int, input().split())

answer = 0

while N != 0:

	N -= 1

	# 1사분면
	if row < 2 ** N and column < 2 ** N:
		answer += (2**N)*(2**N) * 0

	# 2사분면
	elif row < 2 ** N and column >= 2 ** N: 
		answer += (2**N) * (2**N) * 1
		column -= (2**N)
        
	# 3사분면    
	elif row >= 2 ** N and column < 2 ** N: 
		answer += (2**N) * (2**N) * 2
		row -= (2**N)
        
	# 4사분면    
	else:
		answer += (2**N) * (2**N) * 3
		row -= (2**N)
		column -= (2**N)
    
print(answer)