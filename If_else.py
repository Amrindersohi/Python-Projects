monthly_Sale = int(input("Please enter the monthly sale:"))

if monthly_Sale>15000: print("Congrats! you earned $50 bonus.")

else: print("sorry! you did not earn a bonus")

print("thank you for using the application!")


monthly_Sale = int(input("Please enter the monthly sale:"))

if monthly_Sale>15000: print("Congrats! you earned $50 bonus.")

elif 15000>monthly_Sale>10000: print("congrats! you earned $40 bonus")

else: print("sorry! you did not earn a bonus")


annual_sal,experience_years=input("please enter your annual salary and years of experience:").split()
annual_sal,experience_years=int(annual_sal),int(experience_years)

if annual_sal>=40000:
    if experience_years>=5:
         print("Congrat! You qualify for a full loan.")
    elif experience_years<5:
                print("Congrat! You qualify for a 1/2 loan.")

else: print("you are not eligible for loan")

print("thank you for using the application!")

temp,humidity=input("Please, enter the temperature and the humidity percentage:").split()

temp,humidity=int(temp),int(humidity)

if  temp>=30 and humidity>=50:
    print("lets go swimming:")
else:print("thanks for visiting us")