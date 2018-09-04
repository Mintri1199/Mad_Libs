# import os

from termcolor import cprint


class Madlibs():

    def __init__(self):
        self.story = []
        self.selection = []
        self.input_taken = []
        self.chosen_title = ''
        self.story_select = ""
        self.title_library = ['vacation']
        self.story_library = {'vacation.txt': ""}
        self.user_prompts = ["adjective", "adjective", "noun", "noun", "plural noun", "game", "plural noun",
                             'verb ending in "ing"', 'verb ending in "ing"', "plural noun", 'verb ending in "ing"',
                             "noun", 'noun', "part of the body", 'a place', 'verb ending in "ing"', 'adjective',
                             'number']

    # Allow the user to select the story
    def selecting_story(self):
        for indexes, title in enumerate(self.story_library):
            print(indexes, title)

        self.story_select = input("Enter the number associated with the title you want:\n")

        while self.story_select:

            try:
                return int(self.story_select)

            except ValueError:
                cprint("What you've entered wasn't a number!", 'red', attrs=['bold'])
                self.story_select = input("Please input a NUMBER correspond with the story you want\n")

    # Determine the amount of inputs require for the selected Mad Lib
    def required_inputs(self):
        self.chosen_title = self.title_library[int(self.story_select)] + '.txt'

        with open(self.chosen_title) as file:
            read_file = file.read()
            try:
                if len(self.user_prompts) == read_file.count('{}'):
                    for i in self.user_prompts:
                        self.input_taken.append(input(i))

            except KeyError:
                # os.system("clear")
                print()
                self.selecting_story()

    # Allow the use to change their inputs
    def change_input(self):
        for index, string in enumerate(self.input_taken):
            print(index, string)

        flag = input("Do you want to change your answer?  Y/N")

        while flag.upper() == "Y":
            try:
                changing = input('Input the number associated to the desired item: ')

                self.input_taken[int(changing)] = input("Please input a " + self.user_prompts[int(changing)])

                print(*self.input_taken)

            except ValueError:
                exit()

    # Insert the user inputs into the Mad Lib
    def noun_insert(self):
        try:
            with open(self.chosen_title) as file:
                read = file.read()

                return read.format(*self.input_taken)

        except TypeError:
            print("What you've entered wasn't a number: ")

        except IndexError:
            print("You try to choose a story that doesn't exist in our library.")

    # Run the program
    def run(self):
        self.selecting_story()
        self.required_inputs()
        self.change_input()
        self.noun_insert()



test = Madlibs()

test.run()