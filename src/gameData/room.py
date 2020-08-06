# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, desc, acts = 'default'):
        self.name = name
        self.desc = desc
        self.explored = False
        self.acts = acts
        self.actions = []
        '''if acts == 'default':
            self.actions = '''
    def getActions(self):
        for name in [a for a in dir(self) if a.endswith('_to')]:
            if name.startswith('n'):
                self.actions.append('Go North')
            elif name.startswith('e'):
                self.actions.append('Go East')
            elif name.startswith('s'):
                self.actions.append('Go South')
            elif name.startswith('w'):
                self.actions.append('Go West')
        return self.actions
        
        
    #def connections(self):
   # print('Hello, my name is ' + self.name + ' and I am ' + self.age + ' years old!')