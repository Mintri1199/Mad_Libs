import os


testList = {'Test title':'This is {} and this is {}'}

prompt_for_user = ['noun ', 'verb ']

nounList = []


# Allow the use to change their inputs
def change_input(inputted):

    for index, string in enumerate(inputted):
        print(index, string)

    flag = input("Do you want to change your answer?  Y/N")

    while flag.upper() == "Y":
        try:
            changing = input('Input the number associated to the desired item: ')

            inputted[int(changing)] = input("Please input a " + prompt_for_user[int(changing)])

            print(*inputted)

        except TypeError:
            exit()

    print(noun_insert(inputted))


# Determine the amount of inputs require for the selected Mad Lib
def required_inputs():
    input_taken = []
    if len(prompt_for_user) == testList[0].count('{}'):
        for i in prompt_for_user:
            input_taken.append(input(i))

    change_input(input_taken)


# Insert the user inputs into the Mad Lib
def noun_insert(taken_list, selected_story):
    try:
        return testList[selected_story].format(*taken_list)

    except TypeError:
        print("What you've entered wasn't a number: ")

    except IndexError:
        print("You try to choose a story that doesn't exist in our library.")


# Run the program
def run():
    print("Welcome to Mad Libs")
    initial = True

    while initial:

        flag = input("Do you want do some Mad Libs?     Y/N\n")

        if flag.upper() == "Y":
            pass
        elif flag.upper() == "N":
                initial = False

        else:
            print("What you've entered was neither Y or N!\n")

        while flag.upper() == "Y":
            # os.system("clear")
            for indexes, title in enumerate(testList.keys()):
                print(indexes, title)

            flag = "N"

    print("Thank you for stopping by!")


run()