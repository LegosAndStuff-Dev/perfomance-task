import customtkinter
from ytmusicapi import YTMusic
import urllib.request
from PIL import Image
import webbrowser


customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


yt = YTMusic()


#urllib.request.urlretrieve("https://lh3.googleusercontent.com/ZiDnpS4sPXfL33gnC4j3QcYMcY8aaCzFOQ4z7GCY0zWaysDHwRrol9TnKO6_YdpCS0r2P3ojMZs5bANXyw=w120-h120-l90-rj", "Performance Task\local-filename.jpg")

#Possibly

def browser(id: str, type: str):
    if type == "song":
        webbrowser.open(f"https://www.youtube.com/watch?v={id}")

    elif type == "channel":
        webbrowser.open(f"https://www.youtube.com/channel/{id}")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("Song Searcher")
        self.geometry(f"{600}x{400}")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #The main frame in where every element is going to be in
        self.mainFrame = customtkinter.CTkFrame(self, 600, 400, corner_radius=10)
        self.mainFrame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
        self.mainFrame.grid_columnconfigure((0, 1, 2), weight=1)

        #The point of this is to have buffer space between the top and the search row
        self.placeholder = customtkinter.CTkLabel(self.mainFrame, text="")
        self.placeholder.grid(row=0, column=1, padx=10)

        #This is the song user input
        self.songEntry = customtkinter.CTkEntry(self.mainFrame, placeholder_text="Song")
        self.songEntry.grid(row=1, column=0, padx=10, pady=2)

        #This is the artits user input
        self.artistEntry = customtkinter.CTkEntry(self.mainFrame, placeholder_text="Artist")
        self.artistEntry.grid(row=1, column=1, padx=10, pady=2)

        #This is the search button user input
        self.searchButton = customtkinter.CTkButton(self.mainFrame, text="Search", command=self.search_song)
        self.searchButton.grid(row=1, column=2, padx=10, pady=2)

        #Column 0 (actually column 1)
        self.placeholder1 = customtkinter.CTkLabel(self.mainFrame, text="")
        self.placeholder1.grid(row=2, column=0)

        self.imageLabel = customtkinter.CTkLabel(self.mainFrame, text="")
        self.imageLabel.grid(row=3, column=0)

        self.placeholder2 = customtkinter.CTkLabel(self.mainFrame, text="")
        self.placeholder2.grid(row=4, column=0)


    #Button Event when the searchButton is presssed
    def search_song(self):
        song = self.songEntry.get().lower()
        artist = self.artistEntry.get().lower()

        combinded = f"{song} by {artist}"

        self.song_search = yt.search(combinded, "songs")
        self.album_search = yt.search(combinded, "albums")
        self.artist_search = yt.search(artist, "artists")


        print(self.song_search[0])
        print(self.album_search[0])
        print(self.artist_search[0])
        print("--------------------------------------------------------------------------------------------")

        for i in range(len(self.album_search[0]["thumbnails"])):
            if (self.album_search[0]["thumbnails"][i]["width"]) == 120:
                imageID = i

        if imageID == 0:
            imageID = i

        #School Code
        """
        urllib.request.urlretrieve(self.album_search[0]["thumbnails"][imageID]["url"], "Performance Task\local-filename.jpg")
        self.image = customtkinter.CTkImage(Image.open("Performance Task\local-filename.jpg"), size=(120, 120))
        self.imageLabel.configure(image=self.image)
        """
        
        #Home Code
        urllib.request.urlretrieve(self.album_search[0]["thumbnails"][imageID]["url"], "perfomance-task\Performance Task\local-filename.jpg")
        self.image = customtkinter.CTkImage(Image.open("perfomance-task\Performance Task\local-filename.jpg"), size=(120, 120))
        self.imageLabel.configure(image=self.image)
        
        self.songButton = customtkinter.CTkButton(self.mainFrame, text="Song", 
                                                  command=lambda: browser(self.song_search[0]["videoId"], "song")
                                                  #command=self.test
                                                  )
        self.songButton.grid(row=5, column=0, pady=5)

        self.channelButton = customtkinter.CTkButton(self.mainFrame, text="Channel", 
                                                     command=lambda: browser(self.song_search[0]["artists"][0]["id"], "channel")
                                                     )
        self.channelButton.grid(row=6, column=0, pady=5)
        
    def test(self):
        print("hey")




if __name__ == "__main__":
    app = App()
    app.mainloop()