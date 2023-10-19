grammar = {
    "E": [['T',"E'"]],
    "E'": [["+","T","E'"], ""],
    "T": [["F","T'"]],
    "T'": [["*","F","T'"], ""],
    "F": ["(E)", ["id"]]
}

nonterminal=["E","E'","T","T'","F"]
terminal=["id","(",")","*","+"]

parsing_table = {
    "E": {"id": ["T","E'"], 
          "(": ["T","E'"]},
    "E'": {"+": ["+","T","E'"], 
           ")": "", 
           "$": ""},
    "T": {"id": ["F","T'"], 
          "(": ["F","T'"]},
    "T'": {"+": "", 
           "*": ["*","F","T'"], 
           ")": "", 
           "$": ""},
    "F": {"id": ["id"], 
          "(": "(E)"}
}

def convert_to_token(s):
    i=0
    res=[]
    # print(s)
    while i<len(s):
        if  i<len(s)-1 and s[i]=="i" and s[i+1]=='d':
            res.append("id")
            i+=2
        elif s[i] in terminal:
            res.append(s[i])
            i+=1
        elif s[i] == " ":
            i+=1
        else:
            return None
    res.append("$")
    return res

stdv=27
space=15
def ll1_parsing(input_string):
    stack = ["$", "E"]
    input_string=convert_to_token(input_string)
    # print(input_string)
    derivation = []
    t="".join(input_string)
    t1=" ".join(stack[::-1])
    pp=""
    t2=""
    derivation.append(f"{t2: >{stdv-space}}"+f"{pp: <{space}}"+f"{t: >{stdv}}"+f"{t1: >{stdv}}")
    
    while stack and input_string:
        # print(stack,input_string)
        top = stack.pop()
        next_input = input_string[0]
        if top not in grammar:
            if top == next_input:
                input_string = input_string[1:]
                t="".join(input_string)
                t1=" ".join(stack[::-1])
                pp="match  "+top
                derivation.append(f"{t2: >{stdv-space}}"+f"{pp: <{space}}"+f"{t: >{stdv}}"+f"{t1: >{stdv}}")
            
            else:
                return None
        else:
            production = parsing_table[top].get(next_input)
            if production is not None:
                if production != "":
                    for symbol in reversed(production):
                        stack.append(symbol)
                t="".join(input_string)
                t1=" ".join(stack[::-1])
                pp="output "+str(top)+"->"+("".join(production) if production!="" else "ε")
                derivation.append(f"{t2: >{stdv-space}}"+f"{pp: <{space}}"+f"{t: >{stdv}}"+f"{t1: >{stdv}}")
            else:
                return None
    if not stack and not input_string:
        return derivation
    else:
        return None

input_string = "id+(id*id+id)*id"
derivation = ll1_parsing(input_string)
if derivation is not None:
    print(f"The input string {input_string} is accepted by the grammar.")
    print("The derivation steps are:")
    t2=""
    pp="ACTION"
    t="INPUT STRING"
    t1="STACK"
    print(f"{t2: >{stdv-space}}"+f"{pp: <{space}}"+f"{t: >{stdv}}"+f"{t1: >{stdv}}")
    print("-"*90)
    for step in derivation:
        print(step)
else:
    print(f"The input string {input_string} is rejected by the grammar.")
