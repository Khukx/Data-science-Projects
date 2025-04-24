# ************ Practical task Capstone Project ************
#This program calculate the bond repayment and amount of interest to earned on investment.
#it allows the user to choose between bond or investment  and do calculation based on the input of the user
#then out put an answer
# This program allows the user to calculate either the repayment of a home loan (bond)
# or the amount earned on an investment (simple or compound interest).
# The user is prompted to choose between "bond" or "investment" at the start.
#
# 1. If "bond" is selected, the program will ask for the present house value, 
#    interest rate, and number of months to repay the bond, and calculate the 
#    monthly repayment using the bond repayment formula.
# 
# 2. If "investment" is selected, the user will be asked for the deposit amount, 
#    interest rate, number of years to invest, and whether they want to use simple 
#    or compound interest. The program will then calculate and display the final 
#    amount based on the chosen interest type.
#
# The program ensures that the user inputs valid options and handles incorrect inputs 
# with appropriate error messages





#the Import math is a module for  mathematical functions
import math

#asking the user to input an option between bond or investment
sellect_str = input ('''nvestment - to calculate the amount of interest you'll earn on your investment. 
Bond - to calculate the amount you'll have to pay on a home loan.          
 
Enter either “investment” or “bond” from the menu above to 
proceed: ''').strip().lower()

#Checking if the user selected "bond"
if  sellect_str==("bond"):
    pres_house_value = float(input("Input the present house value : ")) 
    interest_rate1=float(input("Input  the interest rate(dont add ""%""): " ))
    repay=int(input("Enter number of months to repay bond: "))
    
     #Converting the interest rate to a monthly rate (divide by 100 to get a decimal and by 12 for monthly)
    interest_rate1=interest_rate1/100
    interest_rate1=interest_rate1/12

    #Calculating the monthly repayment using the formula for bond repayment
    repayment=(interest_rate1*pres_house_value)/(1-(1+interest_rate1)**(-repay))
    # Displaying the result of the bond repayment calculation
    print(f"The answer : {repayment}") 

#Checking if the user inputed "investment"    
elif  sellect_str == ("investment") :

    # Asking for inputs related to the investment calculation
    deposit=float(input (" Input the deposit : "))
    interest_rate2= float(input("Input the interest rate (dont add ""%"") : "))
    years_inv= int(input("Imput number of years to invest : "))
    interest= input("Input  simple or compound: ").strip().lower()

     #If the user input simple interest
    if interest==("simple") :
        A= deposit*(1+interest_rate2/100*years_inv)                                                                            
        print(f" The answer : {A}")
  
    #If the user input compound interest
    elif interest== ("compound") :
        B=deposit*math.pow((1+interest_rate2/100),years_inv)
         
         #Out put the result for compound interest
        print(f"The answer : {B}")
    else : 
        print("incorrect, enter either simple or compound")

#If the user enters an invalid option for the main selection
else :
    print ("Incorrect, Enter either “investment” or “bond” :  ")





