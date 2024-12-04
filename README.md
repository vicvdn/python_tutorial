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

- **dictionnaries** : (Dictionaries)[https://www.geeksforgeeks.org/python-dictionary/] are used to store key-value pairs. They have associated methods to manipulate the data stored in them.

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

## Functions definition

- **Function definition** : A function is a block of code that performs a specific task. It can take parameters as input and return a value as output.

```python
    # Define a function
    def greet(name):
        print(f'Hello, {name}!')

    # Call the function
    greet('Alice')
```
A function can also have a return value : 
- you don't have to specify the type of the return value, which is different than in C, C++
- you can also return multiple values from a function by separating them with a comma (the return values will automatically be packed into a tuple)

```python
    # Define a function
    def add(a, b):
        return a + b

    # Call the function
    result = add(3, 5)
    print(result)
```

## clean code practices

- **DRY principle**, which stands for "Don't Repeat Yourself". It means that we should avoid duplicating code as much as possible by creating functions.

- **Comments & docstrings** to explain the code

- **The help() function** can be used to get information about a function or module. It displays the docstring of the function or module, if available. It's like the man command in Unix.

- **Exceptions** : We can use the `try` and `except` statements to handle exceptions in Python. The `try` block contains the code that might raise an exception, and the `except` block contains the code that handles the exception.

```python
    # Define a variable
    x = 0

    # Try to divide by zero
    try:
        result = 5 / x
        print(result)
    except ZeroDivisionError:
        print('Cannot divide by zero')
```

- (The PEP 8 style guide for Python code)[https://peps.python.org/pep-0008/]

## Modules and packages

- **Modules** : A module is a file containing Python code. It can define functions, classes, and variables. We can import a module using the `import` statement. You generally place it at the top of your python file.

```python
    # Import the math module
    import math

    # Use the sqrt function from the math module
    result = math.sqrt(16)
    print(result)
```
You can also import a specific function from a module you specify :
    
```python
    # Import the sqrt function from the math module
    from math import sqrt

    # Use the sqrt function
    result = sqrt(16)
    print(result)
```

You can create packages by grouping related modules together in a directory. A package is a directory that contains an `__init__.py` file. This file can be empty, or it can contain initialization code for the package.

To use a module from a package you have to specify the name of the package in the import, and it has to be separated by a dot from the name of the module.

```python
    # Import the greet function from the mypackage module
    import mypackage.mymodule

    result = mypackage.mymodule.myfunction()
```

```python
    # we can also import the function directly
    from mypackage.mymodule import myfunction

    # Call the function directly
    result = myfunction()
```

Among the most used packages in Python, we have :
- **Requests** : to send HTTP requests (frequently used to interact with REST APIs)
- **BeautifulSoup** : to parse HTML and XML documents
- **Pandas** : to work with data in tabular form

You can install the packages using the `pip` command. For example, to install the `requests` package, you can run the following command :

```bash
    pip install requests
```

**To summarize:**
- A module is a file containing Python code.
- A package is a directory containing modules linked by an `__init__.py` file.
- You can import a module using the `import` statement.
- You can import a specific function from a module using the `from` statement.
- You can install packages using the `pip` command.

## Extract and manipulate data with web scraping

- **ETL : Extract, Transform, Load** is a process used to extract data from a source, transform it into a format that meets the requirements of the target system, and load it into the target system.

HTML is made up of many tags, and each time there is an opening tag, there is a closing tag. The tags are used to structure the content of the page. The tags are enclosed in angle brackets, and they can have attributes.

```html
    <h1>This is a heading</h1>
    <p>This is a paragraph</p>
    <a href="https://www.example.com">This is a link</a>
```

The Request package we saw earlier comes in handy when we want to extract data from a website. We can use it to send HTTP requests to the website and get the HTML content of the page.

```python
    import requests

    # Send a GET request to the website
    response = requests.get('https://www.example.com')

    # Get the HTML content of the page
    html_content = response.text

    print(html_content)
```
But then we need to parse the content we just got. Good thing is, we have the BeautifulSoup package to help us with that. It allows us to parse HTML and XML documents.

First, we install it with the following command :

```bash
    pip install beautifulsoup4
```

Then we can use it like this :

```python
    import requests 
    from bs4 import BeautifulSoup

    url = 'https://www.example.com'
    # Send a GET request to the website
    response = requests.get(url)
    # Get the HTML content of the page
    page = response.content
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
```

Here, the soup object is an instance of the BeautifulSoup class. It represents the parsed HTML content of the page. We can use it to extract data from the page.

```python
    # Find the first h1 tag on the page
    h1_tag = soup.find('h1')

    # Get the text inside the h1 tag
    h1_text = h1_tag.text

    print(h1_text)
```

If we want to access the content of an index.html file for example, we could do it that way:
    
```python
    with open('index.html') as file:
        soup = BeautifulSoup(file, 'html.parser')
```

## Loading data with integrated functions

- **Reading and writing files** : We can use the `open()` function to open a file. It takes two arguments: the name of the file and the mode in which we want to open the file. The mode can be `'r'` (default mode) for reading, `'w'` for writing, or `'a'` for appending. ("r+" mode allows us to read and write to the file)

```python
    # Open a file in read mode
    with open('data.txt', 'r') as file:
        data = file.read()
        print(data)
```

```python
    # Open a file in write mode
    with open('data.txt', 'w') as file:
        file.write('Hello, world!')
```

The ```with``` statement is used to open the file and automatically close it when we're done with it. It's a good practice to use the `with` statement when working with files because it ensures that the file is properly closed after the block of code is executed.

The CSV package is used to read and write CSV files. It provides a `reader` object to read data from a CSV file and a `writer` object to write data to a CSV file.

The ```reader()``` method parses the data in the CSV file and returns it as a list of lists. Each inner list represents a row in the CSV file. 

```python
    import csv

    # Open a CSV file in read mode
    with open('data.csv', 'r') as file:
        # Create a reader object
        reader = csv.reader(file)

        # Iterate over the rows in the CSV file
        for row in reader:
            print(row)
```

Outputs this :

```python
    ['nom', 'metier', 'couleur_preferee']
    ['Jacob Smith', 'Ingénieur en informatique', 'Violet']
    ['Nora Scheffer', 'Stratégiste numérique', 'Bleu']
    ['Emily Adams', 'Responsable Marketing', 'Orange']
```

But this doesn't recognize the headers of the CSV file. So the DictReader() method is useful to read the data in the CSV file and return it as a list of dictionaries. Each dictionary represents a row in the CSV file, with the keys being the column headers.

```python
    import csv

    with open('couleurs_preferees.csv') as fichier_csv:
        reader = csv.DictReader(fichier_csv, delimiter=',')
        for ligne in reader:
            print(ligne['nom'] + " travaille en tant que " + ligne['metier'] + " et sa couleur préférée est " + ligne['couleur_preferee'])
```

The ```.writer() and writerow() methods``` are used to write data to a CSV file. The writerow() method writes a single row to the CSV file.

```python
    # Open a CSV file in write mode
    with open('data.csv', 'w') as file:
        # Create a writer object
        writer = csv.writer(file)

        # Write data to the CSV file
        writer.writerow(['Alice', 25, 'New York'])
        writer.writerow(['Bob', 30, 'Los Angeles'])
```