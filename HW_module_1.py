import random                                    # import random to generate random numbers

# create list of 100 random numbers from 0 to 1000
randomlist = random.sample(range(0, 1000), 100)  # randomize 100 numbers from interval - 0 up to 1000
print(randomlist)                                # display the result

# sort list from min to max (without using sort())
i, j = 0, 0                                      # assign a value
for i in range(len(randomlist)):                 # value position in the list
    for j in range(len(randomlist) - 1):         # previous value position in the list
        if randomlist[j] > randomlist[j + 1]:    # comparing previous and next values
            randomlist[j + 1], randomlist[j] = randomlist[j], randomlist[j + 1]  #swap values
print(randomlist)                                # display the result

# calculate average for even and odd numbers
even_count, odd_count = 0, 0                    # assign a value - counts
sum_even, sum_odd = 0, 0                        # assign a value - sums

for num in randomlist:                          # iterating each number in list
    if num % 2 == 0:                            # checking condition
        even_count += 1                         # add +1 to count even number
        sum_even += num                         # get general result of sum_even
    else:
        odd_count += 1                          # add +1 to count odd number
        sum_odd += num                          # get general result of sum_odd

# here we check using exception ZeroDivisionError, calculate the result, round it
try:                                             # check if we don't divide by zero
    even_avg = round(sum_even / even_count, 2)   # then calculate the average for even numbers
    print("Average for even numbers in the random list: ", even_avg)  # print the result for even numbers
except ZeroDivisionError:                        # if we divide by zero
    print("It's impossible to calculate average for odd numbers because we can't delete by zero")

try:                                             # check if we don't divide by zero
    odd_avg = round(sum_odd / odd_count, 2)      # then calculate the average for odd numbers
    print("Average for odd numbers in the random list: ", odd_avg)  # print the result for odd numbers
except ZeroDivisionError:                        # if we divide by zero
    print("It's impossible to calculate average for odd numbers because we can't delete by zero")