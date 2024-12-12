# Python Functions, Modularity and Code Organization

## Module Structure
A well-organized Python project should have a clear module structure:

```
project/
├── src/
│   ├── __init__.py
│   ├── core/
│   │   ├── __init__.py
│   │   └── base.py
│   ├── utils/
│   │   ├── __init__.py
│   │   └── helpers.py
│   └── services/
│       ├── __init__.py
│       └── data_service.py
├── tests/
│   └── test_core.py
└── main.py
```

## Functions in Python

### Basic Function Definition
```python
def greet(name: str) -> str:
    """
    Greets a person by name.
    
    Args:
        name (str): The name of the person to greet
        
    Returns:
        str: The greeting message
    """
    return f"Hello, {name}!"
```

### Function Parameters
```python
# Required parameters
def add(a: int, b: int) -> int:
    return a + b

# Default parameters
def greet_with_title(name: str, title: str = "Mr.") -> str:
    return f"Hello, {title} {name}!"

# Variable number of arguments
def sum_all(*args: int) -> int:
    return sum(args)

# Keyword arguments
def create_person(**kwargs) -> dict:
    return kwargs

# Mixed parameter types
def process_data(required_param, *args, default_param="default", **kwargs):
    pass
```

### Return Values
```python
# Single return value
def get_square(n: int) -> int:
    return n * n

# Multiple return values using tuple
def get_stats(numbers: list) -> tuple:
    return min(numbers), max(numbers), sum(numbers)

# Early returns
def check_value(x: int) -> bool:
    if x < 0:
        return False
    if x > 100:
        return False
    return True
```

### Function Decorators
```python
from functools import wraps
import time

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.2f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
```

### Lambda Functions
```python
# Simple lambda function
square = lambda x: x * x

# Lambda with multiple parameters
rectangle_area = lambda length, width: length * width

# Lambda with conditional logic
is_adult = lambda age: True if age >= 18 else False
```

## Best Practices for Functions

### 1. Single Responsibility Principle
```python
# Bad: Function does too many things
def process_user_data(user_data):
    validate_data(user_data)
    save_to_database(user_data)
    send_email(user_data)

# Good: Split into focused functions
def validate_user_data(user_data):
    # Validation logic only
    pass

def save_user_data(user_data):
    # Database operations only
    pass

def notify_user(user_data):
    # Email notification only
    pass
```

### 2. Function Length
```python
# Good: Short, focused function
def calculate_average(numbers: list) -> float:
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)

# Good: Complex logic broken down
def process_data(data: list) -> dict:
    cleaned_data = clean_data(data)
    validated_data = validate_data(cleaned_data)
    return transform_data(validated_data)
```

### 3. Clear Parameter Names
```python
# Bad
def p(x, y):
    return x * y

# Good
def calculate_price(quantity: int, unit_price: float) -> float:
    return quantity * unit_price
```

### 4. Type Hints and Documentation
```python
from typing import List, Dict, Optional

def find_user(
    user_id: int,
    users: List[Dict[str, any]],
    include_inactive: bool = False
) -> Optional[Dict[str, any]]:
    """
    Find a user by their ID in a list of users.
    
    Args:
        user_id: The ID of the user to find
        users: List of user dictionaries
        include_inactive: Whether to include inactive users
        
    Returns:
        The user dictionary if found, None otherwise
        
    Raises:
        ValueError: If user_id is negative
    """
    if user_id < 0:
        raise ValueError("User ID cannot be negative")
        
    for user in users:
        if user["id"] == user_id:
            if include_inactive or user["active"]:
                return user
    return None
```

## Best Practices for Modularity

### 1. Single Responsibility Principle
```python
# Good: Each class has a single responsibility
class UserAuthentication:
    def authenticate(self, username, password):
        pass

class UserProfile:
    def get_profile(self, user_id):
        pass
```

### 2. Dependency Injection
```python
# Good: Dependencies are injected
class DataProcessor:
    def __init__(self, data_source):
        self.data_source = data_source
    
    def process(self):
        data = self.data_source.get_data()
        return self.transform(data)
```

### 3. Interface Segregation
```python
# Good: Specific interfaces instead of one large interface
class DataReader:
    def read_data(self):
        pass

class DataWriter:
    def write_data(self, data):
        pass
```

### 4. Utility Modules
```python
# utils/string_helpers.py
def capitalize_words(text: str) -> str:
    return " ".join(word.capitalize() for word in text.split())

def remove_extra_spaces(text: str) -> str:
    return " ".join(text.split())

# utils/validation.py
def is_valid_email(email: str) -> bool:
    import re
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone: str) -> bool:
    import re
    pattern = r'^\+?1?\d{9,15}$'
    return bool(re.match(pattern, phone))
```

### 5. Configuration Management
```python
# config/settings.py
class Config:
    DEBUG = False
    DATABASE_URL = "sqlite:///app.db"
    SECRET_KEY = "your-secret-key"

class DevelopmentConfig(Config):
    DEBUG = True

class ProductionConfig(Config):
    DATABASE_URL = "postgresql://user:pass@localhost/db"
```