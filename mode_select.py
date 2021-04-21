import random

# class DataEdit:
#     def __init__(self, data, lower_range, upper_range):
#         self.data = data
#         self.lower_range = lower_range
#         self.upper_range = upper_range
#         self.item_range = list(range(self.lower_range,self.upper_range))

#     def putZeros(self, value):
#         if value < 10:
#             return f'0{value}'
#         else:
#             return str(value)

#     def show_item_list(self):
#         return list(map(lambda x: self.putZeros(x), self.item_range))


class ModeSelect:
    def __init__(self, mode, item_list):
        self.mode = mode
        self.count = 0
        self.indexVal = 0
        self.item_list = item_list

    def give_values(self):
        if self.mode == 'r':
            self.indexVal = int(random.choice(self.item_list))
            return self.indexVal
        
        elif self.mode == 'n':
            self.count += 1
            return self.item_list[self.count-1]

    def change_mode(self, mode):
        self.mode = mode

    def show_count(self):
        return self.count
    
    def show_item_list(self):
        return self.item_list
    