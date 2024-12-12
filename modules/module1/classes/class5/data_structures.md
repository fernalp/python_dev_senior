# Python Data Structures Guide

## Lists
Lists in Python are ordered, mutable sequences that can store elements of different types.

```python
# List creation and basic operations
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "hello", 3.14, True]

# List methods
numbers.append(6)        # Add element to end
numbers.insert(0, 0)    # Insert at specific position
numbers.pop()           # Remove and return last element
numbers.remove(3)       # Remove specific element
```

## Tuples
Tuples are immutable sequences, often used for grouped data that shouldn't change.

```python
# Tuple creation and usage
point = (x, y)
rgb_color = (255, 128, 0)
person = ("John", "Doe", 30)

# Tuple unpacking
name, surname, age = person
```

## Dictionaries
Dictionaries are key-value pairs that allow fast lookups and flexible data organization.

```python
# Dictionary creation and operations
user = {
    "name": "Alice",
    "age": 25,
    "email": "alice@example.com"
}

# Dictionary methods
user["location"] = "New York"  # Add new key-value pair
del user["age"]               # Remove key-value pair
keys = user.keys()            # Get all keys
values = user.values()        # Get all values
```