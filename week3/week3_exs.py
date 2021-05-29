# 1
sc = input("Enter a score from 0 to 100 (decimal points are allowed)")
fl_sc = float(sc)

if fl_sc < 60:
    gr = "F"
elif fl_sc < 70:
    gr = "D"
elif fl_sc < 80:
    gr = "C"
elif fl_sc < 90:
    gr = "B"
else:
    gr = "A"

print("Score", fl_sc, "gets a grade of", gr)

# 2
year = int(input("Please enter a year: "))

if year % 4 == 0 or year % 400 == 0:
    print(True)
elif year % 100 == 0:
    print(False)
else:
    print(False)
# 4
a = 3
b = 5
print(a > b)
a = 3
b = 5
print(a >= b)
a = 19
day = 4
print(a >= 18 and day == 3)
a = 17
day = 3
print(a >= 18 or day != 3)

#5
a=float(input("Enter the right angled triangles 'a' side: "))
b=float(input("Enter the right angled triangles 'b' side: "))
hypo_len=(a**2+b**2)**0.5
print("The hypotenuse of the triangle is:",hypo_len)
#6
num_lst = [3, 20, -1, 9, 10]
is_even=[]
for num in num_lst:
    if num%2==1:
        is_even.append(False)

    else:
        is_even.append(True)

#8
a = 5
b = 6
c = 8

if c==(a**2+b**2)**0.5:
    is_rightangled=True

else:
    is_rightangled=False
#10
sent=input("Enter a sentence")
if sent==sent[::-1]:
    print(True)
else: print(False)