#indexes for loops
i=0
k=0

#max value for loop
max=4000000

#initalizing fibonacci series
fibonacci=[1,2]

#loop that defines the array containg the fibonacci series
while((fibonacci[i]+fibonacci[i+1])<max):
	sum=fibonacci[i]+fibonacci[i+1]
	fibonacci.append(sum)
	i+=1

#reusing sum variable to find final sum of all even members of fibonacci series until max value
sum=0

#going through the loop and adding all even numbers of fibonacci series
for k in range(len(fibonacci)):
	if(fibonacci[k]%2==0):
		sum+=fibonacci[k]


#printing the series until max value and the sum of even numbers in the series
print fibonacci
print sum
	
