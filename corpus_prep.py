#!/usr/bin/python

import argparse
import re
import io

def prep(in_file):
    NCT = re.compile('^NCT[0-9]+\|')
    
    with io.open(in_file, 'r', encoding="utf-8-sig") as source:        
        header = source.readline().strip().split("|")        
        #print ("\t").join(header).encode("utf-8")
        print ("|").join(header).encode("utf-8")
        cur = []
        for line in source:
            line = line.strip()    
            if line:
                mo = re.match(NCT, line)
                if mo:                    
                    if cur != []:                        
                        trial = ("").join(cur).split("|")
                        """
                        if len(trial) != 45:
                            print line
                            print trial[0], len(trial)
                        """
                        print ("|").join(trial).encode("utf-8")

                        #for item in zip(header, trial):
                        #    print item
                        cur = []
                    cur.append(line)                    
                else:
                    cur.append(line)
    return None

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-in', required=True)
    args = parser.parse_args()

    prep(getattr(args, 'in'))
    
        
