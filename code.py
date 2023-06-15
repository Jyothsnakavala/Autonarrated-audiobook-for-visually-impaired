import pytesseract
from pdf2image import convert_from_path
import pyttsx3

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# set the language to Telugu
tessdata_dir_config = '--tessdata-dir "C:\\Program Files\\Tesseract-OCR\\tessdata" '

# function to convert image to text
def img_to_text(_file):

    text = pytesseract.image_to_string(_file, config=tessdata_dir_config)
    print(text)

    # the output of OCR can be saved in a file
    file = open('output.txt', 'w')
    file.write(text)
    file.close()
    # the output text is feed into tts engine
    string_to_voice(text)

# function to convert text to speech
def string_to_voice(text):
    engine = pyttsx3.init()
    engine.setProperty("rate", 120)
    engine.save_to_file(text,'Test1.mp3')
    engine.say(text)
    engine.runAndWait()
    engine.stop()

if __name__ == "__main__":
    # Storing file path in variable '_file'
    _file = input("enter relative path of file:")

    img_to_text(_file)
