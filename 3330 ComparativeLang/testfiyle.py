class DFA:
    current_state = None;
    def __init__(self, states, alphabet, nextState, startState, acceptStates):
        self.states = states;
        self.alphabet = alphabet;
        self.nextState = nextState;
        self.startState = startState;
        self.acceptStates = acceptStates;
        self.currentState = startState;
        return;
    
    def nextInput(self, i):
        if ((self.currentState, i) not in self.nextState.keys()):
            self.currentState = None;
            return;
        self.currentState = self.nextState[(self.currentState, i)];
        return;
    
    def in_accept_state(self):
        return self.currentState in acceptStates;
    
    def go_to_initial_state(self):
        self.currentState = self.startState;
        return;
    
    def runString(self, List):
        self.go_to_initial_state();
        for inp in List:
            self.nextInput(inp);
            continue;
        return self.in_accept_state();
    pass;



states = {'a', 'b', 'c', 'd', 'e', 'f'};
alphabet = {'0', '1'};

tf = dict();
tf[('a', '0')] = 'a';
tf[('a', '1')] = 'b';
tf[('b', '0')] = 'c';
tf[('b', '1')] = 'e';
tf[('c', '0')] = 'e';
tf[('c', '1')] = 'd';
tf[('d', '0')] = 'f';
tf[('d', '1')] = 'b';
tf[('e', '0')] = 'e';
tf[('e', '1')] = 'e';
tf[('f', '0')] = 'f';
tf[('f', '1')] = 'f';
startState = 'a';
acceptStates = {'f'};

dL = input("Enter input string with values 0's and 1's : ")

d = DFA(states, alphabet, tf, startState, acceptStates);

print(d.runString(dL));
