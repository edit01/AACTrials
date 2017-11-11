# statusType.py

import argparse
import io
import codecs
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

from datetime import datetime
from collections import defaultdict

def get_header(in_file):

    with io.open(in_file, 'r', encoding="utf-8-sig") as fh:
        header = fh.readline().strip().split("|")
    return header

def status_frequency(in_file):
    with io.open(in_file, 'r', encoding="utf-8-sig") as fh:
        header = fh.readline().strip().split("|")

        status_frequency = defaultdict(int)
        for line in fh:
            line = line.strip().split("|")
            study = dict(zip(header, line))

            if "OVERALL_STATUS" in study and len(study['OVERALL_STATUS'] < 30):
                status_frequency[study["OVERALL_STATUS"]] += 1
    frequencies = defaultdict(int)
    frequencies = {k: v for k, v in status_frequency.items() if v > 5}

    return frequencies

def calculate_proportions(frequencies):
    '''Calculate frequency proportions'''
    pfreqs = defaultdict(float)
    total = sum(frequencies.values())

    for k, v in frequencies.items():
        proportion = float(v) / total
        if proportion > .03:
            pfreqs[k] = proportion
        else:
            pfreqs["other"] += proportion
    return pfreqs

def generate_pie(values , labels):
    '''Generate pie chart'''

    colors = ['yellowgreen', 'gold', 'lightskyblue', 'lightcoral']
    plt.pie(values, explode=None, labels=labels, colors=colors, autopct='%1.1f%%',
            shadow=True, startangle=90)
    plt.axis('equal')
    plt.show()
    return None

def study_type_frequency(in_file):

    with io.open(in_file, 'r', encoding="utf-8-sig") as fh:
        header = fh.readline().strip().split('|')
        print header

        type_frequency = defaultdict(int)
        len_freq = defaultdict(int)
        for line in fh:
            line = line.strip().split('|')
            len_freq[len(line)] += 1
            study = dict(zip(header, line))

            if study["STUDY_TYPE"]:
                type_frequency[study["STUDY_TYPE"] + study["OVERALL_STATUS"]] += 1

    return type_frequency

def date_frequency(trials):
    date_counts = defaultdict(int)
    for t in trials:
        date_object = datetime.strptime(t[1], '%B %d, %Y')
        date_counts[date_object.year] += 1
    return date_counts

def generate_line(counts, labels):
    x = counts.keys()
    y = counts.values()
    plt.xlabel(labels["xlabel"])
    plt.title(labels["Title"])
    plt.plot(x, y)
    plt.show()
    return None

def generate_hist(counts):
    N = len(counts)
    #menMeans   = (20, 35, 30, 35, 27)
    menMeans   = counts.values()
    womenMeans = (25, 32, 34, 20, 25)
    #menStd     = (2, 3, 4, 1, 2)
    womenStd   = (3, 5, 2, 3, 3)
    ind = np.arange(N)    # the x locations for the groups
    width = 0.35       # the width of the bars: can also be len(x) sequence

    p1 = plt.bar(ind, menMeans,   width)
    #p2 = plt.bar(ind, womenMeans, width, color='y',
    #             bottom=menMeans, yerr=menStd)

    plt.ylabel('# studies registered')
    plt.xlabel('Year')
    plt.title('# Studies registered per year')
    plt.xticks(ind+width/2., counts.keys())
    #plt.yticks(np.arange(0,81,10))
    #plt.legend( (p1[0], p2[0]), ('Men', 'Women') )

    plt.show()
    return None

def process(in_file, add_terms):
    terms = ['NCT_ID'] + add_terms

    trials = []
    with io.open(in_file, 'r', encoding="utf-8-sig") as fh:
        header = fh.readline().strip().split("|")
        print header
        for line in fh:
            line = line.strip().split("|")
            study = dict(zip(header, line))

            retrieved = [study[term] for term in terms]
            trials.append(retrieved)
            #print ("\t").join(retrieved)
    return trials

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-in')
    parser.add_argument('-out')
    args = parser.parse_args()

    header = get_header(getattr(args, 'in'))

    #Study Status: Completed/Ongoing..?
    """
    freqs = status_frequency(getattr(args, 'in'))
    pfreqs = calculate_proportions(freqs)
    generate_pie(pfreqs.values(), pfreqs.keys())
    """

    #Study Type: Observational/Interventional/Other?
    """
    type_freq = study_type_frequency(getattr(args, 'in'))
    type_prop = calculate_proportions(type_freq)
    generate_pie(type_prop.values(), type_prop.keys())
    """

    #Try grouping them by date?    
    # of studies registered by year
    """
    additional_terms = ['FIRSTRECEIVED_DATE']
    trials = process(getattr(args, 'in'), additional_terms)
    date_counts = date_frequency(trials)
    generate_hist(date_counts)
    """

    #of studies over time/trend "Sum"
    """
    total = 0
    date_counts_total = defaultdict(int)
    for k, v in date_counts.items():
        total += v
        date_counts_total[k] = total
        #print "%s => %s, %s" % (k, v, total)
    """
    """
    for k, v in date_counts_total.items():
        print "%s => %s" % (k, v)
    """
    """
    plt_labels = {'xlabel' : 'Year', 'Title' : 'Number of registered studies overtime'}
    generate_line(date_counts_total, plt_labels)
    """

    #print get_header(getattr(args,'in'))
    #Get study description?
    #additional_terms = ['DETAILED_DESCRIPTION']
    additional_terms = ['BRIEF_SUMMARY', 'DETAILED_DESCRIPTION']

    trials = process(getattr(args, 'in'), additional_terms)
    for i, trial in enumerate(trials):
        #print ("|").join(trial).encode('utf-8')
        file_name = "output/%s_%s.txt" % (trial[0], i)
        with codecs.open(file_name, 'w', encoding='utf-8') as fh:
            #fh.write(trial[1])
            data = trial[1] + trial[2]
            fh.write(data)
