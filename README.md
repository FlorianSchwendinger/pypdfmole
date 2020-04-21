# pdfmole

This package is a rewrite from the **R** package 
[pdfmole](https://github.com/FlorianSchwendinger/pdfmole)
to put some **Python** scripts originally stored in the **R** package into
a dedicated **Python** package.

## Motivation
- In 2013, I was working at a company where we had often to deal with clients which provided their data only in the form of PDF reports. To this end the company has bought several commercial products to read PDF files. However, with this software the options of customization and automation where very limited. What means they tried to predict the entire structure of the document and users could only choose to use their prediction or not and had no option to provide additional information (e.g., number of columns, ...) to improve the prediction accuracy. At this time I discovered **pdfminer** which is great you have the option to convert your data into a XML-file where you get the coordinate for each character.
- In 2015, I was part of a scientific project to analyze the regional effects of EU spending. Back then each region reported their spending only on their homepage (typically pdf-files created based on spreadsheets). Some of these documents could not be read by other software due to formatting errors (e.g., since the column width was set to low and therefore not the entire column was shown, ...). However, **pdfminer** was able to reliably retrieve the coordinates of each letter, even when all the commercial solutions we tried failed. Back then I re-wrote the **pdfminer** code for XML conversion such that, I get a dictionary instead of the XML-file. Additionally, several **R** scripts which allowed to retrieve the table even in the presence of formatting mistakes. Back then I found, and I am still convinced that **pdfminer** is a great tool! However, it is much stronger in providing the data necessary for the alignment than performing the actual alignment. Which was the motivation in creating the **R** package pdfmole.
- In 2016, I started with the creation of the **R** package pdfmole, which basically was a rewrite of the scripts for the EU-Funds project into a package. The basic idea was to improve data extraction from pdf-files by decoupling data extraction and data alignment (transforming the extracted data into a table format). 
  + For data extraction **pdfminer** is great.  
  + For the data alignment a more flexible solution which allows the user to provide additional information would be desirable.


## Examples
- [Basic usage]()

## Installation
### Imports (packages needed to use pdfmole)
- [`pdfminer.six`](https://github.com/pdfminer/pdfminer.six)
### Suggests (packages needed to use optional functionality)
- [`PyQt5`](https://www.riverbankcomputing.com/software/pyqt/intro)

## TODO:
- write docs
- extend examples and clustering options

