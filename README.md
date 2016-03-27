#AACTrials
Contains some scripts for the corpus prep.
You can download the AACT corpus [here][1]

Download the pipe delimited text output so you don't have to bother with installing OracleDB.The state of the pipe delimited text output is...unfavorable. You will need to make sure the character encoding matches up. UTF-8 is standard but that's hardly reliable when the source isn't entirely UTF-8.

It would also be wise to read the comprehensive data dictionary and other various documentation files for this corpus before you begin. Why they use pipe delimited files...I do not know...

#TODO
1. Cleanup scripts
2. Undergoing discussion on what format to convert clinical trial detailed_description to.

#FORMAT
1. It should be considered an NLP corpus resource
2. It should be easy to distribute, use, and understand
3. It should be a common type format
4. Let's stay away from db & SQL

[1]: http://www.ctti-clinicaltrials.org/what-we-do/analysis-dissemination/state-clinical-trials/aact-database



