print("Welcome to Mad Libs")

user_inputs = []

# Mad_Libs = {'Mad Lib 1 title': "sososo"}

# The part of speech list are empty


testList = ['This is {!r} and this is {!r}']

nounList = []

verbList = []

adjectiveList = []


def noun_input():
    i = 0
    while i < testList[0].count('{!r}'):

        noun = user_input('Please input a noun: ')
        nounList.append(noun)
        i += 1


def noun_insert():

    print(testList[0].format( nounList[0], nounList[1]))


def user_input(prompt):

    return input(prompt)


def test():
    # The user will be able to input
    pass





noun_input()

print(nounList)

noun_insert()
