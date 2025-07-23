## Image Watermarking Desktop App

#### Tools used:
```pip install pillow``` ```pip install tkinter```

#### Requirements
| Requirement  | Must-have                                                                                                          | Extra      |
|--------------|--------------------------------------------------------------------------------------------------------------------|------------|
| Upload image | ✅ Single                                                                                                           | Multiple   |
| Watermark    | ✅ Text Only                                                                                                        | ✅ Logo       |
| Style Watermark | ✅ Change Font<br>✅ Change Color<br>✅ Change Size<br>✅ Change Opacity<br>✅ Change Location | ✅ Change Opacity<br>✅ Change Location      |
| Preview      | ✅ Single Image                                                                                                     | All Image  |
| Save Image   | ✅ Single                                                                                                           | All Image  |

### STEPS IMPLEMENTED
1. Make Initial UI with Canvas and Upload Button (TKinter) ```class ImageWaterMark(Tk)``` 
2. Create function for the upload button (PIL) ```def upload_image```
3. Develop separate UI window for watermark text properties ```def open_stamp_text_window```
4. Stamp💟 watermark text  ```def stamp_watermark_text```
5. Develop separate UI window for watermark logo properties ```def open_stamp_logo_window```
6. Stamp💟 watermark logo  ```def stamp_watermark_logo```
7. Save the watermarked image  ```def download_image```
8. Preview the watermarked image ```def preview_watermarked_image```

### Final Product

![day-85-stamp-logo](https://github.com/user-attachments/assets/058a342b-4b1a-489c-b16e-a98bf645687f)
![day-85-stamp-text](https://github.com/user-attachments/assets/05e4757e-918f-491f-8f41-1e621522b059)


#### Questions that came up:
1. Switched from PyCharm to VSCode -> How to use same virtual env in MacOS
    * Command + Shift + P 
    * Select Interpreter Path
    * Go to the workspace's venv folder
    * Find venv/bin/activate
    * Select the activate file

2. [Multiple file types in one variable for the filedialog attribute](https://stackoverflow.com/questions/44403566/add-multiple-extensions-in-one-filetypes-mac-tkinter-filedialog-askopenfilenam)

3. [Selecting multiple images](https://stackoverflow.com/questions/68079128/unable-to-select-multiple-files-in-tkinter)

4. [Save file in the selected directory](https://stackoverflow.com/questions/42190249/how-to-save-as-an-edited-image-png-using-a-file-dialog-in-tkinter-and-pil-in)

5. [How to check if image is transparent](https://stackoverflow.com/questions/65615059/check-if-an-image-is-transparent-or-not)

6. [How to overlay image on top of another](https://stackoverflow.com/questions/62427131/python3-and-pillow-pil-add-an-image-on-top-of-other-image-with-transparency)


#### Resources used:
<ul>
   <li>Image from xiSerge: https://pixabay.com/photos/reinebringen-lofoten-islands-sea-9710168/</li>
   <li>Check icon from flaticon.com: <a href="https://www.flaticon.com/free-icons/tick" title="tick icons">Tick icons created by Roundicons - Flaticon</a></li>
</ul>



