import unittest
import inspect


class TestEntityPrompts(unittest.TestCase):
    def test_ACE(self):
        from src.tasks.ace.prompts import Person

        print()
        print(inspect.getsource(Person))
