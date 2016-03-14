

## CS 562 Project - Alghamha ##
### Astropy Installation and Usage Instructions ###

#### Installation ####
You can install Astropy using the following commands:

`pip install astropy” OR “pip install --no-deps astropy`

For this project we are using:

```bash
Python version 2.7.5
coverage version 4.0.3
```

Note: Astropy uses numpy library, therefore it is required for this project

#### Code Coverage ####

To enable Code Coverage you must use the directory where astropy folder is located. In my case I did the following:

```bash
source: /usr/lib64/python2.7/site-packages/astropy/table/table.py
```

#### Running the Files ####

To run the file you need to use the following commands. Pay attention to the comments in each file:

```bash
tstl FileName.tstl
python randomtester.py -t Number
```

### Functions To be Tested ###

In this project, the following functions have been tested. There are some functions embedded under these functions and doesn't need to be tested individually. 
All [Astropy Table Functions] can be found in the this [URL] with breif descriptions of each:

[URL]: http://docs.astropy.org/en/stable/api/astropy.table.Table.html

```
1- Adding Columns
2- Adding Rows
3- Copy Table
4- Column Index
5- Remove Columns
6- Group By
7- Rename Column
8- Reverse Order
9- Sort
10- Remove Rows
11- As Array returns a copy of the table as np
12- keep Columns
```

### Functions will not be Tested ###

The following fucntions are not part of the scope as they are meant for printing, reading or writing to a file. Someother functions can only work with python 3.
However, some of these functions have been partialy used in testing:
 
```
1- Field
2- Filled
3- More
4- Next
5- Pformat
6- pprint
7- Read
8- Show in browser
9- Write
10- convert_bytestring_to_unicode - python3 only
11- convert_unicode_to_bytestring - python3 only
12- To_Pandas

```
### Project-Part5 Files ###
#### Bug_1.tstl ####
##### Updating Columns’ Unit Field Bug #####
This bug occurs most of the time when inserting a column more than once with new values to update its content. The library is able to update the tuples’ values of a column but the unit field most of the time does not get the new updates. Missing the unit update may cause a devastating damage to the table’s data when for example a user uses a loop to remove data from the table based on their units’ values. User’s expectations is that the update has been implemented, since there was no error messages and further actions can be applied. As a result, this will eventually results in table’s data inconsistency. Someone, could argue that this might have been part of the design to easy the development of other staff. However, this kind of argument cannot be taken into account because any library APIs should expect the users’ unexpected behaviors. Therefore, a good design could be either updating all the values including the unit field or not updating the values at all by raising an exception. Moreover, documenting this kind of action is essential to make the user better understand the library APIs and use them correctly. #### Bug_2.tstl ####
##### Local variable 'new_name' referenced before assignment #####
This uncaught exception occurs when inserting a column randomly to the table while the rename_duplicate option is enabled and the column is not exist in the table. This bug is impractical as it shows some API weaknesses that may lower user’s overall satisfaction.  Usually, user’s expectations when adding a column to a table with the option rename-duplicate enabled, the column will be added no matter what, and even if it is not exist in the table it will be at least inserted with the same name. A proper action for similar situation is checking for the column existence first, and based on that apply an action either inserting the column with the same name if it is not exist, otherwise rename_duplicate the column when it is exist.#### Bug_3.tstl ####
##### Updating Tuples (Indices) of Type (String) Bug #####
This bug occurs when updating a tuple value of type (string). In Astropy.table library, there are different types of columns such as Integers, float, string, object, and more that can be used for each column. String type was interesting to test because it uses the length of the first insertion of columns’ tuples and hard coded the longest string length as a type. For example, if you have ‘Hafed’ as the longest string tuple, then the corresponding type of a column would be S5. This was an interesting technique to test and a bug was detected when updating tuples. The detected bug appears when updating a tuple with longer string after normal column insertion where the updated tuple will only have a portion of the new string. Apparently, it is only updating the field based on the original column type when it was first inserted, ignoring that it can be updated with a longer string which in turn results in table data inconsistency and unreliability. This is a major bug because the user is expecting the field to be updated with the new string value but in reality it is not, because of the hardcoded length of the original string column type. We are not sure what the reason behind this approach is, but a good way to fix this bug can be possibly achieved by first checking the old string length type and the new inserted string length, then adjust the string type of the column accordingly.##### Astropy_Testing_Final_v3.tstl ####
This file has all the functions to be tested including the bugs. To check an error, you need to read the comments of each line and comment or uncomment the lines that should generate the error as per instructions.