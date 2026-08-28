<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="light" data-type="VERTICAL" data-vanity="arnabadhikary" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/arnabadhikary?trk=profile-badge">Arnab Adhikary</a></div>
              
# Python for Everybody Assignments

This folder contains standalone Python scripts completed for the Python for Everybody course. Run them from this folder with Python.

## How to run the scripts

- On Windows, use: py scriptname.py
- Some scripts ask for input at runtime.
- If no filename is provided, many scripts use a default sample file such as mbox-short.txt, mbox.txt, romeo.txt, or regex_sum_2454922.txt.

## Scripts, run instructions, and files used

| Script | What it does | Run command | Files read / DB updated |
| --- | --- | --- | --- |
| helloworld.py | Prints a simple introductory Python message. | py helloworld.py | No input file required. |
| stringassignment.py | Demonstrates string slicing and numeric conversion. | py stringassignment.py | Uses a built-in sample string; no external file. |
| fileassignment.py | Prints each line from a file in uppercase. | py fileassignment.py | Prompts for a text file such as words.txt or romeo.txt. |
| filemboxassignment.py | Calculates the average spam confidence from a mailbox file. | py filemboxassignment.py | Reads a mailbox file such as mbox-short.txt or mbox.txt. |
| dictionaryassignment.py | Counts the number of emails received from each sender. | py dictionaryassignment.py | Reads mbox-short.txt by default, or another mailbox file if provided. |
| tuplesassignment.py | Counts emails by hour of day. | py tuplesassignment.py | Reads mbox-short.txt by default, or another mailbox file if provided. |
| listsort.py | Sorts unique words from a text file. | py listsort.py | Reads romeo.txt by default, or another text file if provided. |
| listoperationassignment.py | Extracts sender addresses from mailbox data. | py listoperationassignment.py | Reads mbox-short.txt by default, or another mailbox file if provided. |
| highestoccurenceinfile.py | Finds the most common word in a file. | py highestoccurenceinfile.py | Reads any text file provided at runtime. |
| regexassignment.py | Practice with regular expressions and number extraction. | py regexassignment.py | Reads regex_sum_2454922.txt by default, or another text file if provided. |
| jsonassignment.py | Reads JSON data from a URL and computes totals. | py jsonassignment.py | Uses a remote JSON URL; no local file is required. |
| xmlassignment.py | Reads XML data from a URL and computes totals. | py xmlassignment.py | Uses a remote XML URL; no local file is required. |
| socketassignment.py | Connects to a server over a socket and fetches a text page. | py socketassignment.py | Reads data from the remote URL http://data.pr4e.org/intro-short.txt. |
| urlassignment.py | Parses HTML content using BeautifulSoup. | py urlassignment.py | Reads HTML from a remote web page. |
| urllinksassignment.py | Follows a sequence of links from a web page. | py urllinksassignment.py | Reads HTML from a remote web page and follows links. |
| openstreetmapapiassignment.py | Queries the OpenStreetMap API for location information. | py openstreetmapapiassignment.py | Uses a remote API endpoint; no local file is required. |
| emailcountdb.py | Stores email-domain counts in a SQLite database. | py emailcountdb.py | Reads a mailbox file such as mbox.txt and creates/updates emaildb.sqlite. |
| rename_py_files.py | Utility script that renames Python files in a target folder. | py rename_py_files.py | Updates files in the specified folder path. |

## Supporting files

- HelloWorldJupyterENvironment.ipynb: Jupyter notebook for the introductory environment setup.
- mbox-short.txt and mbox.txt: sample mailbox data used by several assignments.
- romeo.txt and words.txt: sample text files used by file-processing exercises.
- regex_sum_42.txt and regex_sum_2454922.txt: sample input files for regex exercises.

## Notes

These scripts are small standalone exercises that demonstrate core Python concepts such as file input/output, strings, lists, dictionaries, tuples, regular expressions, networking, web data access, parsing, and SQLite databases.

