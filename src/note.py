class Note:
    def __init__(self, idx, first_name, last_name, number, address=None, date=None):
        self.idx = idx
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.address = address
        self.date = date

    def __str__(self):
        text_line = f'Id = {self.idx}, First name: {self.first_name}, Last name: {self.last_name}, number: {self.number}'
        if len(self.address) > 0:
            text_line += f', address: {self.address}'
        if len(str(self.date)) > 0:
            text_line += f', Birth dade: {self.date}'
        return text_line

