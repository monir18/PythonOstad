"""
Data Types in Python
	- int
	- float
	- complex
	- string
	- list
	- tuple
	- boolean
	- None
	- Set Types
	- Mapping / Dictionary
"""

age = 34
taka = 1010.50
i = 1+2j
name = "Md. Moniruzzaman Monir"
fruits = ["Apple","banana","cherry","Mango"]
cities = ("Dhaka","Rajshahi","Rangpur")
isLogin = True
MicrophoneModel = None
BCsQuestionSet = {"Padma","Meghna","Jamuna"}

myAddress = {
    "House":33,
    "Road":8,
    "PostOffice":"Adabor",
    "Dist":"Dhaka"
}

"""
Data Types Check
    - int       ==> type()
	- float     ==> type()
	- complex   ==> type()
	- string    ==> type()
	- list      ==> type()
	- tuple     ==> type()
	- boolean   ==> type()
	- None      ==> type()
	- Set Types ==> type()
	- Mapping / Dictionary  ==> type()
"""
print("Age Data Type is ",type(age))
print("Taka Data Type is ",type(taka))
print("i Data Type is ",type(i))
print("Name Data Type is ",type(name))
print("Fruits Data Type are ",type(fruits))
print("Cities Data Type are ",type(cities))
print("IsLogin Data Type is ",type(isLogin))
print("MicrophoneModel Data Type is ",type(MicrophoneModel))
print("BCsQuestionSet Data Type is",type(BCsQuestionSet))
print("myAddress Data Type is",type(myAddress))