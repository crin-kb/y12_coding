#   Lists

#examples
summer = ["June", "July", "August"]
numbers = []
data = [8, True, "Hello", 3.14]
planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# access individual list items
List[index] # access items in a list, current position in the list starting from 0
month = summer[0]
data[1] = False#
position = planets.index()
previous = planets[position-1]
sum = numbers[i]+numbers[i+1]


#list slices

# syntax = list[start index:end index:step]
#   > a slice of a list is a new list that includes the list of items from a start index up to but not including an end index. Specifying a step skips over items.

# Examples:
summer = month[5:8]
head = data[1:100]
skipped = values[:2]

# list methods
# > special functrions that are applied to lists. uses dot notation.

#add items:
#syntax 
list.append(item) # adds item to the end of the list

numbers.append(42)

list.insert(index, item) # adds item at the specified index

list.pop(index) #removes an item from a specific index in the list and returns it.

list.remove(item) #removes the list, taises a value error if there is no such item
#example:
countries.remove("China")

list.index(item) # Searches for the first occurance of an item in the list and returns it index.

list.count(item) # returns the number of time an item appears in the list.
#example:
nb_the = words.count("the")

# other list operations:
list.reverse() # reverses the order of the items in the list
list.sort() # sorts the items in the list in ascending order

# List Functions
# > built-in functions that can operate on lists.

len(list) # returns the number of items in the list
sum(list) # returns the sum of all items in the list
min(list) # returns the minimum
max(list) # returns the maximum

#List operators:
item in list # checks if the list contains items with a specific value = returns bool value (true or false)
#example:
"Pluto" in planets # returns True

list + list # evalutates to a new list that is the JOINING  of the two lists
#example:
numbers = [1, 2, 3] + [4, 5, 6]

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Strings
# > data type that represents a sequence of characters. Cant be modified during a program excution.

#Create a string
"Meow" #syntax 
#EXAMPLES:
cat = "meow"
empty = ""

#access individual characters in a string
string[index] # string character can be access via index, i.e their current postition in the string starting with 0
#examples: 
cat_name = cat[position-1] #can be the value of an expression
first_letter = cat[0] # retrieves the first character in the string

#string slices
variable = list[start index:end index:step]
# a slice if a string is a new string that includes the character fron the start index up to the end of the string. Specifying a step skips over characters.

#examples:
substring = words[5:8]
prefix = words[:3] 
skipped = name[: :2]

#String Functions:
# > some functions can accept strings as arguments 
len(list) #returns the length of (numbers of characters) of the string
#example:
len(password)

# String Operators:
# allows you to form expressions that can involve strings and be evaluated

substring in string # checks if the string contains a substring. Returns a boolean value (true or false)
#example:
"sub" in word
letter in "aeiou"
word in text

# adding strings together
string + string  # evaluates to a new string that is the joining of the two strings

#examples:
greeting = "Hello"+ "Name" + "!"
fullname = firstname + lastname

# split and join strings
# > it is often convenient to split a string into a list or join a list into a string

string.split(separator) # splits the string into a list of substrings. The separator is a string that appears between substrings.
seperator.join(list) # joins the elements of a list into a string. The separator is a string that appears between the elements.

#example:
names = line.split(",")#
"".join(letters)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Iterating over sequences

# :> for loops is a special type of control structer that can be used to interate over the elements of as sequences (lists, strings, tuples)

for element in sequence:
   " block of statement"
#for every element in the sequence, the return statement is executed

#iterating over list items

for item in list:
    "block of statements"
    # executes the block of statements for each item in the list

#example:
for name in guests:
    print(name)

#Iterating over string characters
for char in string:
    "block of statements"
#executes the block of statements for each character in the string
#examples:
for characters in password:
    print(characters)

#Using while instead of for
# > one way to use while in order to achieve a simillar effect as for, follow this pattern.

index = 0
while index < len(sequence):
    element = sequence[index]
    "block of statements"
    index = index + 1
    #iterate over all indicies, retrive the corresponding element and execute the block of statements









