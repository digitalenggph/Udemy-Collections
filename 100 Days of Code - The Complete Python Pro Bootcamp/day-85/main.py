from tkinter import *
from PIL import Image, ImageDraw, ImageFont

class ImageWaterMark(Tk):
    def __init__(self):
        super().__init__()
        self.title("Krloves Water Mark")
        self.minsize(width=800, height=600)
        self.config(padx=50, pady=50)

        # canvas config
        self.canvas = Canvas(width=700, height=450, bg='#A2AAAD', highlightthickness=0)  # values in pixels
        self.tomato_img = PhotoImage(file="tomato.png")
        self.canvas.create_image(350, 225, image=self.tomato_img)  # center x, y
        upload_text = self.canvas.create_text(350, 225,
                                              text="Upload your image",
                                              fill="white",
                                              font=('Helvetica', 35, "bold"))
        self.canvas.grid(column=0, row=1, columnspan=5)

        # buttons
        self.upload_button = Button(text='Upload',  padx=10, pady=10,)
        self.upload_button.grid(column=2, row=1)

        # self.download_button = Button(text='Download', padx=10, pady=10,)
        # self.download_button.grid(column=1, row=1)


    def upload_image(self):
        pass

    def download_image(self):
        pass


if __name__ == '__main__':
    window = ImageWaterMark()
    window.mainloop()


