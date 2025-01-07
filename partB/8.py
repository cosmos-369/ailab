from sympy import symbols, Not, Or, simplify 

def resolve(clause1, clause2): 
    resolvent = [] 
    for literal1 in clause1: 
        for literal2 in clause2: 
            if literal1 == Not(literal2) or literal2 == Not(literal1): 
                for i in (clause1 + clause2): 
                    if i != literal1 and i != literal2: 
                        resolvent.append(i) 
    return list(set(resolvent))

def resolution(clauses): 
    new_clauses = list(clauses) 
    while True: 
        n = len(new_clauses) 
        print(new_clauses) 
        print(" ") 
        # create pairs 
        pairs = [] 
        for i in range(n): 
            for j in range(i+1, n): 
                pairs.append((new_clauses[i], new_clauses[j])) 
        
        for c1, c2 in pairs: 
            print(c1) 
            print(c2) 

            resolvent = resolve(c1, c2)
            print(resolvent) 
            print() 

            if not resolvent: 
                return True 
            
            if resolvent not in new_clauses: 
                new_clauses.append(resolvent) 

        if n == len(new_clauses): 
            return False

if __name__ == "__main__":
    # p   !q 
    # !p   q 
    # !p  !q 
    c1 = [symbols('P'), Not(symbols('Q'))]
    c2 = [Not(symbols('P')), symbols('Q')]
    c3 = [Not(symbols('P')), Not(symbols('Q'))]

    clauses = [c1, c2, c3]
    result = resolution(clauses) 
    if not result: 
        print("the set of clauses is unsatifiable(contradiction found)") 
    else: 
        print("the set of clauses is satisfiable") 

    