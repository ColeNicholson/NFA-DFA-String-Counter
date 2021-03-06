# Written by: Cole Nicholson-Rubidoux, Dustin Yan

#

from automata.fa.nfa import NFA
from automata.fa.dfa import DFA


def build_dfa():
    # This function defines the NFA listed in the problem description
    nfa = NFA(
        states={'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q0_', 'q1_', 'q2_', 'q3_', 'q4_', 'q5_', 'q6_', 'qs', 'qf'},
        input_symbols={'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'},
        transitions={
            'qs': {'0': {'qf'}, '1': {'q0_', 'q1'}, '2': {'q0_', 'q2'}, '3': {'q0_', 'q3'}, '4': {'q0_', 'q4'},
                   '5': {'q0_', 'q5'}, '6': {'q0_', 'q6'}, '7': {'q0_', 'q0'}, '8': {'q0_', 'q1'}, '9': {'q0_', 'q2'}},
            'qf': {'0': {'qf'}, '1': {'qf'}, '2': {'qf'}, '3': {'qf'}, '4': {'qf'}, '5': {'qf'}, '6': {'qf'},
                   '7': {'qf'}, '8': {'qf'}, '9': {'qf'}},
            'q0': {'0': {'q0_', 'q0'}, '1': {'q0_', 'q1'}, '2': {'q0_', 'q2'}, '3': {'q0_', 'q3'}, '4': {'q0_', 'q4'},
                   '5': {'q0_', 'q5'}, '6': {'q0_', 'q6'}, '7': {'q0_', 'q0'}, '8': {'q0_', 'q1'}, '9': {'q0_', 'q2'}},
            'q0_': {'0': {'q0_'}, '1': {'q1_'}, '2': {'q2_'}, '3': {'q3_'}, '4': {'q4_'}, '5': {'q5_'}, '6': {'q6_'},
                    '7': {'q0_'}, '8': {'q1_'}, '9': {'q2_'}},
            'q1': {'0': {'q1_', 'q3'}, '1': {'q1_', 'q4'}, '2': {'q1_', 'q5'}, '3': {'q1_', 'q6'}, '4': {'q1_', 'q0'},
                   '5': {'q1_', 'q1'}, '6': {'q1_', 'q2'}, '7': {'q1_', 'q3'}, '8': {'q1_', 'q4'}, '9': {'q1_', 'q5'}},
            'q1_': {'0': {'q3_'}, '1': {'q4_'}, '2': {'q5_'}, '3': {'q6_'}, '4': {'q0_'}, '5': {'q1_'}, '6': {'q2_'},
                    '7': {'q3_'}, '8': {'q4_'}, '9': {'q5_'}},
            'q2': {'0': {'q2_', 'q6'}, '1': {'q2_', 'q0'}, '2': {'q2_', 'q1'}, '3': {'q2_', 'q2'}, '4': {'q2_', 'q3'},
                   '5': {'q2_', 'q4'}, '6': {'q2_', 'q5'}, '7': {'q2_', 'q6'}, '8': {'q2_', 'q0'}, '9': {'q2_', 'q1'}},
            'q2_': {'0': {'q6_'}, '1': {'q0_'}, '2': {'q1_'}, '3': {'q2_'}, '4': {'q3_'}, '5': {'q4_'}, '6': {'q5_'},
                    '7': {'q6_'}, '8': {'q0_'}, '9': {'q1_'}},
            'q3': {'0': {'q3_', 'q2'}, '1': {'q3_', 'q3'}, '2': {'q3_', 'q4'}, '3': {'q3_', 'q5'}, '4': {'q3_', 'q6'},
                   '5': {'q3_', 'q0'}, '6': {'q3_', 'q1'}, '7': {'q3_', 'q2'}, '8': {'q3_', 'q3'}, '9': {'q3_', 'q4'}},
            'q3_': {'0': {'q2_'}, '1': {'q3_'}, '2': {'q4_'}, '3': {'q5_'}, '4': {'q6_'}, '5': {'q0_'}, '6': {'q1_'},
                    '7': {'q2_'}, '8': {'q3_'}, '9': {'q4_'}},
            'q4': {'0': {'q4_', 'q5'}, '1': {'q4_', 'q6'}, '2': {'q4_', 'q0'}, '3': {'q4_', 'q1'}, '4': {'q4_', 'q2'},
                   '5': {'q4_', 'q3'}, '6': {'q4_', 'q4'}, '7': {'q4_', 'q5'}, '8': {'q4_', 'q6'}, '9': {'q4_', 'q0'}},
            'q4_': {'0': {'q5_'}, '1': {'q6_'}, '2': {'q0_'}, '3': {'q1_'}, '4': {'q2_'}, '5': {'q3_'}, '6': {'q4_'},
                    '7': {'q5_'}, '8': {'q6_'}, '9': {'q0_'}},
            'q5': {'0': {'q5_', 'q1'}, '1': {'q5_', 'q2'}, '2': {'q5_', 'q3'}, '3': {'q5_', 'q4'}, '4': {'q5_', 'q5'},
                   '5': {'q5_', 'q6'}, '6': {'q5_', 'q0'}, '7': {'q5_', 'q1'}, '8': {'q5_', 'q2'}, '9': {'q5_', 'q3'}},
            'q5_': {'0': {'q1_'}, '1': {'q2_'}, '2': {'q3_'}, '3': {'q4_'}, '4': {'q5_'}, '5': {'q6_'}, '6': {'q0_'},
                    '7': {'q1_'}, '8': {'q2_'}, '9': {'q3_'}},
            'q6': {'0': {'q6_', 'q4'}, '1': {'q6_', 'q5'}, '2': {'q6_', 'q6'}, '3': {'q6_', 'q0'}, '4': {'q6_', 'q1'},
                   '5': {'q6_', 'q2'}, '6': {'q6_', 'q3'}, '7': {'q6_', 'q4'}, '8': {'q6_', 'q5'}, '9': {'q6_', 'q6'}},
            'q6_': {'0': {'q4_'}, '1': {'q5_'}, '2': {'q6_'}, '3': {'q0_'}, '4': {'q1_'}, '5': {'q2_'}, '6': {'q3_'},
                    '7': {'q4_'}, '8': {'q5_'}, '9': {'q6_'}},
        },
        initial_state='qs',
        final_states={'q0', 'q0_'}
    )
    dfa = DFA.from_nfa(nfa)
    return dfa


def count_strings(dfa, n):
    # This function counts the number of accepting strings
    prev = {}
    cur = {}
    for state in dfa.states:
        prev[state] = 0
        cur[state] = 0
    for state in dfa.final_states:
        prev[state] = 1
    for i in range(n):
        for state in dfa.states:
            cur[state] = (prev[dfa.transitions[state]['0']] + prev[dfa.transitions[state]['1']] +
                          prev[dfa.transitions[state]['2']] + prev[dfa.transitions[state]['3']] +
                          prev[dfa.transitions[state]['4']] + prev[dfa.transitions[state]['5']] +
                          prev[dfa.transitions[state]['6']] + prev[dfa.transitions[state]['7']] +
                          prev[dfa.transitions[state]['8']] + prev[dfa.transitions[state]['9']])
        for state in dfa.states:
            prev[state] = cur[state]
    return cur[dfa.initial_state]


def main():
    n = int(input("Enter an integer for n between 1 and 100: "))
    if n < 1 or n > 100:
        print("The value of n must be >= 1 and <= 100")
        exit(1)
    print("There are", count_strings(build_dfa(), n), "integers of length", n, "that are weakly divisible by 7\n")
    exit(0)


main()
