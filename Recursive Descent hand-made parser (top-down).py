epsilon="ε"

constant="id"

tree=[]

stdv=24

def tp(dash=0):
    return "".join(tree)

def E(end = 0):
    global cursor
    print(f"{cursor: <{stdv}}"+tp(end)+"E -> T E'")
    try:
        tree.pop()
        tree.append("|  ")
    except:
        pass
    if end:
        tree.pop()
        tree.append("   ")
    tree.append("|--")
    if T(0):
        tree.pop()
        tree.append("|--")
        if Edash(1):
            try:
                tree.pop()
            except:
                pass
            return True
        else:
            return False
    else:
        return False

def Edash(end=0):
    global cursor
    if cursor and cursor[0] == '+':
        print(f"{cursor: <{stdv}}"+tp(end)+"E' -> + T E'")
        tree.pop()
        tree.append("|  ")
        if end:
            tree.pop()
            tree.append("   ")
        tree.append("|--")

        cursor = cursor[1:]
        if T(0):
            tree.pop()
            tree.append("|--")
            if Edash(1):
                tree.pop()
                return True
            else:
                return False
        else:
            return False
    else:
        print(f"{cursor: <{stdv}}"+tp(end)+"E' -> "+epsilon)
        tree.pop()
        tree.append("|  ")
        if end:
            tree.pop()
            tree.append("   ")
        return True

def T(end=0):
    global cursor
    print(f"{cursor: <{stdv}}"+tp(end)+"T -> F T'")
    tree.pop()
    tree.append("|  ")
    if end:
        tree.pop()
        tree.append("   ")
    tree.append("|--")
    if F(0):
        tree.pop()
        tree.append("|--")
        if Tdash(1):
            tree.pop()
            return True
        else:
            return False
    else:
        return False

def Tdash(end=0):
    global cursor
    if cursor and cursor[0] == '*':
        print(f"{cursor: <{stdv}}"+tp(end)+"T' -> * F T'")
        tree.pop()
        tree.append("|  ")
        if end:
            tree.pop()
            tree.append("   ")
        tree.append("|--")
        cursor = cursor[1:]
        if F(0):
            tree.pop()
            tree.append("|--")
            if Tdash(1):
                tree.pop()
                return True
            else:
                return False
        else:
            return False
    else:
        print(f"{cursor: <{stdv}}"+tp(end)+"T' -> "+epsilon)
        tree.pop()
        tree.append("|  ")
        if end:
            tree.pop()
            tree.append("   ")
        return True

def F(end=0):
    global cursor
    if cursor and cursor[0] == '(':
        print(f"{cursor: <{stdv}}"+tp(end)+"F -> ( E )")
        tree.pop()
        tree.append("|  ")
        if end:
            tree.pop()
            tree.append("   ")
        tree.append("|--")
        cursor = cursor[1:]
        if E(1):
            if cursor and cursor[0] == ')':
                cursor = cursor[1:]
                tree.pop()
                return True
            else:
                return False
        else:
            return False
    elif len(cursor)>=2 and cursor[0:2] == constant:
        print(f"{cursor: <{stdv}}"+tp(end)+"F -> "+constant)
        tree.pop()
        tree.append("|  ")
        if end:
            tree.pop()
            tree.append("   ")
        cursor = cursor[2:]
        return True
    else:
        return False

if __name__ == "__main__":
    print("Enter the string")
    # input_string="(id+id*id+(id+id))*id"
    input_string=input()
    cursor = input_string
    print("")
    print("Input                   Action")
    print("--------------------------------")
    if E() and not cursor:
        print("--------------------------------")
        print("String is successfully parsed")
    else:
        print("--------------------------------")
        print("Error in parsing String")
