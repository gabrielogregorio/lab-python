# pip install pytest
import pytest


def somar(x, y):
  return x + y

def test_somar():
  assert somar(10, 20) == 30

# python -m pytest .\usando_pytest.py