#the number you want the prime factorization of
number=600851475143

#indexes for loops
i=2


#bool containing if number is prime
prime=True

max=0

#logic for getting all the prime numbers needed
for i in range(2,number/2):
	for k in range(1,i):	
		if(i%k==0 and (k!=1 and k!=i)):
			prime=False
	
	if(prime==True and number%i==0):
			max=i
			print max
		
	if(prime==False):
		prime=True	

print max
