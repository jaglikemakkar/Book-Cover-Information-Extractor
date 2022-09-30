import sys, os
import cv2
from validator import ImageValidator, Validator
from extract_data import ExtractData
from write_csv import WriteToFile
from parse_image import Parser

dir_path = "C:\\Academics\\6th Sem\\CS305_Software_Engineering\\Assignments\\Assignment-3\\pictures"
flag = '-d'

class App:

    # Initializing path and flag
    def __init__(self, path):
        self.path = path
        flag = '-1'

        # Checking if the given path is file or directory
        # If path is directory, flag will be '-d'
        if os.path.isdir(path):
            flag = '-d'

        # If path is a directory, flag will be '-f'
        elif os.path.isfile(path):
            flag = '-f'
        self.flag = flag

        # Validating the input path
        validator = ImageValidator(path, flag)
        validator.validate()
    
    # Function to load images from directory
    def load_images(self):
        # Checking if path is a directory
        if self.flag == '-d':
            images = []

            # Iterating over all the files in directory
            for filename in os.listdir(self.path):
                img = cv2.imread(os.path.join(self.path,filename))

                # If image is not None, storing it in array.
                if img is not None:
                    images.append(os.path.join(self.path,filename))
            return images

        else:
            # If path was single image
            img = cv2.imread(self.path)
            return [img]

    # Function to extract data from image
    def extract_data(self, lang):
        
        # Loading all the images in directory
        images = self.load_images()

        # Dictionary to store result
        result = {"Title": [], "Author": [], "Publisher": [], "Isbn": []}

        # Iterating over all the images
        for img in images:
            
            parser = Parser(img, lang)

            # Parsing the image
            img_data = parser.get_data()
            for i in img_data:
                print(i)
            print()
            print()

            # Creating object of extract data class
            extractor = ExtractData(img_data)

            # Extracting Title, isbn, author and publisher
            title = extractor.get_title()
            isbn = extractor.get_isbn()
            author = extractor.get_authors()
            publisher = extractor.get_orgs()

            # Stroing the extracted data in dictionary
            result["Title"].append(title)
            result["Author"].append(author)
            result["Publisher"].append(publisher)
            result["Isbn"].append(isbn)

            print("Title: ", title)
            print("Author: ", author)
            print("Publisher:", publisher)
            print("Isbn: ", isbn)
            print()
            print()
            
        # Writing the result to XLSX file
        writer = WriteToFile(result)
        writer.write()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("USAGE: {} [path]".format(sys.argv[0]))
        exit()
    path = sys.argv[1]
    print(path)
    app = App(path)
    app.extract_data('en')