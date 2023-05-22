print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
total=name1+name2
total.lower()
t=total.count('t')
r=total.count('r')
u=total.count('u')
e=total.count('e')

sm=t+r+u+e

l=total.count('l')
o=total.count('o')
v=total.count('v')
e=total.count('e')

ad=l+o+v+e

to=str(sm)+str(ad)
tot=int(to)

if tot<10 or tot>90:
    print(f'Your score is {to}, you go together like coke and mentos.')
if tot>=40 and tot<=50:
    print(f'Your score is {to}, you are alright together.')
else:
    print(f'Your score is {to}.')
