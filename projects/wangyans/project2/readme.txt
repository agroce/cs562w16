In this project, I was trying to use the tstl tool to test some functions coming from a python library which is used for translating the Chinese characters into the Latin alphabet. First of all, I created a tstl file including some variables defined by myself and put them into the library's functions. Then I use the tstl command to generate a python file named "sut.py". Finally, I used the "randomtester.py" which is given by the professor to print out some results which is for checking out whether or not those functions are working in this library.

In this python library, it contains the following functions:
get_pinyin(<str>): It is used for translating the Chinese characters into the Latin alphabet.
get_pinyin(<str>, show_tone_marks=True): It is used for marking the pronunciation of each words.
get_initials(<str>):: The inputs of this function are some string lists, and the function returns some initial capital letters of each character.
get_initial(<str>): The input of this function is a signal Chinese character, and the function returns the initial capital letter of this character.

project steps:
1. git clone https://github.com/lxneng/xpinyin
2. pip install xpinyin (this step may need to use the sudo command)
3. tstl pinyin.tstl --nocover
4. After I generate the "sut.py", I need to copy the (# -*- coding: utf-8 -*-") into the first line of the "sut.py" to specify this file is the utf-8 encoding.
5. python randomtester.py --nocover