# The Notebook

This program is created to work with notes as objects: to add them into the notebook, modify them and see the result.

As a result, there is a module with the menu that has 5 options:
- Show all notes
- Search notes by a string: gives information about all notes that have such string
- Add note by writing a memo and tag. Automatically gives an id to the note.
- Modify note: chance to change the memo or/and change/add a tag.
- Quit

The program is created for entartainment, work with notes and notebook and better understanding of classes in Python.

The program contains *2 modules* that serve for the problem solving.

- The first module is notebook. It contains two classes: Note and Notebook. They work with notes and notebook.
- The second module is menu. It creates the navigation for user to choose options what to do with the notebook.

There are no special requirements.

> To use the program, download two modules: notebook.py and menu.py
> Then open and start menu.py
> You will have the opportunity to chhose what to do with the notebook until you decide to quit the program.

### An example of the program use

```sh
>>> python menu.py
Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit

Enter an option: 3
Enter a memo: new_memo
Enter tags: new_tag
Your note has been added.

Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit

Enter an option: 4
Enter a note id: 1
Enter a memo: modified_memo
Enter tags:

Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit

Enter an option: 1
1: new_tag
modified_memo

Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit

Enter an option: 2
Search for: memo
1: new_tag
modified_memo

Notebook Menu
1. Show all Notes
2. Search Notes
3. Add Note
4. Modify Note
5. Quit

Enter an option: 5
Thank you for using your notebook today.
```

#### Have fun using The Notebook program!