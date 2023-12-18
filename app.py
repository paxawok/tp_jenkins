import datetime

class DictionaryList:

    def __init__(self):
        self.items = []
    
    def empty(self):
        return len(self.items) == 0

    def add(self, num, date):

        try:
            num = int(num)
            date_obj = datetime.datetime.strptime(date, '%Y-%m-%d')
            item = {'number': num,
                'verification_date': date_obj}
            self.items.append(item)
        except ValueError: 
                print("Помилка!")

    def remove(self, number):
        for item in self.items:
            if item['number'] == number:
                self.items.remove(item)
                return True  
        return False 
    
    def clear_values(self):
        for item in self.items:
            item.clear()

    def oldest_verification_date(self):
        if not self.empty():
            oldest_date = min(item['verification_date'] for item in self.items)
            return oldest_date
        else:
            return None  
    
    def find_by_number(self, number):
        for item in self.items:
            if item['number'] == number:
                return item['verification_date']
        return None  

    def print_all(self):
        if not self.empty():
            for item in self.items:
                print(f'Номер квартири: {item["number"]}, Дата повірки: {item["verification_date"].strftime("%Y-%m-%d")}')

        
    def __len__(self):
        return len(self.items)