class Cat:

    def __init__(self, name):
        """Constructor."""
        self.name = name

    def speak(self):
        """Print a phrase."""
        print(f"¡Hello, my name is: {self.name}!")

if __name__ == "__main__":

    cristhian_cat= Cat( 'cristhian')

    cristhian_cat.speak()

