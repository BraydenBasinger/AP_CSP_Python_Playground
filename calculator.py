
def calc():
  print(u"\u001B[0m")
  print("=======================")
  print("1 - Addition")
  print("2 - Subtraction")
  print("3 - Multiplication")
  print("4 - Division")
  print("5 - Power")
  print("=======================")
  selection = int(input("\u001b[31mPick a Function   "))
  print(u"\u001B[0m")
  number_1 = input("Enter A Number - ")
  number_2 = input("Enter A Number - ")
  print(u"\u001B[0m")
  result_1 = float(number_1) + float(number_2)
  result_2 = float(number_1) - float(number_2)
  result_3 = float(number_1) * float(number_2)
  result_4 = float(number_1) / float(number_2)
  result_5 = float(number_1) ** float(number_2)

  while True:
    if selection == 1:
      print("\u001b[31m_____________")
      print(u"\u001B[0m")
      print(result_1)
      print("\u001b[31m_____________")
      print(u"\u001B[0m")
      print("        ")
      break
      
    if selection == 2:
      print("\u001b[31m_____________")
      print(u"\u001B[0m")
      print(result_2)
      print("\u001b[31m_____________")
      print(u"\u001B[0m")
      print("        ")
      break
      
      
    if selection == 3:
      print("\u001b[31m_____________")
      print(u"\u001B[0m")
      print(result_3)
      print("\u001b[31m_____________")
      print(u"\u001B[0m")
      print("        ")
      break
        
      
    if selection == 4:
      print("\u001b[31m_____________")
      print(u"\u001B[0m")
      print(result_4)
      print("\u001b[31m_____________")
      print(u"\u001B[0m")
      print("        ")
      break
       
      
    if selection == 5:
      print("\u001b[31m_____________")
      print(u"\u001B[0m")
      print(result_5)
      print("\u001b[31m____________")
      print(u"\u001B[0m")
      print("        ")
      break
      
      
      
    
      
   
 
