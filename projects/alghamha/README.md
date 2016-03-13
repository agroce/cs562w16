

## CS 562 Project - Alghamha ##
### Astropy Installation Requirements ###

You can install Astropy using the following commands:

`pip install astropy” OR “pip install --no-deps astropy`

For this project we are using:

```Python 2.7.5
# coverage --version
Coverage.py, version 4.0.3.
```

Note: Astropy uses numpy library, therefore it is required for this project

### Code Coverage ###

To enable Code Coverage you must use the directory where astropy folder is located. In my case I did the following:

```bash
source: /usr/lib64/python2.7/site-packages/astropy/table/table.py
```

### Function To be Tested ###

All Table Functions can be found in the following URL with breif descriptions of each:

` https://astropy.readthedocs.org/en/v0.3/api/astropy.table.table.Table.html#astropy.table.table.Table `

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
10 - Remove Rows
11 - As Array returns a copy of the table as np
12 - keep Columns
```

### Function will not be Tested ###

The following fucntions are not part of the scope as they are meant for printing, reading or writing to a file.
Although, some of them have been partialy used in testing:
 
```
1- Field
2- Filled
3- More
4- Next
5- Pformat
6- pprint
7- Read
8- Show in browser
9 - Write(*args, **kwargs) 
```
