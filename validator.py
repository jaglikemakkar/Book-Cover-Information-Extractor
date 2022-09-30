import os, sys

# Class to validate the input arguments
class Validator:

    # Initializing path and flag
    def __init__(self, path, flag):
        self.path = path
        self.flag = flag
    
    # Function to check if path is a directory
    def is_dir(self):
        return os.path.isdir(self.path)

    # Function to check if path is an image
    def is_file(self):
        return os.path.isfile(self.path)

    # Function to validate path
    def is_path_correct(self):
        is_valid = True

        # If flag says file, check file
        if self.flag == '-f':
            is_valid = self.is_file()

        # If flag says directory, check directory
        elif self.flag == '-d':
            is_valid = self.is_dir()
        
        # Else invalid
        else:
            is_valid = False

        if is_valid == False:
            print("Invalid Arguments")
            exit()

# Class to check if input files are images
class ImageValidator(Validator):
    def __init__(self, path, flag):
        self.path = path
        self.flag = flag
    
    # Function to check if file is allowed
    def allowed_file(self, filename):
        allowed_extensions = ['jpg', 'jpeg', 'png']
        allowed = True

        # Checking if dot is present in filename or not
        if '.' not in filename:
            allowed = False
        
        # Checking the filename extension
        if filename.rsplit('.', 1)[1].lower() not in allowed_extensions:
            allowed = False

        if not allowed:
            print("Invalid File")
            exit()
        return allowed

    # Function to validate the path
    def validate(self):

        # Checking if the path is correct
        self.is_path_correct()

        # Checking extension of the file
        if self.flag == '-f':
            filename = self.path.split('\\')[-1]
            self.allowed_file(filename)
        
        # If it was a directory
        elif self.flag == '-d':
            images = []

            # Checking extension of all the files in directory
            for filepath in os.listdir(self.path):
                filename = filepath.split('\\')[-1]
                self.allowed_file(filename)

        return True