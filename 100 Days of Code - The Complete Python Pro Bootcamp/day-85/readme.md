## Image Watermarking Desktop App

#### Tools to be used:
```pip install pillow```

```pip install tkinter```

#### Requirements
| Requirement  | Must-have    | Extra      |
|--------------|--------------|------------|
| Upload image | Single       | Multiple   |
| Watermark    | Text Only    | Logo       |
| Preview      | Single Image | All Image  |
| Save Image   | Single       | All Image  |

### STEPS FOLLOWED
1. Make Initial UI with Canvas and Upload Button (TKinter)<br>
```class ImageWaterMark(Tk)``` 
2. Create function for the upload button (PIL)<br>
```def upload_image```
3. Set the blank canvas to be the uploaded image/s.<br>
```self.canvas.create_image(...)```
4. Create watermark text



#### Questions that arised:
1. Switched from PyCharm to VSCode -> How to use same virtual env in MacOS
    * Command + Shift + P 
    * Select Interpreter Path
    * Go to the workspace's venv folder
    * Find venv/bin/activate
    * Select the activate file

2. Multiple file types in one variable for the filedialog attribute
    * Reference: https://stackoverflow.com/questions/44403566/add-multiple-extensions-in-one-filetypes-mac-tkinter-filedialog-askopenfilenam


3. Selecting multiple images:
    * Reference: https://stackoverflow.com/questions/68079128/unable-to-select-multiple-files-in-tkinter

4. Save file in the selected directory
    * https://stackoverflow.com/questions/42190249/how-to-save-as-an-edited-image-png-using-a-file-dialog-in-tkinter-and-pil-in




