import pytest

# Przykładowa funkcja do testowania
def add_numbers(a, b):
    return a + b

# Prosty test jednostkowy
def test_add_numbers():
    result = add_numbers(3, 5)
    assert result