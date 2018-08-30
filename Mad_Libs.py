print("Welcome to Mad Libs")

user_inputs = []

# Mad_Libs = {'Mad Lib 1 title': "sososo"}

# The part of speech list are empty


testList = ['This is {} and this is {}']

prompt_for_user = ['noun ', 'verb ']
nounList = []


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


# Determine the amount of inputs require for the selected Mad Lib
def required_inputs():
    input_taken = []
    if len(prompt_for_user) == testList[0].count('{}'):
        for i in prompt_for_user:
            input_taken.append(input(i))

    change_input(input_taken)


def noun_input():
    i = 0
    while i < testList[0].count('{}'):

        noun = input('Please input a noun: ')
        nounList.append(noun)
        i += 1


def noun_insert(value):

    print(testList[0].format(*value))


def test():
    # The user will be able to input
    pass


required_inputs()
