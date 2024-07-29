#In Python, lists allow us to store a sequence of items in a single variable.
#Creating a List
my_list=[0,1,2,3,4,5,6,7,8,9,10]
#Printing the Current List
print("\nCurrent List : ",my_list)
#Adding an Element to the List
my_list.append(11)
#Printing the Current List
print("\nCurrent List after adding : ",my_list)
#Deleting an Element from the List
my_list.remove(0)
#Printing the Current List
print("\nCurrent List after Removing : ",my_list)
#Modifying the List
my_list[0]=0
#Printing the Current List
print("\nCurrent List after Modifying: ",my_list)

#A Python dictionary is a collection of items, similar to lists and tuples.
# However, unlike lists and tuples, each item in a dictionary is a key-value pair (consisting of a key and a value).
#Creating a Dictionary
my_dict={'name':'Senthil','age':18,'dept':'Cse'}
#Printing the Current Dictionary
print("\nCurrent Dictionary : ",my_dict)
#Adding an Element to the dictionary
my_dict['gender']='Male'
#Printing the Current Dictionary
print("\nCurrent Dictionary after Adding : ",my_dict)
#Removing an Element from the Dictionary
del my_dict['dept']
#Printing the Current Dictionary
print("\nCurrent Dictionary after Removing : ",my_dict)
#Modifying the Dictionary
my_dict['name']='SenthilKumar ArunKumar'
#Printing the Current Dictionary
print("\nCurrent Dictionary after Modifying : ",my_dict)

#A set is a collection of unique data, meaning that elements within a set cannot be duplicated.
#Creating a Set
my_set={1,2,3,4,5}
#Printing the Current Set
print("\n Current Set : ",my_set)
#Adding an Element to the Set
my_set.add(0)
#Printing the Current Set
print("\n Current Set after Adding : ",my_set)
#Deleting an Element From the Set
my_set.discard(0)
#Printing the Current Set
print("\n Current Set after Deleting : ",my_set)
#Modifying the Current Set
my_set1={6,7,8,9,10}
my_set.update(my_set1)
#Printing the Current Set
print("\n Current Set after Modifying : ",my_set)