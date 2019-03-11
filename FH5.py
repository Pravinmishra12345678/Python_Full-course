class what:
    def yes(self):
        self.Countries = map(str, input().lower().split())


Capitals = dict()

# Fill it with some values
Capitals['india'] = 'delhi'
Capitals['Gujrat'] = 'surat'
Capitals['u.p'] = 'lucknow'
sl = []
s = what()
s.yes()
sl.append(s.Countries)
k = s.Countries

for country in k:

    if country in Capitals:
        print('The capital of ' + country + ' is ' + Capitals[country])

    else:
        print(None)

