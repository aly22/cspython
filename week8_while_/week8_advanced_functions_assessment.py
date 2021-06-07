# 1
def mult(num, numstri=6):
    return num * numstri


# 2

def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl


print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))


# 3

def sum(intx, intz=5):
    return intz + intx


# 4
def test(num, boo=True, dict1={2: 3, 4: 5, 6: 8}):
    if boo:
        if num in list(dict1.keys()):
            return dict1[num]
    return False


test(5)
# 5
def checkingIfIn(str1,direction=True,d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction:

        if str1 in list(d.keys()):
            return True
        else:
            return False
    if not direction:
        if str1 not in list(d.keys()):
            return True
        else:
            return False
# 6

def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false=checkingIfIn("kaka",direction=True)
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true=checkingIfIn("6",direction=False)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans=checkingIfIn("fruit")
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check=checkingIfIn("fruit",d={"fruit":8})
