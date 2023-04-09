"""
WHAT ABOUT
"""

#
# LIBRARY CODE (functions, classes, constants,...)
#
def recurse(x):
    if x >= 1:
        print(x)
        recurse(x-1)


if __name__ == "__main__":
  # FILE CODE / TESTING / DEVELOPMENT
  recurse(10)
