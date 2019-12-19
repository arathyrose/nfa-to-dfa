import json


def generatePowerSet(given_set, no_of_elements):
    pow_set_size = (int)(pow(2, no_of_elements))
    power_set = list()
    for counter in range(0, pow_set_size):    # Run the counter from 000..0 to 111..1
        each_element = list()
        for j in range(0, no_of_elements):
            # Check if jth bit in the counter is set and then append it to the given_set
            if((counter & (1 << j)) > 0):
                each_element.append(given_set[j])
        power_set.append(each_element)  # append the given_set to the power set
    return power_set


def final_set_generator(set1, set2):
    # find all those elements in set1 containing some of the elements in set2
    finale = list()
    for i in set1:
        # if intersection of i and set2 is not NULL
        if([value for value in i if value in set2] != []):
            finale.append(i)
    return finale


def op_for(initial_state, t_func, input):
    # finds the union of the outputs of each element in initial_state for given input
    ans = list()
    for i in t_func:
        if(i[1] == input):
            if(i[0] in initial_state):
                ans = list(set(ans) | set(i[2]))
    return ans


def generate_t_func_dfa(t_func_nfa, alphabet, all_states_dfa):
    t_func_dfa = list()
    for i in all_states_dfa:
        for j in alphabet:
            p = list()
            p.append(i)  # starting state
            p.append(j)  # input character
            p.append(op_for(i, t_func_nfa, j))  # next state
            t_func_dfa.append(p)
    return t_func_dfa


if __name__ == "__main__":
    nfa = dict()
    with open('input.json', 'r') as f:  # load the NFA from the file
        nfa = json.load(f)
    # print(nfa)
    dfa = dict()  # Initialise dfa as an empty dictionary
    # Number of states in a DFA is 2^number of states of an NFA
    dfa["states"] = pow(2, nfa["states"])
    # Both NFA and DFA follow the same alphabet
    dfa["letters"] = nfa["letters"]
    all_states_dfa = generatePowerSet(
        list(range(0, nfa["states"])), nfa['states'])  # The states of the DFA is the power set of all the states of the NFA.
    dfa["t_func"] = generate_t_func_dfa(
        nfa["t_func"], nfa["letters"], all_states_dfa)
    dfa["start"] = [nfa["start"]]  # Both have the same start state.
    dfa["final"] = final_set_generator(all_states_dfa, nfa["final"])
    # print(dfa)
    with open('output.json', 'w') as outfile:
        json.dump(dfa, outfile, indent=2)

    """ with open('output_check.json', 'r') as f:  # load the DFA to test from the file
        dfa_check = json.load(f)
    print(dfa["states"]==dfa_check["states"])
    print(dfa["letters"]==dfa_check["letters"])
    print(dfa["start"]==dfa_check["start"])
    print(sorted(dfa["final"])==sorted(dfa_check["final"]))
    print(sorted(dfa["t_func"])==sorted(dfa_check["t_func"])) """
