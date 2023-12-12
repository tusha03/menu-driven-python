
def armstrongNum():
    '''if the sum of its own digits raised to the power
    number of digits gives the number itself. '''
    while(1):
        print("\nCheck Number is Armstrong or Not")
        
        #input from user and initialize num_count,num_back,all_sum
        num=int(input("\nEnter Number : "))
        num_count=0;
        num_back=num;
        all_sum=0;
        
        #count the digit in given number
        while(num!=0):
            num=num//10;
            num_count+=1;
        num=num_back;
        
        #calculate the power of digit 
        while(num!=0):
            rem=num%10;
            num=num//10;
            count_back=num_count;
            sum1=1;
            
            #calculate power
            while(count_back!=0):
                sum1=sum1*rem;
                count_back=count_back-1
            all_sum=all_sum+sum1;#add all digit power sum
            
        #check condition the number is armstrong number
        if(num_back==all_sum):
            print("\n",num_back," is Armstrong Number");
        else:
            print("\n",num_back," is Not Armstrong Number");
        
        ch=input("\nYou Want to Continue (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return




#=============================================================


def fabo(n):
    #find nth fabonacci number
    if(n==1 or n==2):
        return 1 
    else:
        return fabo(n-1)+fabo(n-2)
    
def nthFabonaci():
    #find nth fabonacci number 
    #1, 1, 2, 3, 5, 8, 13, ...
    print("\nFind nth Fabonacci Number")
    num = int(input("\nEnter Number : "))
    res=fabo(num) #call def
    print("\n",num,"th Fabonacci Number is ",res)

def fabonacci():
    #Fabonacci Menu
    while(1):
        print("\n*****Fabonacci Menu*****")
        print("\n1. nth Fabonacci Number")
        print("2. Fabonacci in given Range")
        print("3. Back")
        ch=int(input("\nEnter Choice : "))
        match ch:
            case 1 : nthFabonaci()
            case 2 : uptoFabo()
            case 3 : return
            case default : print("Invalid Choice")
           
        ch=input("\nYou Want to Continue (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return

def uptoFabo():
    #print fabonacci number in between range
   
    print("\nDisplay Fabonacci Number in given Range")
    
    #take input from user starting and ending numbers
    st=int(input("\nEnter Starting Number : "))
    ed=int(input("\nEnter Ending Number : "))
    
    #initialize n1,n2,n3
    n1=0
    n2=0
    n3=1
    
    #check the condition 
    if(st<=ed and st!=0):
        
        #find starting number
        #print series
        print("\nSeries : ",end=" ")
        
        if(st==1):
            print(1,end=" ")
        while(n2<=st):
            n1=n2
            n2=n3
            n3=n1+n2
        
        #print 1 by 1 
        while(n1<=ed):
            print(n1,end=" ")
            n1=n2
            n2=n3
            n3=n1+n2
    else:
        print("\nEnter Valid Starting and Ending Numbers")
        
    # ch=input("\nYou Want to Continue (Y/N) :")
    # if(ch!='Y' and ch!='y'):
    #     return
               
        
        
#============================================================


def fact(n):
    if(n==0):
        return 1 
    else:
        return n*fact(n-1)

def factorial():
    #find factorial 
    
    while(1):
        print("\nFind Factorial")
        num=int(input("\nEnter Number : "))
        if(num>=0):
            res=fact(num)
            print("\n",num," Factorial is ",res)
        else:
            print("\nEnter Valid Input")
            
        ch=input("\nYou Want to Continue (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return
        
        
        
#========================================================


def dateToDay():
    def leapYear(y):
        #check leap year and return true or false
        if y%400==0 and y%100==0 or y%4==0:
            return True
        else:
            return False

    def monthCode(m,y):
        #find code of respective month
        t=(6,2,2,5,7,3,5,1,4,6,2,4)
        
        #check leap year
        if leapYear(y):  
            if m==1 or m==2:
                return t[m-1]-1
            else:
                return t[m-1]
        else:
            return t[m-1]
        
    def yearCal(y):
        #calculate year and return cal
        res=0
        rem2=400
        
        #check conditions
        if 400<=y:
            res=0
            rem2=y%400
        if rem2>=300 and 300<=y:
            res=1
            if rem2!=400:
                rem2=rem2%300
            else:
                rem2=y%300
        if rem2>=200 and 200<=y:
            res=3
            if rem2!=400:
                rem2=rem2%200
            else:
                rem2=y%200
        if rem2>=100 and 100<=y:
            res=5
            if rem2!=400:
                rem2=rem2%100
            else:
                rem2=y%100
        if rem2==400:
            rem2=y
            
        #calculate cal
        cal=rem2+(rem2//4)+res
        return cal


    def cal(d,m,y):
        cal=d+monthCode(m, y)+yearCal(y) #call def monthCode and yearCal
        cal=cal%7
        
        #check remiander and return respective value in given dictionary
        dic={0:"Sunday",1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday"}
        return dic[cal]
    
    #this def star 
    while(1):        
        print("\nHello My Friend...")
        print("\nYou Are Interested to Know Your Date of the Day!")
        d=int(input("\nEnter Day : "))
        m=int(input("\nEnter Month No. : "))
        y=int(input("\nEnter Year : "))
        day=cal(d,m,y)  #call def cal
        print()
        print(f"Date : {d}-{m}-{y}")
        print(f"Day : {day}")
        print("\nYou Have A Nice Day...")
        
        ch=input("\nYou Want to Continue (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return


#===============================================================

        

def calMinNot():
    #calculate minimum number of notes 
    while(1):
        print("\nCalculate Minimum Number of Notes to given Amount")
        amt=int(input("\nEnter Amount : "))
        print()
        
        #check amount is greater than equal to 500 or not
        if(500<=amt):
            #print number of notes
            print("500 Notes\t",amt//500) 
            #amt store the remaing amt
            amt=amt%500
            
        #same as above
        if(200<=amt):
            print("200 Notes\t",amt//200)
            amt=amt%200
            
        if(100<=amt):
            print("100 Notes\t",amt//100)
            amt=amt%100
            
        if(50<=amt):
            print("50 Notes\t",amt//50)
            amt=amt%50
            
        if(20<=amt):
            print("20 Notes\t",amt//20)
            amt=amt%20
            
        if(10<=amt):
            print("10 Notes\t",amt//10)
            amt=amt%10
            
        if(5<=amt):
            print("5 Notes\t\t",amt//5)
            amt=amt%5 
            
        if(2<=amt):
            print("2 Notes\t\t",amt//2)
            amt=amt%2 
            
        if(1<=amt):
            print("1 Notes\t\t",amt)
    
        ch=input("\nYou Want to Continue (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return
        
    
    
#=========================================================    


def arthOpe():
    #perform basic arthmatic operations
    while(1):
        print("\nPerform Arthmatic Operation")
        num1=0
        num2=0
        
        #menu
        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Back")
        ch=int(input("\nEnter Choice : "))
        if(ch<=4 and ch>0):
            num1=int(input("\nEnter First Number : "))
            num2=int(input("\nEnter Second Number : "))
        match ch:
            case 1 : 
                    print("\nAddition : ",num1+num2)
            case 2 :
                    print("\nSubtraction : ",num1-num2)
            case 3 : 
                    print("\nMultiplication : ",num1*num2)
            case 4 : 
                    print("\nDivision : ",num1//num2)
            case 5 : 
                    return               
            case default : 
                        print("\nInvalid Input")
        ch=input("\nYou Want to Continue (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return
            
            
#=======================================================


def numPy(n):
    #number pyramid 
    for i in range(1,n+1):
         for j in range(1,n-i+1):
             print(end=" ")
         for j in range(1,i+1):
             print(i,end=" ")
         print()
         
def halfPy(n):
    #half pyramid
    for i in range(1,n+1): 
        for j in range(1,i+1):
            print(j,end=" ")
        print()
         
         
def palPat(n):
    #palindromic 
    for i in range(1,n+1):
        for j in range(1,n-i+1):
            print(end=" ")
        for j in range(i,0,-1):
            print(j,end="")
        for j in range(2,i+1):
            print(j,end="")
        print()

def triPat(n):
    #tirangular
    num_sp=(n-1)*2-1
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end="")
        for sp in range(1,num_sp+1):
            print(end=" ")
        for k in range(j,0,-1):
            print(k,end="")
        num_sp-=2
        print()
    
def diaPat(n):
    #diamond
    for i in range(1,n*2):
        for sp in range(1,n-i+1):
            print(end=" ")
        for sp in range(1,i-n+1):
            print(end=" ")
        if(i==n):
           sp-=1
        for j in range(1,n-sp+1):
            print(j,end="")
        for k in range(j-1,0,-1):
            print(k,end="")
        print()
         
def pat():
    #print 5 different patterns 
    while(1):
        print("\n*****Patters Menu*****")
        print("\n1. Pyramid")
        print("2. Palindromic Pattern")
        print("3. Half Pyramid")
        print("4. Diamond")
        print("5. Triangular")
        print("6. Back")
        ch=int(input("\nEnter Choice : "))
        num=0
        if(ch!=6):
            num=int(input("\nEnter Size : "))
        match ch:
            case 1 :
                numPy(num)
            case 2 :
                palPat(num)
            case 3 :
                halfPy(num)
            case 4 : 
                diaPat(num)
            case 5 : 
                triPat(num)
            case 6 : 
                return 
            case defulat : 
                print("\nInvalid Choice")
                
        ch=input("\nYou Want to Continue  (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return
     
    
#=========================================================  


def numConv():
    while(1):
        print("\n\n***** Number Conversion *****")
        print("\n1. Decimal To Binary")
        print("2. Decimal To Hexadecimal")
        print("3. Decimal To Octal")
        print("4. Back")
        ch = int(input("\nEnter Choice : "))
        if(ch==1):
            print('\nDecimal To Binary Conversion')
            n=int(input("\nEnter Number : "))
            print("Binary Number : ",end="")
            decToBin(n)
        if(ch==2):
            print('\nDecimal To Hexadecimal Conversion')
            n=int(input("\nEnter Number : "))
            print("Hexadecimal Number : ",end="")
            decToHex(n)
        if(ch==3):
            print('\nDecimal To Octal Conversion')
            n=int(input("\nEnter Number : "))
            print("Octal Number : ",end="")
            decToOct(n)
        if(ch==4):
            return
        if(5<=ch):
            print("\nInvalid Choice")
        ch=input("\nYou Want to Continue  (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return
   
def decToBin(n):
    if(n>1):
        decToBin(n//2)
    print(n%2,end="")

def decToHex(n):
    conversion_table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
                    5: '5', 6: '6', 7: '7',
                    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
                    13: 'D', 14: 'E', 15: 'F'}
    hexadecimal=""
    while(n>0):
        rem = n%16
        hexadecimal = conversion_table[rem]+hexadecimal
        n=n//16
    print(hexadecimal,end="")
    
def decToOct(n):
    octalNum = 0
    countval = 1
 
    while (n != 0):
        remainder = n % 8
        octalNum += remainder * countval
        countval = countval * 10
        n //= 8

    print(octalNum,end="")

#=========================================================   

def primeNum():
    while(True):
        print("\n\n***** Check Number is Prime or Not *****")
        n=int(input("\nEnter the Number: "))
        count=0
        for i in range(2,n//2):
            if(n%i==0):
                count+=1
                break
        if(count==0 and n>1):
            print("The Number is the prime number")
        else:
            print("The number is not a prime number")
        ch=input("\n\nYou Want to Continue  (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return
    
    
#=========================================================

def perfectNum():
    while(True):
        print("\n\n***** Check Perfect Number *****")
        n=int(input("\nEnter the Number: "))
        sum=0
        for j in range(1,n):
            if(n%j==0):
                sum+=j
        if(sum==n):
            print(n," is Perfect Number")
        else:
            print(n," is Not a Perfect Number")
        ch=input("\n\nYou Want to Continue  (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return

#=========================================================        

def pallStr():
    while(True):
        print("\n\n***** Check Pallindrome *****")
        s1=str(input("\nEnter the String: "))

        s2=s1[::-1]
        if(s1==s2):
            print(s1," is Pallindrome")
        else:
            print(s1," is Not a Pallindrome")
        ch=input("\n\nYou Want to Continue  (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return

#=========================================================            

def isValidTri(a,b,c):
    if a+b>=c and b+c>=a and c+a>=b:
        return True
    else:
        return False

# Function definition for type
def typeOfTri(a,b,c):
    if a==b and b==c:
        print('Triangle is Equilateral.')
    elif a==b or b==c or a==c:
        print('Triangle is Isosceles.')
    
    elif (a*a==(b*b)+(c*c)) or (b*b==(a*a)+(c*c)) or (c*c==(a*a)+(b*b)):
        print("Right angled Triangle")
    else:
        print('Triangle is Scalane')

def triType():
    # Reading Three Sides
    while(True):
        print("\n\n***** Check Triangle Type *****")
        side_a = float(input('\nEnter length of side a : '))
        side_b = float(input('Enter length of side b : '))
        side_c = float(input('Enter length of side c : '))
        
        # Function call & making decision
        if isValidTri(side_a, side_b, side_c):
           typeOfTri(side_a, side_b, side_c)
        else:
            print('\nTringle is not possible from given sides.')
        ch=input("\n\nYou Want to Continue  (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return

#=========================================================  

def calEleBill():
    while(True):
        print("\n\n***** Calculate Electricity Bill *****")
        units = int(input("\nPlease Enter Number of Units you Consumed : "))

        if(units < 50):
            amount = units * 2.60
            surcharge = 25
        elif(units <= 100):
            amount = 130 + ((units - 50) * 3.25)
            surcharge = 35
        elif(units <= 200):
            amount = 130 + 162.50 + ((units - 100) * 5.26)
            surcharge = 45
        else:
            amount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
            surcharge = 75

        total = amount + surcharge
        print("\nElectricity Bill = %.2f"  %total)
        ch=input("\n\nYou Want to Continue  (Y/N) :")
        if(ch!='Y' and ch!='y'):
            return

#========================================================= 

import sys

#Main menu
while(1):
    print("\n\n*****Main Menu*****")
    print("\n1. Perform Arthmatic Operations")
    print("2. Number Conversion")
    print("3. Prime Number")
    print("4. Perfect Number")
    print("5. Armstrong Number")
    print("6. Palindrom Number")
    print("7. Fabonacci Numbers")
    print("8. Factorial")
    print("9. Check Type of Triangle")
    print("10. Calculate Electricity Bill")
    print("11. Calculate Minimum Number of Notes")
    #print("12. Calculate Employee Gross Salary")
    print("12. Date Says Day")
    #print("14. Check Repeation of Calender")
    print("13. Number Patterns")
    print("14. Exit")
    
    ch=int(input("\nEnter Choice : "))
    #cal respective def
    match ch:
        case 1 : arthOpe()
        case 2 : numConv()
        case 3 : primeNum()
        case 4 : perfectNum()
        case 5 : armstrongNum()
        case 6 : pallStr()
        case 7 : fabonacci()
        case 8 : factorial()
        case 9 : triType()
        case 10 : calEleBill()
        case 11 : calMinNot()
       # case 12 : print("\nInProcess")
        case 12 : dateToDay()
       # case 14 : print("\nInProcess")
        case 13 : pat()
        case 14 : sys.exit()
        case default : print("\nInvalid Choice")
        
    ch=input("\nYou Want to Continue  Main Menu (Y/N) :")
    if(ch!='Y' and ch!='y'):
       sys.exit()
    
            
    
    
            
    
            