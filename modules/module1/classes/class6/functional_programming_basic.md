# Functional Programming in Python

## Pure Functions
Pure functions always produce the same output for the same input and have no side effects.

```python
# Pure function example
def multiply(x, y):
    return x * y

# Impure function example (for comparison)
total = 0
def add_to_total(x):
    global total
    total += x
    return total
```

## Lambda Functions
Lambda functions are small anonymous functions defined using the `lambda` keyword.

```python
# Lambda function examples
square = lambda x: x * x
add = lambda x, y: x + y
```

## Map, Filter, and Reduce
Common functional programming operations in Python:

```python
# Map: Apply function to every item in a sequence
numbers = [1, 2, 3, 4, 5]
squares = map(lambda x: x * x, numbers)

# Filter: Create a sequence of elements that satisfy a condition
evens = filter(lambda x: x % 2 == 0, numbers)

# Reduce: Apply function of two arguments cumulatively to sequence
from functools import reduce
sum_all = reduce(lambda x, y: x + y, numbers)
```

## List Comprehensions
A more Pythonic way to apply functional concepts:

```python
# List comprehension examples
squares = [x * x for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```