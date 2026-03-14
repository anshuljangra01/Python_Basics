  # ----------------- Class and Objects ------------------
# class Employee:
#     name="Anshul"
#     language="Py" # This is class attribute 
#     Salary=1200000


# Anshul=Employee()
# print(Anshul.name,Anshul.language)

# jai =Employee()
# print(jai.Salary,jai.language)

# Aman =Employee()
# Aman.name="Aman " # This is an object attribute or instance attribute
# print(Aman.name,Aman.language,Aman.Salary)

# Here name is object attribute and salary and language are class attributes as they directly belong to the class


# -------------------Instance Attribute vs Class Attribute -------------------
class Employee:
    lang="Python" # This is class attribute
    salary = 1200000

anshul =Employee()
anshul.lang  ="Java" # This is Instance or Object attribute
print(anshul.lang,anshul.salary)

# this code print java because:  
# Instance attribute take pefereance over class attributes during assignment & retrival 
