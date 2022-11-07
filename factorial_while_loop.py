#!/usr/bin/env python3
# Created by: Kyanh Pham
# Created on: Oct 2022
# This program uses while loops


def main():

    loop_counter = 0
    multiply_int = 1

    # This function multiplies all the whole numbers up to the inputted number

    # Input
    positive_string = input("Please enter a positive number: ")
    print("")

    # Process and output
    try:
        positive_integer = int(positive_string)
        if positive_integer >= 0:
            while loop_counter < positive_integer:
                loop_counter = loop_counter + 1
                multiply_int = multiply_int * loop_counter
            print("{0}! = {1}.".format(positive_integer, multiply_int))
        else:
            print("{0} is not a positive integer".format(positive_string))
    except ValueError:
        print("{0} is not a valid input".format(positive_string))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
