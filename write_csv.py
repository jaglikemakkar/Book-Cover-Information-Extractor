import pandas as pd

# Class to write data to a csv File
class WriteToFile:
    def __init__(self, data):
        self.data = data

    # Function to write the data
    def write(self):
        dataframe = pd.DataFrame(self.data)
        dataframe.to_excel("result.xlsx", index = False)    
        