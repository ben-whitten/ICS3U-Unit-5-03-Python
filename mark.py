#!/usr/bin/env python3

# Created by: Ben Whitten
# Created on: November 2019
# This is a program which converts your mark from number to percent.


# This allows me to do things with the text.
class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


print("This program converts a mark from a number"
      " to a percent.")


def Calculations(mark_as_number_copy):
    # This converts your mark.

    if mark_as_number_copy == ("NE"):
        percent = ("0%")

    elif mark_as_number_copy == ("R"):
        percent = ("30%")

    elif mark_as_number_copy == ("1-") or mark_as_number_copy == ("D-"):
        percent = ("50%")

    elif mark_as_number_copy == ("1") or mark_as_number_copy == ("D"):
        percent = ("53%")

    elif mark_as_number_copy == ("1+") or mark_as_number_copy == ("D+"):
        percent = ("57%")

    elif mark_as_number_copy == ("2-") or mark_as_number_copy == ("C-"):
        percent = ("60%")

    elif mark_as_number_copy == ("2") or mark_as_number_copy == ("C"):
        percent = ("63%")

    elif mark_as_number_copy == ("2+") or mark_as_number_copy == ("C+"):
        percent = ("67%")

    elif mark_as_number_copy == ("3-") or mark_as_number_copy == ("B-"):
        percent = ("70%")

    elif mark_as_number_copy == ("3") or mark_as_number_copy == ("B"):
        percent = ("73%")

    elif mark_as_number_copy == ("3+") or mark_as_number_copy == ("B+"):
        percent = ("77%")

    elif mark_as_number_copy == ("4-") or mark_as_number_copy == ("A-"):
        percent = ("80%")

    elif mark_as_number_copy == ("4") or mark_as_number_copy == ("A"):
        percent = ("87%")

    elif mark_as_number_copy == ("4+") or mark_as_number_copy == ("A+"):
        percent = ("95%")

    elif mark_as_number_copy == ("4++") or mark_as_number_copy == ("A++"):
        percent = ("100%")

    else:
        percent = ("-1")

    return percent


def main():
    # This is what gets your mark as a number.
    while True:
        mark_as_number = input(color.YELLOW + 'Input the base of the' +
                               ' triangle: ' + color.END)

        mark_as_percent = Calculations(mark_as_number)

        if mark_as_percent == ("-1"):
            print(color.PURPLE + color.UNDERLINE + 'That is not a valid'
                  ' number...' + color.END)
            print("")
            print("")
        else:
            print(color.GREEN + 'You got about {0}'.format(mark_as_percent)
                  + color.END)
            break


if __name__ == "__main__":
    main()
