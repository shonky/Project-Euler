#nt the prime factorization of
number=600851475143

#indexes for loops
i=2


#bool containing if number is prime
prime=True

max=0


while (i*i < number):
    while number%i==0:
        number=number/i
    i=i+1
print (number)
