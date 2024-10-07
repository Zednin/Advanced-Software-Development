class Holiday:
    def __init__(self, destination="Unknown", duration=0, cost=0):
        self.destination = destination
        self.duration = duration
        self.cost = cost

    # Getters and Setters
    def getDestination(self):
        return self.destination

    def setDestination(self, destination):
        self.destination = destination

    def getDuration(self):
        return self.duration

    def setDuration(self, duration):
        self.duration = duration

    def getCost(self):
        return self.cost

    def setCost(self, cost):
        self.cost = cost

    def __str__(self):
        return f"Holiday{{destination={self.destination}, duration={self.duration} days, cost=${self.cost}}}"

class TravelAgent:
    def __init__(self, name, postcode):
        self.name = name
        self.postcode = postcode
        self.holidays = []

    # Getters and Setters
    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getPostcode(self):
        return self.postcode

    def setPostcode(self, postcode):
        self.postcode = postcode

    def addHoliday(self, holiday):
        self.holidays.append(holiday)

    def __str__(self):
        holidays_str = "\n".join(str(holiday) for holiday in self.holidays)
        return f"{self.name} at {self.postcode}\n{holidays_str}"



class RunTravelAgent:
    h1 =  Holiday("Bermuda", 2, 800)
    h2 =  Holiday("Hull", 14, 8)
    h3 =  Holiday("Los Angeles", 12, 2100)

    t1 = TravelAgent("CheapAsChips", "MA99 1CU")

    t1.addHoliday(h1)
    t1.addHoliday(h2)
    t1.addHoliday(h3)

    t2 = TravelAgent("Shoe String Tours", "CO33 2DX")

    print(t1)

    print("h3 Duration= "+str(h3.getDuration())+" days & Cost= "+str(h3.getCost()))
    print("t2 "+str(t2.getName())+" "+ str(t2.getPostcode()))
    
    
    
class BankAccount:
    def __init__(self, pinnumber):
        self.__pin = pinnumber
        self.__balance = 100  

    def deposit(self, pinnumber, amount):
        if pinnumber == self.__pin:
            self.__balance += amount
            return self.__balance
        else:
            return "Invalid Pin"

    def withdraw(self, pinnumber, amount):
        if pinnumber == self.__pin:
            if amount <= self.__balance:
                self.__balance -= amount
                return amount
            else:
                return "Insufficient funds"
        else:
            return "Invalid Pin"

    def get_balance(self, pinnumber):
        if pinnumber == self.__pin:
            return self.__balance
        else:
            return "Invalid Pin"

    def change_pin(self, oldpinnumber, newpinnumber):
        if oldpinnumber == self.__pin:
            self.__pin = newpinnumber
            return "Pin Changed"
        else:
            return "Invalid Pin"
