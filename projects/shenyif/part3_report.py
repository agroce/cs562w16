From current testing work, the insertion of number, and the character of color do not have bugs. However, there is some bad design of function. It is not the bug, but it can not show the result directly and I used to think that is a bug. For example, the inorder walk and reverse inorder walk. It could not output the number when it operate the walk.
To test the red black tree library, we must write some code to test its feature. Red black tree is similar to AVL tree to a certain extent, because the red node could not have the red children nodes, the height of different branches of the tree will be similar. In the first version of tstl testing code, I create four different int number and a red black tree. To test the basic characteristic of the tree, I design some actions and test. Because the red black tree is a tree, we can insert number to the tree, and the tree can help us find the correct position to insert the number. At the same time, each node inserted into the tree will have its own color and the color is either black or red. To this feature, we can assert that the height of black nodes are smaller than the size of tree. To make the tstl code abort at some degree, I add a restrained requirement: the size of the tree will not be larger than 15. The color is the most important feature of red black tree, so in the second version of tstl testing code, I add some functions to test the color feature of the tree. Because the black red tree has a feature that the each route to the leave nodes will have the same number of black nodes, I write a code to test the number of black nodes on each route. I use the recursion to get all the leave nodes and put the number of black nodes along the route to a array. Then I test whether the sorted array is equal to the reverse sorted array. If they are the same, the black nodes along each route is the same and the character of red black tree is correct.
I think there are still some improvements that can be done by the end of the term. For example, test the children color to check whether there are two neighboring nodes have the red color which is against the red black tree law. And I think I can add more actions such as delete, search and so on.
System under test is the final operation in the software development, it will test the whole functions in the system. So from my point of view, it will help us find more problems in the software. Maybe we can correctly deal with each single function, but when we combine these single functions together, there are usually some errors. And this is the sut works for. By the tstl testing, I find that the red black tree library is correct in most of the function implementation, because it can operate most of common action. To the code coverage, I still need learn more to use that .