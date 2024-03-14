from user_input import get_selection, SelectionFromNumber
from time import time

fruits = ["apple", "banana", "orange", "grape", "watermelon", "strawberry", "pineapple", "mango", "kiwi", "pear",
          "cherry", "blueberry", "lemon", "lime", "peach", "plum", "raspberry", "blackberry", "pomegranate", "avocado"]


def selection():
    sel = SelectionFromNumber(fruits)
    sel.answer = "1 4-8 14-18 20"
    sel.prompt_process()
    sel.make_selection()
