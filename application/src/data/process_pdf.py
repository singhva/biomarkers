'''
Created on Apr 13, 2015

@author: varun
'''

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine, LTFigure, LTImage
from urllib2 import urlopen
import requests
import re
import codecs


class PdfReader():
    ABSTRACT = "ABSTRACT"
    INTRODUCTION = "INTRODUCTION"
    MM = "MM"
    RESULTS = "RESULTS"
    CONCLUSIONS = "CONCLUSIONS"
    DISCUSSION = "DISCUSSION"
    REFERENCES = "REFERENCES"
    
    ABSTRACT_RE = re.compile("[0-9.\s]*abstract", re.IGNORECASE)
    INTRO_RE = re.compile("[0-9.\s]*introduction", re.IGNORECASE)
    MM_RE = re.compile(r"[0-9.\s]*(materials[s]? and methods\b|methods\b|patients and methods)", re.IGNORECASE)
    RESULTS_RE = re.compile("[0-9.\s]*results", re.IGNORECASE)
    CONCLUSIONS_RE = re.compile("[0-9.\s]*conclusion[s]?", re.IGNORECASE)
    DISCUSSION_RE = re.compile("[0-9.\s]*discussion", re.IGNORECASE)
    REFERENCES_RE = re.compile("[0-9.\s]*references[s]?", re.IGNORECASE)
    
    def __init__(self, pdf_file):
        self.raw_file = pdf_file
        self.sections = { 
                         PdfReader.ABSTRACT : { "re" : PdfReader.ABSTRACT_RE, "text" : [] }, 
                         PdfReader.INTRODUCTION : { "re" : PdfReader.INTRO_RE, "text" : [] }, 
                         PdfReader.MM : { "re" : PdfReader.MM_RE, "text" : [] },
                         PdfReader.RESULTS : { "re" : PdfReader.RESULTS_RE, "text" : [] },
                         PdfReader.CONCLUSIONS : { "re" : PdfReader.CONCLUSIONS_RE, "text" : [] },
                         PdfReader.DISCUSSION : { "re" : PdfReader.DISCUSSION_RE, "text" : [] },
                         PdfReader.REFERENCES : { "re" : PdfReader.REFERENCES_RE, "text" : [] }
                        }
        
    def parse(self):
        fp = open(self.raw_file, 'rb')
        parser = PDFParser(fp)
        document = PDFDocument(parser)
        if not document.is_extractable:
            raise PDFTextExtractionNotAllowed
        
        rsrcmgr = PDFResourceManager()
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        text_content = []
        current_section = None
        
        for i, page in enumerate(PDFPage.create_pages(document)):
            interpreter.process_page(page)
            layout = device.get_result()
            for obj in layout:
                if isinstance(obj, LTTextBox) or isinstance(obj, LTTextLine):
                    text = obj.get_text()

                    for section in self.sections:
                        if re.match(self.sections[section]["re"], text.strip()):
                            current_section = section
                            break
                        
                    text_content.append(text)
                    if current_section: self.sections[current_section]["text"].append(text)
                
        self.text = codecs.encode("\n".join(text_content), "utf-8")
        fp.close()
        
if __name__ == "__main__":
    pdf_file = "/Users/varun/Documents/papers/NLP/Cancer Res/22962265_Cancer Res-2012-Vicent-5744-56.pdf"
    pubmed_id = "26028407"
    pdf_reader = PdfReader(pdf_file)
    pdf_reader.parse()
    abstract = pdf_reader.sections[PdfReader.ABSTRACT]["text"]
    print "*********** ABSTRACT *************"
    print "\n".join(abstract[:2])
    print "***********************************"
    print "*********** INTRO *************"
    introduction = pdf_reader.sections[PdfReader.INTRODUCTION]["text"]
    print "\n".join(introduction)
    print "***********************************"
    print "*********** MATERIALS *************"
    print "\n"
    mm = pdf_reader.sections[PdfReader.MM]["text"]
    print "\n".join(mm)
    print "\n"
    print "***********************************"
    print "*********** RESULTS ***************"
    print "\n".join(pdf_reader.sections[PdfReader.RESULTS]["text"])
    print "***********************************"
    #print pdf_reader.text