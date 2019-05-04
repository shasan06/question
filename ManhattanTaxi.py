
class ManhattanTaxi:
    def  __init__(self, initX, initY, consumption, init_fuel):
        self.cons = consumption
        self.pos = (initX, initY)
        self.fuel=float(init_fuel)

    "Methods"

    def moveto(self, X, Y):
        distance = abs(X-self.pos[0])+ abs(Y-self.pos[1])
        print(distance)
        fuel_consumption = distance*self.cons
        if self.fuel>=fuel_consumption:
            self.pos=(X,Y)
            self.fuel-=fuel_consumption
            return True
        else:
            return False

    def add_fuel(self, n):
        self.init_fuel+=n

t789 = ManhattanTaxi(5,5,1,30)
assert t789.moveto(3,9)==True
assert t789.pos[0]==3 and t789.pos[1]==9
assert abs(t789.fuel-24)<0.01
print(t789.fuel)

