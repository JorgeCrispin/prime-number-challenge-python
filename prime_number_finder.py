def prime_finder(n):
  # make a place to store prime numbers
  prime_numbers = []
  # make a place to filter other numbers
  garbage_numbers = []
  # get a list of numbers from n
  list_of_numbers = range(n+1)
  # start by iterating through numbers to find what is divisible by one and itself
  for numbers in list_of_numbers:
    if numbers == 0 or numbers == 1:
      continue
    if numbers > 2 and numbers%2 == 0 :
      continue    
    #print(numbers)
    if numbers > 3 and numbers%3 == 0 :
      continue
    if numbers > 5 and numbers%5 == 0:
      continue  
    if numbers > 7 and numbers%7 == 0:
      continue
    if numbers > 11 and numbers%11 == 0:
      continue   
    prime_numbers.append(numbers)
  return prime_numbers
    
print(prime_finder(36))
