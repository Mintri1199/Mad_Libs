import os

from termcolor import cprint , colored


class Madlibs:

    def __init__(self):

        vacation = ["adjective", "adjective", "noun", "noun", "plural noun", "game", "plural noun",
                    'verb ending in "ing"', 'verb ending in "ing"', "plural noun", 'verb ending in "ing"',
                    "noun", 'noun', "part of the body", 'a place', 'verb ending in "ing"', 'adjective',
                    'number', 'plural noun']

        park = ['adjective', 'plural noun', 'noun', 'adverb', 'number', 'past tense verb', '-est adjective',
                'past tense verb', 'adverb', 'adjective']

        jungle = ['adjective','adjective', 'adjective', 'noun', 'adjective', 'adjective','noun','verb','verb',
                  'adjective', 'noun', 'verb','noun', 'verb', 'adjective']

        zoo = ['adjective', 'noun', 'verb, past tense', 'adverb', 'adjective', 'noun', 'noun', 'adjective', 'verb',
               'adverb', 'verb, past tense', 'adjective']

        self.story = []
        self.selection = []
        self.input_taken = []
        self.chosen_title = ''
        self.story_select = ""
        self.title_library = ['vacation', 'park', 'jungle', 'zoo']
        self.story_library = {'vacation.txt': vacation, 'park.txt' : park, 'jungle.txt': jungle , 'zoo.txt': zoo}

    # Allow the user to select the story
    def selecting_story(self):
        for indexes, title in enumerate(self.title_library):
            print(indexes, title)

        self.story_select = input("Enter the number associated with the title you want:\n")

        while self.story_select:

            try:
                return int(self.story_select)

            except ValueError:
                cprint("What you've entered wasn't a number!\n", 'red', attrs=['bold'])
                self.story_select = input("Please input a NUMBER correspond with the story you want\n")

    # Determine the amount of inputs require for the selected Mad Lib
    def required_inputs(self):
        try:
            self.chosen_title = self.title_library[int(self.story_select)] + '.txt'

            with open(self.chosen_title) as file:
                read_file = file.read()

                if len(self.story_library[self.chosen_title]) == read_file.count('{}'):
                    for i in self.story_library[self.chosen_title]:
                        self.input_taken.append(input(i + ": "))

                    os.system("clear")

        except IndexError:
            os.system("clear")
            cprint("The story you select did not exist!", 'red', attrs=['bold'])
            self.selecting_story()

    # Allow the use to change their inputs
    def change_input(self):
        done = colored("done", 'green', attrs=['bold'])
        for index, string in enumerate(self.input_taken):
            print(index, string)

        flag = input("Do you want to change your answer?  Y/N ")

        while flag.upper() == "Y":
            try:
                changing = input('Input the number associated to the desired item or input ' + done + ' to finish: ')
                if changing.upper() == "DONE":
                     flag = changing

                else:
                    self.input_taken[int(changing)] = input("Please input a " +
                                                            self.story_library[self.chosen_title][int(changing)] + ": ")

            except IndexError:
                cprint("What you try to change is not with the list of inputs!", 'red', attrs=['bold'])

    # Insert the user inputs into the Mad Lib
    def input_insert(self):

        try:
            with open(self.chosen_title) as file:
                read = file.read()

                os.system("clear")

                print(read.format(*self.input_taken))

        except TypeError:
            print("What you've entered wasn't a number: ")

        except IndexError:
            print("You try to choose a story that doesn't exist in our library.")

    # Run the program
    def run(self):
        cprint('Welcome to Mad Libs', 'green', attrs=['bold'])
        initial = True

        while initial:

            starting_question = input("Do you want do some Mad Libs?     Y/N\n")

            if starting_question.upper() == "Y":
                pass

            elif starting_question.upper() == "N":
                initial = False

            else:
                print("What you've entered was neither Y or N!\n")

            while starting_question.upper() == "Y":
                # os.system("clear")

                self.selecting_story()
                self.required_inputs()
                self.change_input()
                self.input_insert()

                starting_question = "N"

        cprint('Thank for stopping by!', 'magenta')


test = Madlibs()

test.run()
