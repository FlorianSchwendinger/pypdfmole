#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author Florian Schwendinger
"""

import os
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from .pdf import XML2Converter, PdfDoc


def read_pdf(pdffile, page_numbers=[], codec='utf-8', strip_control=False,
             password="", caching=True, maxpages=0, rotation=0, image_dir=None):
    
    if not (os.path.splitext(pdffile)[1] == ".pdf"):
        raise IOError("PDF-file expected got '%s'!" % (os.path.splitext(pdffile)[1], ))
    
    if not os.path.exists(pdffile):
        raise IOError("Could not find PDF-file '%s'!" % (pdffile, ))
        
    if image_dir is None:
        imagewriter = None
    else:
        if not os.path.exists(image_dir):
            os.mkdir(image_dir)
        imagewriter = ImageWriter(image_dir)

    rsrcmgr = PDFResourceManager(caching=caching)
    laparams = LAParams()
    
    device = XML2Converter(rsrcmgr, codec=codec, laparams=laparams, imagewriter=imagewriter,
                           stripcontrol=strip_control)
    
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    
    with open(pdffile, 'rb') as con:
        if (page_numbers is None) or (len(page_numbers) == 0):
            page_numbers = [i[0] for i in enumerate(PDFPage.get_pages(con))]
    
        for page in PDFPage.get_pages(con, page_numbers, maxpages=maxpages, password=password,
                                      caching=caching, check_extractable=True):
            page.rotate = (page.rotate + rotation) % 360
            interpreter.process_page(page)
    
    return PdfDoc(device.doc)
