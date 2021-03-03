'''This module creates a menu for work with notebook.'''

import sys
from notebook import Notebook, Note

class Menu:
    '''Display a menu and respond to choices when run.'''

    def __init__(self):
        '''Creates a menu.'''
        self.notebook = Notebook()
        self.choices = {
        "1": self.show_notes,
        "2": self.search_notes,
        "3": self.add_note,
        "4": self.modify_note,
        "5": self.quit
        }


    def display_menu(self):
        ''' Displays the menu options.'''
        print("""
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit
""")


    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))


    def show_notes(self, notes=None):
        '''Prints the information about notes.'''
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(note.note_id, note.tags, note.memo))


    def search_notes(self):
        '''Prints notes with memos that contain a string that a user inputs
        or error message if there are no such memos.'''
        filter_str = input("Search for: ")
        notes = self.notebook.search(filter_str)
        if notes:
            self.show_notes(notes)
        else:
            print('There are no notes with such filter.')


    def add_note(self):
        '''Adds a new note to the notebook.'''
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        self.notebook.new_note(memo, tags)
        print("Your note has been added.")


    def modify_note(self):
        '''Changes the memo or/and tag of the note with note_id.'''
        note_id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(note_id, memo)
        if tags:
            self.notebook.modify_tags(note_id, tags)


    def quit(self):
        '''Quits the notebook use.'''
        print("Thank you for using your notebook today.")
        sys.exit(0)


if __name__ == "__main__":
    Menu().run()
