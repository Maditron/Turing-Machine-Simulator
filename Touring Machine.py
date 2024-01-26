import os

class TuringMachine():
    
    def __init__(self, Q, sigma, symbols, delta, F, tape):
        self.Q = Q
        self.sigma = sigma
        self.symbols = symbols
        self.F = F
        self.delta = delta
        self.tape = tape
        self.current_state = Q[0]
        i = 0
        while tape[i] == 'blank': 
            i += 1
        self.head = i

    def run(self):
        while f'{self.current_state}{self.tape[self.head]}' in self.delta:
            self.current_state, input, dir = self.delta[f'{self.current_state}{self.tape[self.head]}']
            self.tape[self.head] = input
            if dir == 'R': self.head += 1
            else: self.head -= 1


    def interpreter(self):
        self.run()
        return self.tape


    def acceptor(self):
        self.run()
        if self.current_state in self.F:
            return True
        return False




def anbn_acceptor(word):
    print('--------------------------------anbn acceptor-----------------------------')
    Q = ['q0','q1','q2','q3','q4']
    sigma = ['a','b']
    symbols = ['a','b','x','y', 'blank']
    F = 'q4'
    delta = {'q0a':['q1','x','R'], 'q1a':['q1','a','R'], 'q1y':['q1','y','R'], 'q1b':['q2','y','L'], 'q2y':['q2','y','L'],
            'q2a':['q2','a','L'], 'q2x':['q0','x','R'], 'q0y':['q3','y','R'], 'q3y':['q3','y','R'], 'q3blank':['q4','blank','L']}
    tape = []
    tape.append('blank')
    for w in word:
        tape.append(w)
    tape.append('blank')
    tm = TuringMachine(Q,sigma,symbols,delta,F,tape)
    if tm.acceptor() == False:
        print(f'{word} not accepted')
        print('------------------------------------------------------------------')
    else:
        print(f'{word} accepted')
        print('------------------------------------------------------------------')
    return


def sum(input):
    print('--------------------------------sum operation-----------------------------')
    n1, n2 = input.split('+')
    try:
        n1 = int(n1); n2 = int(n2)
    except:
        print('wrong input!! Try again')
        return
    tape = []
    tape.append('blank')
    for i in range(n1):
        tape.append(1)
    tape.append(0)
    for i in range(n2):
        tape.append(1)
    tape.append('blank')
    Q = ['q0','q1','q2','q3','q4']
    sigma = ['0','1']
    symbols = ['0','1', 'blank']
    F = 'q4'
    delta = {
        'q01':['q0',1,'R'], 'q00':['q1',1,'R'], 'q11':['q1',1,'R'], 'q1blank':['q2','blank','L'], 'q21':['q3',0,'L'],
        'q31':['q3',1,'L'], 'q3blank':['q4','blank','R']
    }
    tm = TuringMachine(Q,sigma,symbols,delta,F,tape)
    output = tm.interpreter()
    s = 0
    for i in output:
        if i == 1 or i == '1':
            s += 1
    print(f'the result of operation: {s}')
    print('------------------------------------------------------------------')




def menu():
    acceptors = [anbn_acceptor]
    acceptors_str = ['anbn_acceptor']
    interpreters = [sum]
    interpreters_str = ['sum', 'multiplication']
    while True:
        print('1. acceptor')
        print('2. interpreter')
        print('3. Exit')
        num = input('hi, choose the operation by Turing Machine: ')
        if num == '3':
            print('Goodbye')
            break
        print('------------------------------------------------------------------')
        if num == '1':
            for i in range(len(acceptors)):
                print(f'{i+1}. {acceptors_str[i]}')
            print(f'{i+2}. ...')
            try:
                acceptor = int(input('choose your acceptor: '))
                word = input('write your word: ')
                acceptors[acceptor-1](word)
            except:
                print('wrong input!!!!!! Try again')
                continue
        elif num == '2':
            for i in range(len(interpreters)):
                print(f'{i+1}. {interpreters_str[i]}')
            print(f'{i+2}. ...')
            try:
                interpreter = int(input('choose your interpreter: '))
                word = input('enter your input ex(2+3): ')
                interpreters[interpreter-1](word)
            except:
                print('something went wrong!!! Try again')
                continue
        else:
            print('wrong input!!!!!! Try again')
            continue



menu()