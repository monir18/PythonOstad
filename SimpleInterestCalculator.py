principle_amt = input("Enter the principle amount : ")
interest_rate = input("Enter the rate of interest : ")
time = input("Enter the time (in year) : ")

principle_amt = float(principle_amt)
interest_rate = float(interest_rate)
time = float(time)

interest = (principle_amt * interest_rate * time) / 100
print("The simple interest is : ", interest)