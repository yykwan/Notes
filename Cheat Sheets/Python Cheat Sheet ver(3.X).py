'''
Python Cheat Sheet (Python3.X) with expansions in 
- Specialized Libraries (numpy, pandas, matplotlib, requests)
- Web Frameworks (Flask, Django, FastAPI)
- Database Interaction (sqlite3, SQLAlchemy, PostgreSQL)
- Concurrency & Parallelism (threading, multiprocessing, asyncio)
- Testing & Debugging (unittest, pytest, pdb)
- Python’s Internals (GIL, memory management, __slots__)
'''

# ==============================================
# 1. VARIABLES AND DATA TYPES
# ==============================================

# Integer
x = 10  # Stores whole numbers
print(type(x))  # Output: <class 'int'>

# Float
y = 3.14  # Stores decimal numbers
print(type(y))  # Output: <class 'float'>

# String
name = "Python"  # Stores text (sequence of characters)
print(type(name))  # Output: <class 'str'>

# Boolean
is_active = True  # Stores True or False
print(type(is_active))  # Output: <class 'bool'>

# NoneType
result = None  # Represents absence of value
print(type(result))  # Output: <class 'NoneType'>

# Type conversion
str_num = "123"
int_num = int(str_num)  # Convert string to integer
float_num = float(str_num)  # Convert string to float

# ==============================================
# 2. OPERATORS
# ==============================================

# Arithmetic Operators
a, b = 10, 3
print(a + b)  # Addition: 13
print(a - b)  # Subtraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333...
print(a // b) # Floor division: 3
print(a % b)  # Modulus: 1
print(a ** b) # Exponentiation: 1000

# Comparison Operators
print(a == b)  # Equal: False
print(a != b)  # Not equal: True
print(a > b)   # Greater than: True
print(a < b)   # Less than: False
print(a >= b)  # Greater or equal: True
print(a <= b)  # Less or equal: False

# Logical Operators
print(True and False)  # AND: False
print(True or False)   # OR: True
print(not True)        # NOT: False

# Assignment Operators
x = 5      # Basic assignment
x += 2     # x = x + 2
x -= 1     # x = x - 1
x *= 3     # x = x * 3
x /= 2     # x = x / 2
x **= 2    # x = x ** 2
x %= 3     # x = x % 3

# Identity Operators (check memory location)
x = [1, 2]
y = [1, 2]
print(x is y)     # False (different objects)
print(x is not y) # True

# Membership Operators
print(2 in [1, 2, 3])      # True
print(4 not in [1, 2, 3])   # True

# Bitwise Operators
print(5 & 3)  # AND: 1
print(5 | 3)  # OR: 7
print(5 ^ 3)  # XOR: 6
print(~5)     # NOT: -6
print(5 << 1) # Left shift: 10
print(5 >> 1) # Right shift: 2

# ==============================================
# 3. DATA STRUCTURES
# ==============================================

# Lists (Mutable, ordered sequence)
fruits = ['apple', 'banana', 'cherry']
fruits.append('orange')     # Add item to end
fruits.insert(1, 'mango')  # Insert at index
fruits.remove('banana')    # Remove item
popped = fruits.pop()      # Remove and return last item
print(fruits[0])           # Access by index
print(fruits[-1])          # Negative indexing
print(len(fruits))         # Length of list

# List Slicing
nums = [0, 1, 2, 3, 4, 5]
print(nums[1:4])    # [1, 2, 3] (start:end-1)
print(nums[:3])     # [0, 1, 2] (from start)
print(nums[3:])     # [3, 4, 5] (to end)
print(nums[::2])    # [0, 2, 4] (step by 2)
print(nums[::-1])   # [5, 4, 3, 2, 1, 0] (reverse)

# List Comprehensions
squares = [x**2 for x in range(5)]  # [0, 1, 4, 9, 16]
even_squares = [x**2 for x in range(10) if x % 2 == 0]

# Tuples (Immutable, ordered sequence)
colors = ('red', 'green', 'blue')
print(colors[1])    # Access by index
# colors[1] = 'yellow'  # Error: tuples are immutable

# Sets (Unordered, unique elements)
unique_nums = {1, 2, 3, 3, 4}  # {1, 2, 3, 4}
unique_nums.add(5)  # Add element
unique_nums.remove(2)  # Remove element
print(1 in unique_nums)  # Membership test

# Set Operations
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)  # Union: {1, 2, 3, 4, 5}
print(a & b)  # Intersection: {3}
print(a - b)  # Difference: {1, 2}
print(a ^ b)  # Symmetric difference: {1, 2, 4, 5}

# Dictionaries (Key-value pairs)
person = {'name': 'Alice', 'age': 25, 'city': 'NY'}
print(person['name'])      # Access value by key
person['age'] = 26         # Modify value
person['job'] = 'Engineer' # Add new key-value pair
print('city' in person)    # Check key existence
print(person.keys())       # List of keys
print(person.values())     # List of values
print(person.items())      # List of (key, value) tuples

# Dictionary Comprehensions
square_dict = {x: x**2 for x in range(5)}  # {0:0, 1:1, 2:4, 3:9, 4:16}

# ==============================================
# 4. CONTROL FLOW
# ==============================================

# If-elif-else
age = 20
if age < 18:
    print("Minor")
elif 18 <= age < 65:
    print("Adult")
else:
    print("Senior")

# Ternary Operator
status = "Adult" if age >= 18 else "Minor"

# For Loop
for i in range(5):  # 0 to 4
    print(i)

# For Loop with enumerate
for index, value in enumerate(['a', 'b', 'c']):
    print(index, value)

# While Loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break and Continue
for num in range(10):
    if num == 3:
        continue  # Skip current iteration
    if num == 8:
        break     # Exit loop
    print(num)

# Else in Loops (executes if loop completes normally)
for num in range(5):
    print(num)
else:
    print("Loop completed")

# ==============================================
# 5. FUNCTIONS
# ==============================================

# Basic Function
def greet(name):
    """This function greets the person passed in"""
    return f"Hello, {name}!"

print(greet("Alice"))  # Call function

# Default Arguments
def power(num, exponent=2):
    return num ** exponent

print(power(3))     # Uses default exponent (2)
print(power(3, 3))  # Override default

# Variable-length Arguments
def sum_all(*args):
    """Accept any number of positional arguments"""
    return sum(args)

print(sum_all(1, 2, 3, 4))  # 10

def print_info(**kwargs):
    """Accept any number of keyword arguments"""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25)

# Lambda Functions (Anonymous functions)
square = lambda x: x ** 2
print(square(5))  # 25

# Function Annotations
def add(a: int, b: int) -> int:
    """Type hints (not enforced, just documentation)"""
    return a + b

# ==============================================
# 6. FILE HANDLING
# ==============================================

# Writing to a file
with open('example.txt', 'w') as f:  # 'w' for write
    f.write("Hello, World!\n")
    f.write("This is a second line\n")

# Reading from a file
with open('example.txt', 'r') as f:  # 'r' for read
    content = f.read()               # Read entire file
    # lines = f.readlines()         # Read as list of lines
print(content)

# Appending to a file
with open('example.txt', 'a') as f:  # 'a' for append
    f.write("This line was appended\n")

# ==============================================
# 7. EXCEPTION HANDLING
# ==============================================

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
except (TypeError, ValueError) as e:
    print(f"Error occurred: {e}")
else:
    print("No exceptions occurred")
finally:
    print("This always executes")

# Raising Exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# Custom Exceptions
class MyError(Exception):
    pass

try:
    raise MyError("Something went wrong")
except MyError as e:
    print(f"Custom error: {e}")

# ==============================================
# 8. OBJECT-ORIENTED PROGRAMMING
# ==============================================

# Class Definition
class Dog:
    # Class attribute (shared by all instances)
    species = "Canis familiaris"
    
    # Constructor (initializer)
    def __init__(self, name, age):
        # Instance attributes
        self.name = name
        self.age = age
    
    # Instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    
    # Another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"

# Creating Objects
dog1 = Dog("Buddy", 5)
print(dog1.description())
print(dog1.speak("Woof"))

# Inheritance
class Bulldog(Dog):  # Inherits from Dog
    def run(self, speed):
        return f"{self.name} runs at {speed} mph"

dog2 = Bulldog("Max", 3)
print(dog2.speak("Bark"))  # Inherited method
print(dog2.run(12))        # New method

# Magic/Dunder Methods
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __len__(self):
        return len(self.title)

book = Book("Python 101", "John Doe")
print(str(book))  # Calls __str__
print(len(book))  # Calls __len__

# Property Decorator
class Circle:
    def __init__(self, radius):
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
    
    @property
    def area(self):
        return 3.14 * self._radius ** 2

circle = Circle(5)
print(circle.area)  # 78.5 (read-only property)
circle.radius = 7   # Uses setter

# ==============================================
# 9. MODULES AND PACKAGES
# ==============================================

"""
# mymodule.py
def greet(name):
    return f"Hello, {name}!"

PI = 3.14159
"""

# Importing
import mymodule
print(mymodule.greet("Alice"))
print(mymodule.PI)

# Import specific items
from mymodule import greet, PI
print(greet("Bob"))

# Import with alias
import math as m
print(m.sqrt(16))

# Package structure
"""
mypackage/
    __init__.py
    module1.py
    module2.py
    subpackage/
        __init__.py
        module3.py
"""

# ==============================================
# 10. ITERATORS AND GENERATORS
# ==============================================

# Iterator Protocol
my_list = [1, 2, 3]
my_iter = iter(my_list)  # Get iterator
print(next(my_iter))     # 1
print(next(my_iter))     # 2

# Custom Iterator
class CountDown:
    def __init__(self, start):
        self.current = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        num = self.current
        self.current -= 1
        return num

for num in CountDown(3):
    print(num)  # 3, 2, 1

# Generator Function (yields values one at a time)
def count_up_to(max):
    count = 1
    while count <= max:
        yield count  # Pauses here, returns count
        count += 1

counter = count_up_to(3)
print(next(counter))  # 1
print(next(counter))  # 2

# Generator Expression
squares_gen = (x**2 for x in range(5))
print(list(squares_gen))  # [0, 1, 4, 9, 16]

# ==============================================
# 11. DECORATORS
# ==============================================

# Simple Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Decorator with Arguments
def repeat(num_times):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(num_times=3)
def greet(name):
    print(f"Hello {name}")

greet("Alice")

# ==============================================
# 12. CONTEXT MANAGERS
# ==============================================

# Using 'with' statement (built-in)
with open('file.txt', 'r') as f:
    content = f.read()
# File automatically closed here

# Custom Context Manager (class-based)
class ManagedFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
    
    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

with ManagedFile('file.txt', 'w') as f:
    f.write("Hello")

# Context Manager using contextlib
from contextlib import contextmanager

@contextmanager
def managed_file(filename, mode):
    try:
        f = open(filename, mode)
        yield f
    finally:
        f.close()

with managed_file('file.txt', 'w') as f:
    f.write("Hello again")

# ==============================================
# 13. REGULAR EXPRESSIONS
# ==============================================

import re

# Basic matching
pattern = r"apple"
text = "I have an apple and a banana"
match = re.search(pattern, text)
if match:
    print("Found:", match.group())  # Found: apple

# Find all matches
all_matches = re.findall(r"\b\w{5}\b", text)  # Words with 5 letters
print(all_matches)  # ['apple', 'banana']

# Substitution
new_text = re.sub(r"apple", "orange", text)
print(new_text)  # "I have an orange and a banana"

# Groups
phone_pattern = r"(\d{3})-(\d{3})-(\d{4})"
phone = "123-456-7890"
match = re.search(phone_pattern, phone)
print(match.groups())  # ('123', '456', '7890')

# ==============================================
# 14. COMMON LIBRARIES
# ==============================================

# Math
import math
print(math.sqrt(16))      # 4.0
print(math.pi)            # 3.141592653589793
print(math.factorial(5))  # 120

# Random
import random
print(random.random())         # Random float 0-1
print(random.randint(1, 10))   # Random int 1-10
print(random.choice(['a', 'b', 'c']))  # Random choice

# Datetime
from datetime import datetime, timedelta
now = datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Formatted date
tomorrow = now + timedelta(days=1)         # Date arithmetic

# Collections
from collections import Counter, defaultdict, deque

# Counter
count = Counter(['a', 'b', 'a', 'c', 'b', 'a'])
print(count)  # {'a': 3, 'b': 2, 'c': 1}

# defaultdict
d = defaultdict(int)
d['a'] += 1  # No KeyError for missing keys

# deque
queue = deque([1, 2, 3])
queue.append(4)    # Add to end
queue.popleft()    # Remove from front

# JSON
import json
data = {'name': 'Alice', 'age': 25}
json_str = json.dumps(data)  # Convert to JSON string
data_back = json.loads(json_str)  # Parse JSON string

# ==============================================
# 15. ADVANCED FEATURES
# ==============================================

# Closures
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

closure = outer_func(10)
print(closure(5))  # 15

# Partial Functions
from functools import partial
def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25

# Metaclasses
class Meta(type):
    def __new__(cls, name, bases, dct):
        dct['version'] = 1.0
        return super().__new__(cls, name, bases, dct)

class MyClass(metaclass=Meta):
    pass

print(MyClass.version)  # 1.0

# Async/Await
import asyncio

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)  # Simulate I/O operation
    print("Done fetching")
    return {'data': 1}

async def main():
    task = asyncio.create_task(fetch_data())
    print("Do other things")
    data = await task
    print(data)

asyncio.run(main())

# Type Hinting (Python 3.5+)
from typing import List, Dict, Tuple, Optional, Union

def process_items(
    items: List[str],
    counts: Dict[str, int],
    value: Union[int, float],
    flag: Optional[bool] = None
) -> Tuple[int, str]:
    # Function implementation
    return (1, "success")

# Walrus Operator (Python 3.8+)
if (n := len([1, 2, 3])) > 2:
    print(f"List is long with {n} elements")

# Structural Pattern Matching (Python 3.10+)
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case _:
            return "Unknown error"

# ==============================================
# 16. BEST PRACTICES
# ==============================================

# List vs Tuple: Use lists for mutable sequences, tuples for immutable

# Dictionary keys: Must be hashable (immutable types like str, int, tuple)

# String formatting (f-strings Python 3.6+)
name = "Alice"
print(f"Hello, {name}!")  # Preferred over .format()

# Use enumerate() instead of range(len()) for index and value
for i, value in enumerate(['a', 'b', 'c']):
    print(i, value)

# Use zip() to iterate over multiple sequences
names = ['Alice', 'Bob']
scores = [85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Use get() with dictionaries to handle missing keys
d = {'a': 1}
print(d.get('b', 0))  # 0 (default instead of KeyError)

# Use collections.defaultdict for default values
from collections import defaultdict
dd = defaultdict(int)  # Default to 0 for missing keys

# Use context managers for resource management
with open('file.txt') as f:
    content = f.read()
# File automatically closed

# Use main guard
if __name__ == "__main__":
    print("This runs when executed directly")

"""
This expanded cheat sheet includes additional sections for:
- Specialized Libraries (numpy, pandas, matplotlib, requests)
- Web Frameworks (Flask, Django, FastAPI)
- Database Interaction (SQLite, SQLAlchemy, PostgreSQL)
- Concurrency & Parallelism (threading, multiprocessing, asyncio)
- Testing & Debugging (unittest, pytest, pdb)
- Python Internals (GIL, memory management, __slots__)
"""

# ==============================================
# 17. SPECIALIZED LIBRARIES
# ==============================================

# --------------------------
# numpy (Numerical Computing)
# --------------------------
import numpy as np

# Creating arrays
arr = np.array([1, 2, 3])          # 1D array
matrix = np.array([[1, 2], [3, 4]]) # 2D array
zeros = np.zeros((3, 3))            # 3x3 zeros matrix
ones = np.ones((2, 2))              # 2x2 ones matrix
range_arr = np.arange(0, 10, 2)     # [0, 2, 4, 6, 8]

# Array operations
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)   # [5 7 9]
print(a * 2)   # [2 4 6]
print(np.dot(a, b))  # Dot product: 32

# Array indexing/slicing
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[1, 2])    # 6 (row 1, column 2)
print(arr[:, 1:3])  # All rows, columns 1-2

# --------------------------
# pandas (Data Analysis)
# --------------------------
import pandas as pd

# Series (1D)
s = pd.Series([1, 3, 5, np.nan, 6, 8])

# DataFrame (2D)
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['NY', 'LA', 'Chicago']}
df = pd.DataFrame(data)

# DataFrame operations
print(df.head(2))       # First 2 rows
print(df.describe())    # Statistics summary
print(df[df['Age'] > 28])  # Filtering

# Reading/Writing data
# df = pd.read_csv('data.csv')
# df.to_excel('output.xlsx')

# --------------------------
# matplotlib (Plotting)
# --------------------------
import matplotlib.pyplot as plt

# Line plot
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Simple Plot')
# plt.show()

# Bar chart
categories = ['A', 'B', 'C']
values = [15, 10, 20]
plt.bar(categories, values)
# plt.show()

# --------------------------
# requests (HTTP)
# --------------------------
import requests

# GET request
response = requests.get('https://api.github.com')
print(response.status_code)
print(response.json())

# POST request
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=payload)

# ==============================================
# 18. WEB FRAMEWORKS
# ==============================================

# --------------------------
# Flask (Micro Framework)
# --------------------------
"""
# flask_app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/api', methods=['POST'])
def api():
    data = request.get_json()
    return jsonify({"received": data})

if __name__ == '__main__':
    app.run(debug=True)
"""

# Run with: python flask_app.py
# Access at: http://localhost:5000/

# --------------------------
# Django (Full-featured Framework)
# --------------------------
"""
1. Install: pip install django
2. Create project: django-admin startproject mysite
3. Create app: python manage.py startapp myapp
4. Define models in myapp/models.py
5. Create views in myapp/views.py
6. Configure URLs in mysite/urls.py
7. Run: python manage.py runserver
"""

# --------------------------
# FastAPI (Modern API Framework)
# --------------------------
"""
# fastapi_app.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/items/")
def create_item(item: dict):
    return {"item": item}

# Run with: uvicorn fastapi_app:app --reload
# Access at: http://localhost:8000/
"""

# ==============================================
# 19. DATABASE INTERACTION
# ==============================================

# --------------------------
# SQLite (Built-in)
# --------------------------
import sqlite3

# Connect to database (creates if doesn't exist)
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Create table
cursor.execute('''CREATE TABLE IF NOT EXISTS users
               (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)''')

# Insert data
cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Alice', 25))

# Query data
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Commit and close
conn.commit()
conn.close()

# --------------------------
# SQLAlchemy (ORM)
# --------------------------
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Connect to database
engine = create_engine('sqlite:///example.db')
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Add new user
new_user = User(name='Bob', age=30)
session.add(new_user)
session.commit()

# Query
users = session.query(User).filter(User.age > 25).all()
for user in users:
    print(user.name, user.age)

# --------------------------
# PostgreSQL (psycopg2)
# --------------------------
"""
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="mydb",
    user="user",
    password="password"
)

cursor = conn.cursor()
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

conn.close()
"""

# ==============================================
# 20. CONCURRENCY & PARALLELISM
# ==============================================

# --------------------------
# threading
# --------------------------
import threading
import time

def worker(num):
    print(f"Worker {num} started")
    time.sleep(2)
    print(f"Worker {num} finished")

threads = []
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# --------------------------
# multiprocessing
# --------------------------
from multiprocessing import Process

def cpu_bound_task(n):
    return sum(i*i for i in range(n))

if __name__ == '__main__':
    processes = []
    for i in range(4):
        p = Process(target=cpu_bound_task, args=(1000000,))
        processes.append(p)
        p.start()
    
    for p in processes:
        p.join()

# --------------------------
# asyncio
# --------------------------
import asyncio

async def fetch_data():
    print("Start fetching")
    await asyncio.sleep(2)
    print("Done fetching")
    return {'data': 1}

async def main():
    task1 = asyncio.create_task(fetch_data())
    task2 = asyncio.create_task(fetch_data())
    await task1
    await task2

asyncio.run(main())

# ==============================================
# 21. TESTING & DEBUGGING
# ==============================================

# --------------------------
# unittest
# --------------------------
import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()

# --------------------------
# pytest
# --------------------------
"""
# test_sample.py
def func(x):
    return x + 1

def test_answer():
    assert func(3) == 4

# Run with: pytest test_sample.py
"""

# --------------------------
# pdb (Debugger)
# --------------------------
import pdb

def buggy_function(x):
    result = x * 2
    pdb.set_trace()  # Breakpoint here
    return result + 5

# buggy_function(10)
# Commands: n (next), c (continue), p (print), q (quit)

# ==============================================
# 22. PYTHON INTERNALS
# ==============================================

# --------------------------
# GIL (Global Interpreter Lock)
# --------------------------
"""
- Python has a Global Interpreter Lock that allows only one thread to execute Python bytecode at a time
- This means CPU-bound Python code doesn't benefit from threading
- Workarounds: multiprocessing, C extensions, asyncio for I/O-bound tasks
"""

# --------------------------
# Memory Management
# --------------------------
import sys

x = [1, 2, 3]
print(sys.getsizeof(x))  # Memory used by list

# Reference counting
a = []
b = a
print(sys.getrefcount(a))  # Number of references

# Garbage collection
import gc
gc.collect()  # Manually run garbage collector

# --------------------------
# __slots__
# --------------------------
class Regular:
    pass

class Slotted:
    __slots__ = ['x', 'y']

r = Regular()
r.x = 1
r.y = 2
r.z = 3  # Can add new attributes

s = Slotted()
s.x = 1
s.y = 2
# s.z = 3  # AttributeError (no z in __slots__)

# Benefits: Faster attribute access, memory savings
