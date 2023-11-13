class Parser:
    def __init__(self, grammar):
        self.grammar = grammar
        self.actions = {}
        self.gotos = {}

    def parse(self, tokens):
        stack = [0]
        symbol_stack = []
        stdv=27
        space=20
        space2=20
        t2=""
        pp="Stage Stack"
        t="Symbol Stack"
        t1="Input String"
        print(f"{t2: >{stdv-space}}"+f"{pp: <{space}}"+f"{t2: >{stdv-space2}}"+f"{t: <{space2}}"+f"{t1: >{stdv}}")
        print("-"*90)

        while True:
            pp=" ".join(map(str,stack))
            t =" ".join(symbol_stack)
            t1="".join(tokens)
            print(f"{t2: >{stdv-space}}"+f"{pp: <{space}}"+f"{t2: >{stdv-space2}}"+f"{t: <{space2}}"+f"{t1: >{stdv}}")
            state = stack[-1]
            symbol = tokens[0]
            if state in self.actions and symbol in self.actions[state]:
                action = self.actions[state][symbol]
                if action[0] == 's':
                    stack.append(int(action[1:]))
                    symbol_stack.append(tokens.pop(0))
                elif action[0] == 'r':
                    rule = self.grammar[int(action[1:])]
                    for _ in range(len(rule[1])):
                        stack.pop()
                        symbol_stack.pop()
                    state = stack[-1]
                    stack.append(self.gotos[state][rule[0]])
                    symbol_stack.append(rule[0])
                elif action == 'acc':
                    return True
            else:
                return False


grammar={
    1: ('E', ['T',"E'"]),
    2: ("E'", ['+','T',"E'"]),
    3: ("E'", []),
    4: ('T', ['F',"T'"]),
    5: ("T'", ['*','F',"T'"]),
    6: ("T'", []),
    7: ('F', ['(','E',')']),
    8: ('F', ['id'])
}


parser = Parser(grammar)


parser.actions ={
    0: {'(': 's4', 'id': 's5'}, 
    1: {'$': 'acc'}, 
    2: {'+': 's7', '$': 'r3', '*' : 'r3'}, 
    3: {'*': 's9', '+': 'r6', ')': 'r6', '$': 'r6'}, 
    4: {'(': 's4', 'id': 's5'}, 
    5: {'*': 'r8', '+': 'r8', ')': 'r8', '$': 'r8'}, 
    6: {'$': 'r1'}, 
    7: {'(': 's4', 'id': 's5'}, 
    8: {'+': 'r4',')':'r4','$':'r4'}, 
    9: {'(': 's4', 'id': 's5'}, 
    10:{')': 's14'}, 
    11:{'+': 's16', ')': 'r3'}, 
    12:{'+': 's7', '$': 'r3'}, 
    13:{'*': 's9', '+': 'r6','$':'r6',')':'r6'}, 
    14:{'*': 'r7', '$': 'r7',')':'r7','+':'r7'}, 
    15:{')': 'r1'}, 
    16:{'(': 's4', 'id': 's5'}, 
    17:{'$': 'r2'}, 
    18:{'+': 'r5','$': 'r5',')':'r5'}, 
    19:{'+': 's16', ')': 'r3'}, 
    20:{')': 'r2'}
}

parser.gotos ={
    0: {'E': 1, 'T': 2, 'F': 3},
    2: {"E'": 6},
    3: {"T'": 8},
    4: {'E': 10, 'T': 11, 'F': 3},
    7: {'T': 12, 'F': 3},
    9: {'F': 13},
    11:{"E'": 15},
    12:{"E'": 17},
    13:{"T'": 18},
    16:{'T': 19, 'F': 3},
    19:{"E'": 20}
}

tokens = "id * ( id + id * id ) id".split(" ")+['$']
print(tokens)
print("Accepted by the grammer? - ",parser.parse(tokens)) # prints True
