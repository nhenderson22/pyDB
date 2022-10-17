# pyDB: A Document Oriented Database written in python for fun
pyDB is a personal project that I am currently developing. I am trying to create a new method for storing data an use it as a source to learn better techniques and practices in software engineering. NOTE: pyDB is not meant to be used in any professional capacity it is quite slow and far from a good option.
## Thoughts behind the design implementation
When I designed this database schema I tried to come up with a solution to remembering the key to the desired dataset. This is why each table is stored under a user specified key. An ID scheme can be created by the user or added into the existing code in whatever paradigm the user chooses. This is why the database is relatively lightweight as it is meant to be extended by the user. This simply handles some the reading, writing, and updating of the database and provides a basic cli tool to use it. This being a lightweight package allows the user to build the package up to what they want instead of imposing a paradigm on the user.
## Functions
Currently the Database file contains 3 functions
Write - update the database with the changes that you have made. To use this just call the write function on the database instance you have created <br>
Create Table- a table is a structure I have created for the purpose of this database as. An object is meant to be defined by a user and stored in a python dictionary. A Table is then a dictionary whose key access the dictionary of the object I created based on the key set by the user. This is accomplished by calling createTable(key,data) where data is the object of data the user corrects and stores into a python dictionary. Tables can be nested inside of eachother for better data organization if it is so needed<br>
Update Table- this allows the user to change some of the data in an existing data object. #NOTE Update table currently only works with one dimensional tables at the moment.
## Planned Updates in the future
Like I said this is not a project meant for production use but rather as a proof of concept and an excesize in engineering. As such Im mainly interested in getting the product to its intended vision.
1. Make the CLI actually useful
2. Update the behavior of create table to store new values in a new object.
