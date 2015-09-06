#This program finds the sum of all mulitples of 2 numbers with a maximal value that you define

#Define the numbers of whose multiples you would like to get the sum of
multiple1 = 3
multiple2 = 5

#define the maximal value
max = 1000

#initialize the values used int he for loop
i=0
sum=0

#for loop iterating through and summing the multiples you've defined in the range of he max that you've defined
for i in range(max):
	if(i%multiple1==0 or i%multiple2==0):
		sum+=i
#prints the sum
print sum
