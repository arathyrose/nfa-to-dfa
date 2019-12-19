# AUTOMATA THEORY ASSIGNMENT 1

This contains all the files related to automata theory assignment 1

## PROBLEM STATEMENT

Write a python script to convert a Nondeterministic finite automaton to a deterministic finite automaton.

## FILES CONTAINED

### SUBMITTED ON MOODLE

This folder contains what has been submitted to moodle. (a `2018101042_A1.tar.gz` file that contains a directory `2018101042_A1` that includes `script.py` and `report.pdf`

### Homework_Assignment_1.pdf

Contains the problem statement (as uploaded on moodle)

### Input testing files used and their corresponding output files

input1.json  : output1.json
input2.json  : output2.json
input3.json  : output3.json

### Code fragments used for testing parts of the code

#### generate_op.py

This code is used to produce only the reachable states of the DFA. It prints the union of all the outputs of each line of the t-function. However, this function is no longer required.

#### intersection.py

This code is used to find those elements in set1 which contains all elements in set2.

#### powerset.py

This code is used to generate the powerset of the given set.

### Final python script

> script.py

To check how the file actually works and to run it, refer the report. (`report.pdf`)

### Python script that checks if the output obtained matches with a given file

> checkOutput.py

To run this file, run the following command

> python3 checkOutput.py

This script takes in the input NDA from the `input.json` file, converts it into a DFA, stores it in `output.json` file, and then compares the DFA obtained with the DFA stored in the file `output_check.json`.
Then it prints True or False if their states match, their letters match, their start state match, their allowed final states match and their t-function matches.

### Reports made

- In docx format: `report.docx`
- In markdown format: `report.md`
- In PDF format (required for submission): `Report.pdf`
