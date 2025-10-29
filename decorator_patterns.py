"""
Decorator Patterns in Python
Demonstrates various decorator implementations and use cases.
Decorators allow you to modify or enhance functions without changing their code.
"""

import time
import functools
from typing import Callable, Any


def timer_decorator(func: Callable) -> Callable:
    """
    Decorator that measures execution time of a function.
    
    Args:
        func: Function to be timed
    
    Returns:
        Wrapped function with timing functionality
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds")
        return result
    return wrapper


def debug_decorator(func: Callable) -> Callable:
    """
    Decorator that prints function name, arguments, and return value.
    Useful for debugging.
    
    Args:
        func: Function to debug
    
    Returns:
        Wrapped function with debug output
    """
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Calling {func.__name__}({signature})")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result!r}")
        return result
    return wrapper


def memoize(func: Callable) -> Callable:
    """
    Decorator that caches function results for given arguments.
    Improves performance for expensive recursive or repeated calls.
    
    Args:
        func: Function to memoize
    
    Returns:
        Wrapped function with caching
    """
    cache = {}
    
    @functools.wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Fetching cached result for {func.__name__}{args}")
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


def retry(max_attempts: int = 3, delay: float = 1.0):
    """
    Decorator that retries a function if it raises an exception.
    
    Args:
        max_attempts: Maximum number of retry attempts
        delay: Delay between retries in seconds
    
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    attempts += 1
                    if attempts >= max_attempts:
                        print(f"Failed after {max_attempts} attempts")
                        raise
                    print(f"Attempt {attempts} failed: {e}. Retrying in {delay}s...")
                    time.sleep(delay)
        return wrapper
    return decorator


def validate_types(**type_hints):
    """
    Decorator that validates function argument types.
    
    Args:
        **type_hints: Expected types for function arguments
    
    Returns:
        Decorator function
    """
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Get function parameter names
            func_params = func.__code__.co_varnames[:func.__code__.co_argcount]
            
            # Check positional arguments
            for arg, param_name in zip(args, func_params):
                if param_name in type_hints:
                    expected_type = type_hints[param_name]
                    if not isinstance(arg, expected_type):
                        raise TypeError(
                            f"Argument '{param_name}' must be {expected_type.__name__}, "
                            f"got {type(arg).__name__}"
                        )
            
            # Check keyword arguments
            for param_name, arg in kwargs.items():
                if param_name in type_hints:
                    expected_type = type_hints[param_name]
                    if not isinstance(arg, expected_type):
                        raise TypeError(
                            f"Argument '{param_name}' must be {expected_type.__name__}, "
                            f"got {type(arg).__name__}"
                        )
            
            return func(*args, **kwargs)
        return wrapper
    return decorator


# Example usage and demonstrations
@timer_decorator
def slow_function():
    """Simulates a slow operation."""
    time.sleep(0.1)
    return "Task completed"


@debug_decorator
def add_numbers(a, b):
    """Adds two numbers with debug output."""
    return a + b


@memoize
def fibonacci(n):
    """Calculates fibonacci number with memoization."""
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@timer_decorator
@memoize
def expensive_computation(n):
    """Demonstrates combining multiple decorators."""
    time.sleep(0.01)  # Simulate expensive operation
    return n * n


@validate_types(name=str, age=int)
def create_user(name, age):
    """Creates a user with type validation."""
    return f"User: {name}, Age: {age}"


if __name__ == "__main__":
    print("=" * 60)
    print("1. Timer Decorator Example:")
    print("=" * 60)
    slow_function()
    
    print("\n" + "=" * 60)
    print("2. Debug Decorator Example:")
    print("=" * 60)
    add_numbers(5, 3)
    
    print("\n" + "=" * 60)
    print("3. Memoization Decorator Example:")
    print("=" * 60)
    print(f"Fibonacci(10) = {fibonacci(10)}")
    print(f"Fibonacci(10) = {fibonacci(10)}")  # Cached result
    
    print("\n" + "=" * 60)
    print("4. Multiple Decorators Example:")
    print("=" * 60)
    print(f"Result: {expensive_computation(5)}")
    print(f"Result: {expensive_computation(5)}")  # Faster with cache
    
    print("\n" + "=" * 60)
    print("5. Type Validation Decorator Example:")
    print("=" * 60)
    print(create_user("Alice", 30))
    
    try:
        create_user("Bob", "25")  # This will raise TypeError
    except TypeError as e:
        print(f"Error: {e}")
