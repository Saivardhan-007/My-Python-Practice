t_class = int(input("Total Classes Held :"))
a_class = int(input("Attended Classes :"))
attendence = (a_class / t_class) * 100
eligible = attendence > 75
print("Attendence Percentage :",attendence,"%")
print("Eligible :",eligible)