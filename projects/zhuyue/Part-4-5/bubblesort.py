
#!/usr/bin/python
#############################################################
# Bubblesort for Python                                     #
# by: Dennis Linuz <dennismald@gmail.com>                   #
# Demonstration of a bubble 		                    #
#############################################################




def bubbleSort(array):
	length=len(array)
	result = True
        count = 0
	while result:
		result = False
		i=0
		while (i < length-1):
			if (array[i] > array[i+1]):
				tempVar = array[i]
				array[i] = array[i+1]
				array[i+1] = tempVar
				result = True
			i=i+1
			count+=1
			print "Sorting: " + str(array)
	return array

