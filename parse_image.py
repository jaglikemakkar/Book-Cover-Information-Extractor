import easyocr

# Class to parse the image using easyocr
class Parser:

    # Initalizing path and language
    def __init__(self, path, lang):
        self.path = path
        self.lang = lang

    def get_data(self):
        reader = easyocr.Reader([self.lang])
        data = reader.readtext(self.path)
        
        return data