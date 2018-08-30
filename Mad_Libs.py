print("Welcome to Mad Libs")

user_inputs = []

# Mad_Libs = {'Mad Lib 1 title': "sososo"}

# The part of speech list are empty


testList = ['This is {} and this is {}']

prompt_for_user = ['noun ', 'verb ']
nounList = []


def required_inputs():
    input_taken = []
    if len(prompt_for_user) == testList[0].count('{}'):
        for i in prompt_for_user:
            input_taken.append(user_input(i))

    noun_insert(input_taken)


def noun_input():
    i = 0
    while i < testList[0].count('{}'):

        noun = user_input('Please input a noun: ')
        nounList.append(noun)
        i += 1


def noun_insert(value):

    print(testList[0].format(*value))

    # testList[0] = testList[0].format(i)
    # print(testList[0].format( nounList[0], nounList[1]))


def user_input(prompt):

    return input(prompt)


def test():
    # The user will be able to input
    pass


required_inputs()
