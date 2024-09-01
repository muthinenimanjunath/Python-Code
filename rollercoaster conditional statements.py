print("Welcome to the Rollercoaster!")
height=int(input("Please enter your height in cm "))
bill=0
if height >= 120:
  print("You can ride the rollercoaster")
  age=int(input("Please enter your age "))
  if age < 12:
    bill=5
    print("Child tickets are $5")
  elif age >=12 and age<=18:
    bill=7
    print("Teenagers tickets are $7")
  else:
    bill=12
    print("Adult tickets are $12")

  wants_photo=input("Do you want to take a photo? y for Yes or n for No ")
  if wants_photo == "y":
    print("Your total bill is $ ",bill+3)
  else:
    print("Your total bill is $",bill)
else:
  print("Sorry,Please come back once you have grown taller")
  