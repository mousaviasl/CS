import random

class CootieCatcher:
    
    def __init__(self):
        self.myMessages = [
            "I say, Yes. It will happen!"
            "No, forget about it."
            "Unpredicatable"
            "Most likely seems to happen, but not sure."
            "Most likely seens not happening."
            "It will definitly happen if you fight for it more than now."
            "Try it again, cause I'm confused!"
            "Sorry, this may hurt to know, but it will never ever happens to you."

        ]
        self.final_choice = None
    
    def choose_color(self):
        while True:
            try:
                color = input("Choose a color (red, yellow, green, blue): ").lower()
                if color not in ["red", "yellow", "green", "blue"]:
                    raise ValueError("Invalid color choice")
                
                if len(color) % 2 == 0:
                    return [1, 2, 5, 6]
                else:
                    return [3, 4, 7, 8]
            except ValueError:
                print("Sorry, that is not an option.")

    def choose_number(self, options):
    while True:
        try: