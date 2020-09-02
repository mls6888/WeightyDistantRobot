#Author: Liam Sullivan mls6888@psu.edu
#Collaborator: Olivia Mandola ovm5126@psu.edu
#Collaborator: Tyler Holman   trh5481@psu.edu

temp = float(input("Enter tempurature: "))
letter = (input("Enter unit in F/f or C/c: "))
if letter == "C" or letter == "c":
  fah = ((temp * 1.8) + 32)
  print(f"{temp}° in Celsius is equivalent to {fah}° Fahrenheit.")
elif letter == "F" or letter == "f":
  cel = ((temp - 32) /1.8)
  print(f"{temp}° in Fahrenheit is equivalent to {cel}° Celsius.")
else:
  print(f"Invalid unit({letter}).")
 