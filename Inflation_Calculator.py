"""Project 1: Inflation Calculation"""

"""Assignment:
You will implement a program which can be used to figure out the maximum inflation
 increase from the values the user entered. In other words: which is the largest difference between the consecutive entered values."""

"""Program behavior: 
When the program is started it waits the user to enter monthly values for the inflation figures.
1. Take inputs from user, take at least 2 inputs; otherwise, the program wont work
2. Pick the max and min through all of that inputs to cal the differences of them
3. Return the highest differences of them all 
4. That differences should be displayed as the result written in one decimal accuracy
"""


def main():
    # Store input taken from prompt in a list and create another list for later calculation:
    # create a counter to help with printing different months
    lst = []
    array = []
    count = 1

    # asking for input of the 1st month
    data_in = input("Enter inflation rate for month 1: ")

    # create "while - loop"
    while True:
        if data_in != "":
            lst.append(data_in)
            count = count + 1
            data_in = input("Enter inflation rate for month {}: ".format(count))

        # if the input is empty, then check these conditions:
        elif data_in == "":
            # if there is 0 or 1 input, then end/re-run the program
            # There should be at least 2 inputs taken from prompt
            if len(lst) == 0 or len(lst) < 2:
                print("Error: at least 2 monthly inflation rates must be entered.")
                #data_in = input("Enter inflation rate for month {}: ".format(count))
                break
            else:
                break
    # Remove the # key below for testing
    # print("data: {}, len:{}".format(lst, len(lst)))

    # if the list has more than 2 input to compare:
    while len(lst) != 0 and len(lst) >= 2:
        if len(lst) == 2:
            differences = float(lst[1]) - float(lst[0])
            print("Maximum inflation rate change was {:.1f} points.".format(differences))
            break
        # if there is more than 2 inputs
        # make sure the differences is equals the subtraction between that input and the one before its.
        # make a olist of this diffrences , and select the max value as the final answer
        else:
            n = 1
            for n in range(1, len(lst)):
                differences = float(lst[n]) - float(lst[n - 1])
                array.append(differences)
                # print("present-value: {}, and other:{}".format(lst[n], lst[n - 1]))
            # print("new array: {}".format(array))
            print("Maximum inflation rate change was {:.1f} points.".format(float(max(array))))
            break


if __name__ == "__main__":
    main()
