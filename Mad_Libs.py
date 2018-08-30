#


#

testList = ['This is {} and this is {}']

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

            inputted[int(changing)] = input("Please input a " +
                                            prompt_for_user[int(changing)])
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
def noun_insert(value):
    return testList[0].format(*value)


def run():
    pass


required_inputs()
