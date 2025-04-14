class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.stats = {}

    def update_stats(self, category, correct):
        if category not in self.stats:
            self.stats[category] = {'correct': 0, 'total': 0}
        self.stats[category]['total'] += 1
        if correct:
            self.stats[category]['correct'] += 1
