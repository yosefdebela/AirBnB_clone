![image](https://user-images.githubusercontent.com/106808436/203632781-41505e68-a74c-4907-844a-b682b6b4217b.png)

Welcome to the AirBnB clone project!

# ***Description***

This is an ALX AirBnB clone project, it is a complete web application, integrating database storage, a back-end API, and front-end interfacing in a clone of AirBnB. This project is the first part of the AirBnB clone project and uses a parent class with other classes that inherit from the parent class and uses Json for file storage. rest of the project to continue in subsequent projects....
This project currently only implements the back-end console.

  # ***How to Use Command Interpreter***
|     **COMMAND**  |  SAMPLE USAGE            |       FUNCTIONALITY                           |
|------------------|--------------------------|-----------------------------------------------|
|       Help       |     help                 |  displays all commands available              |

|       Create     |  create <class>          |  creates new object (ex. a new User, Place)   |

|       Update     |  User.update('123',      |  updates attribute of an object               |
|                  |  {'name' : 'Greg_n_Mel'})|                                               |    
  
|       Destroy    |  User.destroy('123')     |   destroys specified object                   |

|       Show       |  User.show('123')        |   retrieve an object from a file, a database  |

|       All        |    User.all()            |  display all objects in class                 |

|       Count      |   User.count()           |  returns count of objects in specified class  |
|                  |
|       Quit       |     quit                 |       exits                                   |
 
  
  
  # **USAGE**
  ## Interactive Mode
  $ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
  
  
  ## Non-Interactive Mode
  $ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
