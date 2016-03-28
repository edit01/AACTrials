#!/usr/bin/python
import argparse
import re
import io

"""
The clincal_study.txt file is what you see is what you get. All of the data for a single trial spans multiple lines in the same file. We therefore need to scan through the lines up until we hit the next study. We can do this pattern matching for the NCT_ID where NCT_ID represents the start of a trial. Text/lines preceding an NCT_ID should be considered part of the previous study.
"""

def prep(in_file):
    NCT = re.compile('^NCT[0-9]+\|')
    
    with io.open(in_file, 'r', encoding="utf-8-sig") as source:        
        header = source.readline().strip().split("|") # Read in the head line and store it in a var
        print ("|").join(header).encode("utf-8")
        
        # Scan through each line and until we hit an NCT_ID. Until we do, append lines to the cursor list.
        # When we do hit the next NCT_ID, join the resulting stored lines up until that point into one "|" delimited line.
        # Reset the cursor list to [] or empty and repeat for the next NCT record.
        cur = []
        for line in source:
            line = line.strip()    
            if line:
                mo = re.match(NCT, line)
                if mo: #If NCT_ID matched                    
                    if cur != []:                        
                        trial = ("").join(cur).split("|")
                        print ("|").join(trial).encode("utf-8")
                        cur = []
                    cur.append(line)                    
                else:
                    cur.append(line)
    return None

# INPUT: raw/clinical_study.txt
# OUTPUT: The output should be written out to a file where each line is a single pipe "|" delimited study record
if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-in', required=True)
    args = parser.parse_args()

    prep(getattr(args, 'in'))
    
        
