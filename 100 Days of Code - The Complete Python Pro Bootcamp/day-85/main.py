import os

from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageDraw, ImageFont, ImageTk


class ImageWaterMark(Tk):
    def __init__(self):
        super().__init__()
        self.img = None
        self.title("krloves ♥ Water Mark")
        self.minsize(width=800, height=600)
        self.config(padx=50, pady=50)
        self.resizable(False, False)

        # canvas config
        self.canvas = Canvas(width=700, height=450, bg='#A2AAAD', highlightthickness=0)  # values in pixels
        upload_text = self.canvas.create_text(340, 150,
                                              text="Drop image here!",
                                              fill="white",
                                              font=('Helvetica', 35, "bold"))
        self.canvas.grid(column=0, row=1, columnspan=5)

        # buttons
        self.upload_button = Button(text='Upload', padx=10, pady=10,
                                    command=self.upload_image)
        self.upload_button.grid(column=2, row=1)

        self.stamp_text_button = Button(text='Stamp text', padx=10, pady=10,
                                      command=self.stamp_watermark_text)
        self.stamp_text_button.grid_remove()

        self.download_button = Button(text='Download', padx=10, pady=10,
                                      command=self.download_image)
        self.stamp_text_button.grid_remove()

        # images
        self.uploaded_image_file_name = ''
        self.uploaded_image_tk = ''
        self.watermarked_image = ''

        # watermark
        self.watermark_text = ''


    def upload_image(self):
        formats = [("Image files", "*.png *.jpg")]
        file_path = filedialog.askopenfilename(title="Select image to be watermarked",
                                               filetypes=formats)
        self.uploaded_image_file_name = os.path.basename(file_path)
        # open file path using TKinter this is okay but need to resize so TKinter has to be used
        # self.uploaded_image = PhotoImage(file=file_path)

        image = Image.open(file_path)            # Replace with your image file path
        self.resized_image = image.resize((700, 450)) # Resize image based on canvas size
        self.uploaded_image_tk = ImageTk.PhotoImage(self.resized_image)
        self.canvas.create_image(340, 150, image=self.uploaded_image_tk)
        self.upload_button.grid(column=0, row=2, sticky='w')
        self.stamp_text_button.grid(column=3, row=2, sticky='e')

    
    def stamp_watermark_text(self):
        font = ImageFont.load_default()
        # font = ImageFont.truetype("arial.ttf", size=30)
        self.watermarked_image = self.resized_image
        draw = ImageDraw.Draw(self.watermarked_image)
        self.watermark_text = draw.text(xy=(250, 250), 
                                        text="Hi! I am a watermark!", 
                                        fill=(0, 0, 0, 128), 
                                        font=font, 
                                        align="left")
        
        # Update the canvas with the new image
        self.uploaded_image_tk = ImageTk.PhotoImage(self.watermarked_image)
        self.canvas.create_image(340, 150, image=self.uploaded_image_tk)
        self.download_button.grid(column=4, row=2, sticky='e')

    def download_image(self):

        root, extension = os.path.splitext(self.uploaded_image_file_name)
        
        file = filedialog.asksaveasfile(initialfile = f"{root}_watermarked",
                                        mode='wb', defaultextension=extension)

        self.watermarked_image.save(file)
        
        
        # if file:
        #     im.save(file) # Saves the image to the input file name.


if __name__ == '__main__':
    window = ImageWaterMark()

    if window.uploaded_image_tk:
        print('hooray')

    window.mainloop()


