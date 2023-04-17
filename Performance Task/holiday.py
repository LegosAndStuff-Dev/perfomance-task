import customtkinter


def holidayEvent(month: str, day: int):
    if month.lower() == "january":
        holiday = ["Polar Bear Plunge Day", "Buffet Day", "Festival of Sleep Day", "Trivia Day",    "Bird Day", "Bean Day", "Old Rock Day", "Earth's Rotation Day", "Word Nerd Day", "Cut Your Energy Costs Day", "Learn Your Name in Morse Code Day", "Marzipan Day", "Make Your Dreams Come True Day", "Organize Your Home Day", "Strawberry Ice Cream Day", "Nothing Day", "Benjamin Franklin Day", "Thesaurus Day", "Popcorn Day", "Penguin Awareness Day", "Squirrel Appreciation Day", "Answer Your Cat's Questions Day", "Handwriting Day", "Compliment Day", "Opposite Day", "Spouse's Day", "Chocolate Cake Day", "Fun at Work Day", "Puzzle Day", "Croissant Day", "Backwards Day"]
    
    elif month.lower() == "february":
        holiday = ["G.I. Joe Day","Play Your Ukulele Day","Carrot Cake Day","Eat Ice Cream for Breakfast Day","Chocolate Fondue Day","Lame Duck Day","Send a Card to a Friend Day","Laugh and Get Rich Day","Toothache Day","Umbrella Day", "Don't Cry Over Spilled Milk Day","Darwin Day","World Radio Day","Ferris Wheel Day","Gumdrop Day","Do a Grouch a Favor Day","Random Act of Kindness Day","Battery Day","Chocolate Mint Day","National Muffin Day","Language Day","Be Humble Day","International Dog Biscuit Appreciation Day","Tortilla Chip Day","World Sword Swallowers Day","Tell a Fairy Tale Day","International Polar Bear Day", "Public Sleeping Day"]

    elif month.lower() == "march":
        holiday = ["World Compliment Day","Old Stuff Day","I Want You to be Happy Day","March Forth and Do Something Day","Learn What Your Name Means Day","Dentist's Day","Alexander Graham Bell Day","Proofreading Day","International Fanny Pack Day","Mario Day","Oatmeal Nut Waffle Day","Alfred Hitchcock Day","Napping Day","Pi Day","Everything You Think is Wrong Day","Absolutely Incredible Kid Day","Submarine Day","Awkward Moments Day","Let's Laugh Day","World Storytelling Day","Common Courtesy Day","International Goof Off Day","Puppy Day","Chocolate Covered Raisins Day","Waffle Day","Make Up Your Own Holiday Day","Spanish Paella Day","Something on a Stick Day","Smoke and Mirrors Day","Take a Walk in the Park Day","Bunsen Burner Day",]

    elif month.lower() == "april":
        holiday = ["Fun at Work Day", "National DIY Day", "World Party Day", "Tell a Lie Day", "Read a Road Map Day", "Sorry Charlie Day", "Walk to Work Day", "Draw a Bird Day", "National Chicken Little Awareness Day", "Siblings Day", "Submarine Day", "Grilled Cheese Day", "Scrabble Day", "International Moment of Laughter Day", "World Pinhole Photography Day", "Wear Pajamas to Work Day", "Haiku Poetry Day", "Columnist Day", "Lover's Day", "Look Alike Day", "Impossible Astronaut Day", "Jelly Bean Day", "Take a Chance Day", "Richter Scale Day", "DNA Day", "Pretzel Day", "Take Our Daughters and Sons to Work Day", "Astronomy Day", "Zipper Day", "Honesty Day"]

    elif month.lower() == "may":
        holiday = ["Batman Day", "No Pants Day", "Free Comic Book Day", "Star Wars Day", "Space Day", "Herb Day", "Beverage Day", "Lost Sock Memorial Day", "Europe Day", "Clean Up Your Room Day", "Eat What You Want Day", "Limerick Day", "Frog Jumping Day", "Dance Like a Chicken Day", "Chocolate Chip Day", "National School Nurse Day", "Pack Rat Day", "No Dirty Dishes Day", "Pizza Party Day", "Be a Millionaire Day", "Talk Like Yoda Day", "Buy a Musical Instrument Day", "Twilight Zone Day", "Scavenger Hunt Day", "Sing Out Day", "World Lindy Hop Day", "Sun Screen Day", "Hamburger Day", "Put a Pillow on Your Fridge Day", "My Bucket's Got a Hole Day", "Macaroon Day"]

    elif month.lower() == "june":
        holiday = ["Say Something Nice Day", "National Doughnut Day", "Repeat Day", "Hug Your Cat Day", "Leave the Office Early Day", "Drive-In Movie Day", "VCR Day", "Best Friends Day", "Donald Duck Day", "Iced Tea Day", "Corn on the Cob Day", "Red Rose Day", "Sewing Machine Day", "Bourbon Day", "Nature Photography Day", "Bloomsday", "World Juggling Day", "International Picnic Day", "International Panic Day", "Sauntering Day", "International Picnic Day", "Daylight Appreciation Day", "Onion Ring Day", "Take Your Dog to Work Day", "Typewriter Day", "Swim a Lap Day", "Please Take my Children to Work Day", "Chocolate Pudding Day", "Helen Keller Day", "Tau Day", "Camera Day", "Meteor Watch Day"]

    elif month.lower() == "july":
        holiday = ["International Joke Day", "World UFO Day", "Compliment Your Mirror Day", "Sidewalk Egg Frying Day", "Workaholics Day", "World Kissing Day", "Tell the Truth Day", "Video Games Day", "Sugar Cookie Day", "Teddy Bears' Picnic Day", "Cheer Up the Lonely Day", "Simplicity Day", "Embrace Your Geekness Day", "Pandemonium Day", "Gummi Worm Day", "Ice Cream Day", "Emoji Day", "Caviar Day", "Stick Out Your Tongue Day", "Space Exploration Day", "Junk Food Day", "Pi Approximation Day", "Vanilla Ice Cream Day", "Cousins Day", "Culinarians Day", "Uncle and Aunt Day", "Take your Pants for a Walk Day", "Milk Chocolate Day", "Lasagna Day", "National Cheesecake Day", "Uncommon Musical Instrument Day"]

    elif month.lower() == "august":
        holiday = ["National Girlfriend Day", "Ice Cream Sandwich Day", "Watermelon Day", "International Beer Day", "Work Like a Dog Day", "Sisters' Day", "Lighthouse Day", "Happiness Happens Day", "Book Lovers Day", "Lazy Day", "Son and Daughter Day", "Middle Child Day", "Left-Handers Day", "Creamsicle Day", "Relaxation Day", "Tell a Joke Day", "Thrift Shop Day", "Mail Order Catalog Day", "World Photo Day", "Chocolate Pecan Pie Day", "Spumoni Day", "Be An Angel Day", "Ride Like the Wind Day", "Pluto Demoted Day", "Kiss and Make up Day", "Dog Appreciation Day", "The Duchess Who Wasn't Day", "Bow Tie Day", "According to Hoyle Day", "Frankenstein Day", "Eat Outside Day"]

    elif month.lower() == "september":
        holiday = ["Emma Nutt Day", "Bison Ten Yell Day", "Skyscraper Day", "Eat an Extra Dessert Day", "Cheese Pizza Day", "Read a Book Day", "Salami Day", "Pardon Day", "Teddy Bear Day", "Swap Ideas Day", "Make Your Bed Day", "Chocolate Milkshake Day", "Positive Thinking Day", "Hug Your Hound Day", "Make a Hat Day", "Collect Rocks Day", "International Country Music Day", "Rice Krispie Treat Day", "International Talk Like a Pirate Day", "Punch Day", "Miniature Golf Day", "Hobbit Day", "Checkers Day", "Punctuation Day", "Comic Book Day", "Love Note Day", "Crush a Can Day", "Ask a Stupid Question Day", "Good Neighbor Day", "Hot Mulled Cider Day"]

    elif month.lower() == "october":
        holiday = ["International Coffee Day", "Phileas Fogg Wager Day", "Balloons Around the World Day", "Taco Day", "Chic Spy Day", "World Smile Day", "Card Making Day", "Frappé Day", "Pierogi Day", "Curious Events Day", "Handbag Day", "It's My Party Day", "Old Farmers Day", "International Skeptics Day", "Mad Hatter Day", "I Love Lucy Day", "National Clean Out Your Virtual Desktop Day", "Wear Something Gaudy Day", "Chocolate Cupcake Day", "Ada Lovelace Day", "International Sloth Day", "Sweetest Day", "Caps Lock Day", "Mole Day", "Bologna Day", "Sourest Day", "Howl at the Moon Day and Night", "American Beer Day", "International Animation Day", "Internet Day", "Candy Corn Day", "Magic Day"]

    elif month.lower() == "november":
        holiday = ["Author's Day", "Deviled Eggs Day", "Sandwich Day", "Common Sense Day", "Zero Tasking Day", "Saxophone Day", "Bittersweet Chocolate with Almonds Day", "Tongue Twister Day", "Chaos Never Dies Day", "Vanilla Cupcake Day", "Origami Day", "Happy Hour Day", "World Kindness Day", "Pickle Day", "Clean Out Your Refrigerator Day", "Fast Food Day", "Take A Hike Day", "Push Button Phone Day", "Men Make Dinner Day", "National Absurdity Day", "World Hello Day", "Go For a Ride Day", "Fibonacci Day", "Celebrate Your Unique Talent Day", "Shopping Reminder Day", "Cake Day", "Buy Nothing Day", "Red Planet Day", "Electronic Greeting Card Day", "Computer Security Day"]

    elif month.lower() == "december":
        holiday = ["Eat a Red Apple Day", "Fritters Day", "Make a Gift Day", "Wear Brown Shoes Day", "Day of the Ninja", "Put on Your Own Shoes Day", "Letter Writing Day", "Pretend to Be a Time Traveler Day", "Christmas Card Day", "Dewey Decimal System Day", "Noodle Ring Day", "Gingerbread House Day", "Microwave Oven Day", "Monkey Day", "Ugly Sweater Day", "Chocolate Covered Anything Day", "Wright Brothers Day", "Official Lost and Found Day", "Underdog Day", "Sangria Day", "International Dalek Remembrance Day", "Date Nut Bread Day", "Festivus", "Eggnog Day", "Alphabet Day or No 'L' Day", "Thank You Note Day", "No Interruptions Day", "Card Playing Day", "Pepper Pot Day", "Bicarbonate of Soda Day", "Make Up Your Mind Day"]

    day = day - 1

    event = holiday[day]

    return event

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fun Holiday")
        self.geometry("460x300")

        # set grid layout 1x2
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.home_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.home_frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        self.home_frame.grid_columnconfigure((0, 1, 2), weight=1)

        self.day = customtkinter.CTkEntry(self.home_frame, placeholder_text="Day", width=120)
        self.day.grid(row=0, column=0, pady=10)

        self.month = customtkinter.CTkOptionMenu(self.home_frame, 
                                                 values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                                                 width=120)
        self.month.grid(row=0, column=1, pady=10)

        self.searchButton = customtkinter.CTkButton(self.home_frame, text="Search", command=self.search, width=120)
        self.searchButton.grid(row=0, column=2, pady=10)

        

    def search(self):
        print(self.day.get())
        print(self.month.get())

        test = holidayEvent(self.month.get(), int(self.day.get()))

        print(test)

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
