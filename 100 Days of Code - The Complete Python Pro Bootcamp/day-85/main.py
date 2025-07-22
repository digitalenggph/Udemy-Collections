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
        self.final_image_watermarked = ''

        # watermark text
        self.var_watermark_text = ''
        self.var_font = ''
        self.var_fontsize = ''
        self.var_color = ''
        self.var_alpha = ''
        self.var_location = ''
        self.font_choose_color = ''

        # watermark logo
        self.original_watermark = ''
        self.var_logo_location = ''
        self.var_logo_alpha = ''

    # -------------------------------------- STARTING WINDOW -------------------------------------- #

    def upload_image(self):
        formats = [("Image files", "*.png *.jpg *.jpeg *.gif")]
        file_path = filedialog.askopenfilename(title="Select image to be watermarked",
                                               filetypes=formats)
        
        if file_path:
            self.uploaded_image_file_name = os.path.basename(file_path)
            self.original_image = Image.open(file_path)

            self.upload_button.grid(column=0, row=2, sticky='w')
            self.stamp_text_button.grid(column=1, row=2)
            self.stamp_logo_button.grid(column=2, row=2)

            self.preview_watermarked_image()

        else:
            messagebox.showwarning("Warning", "Please select image location.")


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
    

    def preview_watermarked_image(self):
        if not self.final_image_watermarked: 
            self.preview_image = self.original_image.resize(self.new_image_size(self.original_image))

        else:
            self.preview_image = self.final_image_watermarked.resize(self.new_image_size(self.original_image))

        self.preview_image_tk = ImageTk.PhotoImage(self.preview_image)
        self.canvas.create_image(self.canvas.winfo_width()//2, 
                                self.canvas.winfo_height()//2, 
                                image=self.preview_image_tk)
        
        self.download_button.grid(column=4, row=2, sticky='e')

    

    # -------------------------------------- STAMP WATERMARK TEXT -------------------------------------- #
    
    def stamp_watermark_text(self):
        try:
            font = ImageFont.truetype(f"/System/Library/Fonts/Supplemental/{self.var_font}.ttf", 
                                      size=self.var_fontsize)
        except OSError:
            font = ImageFont.load_default()
    
        if self.var_location:
            self.final_image_watermarked = self.original_image.copy()
            final_draw = ImageDraw.Draw(self.final_image_watermarked)

            # get multiline bbox dimension
            bbox = final_draw.multiline_textbbox((0, 0), self.var_watermark_text, font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]

            # set where the watermark will be placed
            watermark_anchor=self.watermark_xy(pos=self.var_location,
                                               background_img=self.original_image,
                                               multitext_tuple=(text_width, text_height)
                                              )

            final_draw.text(xy=watermark_anchor, 
                            text=self.var_watermark_text, 
                            fill=self.var_color + (self.var_alpha, ), 
                            font=font, 
                            align="left")
            
            self.preview_watermarked_image()

    
    def open_stamp_text_window(self):
        stamp_text_window = Toplevel(self)
        stamp_text_window.title("Stamp Text Settings")
        stamp_text_window.minsize(200, 300)
        stamp_text_window.resizable(False, False)

        # window title
        window_label = Label(stamp_text_window,
                             text='Edit Stamp Text Settings',
                             pady=10)
        window_label.grid(column=0, row=0, columnspan=3)

        # create input area for watermark text

        watermark_text = Text(stamp_text_window, height=5, width=14) # height in lines, width in characters
        watermark_text.grid(column=0, row=1, rowspan=2)

        # To insert initial text:
        if not self.var_watermark_text:
            watermark_text.insert(END, "HEYYY")

        else:
            watermark_text.insert(END, self.var_watermark_text)

        # create  font dropdown object
        var_font = StringVar(stamp_text_window)
        var_font.set('Arial Black') # default value

        font_dropdown = OptionMenu(stamp_text_window, var_font, *sample_fonts)
        font_dropdown.grid(column=1, row=1)

        if not self.var_font: # if there's no value initiated yet
            var_font.set('Arial')
        else:
            var_font.set(self.var_font)


        # create spinbox for font size
        var_font_size = DoubleVar(value=22)
        font_spinbox =  Spinbox(stamp_text_window, 
                                from_=12, to=250,
                                width=3,
                                textvariable=var_font_size
                                )
        font_spinbox.grid(column=2, row=1)

        if not self.var_fontsize: # if there's no value initiated yet
            var_font_size.set(50)
        else:
            var_font_size.set(self.var_fontsize)

        # choose color
        color_button = Button(stamp_text_window, text = "Select color",
                        command = self.choose_color)
        color_button.grid(column=1, row=2)

        if not self.var_color: # if there's no value initiated yet
            self.font_choose_color = (0, 0, 0)
        else:
            self.font_choose_color = self.var_color

        # Watermark Opacity
        opacity_scale = Scale(stamp_text_window,
                      from_=0, to=100, 
                      orient=HORIZONTAL, 
                      )
        opacity_scale.grid(column=2, row=2)
        
        if not self.var_alpha: # if there's no value initiated yet
            opacity_scale.set(50)
        else:
            opacity_scale.set(self.var_alpha * 100 / 255)


        # radio button
        radio_buttons = ['lt', 'mt', 'rt',
                        'lm', 'mm', 'rm',
                        'lb', 'mb', 'rb']
        radio_names = ['top-left', 'top-middle', 'top-right',
                       'middle-left', 'center', 'middle-right',
                       'bottom-left', 'bottom-middle', 'bottom-right']
        
        var_location = StringVar()

        # set default values
        if not self.var_location: # if there's no value initiated yet
            var_location.set("mm")
        else:
            var_location.set(self.var_location)


        for idx, option in enumerate(radio_buttons):
            row = 3 + idx // 3
            col = idx % 3
            rb = Radiobutton(stamp_text_window, text=radio_names[idx], variable=var_location, value=option)
            rb.grid(row=row, column=col, padx=10, pady=10, sticky='w')



        # stamp
        stamp_button = Button(stamp_text_window, text="OK", 
                              command=lambda: (self.get_stamp_text_values(text=watermark_text.get('1.0', 'end-1c'),  
                                                                            font=var_font.get(),
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
        rgb, _ = colorchooser.askcolor(title ="Choose color") 
        self.font_choose_color = rgb

    
    def get_stamp_text_values(self, text, font, size, color, alpha, location):
        self.var_watermark_text = text
        self.var_font = font
        self.var_fontsize = int(size)
        self.var_color = color
        self.var_location = location
        self.var_alpha = int((alpha/100)*255)


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

        if not self.var_logo_alpha: # if there's no value initiated yet
            opacity_scale.set(50)
        else:
            opacity_scale.set(int(int(self.var_logo_alpha) * 100 / 255))


        # radio buttons
        radio_buttons = ['lt', 'mt', 'rt',
                         'lm', 'mm', 'rm',
                         'lb', 'mb', 'rb']
        radio_names = ['top-left', 'top-middle', 'top-right',
                       'middle-left', 'center', 'middle-right',
                       'bottom-left', 'bottom-middle', 'bottom-right']
        
        var_location = StringVar()
        # set default values
        if not self.var_logo_location: # if there's no value initiated yet
            var_location.set("mm")
        else:
            var_location.set(self.var_logo_location)

        for idx, option in enumerate(radio_buttons):
            row = 4 + idx // 3
            col = idx % 3
            rb = Radiobutton(stamp_logo_window, text=radio_names[idx], variable=var_location, value=option)
            rb.grid(row=row, column=col, padx=10, pady=10, sticky='w')

        stamp_logo_button = Button(stamp_logo_window, 
                                   text="OK", 
                                   command=lambda: (self.get_stamp_logo_values(alpha=opacity_scale.get(), 
                                                                               location=var_location.get()),
                                                    self.stamp_watermark_logo(),
                                                    stamp_logo_window.destroy()
                                                    )
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


    def get_stamp_logo_values(self, alpha, location):
        self.var_logo_location = location
        self.var_logo_alpha = int((alpha/100)*255)


    def stamp_watermark_logo(self):
        # Open overlay image
        watermark_img = self.original_watermark.copy()
        # watermark_img.putalpha(self.var_logo_alpha)

        # original image as background
        original_img_bg = self.original_image.copy()
        offset = self.watermark_xy(pos=self.var_logo_location,
                                   background_img=original_img_bg,
                                   overlay_img=watermark_img)

        original_img_bg.paste(watermark_img, 
                              offset, 
                              mask=watermark_img
                             )
        
        self.final_image_watermarked = original_img_bg
        self.preview_watermarked_image()

    # -------------------------------------- DOWNLOAD IMAGE -------------------------------------- #

    def download_image(self):
        root, extension = os.path.splitext(self.uploaded_image_file_name) 
        file = filedialog.asksaveasfile(initialfile = f"{root}_watermarked",
                                        mode='wb', defaultextension=extension)
        
        if file:
            self.final_image_watermarked.save(file)

    # -------------------------------------- HELPER FUNCTIONS -------------------------------------- #

    def watermark_xy(self, pos, background_img, overlay_img=None, multitext_tuple=None):
        background_w, background_h = background_img.size
        col, row = list(pos)

        if overlay_img is None and multitext_tuple is None:
            column_x = {'l': 0, 'm': int(background_w/2), 'r': background_w}
            row_y =    {'t': 0, 'm': int(background_h/2), 'b': background_h}

        elif background_img and multitext_tuple:
            text_w, text_h = multitext_tuple
            column_x = {'l': 0, 'm': (background_w - text_w)//2, 'r': background_w - text_w}
            row_y    = {'t': 0, 'm': (background_h - text_h)//2, 'b': background_h - text_h - int(0.5 * text_h)} # int(..) is for the tect offset (ascent to avoid cutoff)
            
        else:
            overlay_w, overlay_h = overlay_img.size
            column_x = {'l': 0, 'm': (background_w - overlay_w)//2, 'r': background_w - overlay_w}
            row_y    = {'t': 0, 'm': (background_h - overlay_h)//2, 'b': background_h - overlay_h}
        
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


