#exercise on loops 

list = input("Please enter a list of number with this format : nb1,nb2,nb3,...\n")
print(f"This is the input list as a string {list}")

# splitting in string list
true_list = list.split(',')
print(true_list)

# creating empty int list to fill
int_list = []
sum = 0

# storing in an int list and sum computing
for item in true_list:
    to_add = int(item)
    sum += to_add
    int_list.append(to_add)

print(int_list)
print(f"sum : {sum}")
list_len = len(int_list)
print(f"len : {list_len}")

# Mean computing
mean = sum / list_len
print(f"the mean is : {mean}")


# Numbers superior to mean
sup_to_mean = []
for item in int_list:
    if item > mean :
        sup_to_mean.append(item)

print(f"Number of items superior to mean : {len(sup_to_mean)}")

#number of even numbers in list
even_numbers = 0
for item in int_list:
    if item % 2 == 0:
        even_numbers += 1

print(f"Number of even numbers in list : {even_numbers}")