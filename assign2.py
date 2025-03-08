# Created by: Hiab G
# Date: Wed, Feb. 25th
# This program calculates the surface area and volume of a hexagonal prism  with user input
import math
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)


def calculate_surface_area(a, h):
    # Surface area formula: A = 6ah + 3√3a²
    surface_area = 6 * a * h + 3 * math.sqrt(3) * (a ** 2)
    return surface_area


def calculate_volume(a, h):
    # Volume formula: V = (3√3 / 2) * a² * h
    volume = (3 * math.sqrt(3) / 2) * (a ** 2) * h
    return volume


def main():
    print("Welcome to the Hexagonal Prism Calculator!")

    # User input for base length (a), base (h), units, and color
    Base = float(input("Enter the base (a) of the hexagonal prism: "))
    height = float(input("Enter the height (h) of the hexagonal prism: "))
    units = input("Enter the units of measurement (e.g., meters, inches): ")

# Ask the user for text color and style code from https://www.youtube.com/watch?v=u51Zjlnui4Y 
    print("\nChoose a text color:")
    print("1. Red")
    print("2. Green")
    print("3. Blue")
    print("4. Yellow")
    color_choice = input("Enter the number of your choice (1-4): ")

    print("\nChoose a text style:")
    print("1. Normal")
    print("2. Bright")
    print("3. Dim")
    style_choice = input("Enter the number of your choice (1-3): ")
 
 # Map color choice to Fore color
    if color_choice == "1":
        color = Fore.RED
    if color_choice == "2":
        color = Fore.GREEN
    if color_choice == "3":
        color = Fore.BLUE
    if color_choice == "4":
        color = Fore.YELLOW
     
     # Map style choice to Style
    if style_choice == "1":
        style = Style.NORMAL
    if style_choice == "2":
        style = Style.BRIGHT
    if style_choice == "3":
        style = Style.DIM

    # Calculate surface area and volume
    surface_area = calculate_surface_area(Base, height)
    volume = calculate_volume(Base, height)

    # Display the results
    print("\nHexagonal Prism Details:")
    print(f"Base Length (a): {Base} {units}")
    print(f"Height (h): {height} {units}")
    print(f"Color: {color}")
    print(f"Surface Area: {color + style}{surface_area:.2f} square {units}")
    print(f"Volume: {color + style}{volume:.2f} cubic {units}")


if __name__ == "__main__":
    main()
