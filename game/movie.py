class Movie:
    def __init__(self, data):
        self.title = data['Movie Name']
        self.description = data['Description']

    def check_guess(self, guess):
        return guess.strip().lower() == self.title.strip().lower()

    def show_desc(self):
        return self.description
