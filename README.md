# UNIT-PROJECT-1



## Based on what you’ve learned until now , create a project of your choosing (impress us with your imagination) . This project must at least satisfy the following minimum requirements :

- Must be interactive on CLI.
- Use your coding skills in Python accurately.
- Organize Your Code into modules & (or packages)
- Use git & Github to track changes in your code.

### Library Management System

### Overview 

 The Library Management System is project designed to manage books and members in a library. The system allows admin to add, remove, search, borrow, and return books. It also facilitates member management and tracks borrowing history. The application is divided into several functionalities for both book and member management, ensuring smooth operations for library admin.

### Features 

Book Management: Admin can add, remove, list, search, and update the quantity of books.
Member Management: Admin can add, remove, and list members. It ensures members return books before they are removed.
Borrowing & Returning: Members can borrow books (if available) and return them when done. The system tracks borrowed books and maintains a history.
Borrowing History: Admin can view a member’s borrowing history, including details about borrowed books.

### User Stories

#### As an Admin, I should be able to:
Add a new book to the library.
Remove a book from the library.
List all available books.
Search for a book by title, author, or category.
Update the quantity of a book.
Add a new member to the library system.
Remove a member from the library system.
List all registered members.
Borrow a book to a member.
Return a borrowed book.


#### Usage :

option 1 to add a new book:
Enter the book's title, author, category, and quantity.

option 2 to remove a book:
Enter the book's ID to remove.

option 3 to list all available books:
Shows a table of all books in the library.

option 4 to search for a book:
Choose whether to search by title, author, or category, and enter the search term.

option 5 to update book quantity:
Enter the book's ID and the new quantity.

option 6 to add a new member:
Enter the member’s name.

option 7 to remove a member:
Enter the member’s name.

option 8 to list all registered members:
Shows a table of all members.

option 9 to borrow a book:
Enter the member's name and the book's ID.

option 10 to return a borrowed book:
Enter the member's name and the book's ID.

option 11 to view a member's borrowing history:
Enter the member’s name to see the list of borrowed books and their details.


### For your project. Edit this README.md file to include your own project name,  overview, user stories, and usage. 

### NOTE: before submitting the final project, please do the following command:
`pip freeze > requirements.txt` to enable use to know & use the packages used in your project.
