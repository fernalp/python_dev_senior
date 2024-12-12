"""
Module demonstrating functional programming concepts
"""
from typing import List, Callable, TypeVar, Any
from functools import reduce

T = TypeVar('T')
R = TypeVar('R')

def map_data(func: Callable[[T], R], data: List[T]) -> List[R]:
    """Apply a function to all elements in a list"""
    return list(map(func, data))

def filter_data(predicate: Callable[[T], bool], data: List[T]) -> List[T]:
    """Filter elements based on a predicate"""
    return list(filter(predicate, data))

def reduce_data(func: Callable[[R, T], R], data: List[T], initial: R) -> R:
    """Reduce a list to a single value"""
    return reduce(func, data, initial)

# Common functional operations
get_even_numbers = lambda numbers: filter_data(lambda x: x % 2 == 0, numbers)
sum_numbers = lambda numbers: reduce_data(lambda x, y: x + y, numbers, 0)
double_numbers = lambda numbers: map_data(lambda x: x * 2, numbers)

# Demonstrate functional programming
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = get_even_numbers(numbers)
print(f"Even numbers: {even_numbers}")

doubled = double_numbers(numbers)
print(f"Doubled numbers: {doubled}")

total = sum_numbers(numbers)
print(f"Sum of numbers: {total}")