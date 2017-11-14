#extract data from <seg> </seg> tags

data = []

for line in lines:
    #select lines with seg tags only
    if line.startswith( '<seg>' ):
        #seg tag is 5 characters long and </seg> is 6 characters long
        data.append( line[5:-6] )
    
    return data
    
#--------------------------------

import re
#regex pattern to match data from <seg> tags
patt = '<seg>(?P<data>.+)</seg>'
patt = re.compile(patt)

data = []

for line in lines:
    #re.match starts matching from the start of the text (in this case, line)
    match_res = re.match(patt, line)
    if match_res:
        data.appen( match_res.group('data') )

#-----------------------------------------
from xml.etree import ElementTree as ET

data = []

for line in lines:
    if line.startswith('<seg>'):
        #load each individual line to xml as an individual element tree
        #and get the text from it
        seg_atag = ET.fromstring( line )
        data.append( seg_tag.text )

#----------------------------------------
from xml.etrr import ElementTree as ET

#load the entire xml file as a xml element_tree
xml_data = ET.parse('path_to_xml_file.xml')

seg_data = []

#iterate over <seg> tags in the file
for seg_tag in xml_data.iter('seg'):
    seg_data.append(seg_tag.text)
