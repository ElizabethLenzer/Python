# 1 Update Values Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
x[1][0] = 15
print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
students[0]['last_name'] = "Bryant"
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
sports_directory['soccer'][0] = 'andres'
print(sports_directory)
z = [ {'x': 10, 'y': 20} ]
z[0]['y']=30
print(z)

# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 2 Interate through a list of dictionaries
# Printing both key and dictionary
# has to loop through both list in key and dictionary.
# dictionary and values
students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(Li):
    for var in Li:
        newString=""
        for key, value in var.items():
            newString+=f"{key} - {value} "
            # print(key, value)
        print(newString)
iterateDictionary(students)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 3 Get Values From a List of Dictionaries
# just find the dictionary
# input the key
def interateDictionary2(Li, key):
    for var in Li:
        print(var[key])
interateDictionary2(students, 'last_name')

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 4 Iterate Through a Dictionary with List Values
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(Dlist):
    for key, value in Dlist.items():
        print(key, len(value))
        for string in value:
            print(string)
printInfo(dojo)