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
    
    def validAcceptState(self):
        return self.currentState in acceptStates;
    
    def start(self):
        self.currentState = self.startState;
        return;
    
    def runString(self, List):
        self.start();
        for inp in List:
            self.nextInput(inp);
            continue;
        return self.validAcceptState();
    pass;



states = {'a', 'b', 'c', 'd', 'e', 'f'};
alphabet = {'0', '1'};

dfa = dict();
dfa[('a', '0')] = 'a';
dfa[('a', '1')] = 'b';
dfa[('b', '0')] = 'c';
dfa[('b', '1')] = 'e';
dfa[('c', '0')] = 'e';
dfa[('c', '1')] = 'd';
dfa[('d', '0')] = 'f';
dfa[('d', '1')] = 'b';
dfa[('e', '0')] = 'e';
dfa[('e', '1')] = 'e';
dfa[('f', '0')] = 'f';
dfa[('f', '1')] = 'f';

startState = 'a';
acceptStates = {'f'};

dL = input("Enter input string with values 0's and 1's : ")
for i in range(0, len(dL)):
        if dL[i] > '1' or dL[i] < '0' :
            print("You've entered an invalid alphabet string. Only 0's and 1's please.")
            exit()
        else:
            continue
d = DFA(states, alphabet, dfa, startState, acceptStates);
if d.runString(dL) :
    print("Your string was accepted in the DFA!")
else:
    print("Your string was not accepted in the DFA!")
