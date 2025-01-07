class ForwardChaining: 

    def __init__(self):
        self.facts = set() 
        self.rules = [] 

    def add_fact(self, fact): 
        self.facts.add(fact) 
    
    def add_rule(self, condition, conclution): 
        self.rules.append((condition, conclution)) 

    def infer(self): 
        new_facts = True 
        while new_facts: 
            new_facts = False 
            for condition, conclution in self.rules: 
                if condition.issubset(self.facts) and \
                    conclution not in self.facts: 
                    print(f"applying {condition} : then {conclution}")
                    self.facts.add(conclution) 
                    new_facts = True 
            
    def get_facts(self): 
        return self.facts 
    
if __name__ == "__main__": 
    fc = ForwardChaining() 

    # add facts 
    fc.add_fact("fever") 
    fc.add_fact("cough") 

    fc.add_rule({"fever", "cough"}, "possible flu")
    fc.add_rule({"fever"}, "possible infection") 
    fc.add_rule({"cough"}, "possible bronchitis")

    fc.infer() 

    print("final diagnosis:")
    for res in fc.get_facts(): 
        print(res)