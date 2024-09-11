result = input("Please Enter Your Number : ")

print(type(result))

result = int(result)
if result >= 40:
    print("Pass")
else:
    print("Failed")


print("End")

marks = input("Enter Your Marks : ")
marks = int(marks)

if marks >= 80:
    print("Your CGPA : A+")
elif marks >= 70:
    print("Your CGPA : A")
elif marks >= 60:
    print("Your CGPA : A-")
elif marks >= 50:
    print("Your CGPA : B")
elif marks >= 40:
    print("Your CGPA : C")
elif marks >= 33:
    print("Your CGPA : D")
else:
    print("You are Failed!")

print("Done.")