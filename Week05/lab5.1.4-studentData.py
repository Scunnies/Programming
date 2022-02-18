# a program that stores a students name 
# a list of her courses and grades in a dict
# program then prints out her data


student = {
"name":"Mary",
"modules": [
{
"courseName":"Programming",
"grade": 45
},
{
"courseName":"History",
"grade":99
}
]
}
print ("\t Student\t: {}".format(student["name"]))
for module in student["modules"]:
    print("\t {} \t: {}".format(module["courseName"], module["grade"]))