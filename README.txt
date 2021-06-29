Authors: Cole Nicholson-Rubidoux, Dustin Yan
How to run: This project uses a simple Python script that was tested and ran on the most current
            version of Python. This script also needs to have installed this (https://github.com/caleb531/automata#class-npdapda) library.
            Run command "python -m pip install automata-lib" to install the necessary components. After necessary
            libraries are installed, simply call the script with the python interpreter.
About: This script sets up an NFA then converts it to a DFA which is designed to count the 
       number of strings of length n (where 1 <= n <= 100) which are accepted by the DFA
       and returns the count of the strings. 