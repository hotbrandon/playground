import sys
from datetime import datetime
from time import strftime


print("from using_modules.py")
print("--------------------- \n")

external_variable = "I'm from my_modules"


def my_function():
    if __name__ == "__main__":
        print("don't call me from the same program")
    else:
        now = datetime.now()
        print(now.strftime('%Y-%m-%d'))


# my_function()
