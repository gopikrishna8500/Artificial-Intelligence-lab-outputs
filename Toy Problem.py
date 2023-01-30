# Python 3 Program to maximize the
# number of toys with K amount

# This functions returns the required
# number of toys
def maximum_toys(cost, N, K):
	count = 0
	sum = 0

	# sort the cost array
	cost.sort(reverse = False)
	for i in range(0, N, 1):
		
		# Check if we can buy ith toy or not
		if (sum+cost[i] <= K):
			sum = sum + cost[i]
			# Increment the count variable
			count += 1
	
	return count

# Driver Code
if __name__ == '__main__':
	K = 50
	cost = [1, 12, 5, 111, 200,
			1000, 10, 9, 12, 15]
	N = len(cost)

	print(maximum_toys(cost, N, K))

# This code is contributed by
# Sanjit_Prasad
