# Book-Cover-Information-Extractor
Extract information about book from an image of cover page.

---
**Name:**       Jaglike Makkar\
**Roll No.:**   2019CSB1092\
**Course:**     Software Engineering

---

## What does this program do

This is a python program that takes the path of an image or a directory containing images.
The images should be cover photos of some book. The program will first parse the images
using easyOcr, and then extract the important information of the image.
The program extracts the title, name of authors, name of publisher, and isbn code of the book.
After extracting, it writes the results in a .xlsx file.

## A description of how this program works (i.e. its logic)

**Initialization:** The program takes the path of a file or a directory containing files. It
checks if the path is valid and the files are images. If there is an error, it prints the error
and exits.

**Opening:** If the path is correct, the program opens the images using the CV2 library of
python.

**Parsing:** The program uses the Easyocr library for parsing the images. Easyocr returns
the text and its position.

**Extracting Data:** After the image is parsed, we need to extract the title, authors,
publishers, and ISBN code of the image. Here is how it is done:

**Extracting Title:** The title will have the maximum font size among all the data. I am
calculating the height of every text and calculating the maximum height. After this, I am
taking all the words whose relative difference with maximum height is not more than 0.1.

**Extracting ISBN:** ISBN code will be a 10 or 13-digit number consisting of numbers from
0 to 9 and ‘-’. It will also be preceded by ‘ISBN’. I am using keyword search and regex to
extract ISBN code.

**Extracting Authors:** To extract the authors, I am using the NLP library. We will know if
the given token is a person's name in the image. If there are multiple person names, I
am using a size heuristic to get the author's name.

**Extracting Publisher:** This is done similarly to authors. When NLP returns ‘ORG’, I am
assuming the token to be a publisher

## How to compile and run this program

To run the file:
`python main.py pictures`

To test the code:
`coverage run test_main.py -m -i
coverage html -i`

## Test Results
![image](https://user-images.githubusercontent.com/58853798/193253713-24447c02-1a8a-4a6d-a8de-4763b6155476.png)
