The fuzzywuzzy tool could be downloaded from "https://github.com/seatgeek/fuzzywuzzy".

The fuzzywuzzy tool needs to be installed.

The tstl file "part2_test.tstl" is already in the fuzzywuzzy directory "cs562w16/projects/wanghaox/Part2/fuzzywuzzy/fuzzywuzzy", please use that one to run the test.

The test generally run tests for two functions: 1)fuzz.ratio and 2)fuzz.partial_ratio
The fuzz.ratio compare the whole two string while the fuzz.partial_ratio compares the most common part of these two strings.

Depending on the strategy I used in these tests, the string #1 and string #2 should have a lot in common, so that the fuzz.ratio should have smaller return value than fuzz.partial_ration does and the fuzz.partial_ratio should have a lot return values equal to 100.

The output could be stored in an "out" file in oreder to get rid of the coverage warning. An example out file is already incuded in the folder.

So far, the fuzzywuzzy doesn't show any bugs during he test, more tests should be implemented in the following part of th project.
