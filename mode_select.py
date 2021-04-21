import random

class ModeSelect:
    def __init__(self, mode, lower, ending):
        self.mode = mode
        self.count = 0
        self.indexVal = 0
        
        self.lower = int(lower)
        self.ending = int(ending)
        self.item_range = list(range(self.lower, self.ending))
        self.item_list = list(map(lambda x: self.putZeros(x), self.item_range))


    def give_values(self):
        if self.mode == 'r':
            self.indexVal = int(random.choice(self.item_list))
            return self.indexVal
        
        elif self.mode == 'n':
            self.count += 1
            return self.item_list[self.count-1]
    
    def putZeros(self, value):
        if value < 10:
            return f'0{value}'
        else:
            return str(value) 

    def change_mode(self, mode):
        self.mode = mode

    def show_count(self):
        return self.count
    
    def show_item_list(self):
        return self.item_list
