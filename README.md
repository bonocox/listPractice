Simple Contact Manager
This Python program is a basic contact management tool that allows users to insert, update, delete, and display entries. The data is stored in a predefined list format (list1), which holds four fields: Name, Age, Location, and Telephone.

Features
Insert: Allows the user to add new contact information for each field (Name, Age, Location, and Telephone).
Update: Lets the user select a field to update with new information.
Delete: Clears a selected field from the contact list.
Show Entries: Displays the current values in all fields of the contact list.
Exit: Exits the program.
Code Overview
The main components of this program are:

list1: A list that holds the four contact fields. Initially, it is populated with placeholder values: "Name", "Age", "Location", and "Telephone".
Functions
insert():

Prompts the user to input values for each field in the contact list.
Updates list1 with the provided information.
Displays the updated list.
update():

Asks the user to specify which field they want to update (by entering a number between 0 and 3).
Updates the specified field with the new input.
Confirms that the entry was updated.
delete():

Prompts the user to choose which field to delete (by entering a number between 0 and 3).
Sets the selected field to None, effectively clearing it.
Confirms that the entry was deleted.
Loop Structure:

A while loop continuously prompts the user to choose an action.
Options:
1 for Insert
2 for Update
3 for Delete
4 to Show Entries
5 to Exit the program
Usage
To run this program:

Execute the script in a Python environment.
Follow the on-screen prompts to insert, update, delete, or view entries.
Choose 5 to exit the program when finished.
Sample Interaction
vbnet
Copiar código
What would you like to do?
1-Insert.
2-update.
3-delete.
4-show entries.
5-Exit
Type the corresponding number: 1

Write your name: John
How old are you?: 30
Where are you from?: New York
What's your telephone number?: 123456789

The present list is: 0: John
The present list is: 1: 30
The present list is: 2: New York
The present list is: 3: 123456789
In this sample, the user adds new information for all fields, and the program displays the updated contact list.

Requirements
Python 3.x
This program provides a simple structure for managing a small set of information. It can be modified to add more fields or store multiple entries if needed.
