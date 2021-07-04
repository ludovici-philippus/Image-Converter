from PIL import Image 
import PySimpleGUI as sg

type = ""

sg.theme("DarkBlack")

layout = [[sg.Text("Let's convert some images!", justification="center")],
        [sg.InputText("Enter the image's path", key="img"), sg.FileBrowse()],
        [sg.Radio("PNG", "type", key="png", enable_events="png"), sg.Radio("JPEG", "type", key="jpeg", enable_events="jpeg"), sg.Radio("WebP", "type", key="webp", enable_events="webp")],
        [sg.Button("Convert!", key="cvt")]]

window = sg.Window("Image Converter", layout)

while True:
    event, values = window.read()
    
    if event in ("png", "jpeg", "webp"):
        type = event

    if event == sg.WIN_CLOSED:
        break
    if event == "cvt" and type != "":
        img = Image.open(window["img"].get())
        print(img.filename)
        if type == "png":
            img.save(f"{img.filename}-ImagemConvertida.png", "png")
        elif type == "jpeg":
            img = Image.open(window["img"].get())
            img.convert("RGB").save(f"{img.filename}-ImagemConvertida.jpeg", "jpeg")
        else:
            img.save(f"{img.filename}-ImagemConvertida.webp", "webp")
    
window.close()
