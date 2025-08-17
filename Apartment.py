class Apartment: 
    def __init__ (self, rent, meters_from_UCSB, condition): 
        self.rent = rent 
        self.meters_from_UCSB = meters_from_UCSB
        self.condition  = condition 

    def get_rent(self): 
        return self.rent 
        
    def get_meters_from_UCSB(self): 
        return self.meters_from_UCSB
        
    def get_condition(self):
        return self.condition 
        
    def get_apartment_details (self): 
        return f"(Apartment) Rent: ${self.rent}, Distance From UCSB: {self.meters_from_UCSB}m, Condition: {self.condition}"
        
    def __lt__(self,other):
        if self.rent != other.rent: 
            return self.rent < other.rent 
        elif self.meters_from_UCSB != other.meters_from_UCSB: 
            return self.meters_from_UCSB < other.meters_from_UCSB
        else: 
            condition_rankings = {"bad": 0, "average": 1, "excellent": 2}
            return condition_rankings[self.condition] > condition_rankings[other.condition]

    def __gt__ (self,other): 
        if self.rent != other.rent:
            return self.rent > other.rent
        elif self.meters_from_UCSB != other.meters_from_UCSB:
            return self.meters_from_UCSB > other.meters_from_UCSB
        else:
            condition_rankings = {"bad": 0, "average": 1, "excellent": 2}
            return condition_rankings[self.condition] < condition_rankings[other.condition]
        
    def __eq__(self,other):
        return self.rent == other.rent and self.meters_from_UCSB == other.meters_from_UCSB and self.condition == other.condition