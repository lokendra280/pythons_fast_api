my_list = [1,2,3,4,5,6,7,8,9,10]
odd = []
for number in my_list:
    if number %2 != 0:
        odd.append(number)
        print("odd number", odd)