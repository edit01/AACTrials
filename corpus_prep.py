#usr/bin/python
import argparse
import re
import io

"""
The clincal_study.txt file is WYSIWYG. All of the data for a single trial spans multiple lines in the same file. We therefore need to scan through the lines up until we hit the next study. We can do this pattern matching for the NCT_ID where NCT_ID represents the start of a trial. Text/lines preceding an NCT_ID should be considered part of the previous study.
"""
def prep(in_file, fields=None):

    with io.open(in_file, 'r', encoding="utf-8-sig") as source:        
        columns = source.readline().strip().split("|") # Read in the head line and store it in a var
        print ("|").join(fields).encode("utf-8")
        
        # Scan through each line and until we hit an NCT_ID. Until we do, append lines to a list.
        # When we do hit the next NCT_ID, join the stored lines up until that point into one "|" delimited line.
        # Reset the cursor list to [] or empty and repeat for the next NCT record.
        NCT = re.compile('^NCT[0-9]+\|')
        cur = []
        for line in source:
            line = line.strip()    
            if line:
                mo = re.match(NCT, line)
                if mo: # If NCT_ID matched                    
                    if cur != []:                        
                        study_row = ("").join(cur).split("|") #Join into single line
                        
                        # zip column fields && study so we get a dictionary of keys and values
                        # We want to be able to select our values easily given
                        # our fields file (keys)
                        joined_dict = dict(zip(columns, study_row))
                        selected = [joined_dict[x] for x in fields]
                        print ("|").join(selected).encode("utf-8")
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
    parser.add_argument('-fields')    
    args = parser.parse_args()
    
    # Read fields from file
    if args.fields:
        with open(args.fields) as fh:
            fields = [x.strip('\n') for x in fh.readlines()]
    
        prep(getattr(args, 'in'), fields)
    else:
        prep(getattr(args, 'in'))
        
