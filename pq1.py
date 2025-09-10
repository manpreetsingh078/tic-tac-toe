rent=int(input("enter the rent"))
food=int(input("enter the food"))
unit=int(input("enter the total unit spend"))
charge_perunit=int(input("enter the charge per unit"))
person=int(input("enter the number of person"))

electricity_bill=unit*charge_perunit

output=(rent+food+electricity_bill)/person

print(f"Each member will pay {output} amount")