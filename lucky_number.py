"""Program to generate a lucky number based on user input"""


#import random



def is_valid_color(color):
    """Check if the input is a valid color name using a color list."""
    valid_colors = {
        "red", 
        "blue", 
        "green", 
        "yellow", 
        "orange", 
        "purple", 
        "pink", 
        "brown", 
        "black", 
        "white", 
        "gray", 
        "cyan", 
        "magenta",
        "amber", 
        "aquamarine", 
        "azure", 
        "beige", 
        "burgundy", 
        "chartreuse", 
        "coral", 
        "crimson",
        "emerald", 
        "fuchsia",
        "gold", 
        "indigo", 
        "ivory",
        "jade", 
        "lavender", 
        "lime", 
        "maroon", 
        "navy", 
        "olive", 
        "peach", 
        "plum", 
        "ruby", 
        "sapphire", 
        "scarlet",
        "silver", 
        "teal", 
        "turquoise", 
        "violet", 
        "wheat", 
        "amethyst", 
        "apricot", 
        "blush", 
        "brass", 
        "bronze", 
        "carmine", 
        "cerulean",
        "chocolate", 
        "copper", 
        "ebony", 
        "flax", 
        "garnet", 
        "hunter", 
        "lilac", 
        "malachite", 
        "mauve", 
        "ochre", 
        "onyx", 
        "periwinkle",
        "rose", 
        "saffron", 
        "sepia", 
        "tan", 
        "topaz", 
        "vermilion", 
        "zinc"
        }

    return color.lower() in valid_colors




def ask_color():
    """function to ask for color"""
    while True:

        color = input("What's your favorite color? ")

        if not is_valid_color(color):
            print("That's not a recognized color. Try again.")
        else:
            break


    #if not color:
        #print("Please enter a valid color.")
        #return ask_color()



    #first letter of the inputted color
    first_letter = color[0].upper()


    #corresponding number
    # a:1, b:2 etc.

    letter_number = ord(first_letter) - ord('A') + 1

    #last digit of the corresponding number
    last_digit = letter_number % 10

    #last_digit is never 0
    if last_digit == 0:

        last_digit = 1


    return last_digit

    #return color.strip()







def generate_lucky_number(last_digit):
    """function to generate a lucky number"""

    #return random.randint(1, 9)

    #makes into an 'angel number' or something idrk. people like these numbers
    return last_digit * 111





def main():
    """main"""

    last_digit = ask_color()

    lucky_number = generate_lucky_number(last_digit)

    #triple number
    lucky_number_string = f"{lucky_number}"

    print(f"Your lucky number for is: {lucky_number_string}")





if __name__ == "__main__":
    #only run in __main__ and not during tests
    main()
