#AACTrials
Contains some scripts for the corpus prep.
You can download the AACT corpus [here][1]
Extract into a folder, "raw" if you wish to just use the .gitignore file

Download the pipe delimited text output so you don't have to bother with installing OracleDB.The state of the pipe delimited text output is...unfavorable. You will need to make sure the character encoding matches up. UTF-8 is standard but that's hardly reliable when the source isn't entirely UTF-8.

It would also be wise to read the comprehensive data dictionary and other various documentation files for this corpus before you begin. Why they use pipe delimited files...I do not know...

# TODO
1. Cleanup scripts
2. Undergoing discussion on what format to convert clinical trial detailed_description to.

# USAGE
`corpus_prep.py -in "path/to/file" -fields "path/to/selected_fields_file" > output.txt`

The resulting output file contains one clinical study record per line. Each line will lead with an NCT_ID.

# CORPUS FORMAT IDEAS
1. It should be considered an NLP corpus resource
2. It should be easy to distribute, use, and understand
3. It should be a common type format
4. Let's stay away from db & SQL for now

[1]: http://www.ctti-clinicaltrials.org/what-we-do/analysis-dissemination/state-clinical-trials/aact-database



