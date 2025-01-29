### **Explanation of the Resolution Algorithm for Propositional Logic in Python**

This program implements the **Resolution Algorithm** to check if a given set of clauses is **satisfiable** (i.e., does not lead to a contradiction) or **unsatisfiable** (i.e., contains a contradiction). 

It follows the **Principle of Resolution** in **Propositional Logic**, which is used in **Automated Theorem Proving (ATP) and Artificial Intelligence (AI)**.

---

## **1. Understanding the Components**

### **1.1 Clause Representation**
Each clause is represented as a **list of literals**, where:
- **Positive literals** are represented using `symbols()`
- **Negated literals** are represented using `Not(symbols())`

For example:
```python
c1 = [symbols('P'), Not(symbols('Q'))]  # (P OR ¬Q)
c2 = [Not(symbols('P')), symbols('Q')]  # (¬P OR Q)
c3 = [Not(symbols('P')), Not(symbols('Q'))]  # (¬P OR ¬Q)
```
These clauses are stored in a **list**, forming the knowledge base.

---

### **1.2 Resolving Two Clauses (`resolve` function)**
```python
def resolve(clause1, clause2): 
    resolvent = [] 
    for literal1 in clause1: 
        for literal2 in clause2: 
            if literal1 == Not(literal2) or literal2 == Not(literal1): 
                for i in (clause1 + clause2): 
                    if i != literal1 and i != literal2: 
                        resolvent.append(i) 
    return list(set(resolvent))
```
This function **performs the resolution step** by:
1. **Finding complementary literals**: If one clause has `P` and another has `¬P`, they can be resolved.
2. **Merging the two clauses** while eliminating the complementary literals.
3. **Returning the new resolvent clause**.

Example:
- Clause 1: `P OR ¬Q`
- Clause 2: `¬P OR Q`
- Resolvent: `¬Q OR Q`, which simplifies to `[]` (empty clause, contradiction).

---

### **1.3 The Resolution Process (`resolution` function)**
```python
def resolution(clauses): 
    new_clauses = list(clauses) 
    while True: 
        n = len(new_clauses) 
        print(new_clauses) 
        print(" ") 

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
                return True  # Found a contradiction
            
            if resolvent not in new_clauses: 
                new_clauses.append(resolvent) 

        if n == len(new_clauses): 
            return False  # No new clauses found, problem is satisfiable
```

The **resolution loop**:
1. **Generates all possible clause pairs**.
2. **Resolves each pair** to produce a new clause.
3. **Checks if an empty clause (`[]`) is generated**, indicating a contradiction.
4. **If no new clauses are generated**, it concludes that the set of clauses is **satisfiable**.

---

## **2. Running the Program (`__main__`)**
```python
if __name__ == "__main__":
    c1 = [symbols('P'), Not(symbols('Q'))]  # (P OR ¬Q)
    c2 = [Not(symbols('P')), symbols('Q')]  # (¬P OR Q)
    c3 = [Not(symbols('P')), Not(symbols('Q'))]  # (¬P OR ¬Q)

    clauses = [c1, c2, c3]
    result = resolution(clauses) 
    if result: 
        print("The set of clauses is unsatisfiable (contradiction found)") 
    else: 
        print("The set of clauses is satisfiable") 
```

### **Step-by-Step Execution**
1. **Initialize clauses**:
   ```
   c1 = (P OR ¬Q)
   c2 = (¬P OR Q)
   c3 = (¬P OR ¬Q)
   ```
2. **Resolution Process**:
   - Resolve `(P OR ¬Q)` and `(¬P OR Q)` → `¬Q OR Q` → contradiction (`[]`).
3. **Since a contradiction is found**, the set of clauses is **unsatisfiable**.

### **Output**
```
The set of clauses is unsatisfiable (contradiction found)
```
This means that the given set of clauses **contains a logical inconsistency**.

---

## **3. Summary**
- **What does this program do?**
  - Implements the **resolution principle** to determine whether a set of logical clauses is **satisfiable** or **contains a contradiction**.
  
- **How does it work?**
  - The **resolve function** eliminates complementary literals to form new clauses.
  - The **resolution function** repeatedly resolves clause pairs, checking for an empty clause (`[]`), which indicates a contradiction.
  
- **Key takeaway**
  - If an empty clause is derived → **Contradiction found → The system is unsatisfiable**.
  - Otherwise, the system is **satisfiable**.

This program is useful in **automated theorem proving, AI, and logic-based reasoning systems**. 🚀
