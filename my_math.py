"""Function to calclulate the area of geometric shapes."""

import math
from turtle import width

#SECTION - 2D shapes

#ANCHOR - fun: square
def square(side:float) -> float:
    """Gets the area of a square."""
    return side**2

#ANCHOR - fun: rectangle
def rectangle(length: float, width: float) -> float:
    """Gets the area of a rectangle."""
    return length * width


#!SECTION

if __name__ == "__main__":
    print(f"my_math.py")