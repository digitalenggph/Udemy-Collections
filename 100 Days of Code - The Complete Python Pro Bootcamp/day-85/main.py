import os

from tkinter import *
from tkinter import filedialog, colorchooser, messagebox

from PIL import Image, ImageDraw, ImageFont, ImageTk, ImageColor
from sample_fonts_mac import sample_fonts


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

        self.stamp_text_button = Button(text='Stamp TEXT', padx=10, pady=10,
                                      command=self.open_stamp_text_window)
        self.stamp_text_button.grid_remove()

        self.stamp_logo_button = Button(text='Stamp LOGO', padx=10, pady=10,
                                      command=self.open_stamp_logo_window)
        self.stamp_logo_button.grid_remove()

        self.download_button = Button(text='Download', padx=10, pady=10,
                                      command=self.download_image)
        self.stamp_text_button.grid_remove()

        # images
        self.uploaded_image_file_name = ''
        self.preview_image_tk = ''
        self.preview_image_watermarked = ''

        # watermark text
        self.var_font = 'Arial'
        self.var_fontsize = 12
        self.var_color = (0, 0, 0)
        self.var_alpha = 50
        self.var_location = ''
        self.font_choose_color = (0, 0, 0)
        self.preview_text_watermarked = ''

        # watermark logo
        self.original_watermark = ''

    # -------------------------------------- STARTING WINDOW -------------------------------------- #

    def upload_image(self):
        formats = [("Image files", "*.png *.jpg *.jpeg *.gif")]
        file_path = filedialog.askopenfilename(title="Select image to be watermarked",
                                               filetypes=formats)
        
        if file_path:
            self.uploaded_image_file_name = os.path.basename(file_path)
            self.original_image = Image.open(file_path)

            self.preview_image = self.original_image.resize(self.new_image_size(self.original_image))
            self.preview_image_tk = ImageTk.PhotoImage(self.preview_image)
            self.canvas.create_image(self.canvas.winfo_width()//2, 
                                    self.canvas.winfo_height()//2, 
                                    image=self.preview_image_tk)
            self.upload_button.grid(column=0, row=2, sticky='w')
            self.stamp_text_button.grid(column=1, row=2)
            self.stamp_logo_button.grid(column=2, row=2)


    # -------------------------------------- FOR PREVIEW CANVAS -------------------------------------- #

    def new_image_size(self, uploaded_image):
        width, height = uploaded_image.size
        ratio = width/height
        current_width = self.canvas.winfo_width()
        current_height = self.canvas.winfo_height()


        if width > height: # landscape
            new_width = current_width
            new_height = int(new_width / ratio)
        
        else: # portrait or square
            new_height = current_height
            new_width = int(new_height * ratio)
        
        return (new_width, new_height)
    

    # -------------------------------------- STAMP WATERMARK TEXT -------------------------------------- #
    
    def stamp_watermark_text(self):
        try:
            font = ImageFont.truetype(f"/System/Library/Fonts/Supplemental/{self.var_font}.ttf", 
                                      size=self.var_fontsize)
        except OSError:
            font = ImageFont.load_default()
    
        if self.var_location:
            self.preview_image_watermarked = self.preview_image.copy()
            draw = ImageDraw.Draw(self.preview_image_watermarked)
            watermark_anchor=self.watermark_xy(self.var_location,
                                                width=self.preview_image_watermarked.size[0],
                                                height=self.preview_image_watermarked.size[1]
                                                )
            print(self.var_color + (self.var_alpha, ))
            self.preview_text_watermarked = draw.text(xy=watermark_anchor, 
                                            text="Heyyyyy!", 
                                            fill=self.var_color + (self.var_alpha, ), 
                                            font=font, 
                                            align="center",
                                            anchor=self.var_location)
        
            
            # Update the canvas with the new image
            self.preview_image_tk = ImageTk.PhotoImage(self.preview_image_watermarked)
            self.canvas.create_image(self.canvas.winfo_width()//2, 
                                    self.canvas.winfo_height()//2, 
                                    image=self.preview_image_tk)
            self.download_button.grid(column=4, row=2, sticky='e')

            # Update the actual image
            self.final_image_watermarked = self.original_image.copy()
            final_draw = ImageDraw.Draw(self.final_image_watermarked)
            x, y = self.final_image_watermarked.size
            self.final_text_watermarked = final_draw.text(xy=(int(x/2), int(y/2)), 
                                                            text="Hi! I am a watermark!", 
                                                            fill=(0, 0, 0, 128), 
                                                            font=font, 
                                                            align="left")
        
    
    def open_stamp_text_window(self):
        stamp_text_window = Toplevel(self)
        stamp_text_window.title("Stamp Text Settings")
        stamp_text_window.minsize(200, 300)

        # window title
        window_label = Label(stamp_text_window,
                             text='Edit Stamp Text Settings',
                             pady=10)
        window_label.grid(column=0, row=0, columnspan=3)

        # create  font dropdown object
        var_font = StringVar(stamp_text_window)
        var_font.set('Arial Black') # default value

        font_dropdown = OptionMenu(stamp_text_window, var_font, *sample_fonts)
        font_dropdown.grid(column=1, row=1)

        # create spinbox for font size
        var_font_size = DoubleVar(value=22)
        font_spinbox =  Spinbox(stamp_text_window, 
                                from_=12, to=96,
                                width=3,
                                textvariable=var_font_size
                                )
        font_spinbox.grid(column=2, row=1)

        # choose color
        color_button = Button(stamp_text_window, text = "Select color",
                        command = self.choose_color)
        color_button.grid(column=1, row=2)


        # Watermark Opacity
        opacity_scale = Scale(stamp_text_window,
                      from_=0, to=100, 
                      orient=HORIZONTAL, 
                      )
        opacity_scale.grid(column=2, row=2)

        radio_buttons = ['lt', 'mt', 'rt',
                        'lm', 'mm', 'rm',
                        'lb', 'mb', 'rb']
        radio_names = ['top-left', 'top-middle', 'top-right',
                       'middle-left', 'center', 'middle-right',
                       'bottom-left', 'bottom-middle', 'bottom-right']
        
        var_location = StringVar()
        for idx, option in enumerate(radio_buttons):
            row = 3 + idx // 3
            col = idx % 3
            rb = Radiobutton(stamp_text_window, text=radio_names[idx], variable=var_location, value=option)
            rb.grid(row=row, column=col, padx=10, pady=10, sticky='w')

        
        stamp_button = Button(stamp_text_window, text="OK", 
                              command=lambda: (self.get_stamp_text_values(font=var_font.get(),
                                                                            size=var_font_size.get(),
                                                                            color=self.font_choose_color,
                                                                            alpha=opacity_scale.get(),
                                                                            location=var_location.get()
                                                                    ), 
                                                                    self.stamp_watermark_text(),
                                                                    stamp_text_window.destroy()
                                                )
                            )
        stamp_button.grid(column=1, row=6)


    def choose_color(self):
        # variable to store hexadecimal code of color
        color_code = colorchooser.askcolor(title ="Choose color") 
    
        rgb = ImageColor.getrgb(color_code[1])
        self.font_choose_color = rgb

    
    def get_stamp_text_values(self, font, size, color, alpha, location):
        self.var_font = font
        self.var_fontsize = int(size)
        self.var_color = color
        self.var_location = location
        self.var_alpha = int((alpha/100)*255)

        print(self.var_font, self.var_fontsize, self.var_color, self.var_location,self.var_alpha)


    # -------------------------------------- STAMP WATERMARK LOGO -------------------------------------- #

    def open_stamp_logo_window(self):
        stamp_logo_window = Toplevel(self)
        stamp_logo_window.title("Stamp Logo Settings")
        stamp_logo_window.minsize(200, 300)

         # window title
        window_label = Label(stamp_logo_window,
                             text='Edit Stamp Text Settings',
                             pady=10)
        window_label.grid(column=0, row=0, columnspan=3)

        # Upload Watermark
        upload_watermark_button = Button(stamp_logo_window,
                                         text='Upload Watermark',
                                         command=lambda: self.upload_watermark(stamp_logo_window)
                                         )
        upload_watermark_button.grid(column=0, row=2)

        # Watermark Opacity
        opacity_scale = Scale(stamp_logo_window,
                      from_=0, to=100, 
                      orient=HORIZONTAL, 
                      )
        opacity_scale.grid(column=2, row=2)

        radio_buttons = ['lt', 'mt', 'rt',
                         'lm', 'mm', 'rm',
                         'lb', 'mb', 'rb']
        radio_names = ['top-left', 'top-middle', 'top-right',
                       'middle-left', 'center', 'middle-right',
                       'bottom-left', 'bottom-middle', 'bottom-right']
        
        var_location = StringVar()
        for idx, option in enumerate(radio_buttons):
            row = 4 + idx // 3
            col = idx % 3
            rb = Radiobutton(stamp_logo_window, text=radio_names[idx], variable=var_location, value=option)
            rb.grid(row=row, column=col, padx=10, pady=10, sticky='w')

        
        stamp_logo_button = Button(stamp_logo_window, 
                                   text="OK", 
                                   command=lambda:stamp_logo_window.destroy()
                             )
        stamp_logo_button.grid(column=1, row=7)

    
    def upload_watermark(self, window):
        formats = [("Image files", "*.png *.jpg *.jpeg *.gif")]
        file_path = filedialog.askopenfilename(title="Select watermark image",
                                                filetypes=formats)
        if file_path:
            self.original_watermark = Image.open(file_path)

            if self.has_transparency(self.original_watermark) == True:
                # Preview Watermark
                watermark_image = self.original_watermark
                watermark_image.thumbnail((128, 128))
                self.original_watermark_tk = ImageTk.PhotoImage(watermark_image)


                watermark_preview = Label(window, 
                                        image = self.original_watermark_tk)
                # watermark_preview.image = self.original_watermark_tk
                watermark_preview.grid(column=0, row = 3, columnspan=3)
            
            else:
                messagebox.showwarning("Warning", "Please select image with transparent background.")


    def download_image(self):
        root, extension = os.path.splitext(self.uploaded_image_file_name) 
        file = filedialog.asksaveasfile(initialfile = f"{root}_watermarked",
                                        mode='wb', defaultextension=extension)
        
        if file:
            # self.preview_image_watermarked.save(file)
            self.final_image_watermarked.save(file)




    # -------------------------------------- HELPER FUNCTIONS -------------------------------------- #

    def watermark_xy(self, pos, width, height):
        column_x = {'l': 0, 'm': int(width/2),  'r': width}
        row_y =    {'t': 0, 'm': int(height/2), 'b': height}
        
        col, row = list(pos)
        return (column_x[col], row_y[row])

    def has_transparency(self, img):
        if img.info.get("transparency", None) is not None:
            return True
        if img.mode == "P":
            transparent = img.info.get("transparency", -1)
            for _, index in img.getcolors():
                if index == transparent:
                    return True
        elif img.mode == "RGBA":
            extrema = img.getextrema()
            if extrema[3][0] < 255:
                return True

        return False



if __name__ == '__main__':
    window = ImageWaterMark()
    window.mainloop()


