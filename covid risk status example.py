print("please say 'Yes' or 'No' to following questions")
age = (input("Are you a cigarette addict older than 75 years old?").title())
chronic = (input("Do you have a severe chronic disease?").title())
immune = (input("Is your immune system too weak?").title())
if age == "Yes":
  age=True
else:
  False  
if chronic == "Yes":
  chronic=True
else:
  False  
if immune == "Yes":
  immune=True
else:
  False   
if (age == True and chronic == True) or immune==True:
  print("You are in a risky group") 
else:
    print("You are not in a risky group")