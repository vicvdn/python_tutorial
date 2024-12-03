# Python TUTO

## Introduction

- **basic variables** : int, float, string, bool

- **lists** : Lists are used to store multiple items in a single variable. They have associated methods to manipulate the data stored in them.

```python
    # Create a list
    my_list = [1, 2, 3, 4, 5]

    #extend method to add multiple items to the list
    my_list.extend([6, 7, 8])
    print(my_list)

    #append method to add a single item to the list
    my_list.append(9)
    print(my_list)

    #insert method to add an item at a specific index
    my_list.insert(0, 0)
    print(my_list)

    #remove method to remove an item from the list
    my_list.remove(0)
    print(my_list)

    #pop method to remove an item at a specific index
    my_list.pop(5) #it removes the item in position 5
    print(my_list) 

    #index method to get the index of an item
    print(my_list.index(1))

    #count method to get the number of occurrences of an item
    print(my_list.count(1))

    #reverse method to reverse the list
    my_list.reverse()
    print(my_list)

    #sort method to sort the list
    my_list.sort()
    print(my_list)
```

```The output is :
    [1, 2, 3, 4, 5, 6, 7, 8]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    [1, 2, 3, 4, 5, 7, 8, 9]
    0
    1
    [9, 8, 7, 5, 4, 3, 2, 1]
    [1, 2, 3, 4, 5, 7, 8, 9]
```

- **tuples** : Tuples are used to store multiple items in a single variable. They are immutable, meaning that the data stored in a tuple cannot be changed.

```python
    # Create a tuple
    my_tuple = (1, 2, 3, 4, 5)

    # Access an item in the tuple
    print(my_tuple[0])

    # Iterate over the tuple
    for item in my_tuple:
        print(item)
    #the in operator can be used to check if an item is in the tuple (returns a boolean value)
```

```The output is :
    1
    1
    2
    3
    4
    5
```

- **dictionnaries** : Dictionaries are used to store key-value pairs. They have associated methods to manipulate the data stored in them.

```python
    # Create a dictionary
    my_dict = {
        'name': 'Alice',
        'age': 25,
        'city': 'New York'
    }

    # Access a value in the dictionary
    print(my_dict['name'])

    # Iterate over the dictionary
    for key, value in my_dict.items():
        print(key, value)

    # Add a new key-value pair to the dictionary
    my_dict['email'] = 'toto@mail.com'
    print(my_dict)
```

```The output is :
    Alice
    name Alice
    age 25
    city New York
    {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'toto@mail.com'}
```

To remove a key-value pair from a dictionary, you can use the `pop()` method, as well as the `del` keyword.

```python
    # Remove a key-value pair from the dictionary
    my_dict.pop('age')
    print(my_dict)

    # Remove a key-value pair from the dictionary using the del keyword
    del my_dict['city']
    print(my_dict)
```

```The output is :
    {'name': 'Alice', 'city': 'New York', 'email': 'toto@mail.com'}
    {'name': 'Alice', 'email': 'toto@mail.com'}
```

Methods available for dictionaries :
    - ***keys()*** : returns a list of all the keys in the dictionary
    - ***values()*** : returns a list of all the values in the dictionary
    - ***items()*** : returns a list of tuples containing the key-value pairs in the dictionary
    - ***get(key)*** : returns the value associated with the specified key
    - ***pop(key)*** : removes the key-value pair associated with the specified key
    - ***clear()*** : removes all key-value pairs from the dictionary

We can always use the `in` operator to check if a key is in the dictionary. Like such :

```python
    # Check if a key is in the dictionary
    if 'name' in my_dict:
        print('The key "name" is in the dictionary')
```

## Program logic

- **"if/elif/else" statement** : The `if` statement is used to execute a block of code only if a certain condition is true.

```python
    # Define a variable
    x = 5

    # Check if x is greater than 0
    if x > 0:
        print('x is greater than 0')
    elif x == 0:
        print('x is equal to 0')
    else:
        print('x is less than 0')
```

If we want to check multiple conditions for a single result in the same instruction, we can use the followin logical operators:
- and
- or
- not (if a condition is not true)

```python
    avec_soleil = True
    en_semaine = False
    if avec_soleil and not en_semaine:
        print("on va à la plage !")
    elif avec_soleil and en_semaine:
        print("on va au travail !")
    else:
        print("on reste à la maison !")
```

- **match/case statement** : The `match` statement is used to execute a block of code based on the value of a variable.

```python
    # Define a variable
    x = 5

    # Check the value of x
    match x:
        case 0:
            print('x is equal to 0')
        case 1:
            print('x is equal to 1')
        case 2:
            print('x is equal to 2')
        case _: # default case if none of the above cases are true
            print('x is not equal to 0, 1, or 2')
```

Exercise : We created a little calculator to test our understanding of these notions. We discovered :

- ```raise SystemExit("End of the program")``` which allows to stop the program at any time with a message. The raise keyword is used to raise an exception. We can also use the `exit()` function from the `sys` module to stop the program.

- The `input()` function is used to get user input. It takes a string as an argument, which is displayed to the user as a prompt. The function returns the user input as a string. We can convert the input to an integer using the `int()` function.

```python
    # Here we protect the program from crashing if the user enters a string instead of a number
    while True:
    input_gauche = input("enter left number : ")
    try:
        nombre_a_gauche = int(input_gauche)
        break
    except ValueError :
        print("Please enter a valid number :) ")
```

- **for loops** : The `for` loop is used to iterate over a sequence (such as a list, tuple, or dictionary) and execute a block of code for each item in the sequence.

```python
    # Create a list
    my_list = [1, 2, 3, 4, 5]

    # Iterate over the list
    for item in my_list:
        print(item)
```

- **The range() function** can be used to generate a sequence of numbers. 

```python
    # Generate a sequence of numbers from 0 to 4
    for i in range(5):
        print(i)
```
We can give it more params (start, stop, step) to generate a sequence of numbers from start to stop with a step value.

```python
    # Generate a sequence of numbers from 1 to 10 with a step of 2
    for i in range(1, 11, 2):
        print(i)
```

- **while() loop** : The `while` loop is used to execute a block of code as long as a certain condition is true.

```python
    # Define a variable
    x = 0

    # Execute the block of code as long as x is less than 5
    while x < 5:
        print(x)
        x += 1
```

**When do we use a `for` loop and when do we use a `while` loop ?**
We use a `for` loop when we know the number of iterations in advance, and a `while` loop when we don't know the number of iterations in advance.

- **Break and continue** : same as in c++ or java, the `break` statement is used to exit a loop, and the `continue` statement is used to skip the current iteration of a loop.

```python
    # Create a list
    my_list = [1, 2, 3, 4, 5]

    # Iterate over the list
    for item in my_list:
        if item == 3:
            break
        print(item)
```

```python
    # Create a list
    my_list = [1, 2, 3, 4, 5]

    # Iterate over the list
    for item in my_list:
        if item == 3:
            continue
        print(item)
```

