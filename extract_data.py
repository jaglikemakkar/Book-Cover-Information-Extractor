from parse_image import Parser
import spacy, sqlite3
import mysql.connector

conn = mysql.connector.connect(host='localhost',
                                        database='se3',
                                        user='root',
                                        password='jaglike')

# Class to extract title, author, publisher, isbn from image_data
class ExtractData:

    # Initializing the object
    def __init__(self, data):
        self.data = data

    # Function to fetch title
    def get_title(self):
        max_height = 0
        title = ""

        # Firstly we find the max height of any block
        for i in self.data:

            # Iterating over the self.data and finding corners
            pos = i[0]
            tl = pos[0]
            tr = pos[1]
            br = pos[2]
            bl = pos[3]

            # Calculating height and width
            width = tr[0] - tl[0]
            height = bl[1] - tl[1]
            area = width * height

            # Ignoring unit length strings
            if len(i[1]) == 1:
                continue

            # Updating max_height
            if height > max_height:
                max_height = height
        
        # Setting error = 0.1
        error = 0.1
        title = ""
        for i in self.data:
            pos = i[0]
            tl = pos[0]
            bl = pos[3]

            # Finding height of current block
            height = bl[1] - tl[1]

            # Ignoring unit length strings
            if len(i[1])==1:
                continue
            
            # If height of cur block > max height - error, we include it
            if height >= (max_height - error*max_height):
                title += i[1] + ' '
        
        # Returning the title
        return title

    # Function to check if the given code is ISBN
    def is_isbn(self, code):

        # Allowed characters are 0 to 9 and -
        valid = [str(i) for i in range (10)]
        valid.append('-')
        valid = set(valid)

        # Length of isbn must be 10 or 13
        if len(code)!=10 and len(code)!=13:
            return False
        
        # If all characters are valid, it is isbn
        for i in code:
            if i not in valid:
                return False
        return True
    
    # Function to return Isbn from data
    def get_isbn(self):
        
        isbn = ""

        # Iterating over all blocks
        for i in self.data:
            cur = i[1]

            # Iterating over current string
            for j in range (len(cur)):

                # Checking if string of length 13 is valid isbn
                code = cur[j:j+13]
                if self.is_isbn(code):
                    isbn = code
                    break
                
                # Checking if string of length 10 is valid isbn
                code = cur[j: j+10]
                if self.is_isbn(code):
                    isbn = code
                    break

            if len(isbn):
                break
        
        # Returning isbn
        return isbn

    # Function to get author names
    def get_authors(self):
        names = []

        # Combining all the strings, to improve time complexity
        text = ""
        for i in self.data:
            text += i[1] + ' $$ '

        # Firstly we will check if the name is present in the database or not
        names = []
        for i in self.data:
            cursor = conn.cursor()

            # Clearing the name
            name = i[1].split()[0].upper()
            if not name.isalpha():
                continue

            # Quering on the database
            query = "select * from authors where firstname = '%s'" % (name)
            cursor.execute(query)
            dbdata = cursor.fetchall()

            # If name was present, storing it in array.
            for i in dbdata:
                names.append(i[1])
        if len(names):
            return ', '.join(names)
        
        # We will check if the name is present in the database or not
        title = self.get_title().strip()
        if ''.join(title.split()).isalpha():

            # Querying on the database
            query = "select * from authors where firstname = '%s'" % (title)
            cursor.execute(query)
            dbdata = cursor.fetchall()

            # Storing the results in array
            for i in dbdata:
                names.append(i[1])
        if len(names):
            return ', '.join(names)
        
        # Using NLP to find labels of different tokens
        nlp = spacy.load('en_core_web_md')
        doc = nlp(text)

        # Extracting the names 
        names = []
        for sentence in doc.ents:
            # If the label of token is PERSON, we add it in names
            if sentence.label_ == "PERSON":
                names.append(str(sentence))

        # If NLP was not able to find any name
        if len(names)==0:
            return ""
        
        # If found only one name
        elif len(names)==1:
            return names[0]
        
        # If found more then 1 name, we will return last 2 names
        else:
            names = names[len(names)-2:]
            return names[0] + ', ' + names[1]

    # Function to get publisher name
    def get_orgs(self):
        names = []

        # Combining all the strings, to improve time complexity
        text = ""
        for i in self.data:
            text += i[1] + ' '
        
        # Using NLP to find labels of different tokens
        nlp = spacy.load('en_core_web_md')
        doc = nlp(text)

        # First we will check if the publisher is present in database or not
        names = []
        for i in self.data:

            # Querying on the database
            cursor = conn.cursor()
            name = i[1].split()[0].upper()

            # Clearing name
            if not name.isalpha():
                continue
            query = "select * from publisher where name = '%s'" % (name)
            cursor.execute(query)
            dbdata = cursor.fetchall()

            # If publisher was present storing it.
            for i in dbdata:
                names.append(i[1])
        if len(names):
            return ', '.join(names)

        # First we will check if the publisher is present in database or not
        title = self.get_title().strip()
        if ''.join(title.split()).isalpha():
            # Querying on the database
            query = "select * from publisher where name = '%s'" % (title)
            cursor.execute(query)
            dbdata = cursor.fetchall()
            # Storing the results in array
            for i in dbdata:
                names.append(i[1])
        if len(names):
            return ', '.join(names)

        # Extracting the names of organizations
        names = []
        for sentence in doc.ents:
            # If the label of token is ORG, we add it in names
            if sentence.label_ == "ORG":
                names.append(str(sentence))

        # If NLP was not able to find any name
        if len(names)==0:
            return ""
        else:
            return names[-1]