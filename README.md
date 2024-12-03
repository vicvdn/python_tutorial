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

- dictionnaries : Dictionaries are used to store key-value pairs. They have associated methods to manipulate the data stored in them.

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

