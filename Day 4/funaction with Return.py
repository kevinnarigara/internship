#funaction with return
def disp(name):
    return name
name = disp("kevin")
print(name)

def show():
    name = "narigara kevin"
    contact = 9574295762
    return name,contact
name,contact = show()
print("Name is",name)
print("contact number is",contact)