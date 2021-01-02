class parrot:
    def __init__(self,sex):
        self.sex=sex


p = parrot('male')
p.name = 'mitu'
p.age = 23

q = parrot('female')
print(q.sex)