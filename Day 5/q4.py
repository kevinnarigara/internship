
class cal4():
    def setdata(self):
        self.n1=int(input("enter number: "))

    def display(self):
        ans= self.n1*self.n1
        return ans


c=cal4()
c.setdata()
a=c.display()
print("square of num :",a)