from astropy.table import Table, Column
import numpy as np
import random
from string import ascii_uppercase

def	check_unit():
	t=Table()
	while True:
		Random_column_Unit=(''.join(random.choice(ascii_uppercase) for i in range(1)))
		Random_column_Name=(''.join(random.choice(ascii_uppercase) for i in range(2)))
		Random_description= (''.join(random.choice(ascii_uppercase) for i in range(12)))
		random_int= random.randint(0,9)
		random_int2= random.randint(0,9)
		random_int3= random.randint(0,9)
		t[Random_column_Name]= Column([random_int,random_int2,random_int3], unit= Random_column_Unit, description=Random_description)
		if (Random_column_Unit == t[Random_column_Name].unit):
			print Random_column_Unit, '==', t[Random_column_Name].unit
		else:
			print Random_column_Unit, '!=', t[Random_column_Name].unit

		assert Random_column_Unit == t[Random_column_Name].unit

		print(t)
	
		print 'Pass test for adding column: ', t[Random_column_Name]
	return 

def	check_description():
	t=Table()
	while True:
		Random_column_Unit=(''.join(random.choice(ascii_uppercase) for i in range(1)))
		Random_column_Name=(''.join(random.choice(ascii_uppercase) for i in range(2)))
		Random_description= (''.join(random.choice(ascii_uppercase) for i in range(12)))
		random_int= random.randint(0,9)
		random_int2= random.randint(0,9)
		random_int3= random.randint(0,9)
		t[Random_column_Name]= Column([random_int,random_int2,random_int3], unit= Random_column_Unit, description=Random_description)
		if (Random_description == t[Random_column_Name].description):
			print Random_description, '==', t[Random_column_Name].description
		else:
			print Random_description, '!=', t[Random_column_Name].description

		assert Random_description == t[Random_column_Name].description

		print(t)
	
		print 'Pass test for adding column: ', t[Random_column_Name]
	return 

def	check_value():
	t=Table()
	while True:
		Random_column_Unit=(''.join(random.choice(ascii_uppercase) for i in range(1)))
		Random_column_Name=(''.join(random.choice(ascii_uppercase) for i in range(2)))
		Random_description= (''.join(random.choice(ascii_uppercase) for i in range(12)))
		random_int= random.uniform(0,9)
		random_int2= random.uniform(0,9)
		random_int3= random.uniform(0,9)
		t[Random_column_Name]= Column([random_int,random_int2,random_int3], unit= Random_column_Unit, description=Random_description)
		if ((random_int == t[Random_column_Name].data[0]) and (random_int2 == t[Random_column_Name].data[1]) and (random_int3 == t[Random_column_Name].data[2])):
			print random_int, '==', t[Random_column_Name].data[0]
			print random_int2, '==', t[Random_column_Name].data[1]
			print random_int3, '==', t[Random_column_Name].data[2]
		else:
			print random_int, '!=', t[Random_column_Name].data[0]

		assert random_int == t[Random_column_Name].data[0]
		assert random_int2 == t[Random_column_Name].data[1]
		assert random_int3 == t[Random_column_Name].data[2]
		print(t)
	
		print 'Pass test for updating column : ', t[Random_column_Name]
	return 


def	check_unit_unsing_offical_method():
	t=Table()
	while True:
		Random_column_Unit=(''.join(random.choice(ascii_uppercase) for i in range(1)))
		Random_column_Name=(''.join(random.choice(ascii_uppercase) for i in range(2)))
		Random_description= (''.join(random.choice(ascii_uppercase) for i in range(12)))
		random_int= random.randint(0,9)
		random_int2= random.randint(0,9)
		random_int3= random.randint(0,9)
		t[Random_column_Name]= Column([random_int,random_int2,random_int3], unit= Random_column_Unit, description=Random_description)
		t[Random_column_Name].unit = Random_column_Unit
		if (Random_column_Unit == t[Random_column_Name].unit):
			print Random_column_Unit, '==', t[Random_column_Name].unit
		else:
			print Random_column_Unit, '!=', t[Random_column_Name].unit

		assert Random_column_Unit == t[Random_column_Name].unit

		print(t)
	
		print 'Pass test for adding column: ', t[Random_column_Name]
	return 

def	check_description_unsing_offical_method():
	t=Table()
	while True:
		Random_column_Unit=(''.join(random.choice(ascii_uppercase) for i in range(1)))
		Random_column_Name=(''.join(random.choice(ascii_uppercase) for i in range(2)))
		Random_description= (''.join(random.choice(ascii_uppercase) for i in range(12)))
		random_int= random.randint(0,9)
		random_int2= random.randint(0,9)
		random_int3= random.randint(0,9)
		t[Random_column_Name]= Column([random_int,random_int2,random_int3], unit= Random_column_Unit, description=Random_description)
		t[Random_column_Name].description = Random_description
		if (Random_description == t[Random_column_Name].description):
			print Random_description, '==', t[Random_column_Name].description
		else:
			print Random_description, '!=', t[Random_column_Name].description

		assert Random_description == t[Random_column_Name].description

		print(t)
	
		print 'Pass test for adding column: ', t[Random_column_Name]
	return 

		
#check_unit()   # this action is allowed but it is not updating the field. My point of veiw, It should at least show an error but it is not it baisically accept the command.
#check_description() # this action is allowed but it is not updating the field. My point of veiw, It should at least show an error but it is not it baisically accept the command.
#check_value() # this action is allowed and updating the field of the same culomn. My point of veiw it should either updates all the feilds or none of them
#check_unit_unsing_offical_method() # this has not indicated to be the only way of updating unit in astropy decomentation
check_description_unsing_offical_method() # this has not indicated to be the only way of updating description in astropy decomentation

