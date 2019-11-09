class Figure:
    def __init__(self, a, b, c = 0):
        self.A = a 
        self.B = b 
        self.C = c 
        self.perimeter = self.A + self.B + self.C 
    
fig1 = Figure(1,2,3)
fig2 = Figure(3,4,5)
fig3 = Figure(2,2)

print("FIgure 1 perimeter: ",fig1.perimeter)
print("FIgure 2 perimeter: ",fig2.perimeter)
print("FIgure 3 perimeter: ",fig3.perimeter)