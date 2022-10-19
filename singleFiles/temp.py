numbers = [1, 2, 3, 4, 5, 6, 7]
print("Original list: %s" % numbers)
# list comprehesion
double_nums = [x*2 for x in numbers]
print(double_nums)

odd_nums = [x for x in numbers if x % 2 != 0]
print(odd_nums)

# y = x^2 +1
list_of_y = [y * y + 1 for y in numbers if y % 2 != 0]
print(list_of_y)

list_of_square = [(lambda x: x * x)(z)
                  for z in numbers]  # using lambda function
print(list_of_square)
