import sys
def menu():
    print("*" * 50)
    print("\tWelcome To Calculator")
    print("*" * 50)
    print("\t1.Addition")
    print("\t2.Substraction")
    print("\t3.Multiplication")
    print("\t4.Division")
    print("\t5.Modulo Division")
    print("\t6.Exponentiation")
    print("\t7.Exit")
    print("=" * 50)

def add():
    print("Enter two numbers for addition:")
    a,b=float(input()),float(input())
    print("Addition of ({} + {})={}".format(a,b,a+b))
def sub():
    print("Enter two numbers for subtraction:")
    a,b=float(input()),float(input())
    print("Subtraction of ({} - {})={}".format(a,b,a-b))
def mul():
    print("Enter two numbers for multiplication:")
    a,b=float(input()),float(input())
    print("Multiplication of ({} * {})={}".format(a,b,a*b))
def div():
    print("Enter two numbers for division:")
    a,b=float(input()),float(input())
    print("Floor Division of ({} / {})={}".format(a,b,a//b))
def mod():
    print("Enter two numbers for mod division:")
    a,b=float(input()),float(input())
    print("Mod Division of ({} % {})={}".format(a,b,a%b))
def expop():
    a,b=float(input("Enter Base:")),float(input("Enter Power:"))
    print("Power of ({},{})={}".format(a,b,a**b))

while(True):
     menu()
     d=int(input("Enter Your Choice:"))
     print("="*50)
     match(d):
         case 1:
             add()
         case 2:
             sub()
         case 3:
             mul()
         case 4:
             div()
         case 5:
             mod()
         case 6:
             expop()
         case 7:
             print("Thanks for using this Calculator")
             sys.exit()
         case _:
          print("Your selection of operation is wrong----Please try again")

