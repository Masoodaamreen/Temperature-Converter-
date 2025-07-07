print("TEMPE1RATURE CONVERSION")
a=int(input("Enter a tempature value: "))
print("choose your unit of measurement that you entered")
print("1.Celsius")
print("2.Fahrenheit")
b=int(input("Enter your choice 1 or 2:"))
if b==1:
 print(round( a*1.8+32,2) ,"Faherenheit")
elif b==2:
 print (round((a-32)/1.8,2),"Celsius")
else:
    print("Invalid input! enter your choice correctly only either 1 or 2 ")