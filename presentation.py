# Récupération nom, age, hobby
print("Hello!")
nom = input("Quel est ton nom : ")
age = int(input("Quel est ton age? "))
hobby = input("Quel est ton hobby? ")

print(f"Tu t'appelles {nom}, tu as {age} ans et tu aimes {hobby}")
if age >= 18:
    print("Tu es majeur(e)")
else:
    print("Tu es mineur(e)")

