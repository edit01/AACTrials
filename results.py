#!/usr/bin/python

import argparse
import io
import re
from collections import defaultdict

NCT_REGEX = re.compile('^[0-9]+\|NCT[0-9]+')

def process(in_file):
    with io.open(in_file, 'r', encoding='utf-8') as fh:
        header = fh.readline().strip().split("|")
        print header

        results = []
        cur = []
        for line in fh:
            mo = re.match(NCT_REGEX, line)
            if mo:
                if cur != []:        
                    results.append(cur)
                    cur = []
                cur.append(line.strip())                    
            else:
                cur.append(line.strip())

        cleaned = defaultdict(list)
        for result in results:
            res = ("").join(result).split("|")
            new_res = dict(zip(header, res))
            cleaned[new_res["NCT_ID"]].append(res)
        
        results_count = 0    
        
        for k, v in cleaned.items():
            #print "%s =>" % (k)
            results_count += len(v)
            #for i, r in enumerate(v):
                #print "\t%i.%s\t%s" % (i+1, r[2], r[3])
        
        print "Studies:%s Total results:%s" % (len(cleaned), results_count)
    return None

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('-in')

    args = parser.parse_args()

    process(getattr(args, 'in'))

