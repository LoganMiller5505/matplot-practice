from functools import cache
import sys

sys.setrecursionlimit(10000)

@cache
def funct(n):
    # Base cases exist where n is 1, 2, 3, 4
    # These represent the constant edge points of the square (P1, P2, P3, P4)
    if n <= 1:
        return [0,1]
    elif n == 2:
        return [1,1]
    elif n == 3:
        return [1,0]
    elif n == 4:
        return [0,0]
    
    # Recursion/summation case
    return [(funct(n-3)[0]+funct(n-4)[0])/2, (funct(n-3)[1]+funct(n-4)[1])/2]

import matplotlib.pyplot as plt

def draw_square():
    square_corners = [[0, 0], [0, 1], [1, 1], [1, 0]]
    square_corners.append(square_corners[0])  # Closing the square
    x = [point[0] for point in square_corners]
    y = [point[1] for point in square_corners]
    
    plt.plot(x, y, 'k-')  # Plotting the square

def draw_lines(coordinates):
    if coordinates != [0,0] and coordinates != [0,1] and coordinates != [1,1] and coordinates != [1,0]:
        x = [point[0] for point in coordinates]
        y = [point[1] for point in coordinates]
        
        plt.plot(x, y, 'ro-')  # Plotting the lines

import fractions
from fractions import Fraction

if __name__ == "__main__":

    print("What n value would you like to test to? (n>4): ")
    n = int(input())
    print(funct(n))

    result = funct(n)
    x_value = Fraction(result[0]).limit_denominator()
    y_value = Fraction(result[1]).limit_denominator()

    print(f"X Value: {x_value}")
    print(f"Y Value: {y_value}")

    draw_square()

    value_list = []

    for i in range(5, n):
        draw_lines([funct(i-1), funct(i)])
        value_list.append(funct(i))

    plt.axis('equal')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('11 PP #18')
    plt.grid(True)

    plt.figure()  # Creating a new figure for the second plot

    x_values = list(range(5, n))
    y_values_x = [point[0] for point in value_list]
    y_values_y = [point[1] for point in value_list]

    plt.subplot(2, 1, 1)
    plt.plot(x_values, y_values_x, 'bo-')
    plt.xlabel('N')
    plt.ylabel('X')
    plt.title('X Values')
    plt.grid(True)

    plt.subplot(2, 1, 2)
    plt.plot(x_values, y_values_y, 'ro-')
    plt.xlabel('N')
    plt.ylabel('Y')
    plt.title('Y Values')
    plt.grid(True)

    plt.tight_layout()
    plt.show()