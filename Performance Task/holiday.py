import customtkinter

holidayEvent = {"January": ["Polar Bear Plunge Day", "Buffet Day", "Fruitcake Toss Day", "Trivia Day", "Bird Day", "Bean Day", "Old Rock Day", "Earth's Rotation Day", "Static Electricity Day", "Cut Your Energy Costs Day", "Learn Your Name in Morse Code Day", "Marzipan Day", "Make Your Dreams Come True Day", "Organize Your Home Day", "Strawberry Ice Cream Day", "Nothing Day", "Benjamin Franklin Day", "Thesaurus Day", "Popcorn Day", "Penguin Awareness Day", "Squirrel Appreciation Day", "Hot Sauce Day", "Handwriting Day", "Compliment Day", "Opposite Day", "Spouse's Day", "Chocolate Cake Day", "Fun at Work Day", "Puzzle Day", "Croissant Day", "Backwards Day"]}



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Fun Holiday")
        self.geometry("600x400")

        # set grid layout 1x2
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        
        self.navigation_frame = customtkinter.CTkFrame(self, width=100, corner_radius=0)
        self.navigation_frame.grid(row=0, column=0, sticky="nsew")
        self.navigation_frame.grid_rowconfigure(5, weight=1)

        self.mainLabel = customtkinter.CTkLabel(self.navigation_frame, width=120, text="Holiday", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.mainLabel.grid(row=0, column=0, pady=10)

        self.day = customtkinter.CTkEntry(self.navigation_frame, placeholder_text="Day", width=120, )
        self.day.grid(row=2, column=0, padx=20, pady=10)

        self.month = customtkinter.CTkOptionMenu(self.navigation_frame, 
                                                 values=["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"],
                                                 width=120)
        self.month.grid(row=3, column=0, padx=20, pady=10)

        self.searchButton = customtkinter.CTkButton(self.navigation_frame, text="Search", width=120, command=self.search)
        self.searchButton.grid(row=4, column=0, pady=10)

        self.appearance_mode_label = customtkinter.CTkLabel(self.navigation_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, sticky="s")

        self.appearance_mode = customtkinter.CTkOptionMenu(self.navigation_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode.grid(row=6, column=0, sticky="s", pady=20)

        # create home frame
        self.home_frame = customtkinter.CTkFrame(self, corner_radius=10)
        self.home_frame.grid(row=0, column=1, sticky="nsew", pady=10, padx=10)
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame1 = customtkinter.CTkButton(self.home_frame, text="Hey")
        self.home_frame1.grid(row=0, column=0)

    def search(self):
        print(self.day.get())
        print(self.month.get())

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

if __name__ == "__main__":
    app = App()
    app.mainloop()
