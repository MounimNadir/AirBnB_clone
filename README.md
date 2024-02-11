## Project Description

This project is the command interpreter for the 0x00 Airbnb Console. It is a command-line application that allows users to interact with the Airbnb database and perform various operations such as creating, updating, and deleting objects.

## Command Interpreter 0x00 Airbnb Console

The command interpreter is a Python-based shell that provides a command-line interface for interacting with the Airbnb database. It allows users to execute commands and perform operations on the database.

### How to Start

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Open a terminal or command prompt.
4. Run the command `./console.py` to start the command interpreter.

### How to Use

Once the command interpreter is started, you can use various commands to interact with the Airbnb database. The available commands include:

- `create`: Create a new object in the database.
- `show`: Display information about a specific object.
- `update`: Update the attributes of an object.
- `destroy`: Delete an object from the database.
- `all`: Display all objects in the database.
- `quit`: Exit the command interpreter.

To execute a command, simply type the command followed by any required arguments or options. For example:

```
(hbnb) create User
(hbnb) show User 1234-5678-9012
(hbnb) update User 1234-5678-9012 name "John Doe"
(hbnb) destroy User 1234-5678-9012
(hbnb) all
(hbnb) quit
```

### Examples

Here are some examples of how to use the command interpreter:

- Create a new User object:
```
(hbnb) create User
```

- Show information about a specific User object:
```
(hbnb) show User 1234-5678-9012
```

- Update the name attribute of a User object:
```
(hbnb) update User 1234-5678-9012 name "John Doe"
```

- Delete a User object from the database:
```
(hbnb) destroy User 1234-5678-9012
```

- Display all objects in the database:
```
(hbnb) all
```

- Exit the command interpreter:
```
(hbnb) quit
```

## Authors

- Mounim Nadir
- Kryuel

