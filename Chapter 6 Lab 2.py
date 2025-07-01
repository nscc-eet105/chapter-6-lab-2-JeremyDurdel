#Jeremy Durdel
#Chapter 6 Lab 2
#07/01/2025

import matplotlib.pyplot as plt

def main():
    x = -21
    x_coords = [x for x in range(-20, 21)]
    x += 1

    y_coords = []
    slope = float(input("What is the slop of your line? "))
    y_int = float(input("What is the y-intercept of your line? "))
    for x in x_coords:
        y_coords.append(slope * x + y_int)

    plt.plot(x_coords, y_coords)
    plt.grid(True)
    plt.xlim(xmin=-20, xmax=20)
    plt.ylim(ymin=-20, ymax=20)
    plt.axhline(y=0, color='k')
    plt.axvline(x=0, color='k')
    plt.show()


main()