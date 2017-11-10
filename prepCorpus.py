# prepCorpus.py
"""
Usage:

python prepCorpus.py -in <path to files directory> OR <singular file>

python prepCorpus.py -in "/data/*.xml.gz" OR /data/xin_eng_199501.xml.gz

"""
import argparse
import re
import io

"""
The clincal_study.txt file is WYSIWYG.
All of the data for a single trial spans multiple lines in the same file.
We therefore need to scan through the lines up until we hit the next study.
We can do this pattern matching for the NCT_ID where NCT_ID represents the start of a trial.
Text/lines preceding an NCT_ID should be considered part of the previous study.
1. Scan through each line and until we hit an NCT_ID. Until we do, append lines to a list.
2. When we do hit the next NCT_ID, join the stored lines up until that point into one "|" delimited line
3. Reset the cursor list to [] or empty and repeat for the next NCT record.
"""

def prep_corpus(corpus, fields=None):
    """Description for prep_corpus"""

    with io.open(corpus, 'r', encoding="utf-8-sig") as fh:
        columns = fh.readline().strip().split("|")
        print ("|").join(fields).encode("utf-8")
        nct = re.compile('^NCT[0-9]+\|')
        cur = []
        for line in fh:
            line = line.strip()
            if line:
                mo = re.match(nct, line)
                if mo:
                    if cur != []:
                        study_row = ("").join(cur).split("|")
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
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-in', '--input', required=True)
    parser.add_argument('-F', '--fields', required=False)
    args = parser.parse_args()

    if args.fields:
        with open(args.fields) as fh:
            fields = [x.strip('\n') for x in fh.readlines()]
        prep_corpus(getattr(args, 'in'), fields)
    else:
        prep_corpus(getattr(args, 'in'))
