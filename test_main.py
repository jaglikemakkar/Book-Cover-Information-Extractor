from extract_data import ExtractData
import main
from validator import ImageValidator
from parse_image import Parser

def test_validator_file():
    path = path = "C:\\Academics\\6th Sem\\CS305_Software_Engineering\\Assignments\\Assignment-3\\pictures\\1.png"
    validator = ImageValidator(path, '-f')
    res = validator.validate()
    assert res == True

def test_validator_dir():
    path = path = "C:\\Academics\\6th Sem\\CS305_Software_Engineering\\Assignments\\Assignment-3\\pictures"
    validator = ImageValidator(path, '-d')
    res = validator.validate()
    assert res == True

def test_app_load_imgs():
    path = path = "C:\\Academics\\6th Sem\\CS305_Software_Engineering\\Assignments\\Assignment-3\\pictures\\1.png"
    app = main.App(path)
    res = app.load_images()
    assert len(res)==1

def test_app_load_dir():
    path = path = "C:\\Academics\\6th Sem\\CS305_Software_Engineering\\Assignments\\Assignment-3\\pictures"
    app = main.App(path)
    res = app.load_images()
    assert len(res)==10

def test_extract_data():
    data = [([[571, 25], [679, 25], [679, 45], [571, 45]], 'Prentice', 0.2978680316124861), ([[573, 41], [629, 41], [629, 59], [573, 59]], 'HALL', 0.6145133947295475), ([[54, 68], [302, 68], [302, 96], [54, 96]], 'Robert C Martin Series', 0.7159533022415506), ([[104, 178], [600, 178], [600, 282], [104, 282]], 'Clean Code', 0.999899428287662), ([[44, 283], [663, 283], [663, 334], [44, 334]], 'A Handbook of Agile Software Craftsmanship', 0.9945581463912697), ([[50, 879], [296, 879], [296, 910], [50, 910]], 'Foreword by James 0. Coplien', 0.7065514566054445), ([[481, 874], [665, 874], [665, 910], [481, 910]], 'Robert C Martin', 0.875354761487706)]
    obj = ExtractData(data)
    title = obj.get_title().strip()
    author = obj.get_authors().strip()
    pubhlisher = obj.get_orgs().strip()
    isbn = obj.get_isbn().strip()
    assert title == "Clean Code"
    assert author == "ROBERT C. MARTIN, ROBERT C. MARTIN"
    assert pubhlisher == "PRENTICE HALL"
    assert isbn == ""

# def test_validator_file_error():
#     path = path = "C:\\Academics\\6th Sem\\CS305_Software_Engineering\\Assignments\\Assignment-3\\parse_image.py"
#     validator = ImageValidator(path, '-f')
#     res = validator.validate()

# def test_validator_dir_error():
#     path = path = "C:\\Academics\\6th Sem\\CS305_Software_Engineering\\Assignments\\Assignment-3\\pictures"
#     validator = ImageValidator(path, '-d')
#     res = validator.validate()

def test_app_image():
    path = "C:\\Academics\\6th Sem\\CS305_Software_Engineering\\Assignments\\Assignment-3\\pictures\\1.png"
    app = main.App(path)
    app.extract_data('en')

def test_app_dir():
    path = "C:\\Academics\\6th Sem\\CS305_Software_Engineering\\Assignments\\Assignment-3\\pictures"
    app = main.App(path)
    app.extract_data('en')

if __name__ == "__main__":
    test_validator_file()
    test_validator_dir()
    test_app_load_imgs()
    test_app_load_dir()
    test_extract_data()
    test_app_image()
    test_app_dir()