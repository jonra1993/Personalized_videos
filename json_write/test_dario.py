class dog:
    def __init__(self, n, s):
        self.name = n
        self.school = s

    def print_name(self):
        print(self.name)

    def print_school(self):
        print(self.school)

dario = dog('Dario', 'EPN')

dario.print_name()
dario.print_school()