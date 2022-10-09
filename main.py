#import package
import random

#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    answer = random.randint(0, 100)

    minnumber = 0
    maxnumber = 100

    # print(a)

    while True:
        userinput = input("Guess a number:")
        if(type(userinput) is not int):
            print("Please enter a number")
        else:
            print("Your guess is: " + userinput)
            if int(userinput) > answer:
                maxnumber = userinput
            elif int(userinput) < answer:
                minnumber = userinput
            print(str(minnumber) + " : " + str(maxnumber))
            if int(userinput) == answer:
                print("The correct answer is " + str(answer) + ", you WIN!")
                break