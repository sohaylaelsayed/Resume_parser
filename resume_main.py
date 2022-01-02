# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 17:08:24 2020

@author: sohay
"""
import os 
import csv  
import resume_parser
FeaturesExtraction=resume_parser

    
# field names  
fields = ['Name', 'Phone', 'Email', 'Skil','Education']  
    
    
# name of csv file  
filename = "Resume_Parser.csv"
    
# writing to csv file  
with open(filename, 'w') as csvfile:
    # creating a csv writer object  
    csvwriter = csv.writer(csvfile)  

path='D:\resume parser'
for filename in os.listdir(path):
   with open(filename, 'r') as f: 
    Text=FeaturesExtraction.extract_text_from_pdf(f)  # noqa: T001
    names = FeaturesExtraction.extract_names(Text)
    if names:
        name=names[0]  # noqa: T001
        
    phone_number = FeaturesExtraction.extract_phone_number(Text)

    
    emails = FeaturesExtraction.extract_emails(Text)

    if emails:
        email=emails[0] # noqa: T001
        
    skills = FeaturesExtraction.extract_skills(Text)

    
    education_information = FeaturesExtraction.extract_education(Text)

    
    rows= [ [name],  [ phone_number ], [email], [skills], [education_information] ]
    csvwriter.writerows(rows) 
    