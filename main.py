#Write your code below this row 👇
sum_of_numbers = 0
for n in range(2, 101):
  if n % 2 == 0:
    sum_of_numbers = sum_of_numbers + n
  
print(sum_of_numbers)