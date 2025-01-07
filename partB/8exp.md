### **Detailed Explanation of the Resolution-Based Program**

This Python program implements **Resolution** for propositional logic to check the satisfiability of a set of clauses. The resolution method is used in automated theorem proving, specifically for propositional logic. It attempts to derive a contradiction by combining pairs of clauses and checking for an empty clause, which indicates unsatisfiability.

The program uses the `sympy` library, specifically `symbols`, `Not`, and `Or`, for representing logical expressions and performing logical operations.

### **Key Concepts**

- **Clause**: A clause is a disjunction (OR) of literals (variables or their negations).
- **Literal**: A literal is either a variable or its negation (e.g., `p` or `¬p`).
- **Resolution**: The resolution rule allows you to combine two clauses that contain complementary literals (e.g., `p` and `¬p`) to form a new clause by removing the complementary literals and combining the remaining literals.

### **Program Breakdown**

#### **1. Importing Required Functions**

```python
from sympy import symbols, Not, Or, simplify
```

- **`symbols`**: This is used to create propositional variables (e.g., `p`, `q`).
- **`Not`**: Represents the negation (¬) of a symbol.
- **`Or`**: Represents the logical OR (disjunction) of two or more expressions.
- **`simplify`**: A utility to simplify logical expressions (though it's not directly used in this program).

#### **2. `resolve` Function**

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

- **Purpose**: The `resolve` function is used to apply the resolution rule to two clauses (`clause1` and `clause2`).
- **Steps**:
  1. **Iterate through all literals in `clause1` and `clause2`**:
     - It checks for complementary literals (e.g., `p` and `¬p`).
     - If `literal1` is the negation of `literal2` or vice versa, the resolution rule applies.
  2. **Combine the remaining literals**: Once complementary literals are found and removed, the remaining literals from both clauses are combined to form the `resolvent`.
  3. **Return a simplified resolvent**: A set is used to remove duplicates, and the set is converted back to a list to return a unique list of literals.

#### **3. `resolution` Function**

```python
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
```

- **Purpose**: The `resolution` function applies the resolution rule to a set of clauses until a contradiction (an empty clause) is found, or no further resolution can be made.
- **Steps**:
  1. **Copy Clauses**: It starts by copying the initial set of clauses into `new_clauses`.
  2. **Loop for Resolution**: It repeatedly tries to resolve pairs of clauses until either:
     - A contradiction (empty clause) is found, or
     - No new clauses can be inferred.
  3. **Generate Pairs**: It generates all possible pairs of clauses using a double loop:
     - `pairs.append((new_clauses[i], new_clauses[j]))` adds pairs of clauses to be resolved.
  4. **Resolve Pairs**: For each pair of clauses, it applies the `resolve` function to obtain a `resolvent`:
     - If the `resolvent` is empty, it means a contradiction is found, and the function returns `True`, indicating that the set of clauses is **unsatisfiable**.
     - If the `resolvent` is non-empty and is not already in `new_clauses`, it is added to `new_clauses` for further resolution.
  5. **Stopping Condition**: If no new clauses are added (`n == len(new_clauses)`), it means no further resolution can be made, and the function returns `False`, indicating that the set of clauses is **satisfiable**.

#### **4. Main Program Block**

```python
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
```

- **Purpose**: The main program sets up the clauses, invokes the resolution process, and prints whether the clauses are satisfiable or unsatisfiable.
- **Steps**:
  1. **Define Clauses**: Three clauses are created:
     - `c1`: `p OR ¬q`
     - `c2`: `¬p OR q`
     - `c3`: `¬p OR ¬q`
  2. **Resolution**: The `resolution` function is called with the set of clauses. It attempts to find a contradiction by applying the resolution rule.
  3. **Check Result**: If the resolution function returns `True` (a contradiction is found), the program prints "the set of clauses is unsatisfiable". Otherwise, it prints "the set of clauses is satisfiable".

### **Output Example**

The program may print the following output during the resolution process:

```plaintext
[ [P, ~Q], [~P, Q], [~P, ~Q] ]

[P, ~Q]
[~P, Q]
[P, ~Q] : then [Q]
[P, ~Q]
[~P, ~Q]
[~P, ~Q] : then []
Found contradiction, returning True
```

Finally, the program will output:

```plaintext
the set of clauses is unsatisfiable(contradiction found)
```

This means that a contradiction was found, and therefore the set of clauses is unsatisfiable.

---

### **Key Concepts of Resolution**:

- **Complementary Literals**: The core idea of the resolution rule is to identify complementary literals (e.g., `p` and `¬p`) and resolve them to produce a new clause containing the remaining literals.
- **Contradiction (Empty Clause)**: If, during the resolution process, an empty clause is generated, it means that the clauses are unsatisfiable because we have derived a contradiction (both `p` and `¬p` are required, which is impossible).
- **Satisfiability**: If no contradiction is found after attempting all possible resolutions, the clauses are satisfiable, meaning there is a combination of truth assignments that make all clauses true.

### **Time Complexity**:

- The time complexity depends on the number of clauses and the resolution steps required. In the worst case, the number of pairs of clauses grows quadratically, leading to a **O(n^2)** complexity for finding all possible pairs, where `n` is the number of clauses.

### **Space Complexity**:

- The space complexity is mainly determined by the number of clauses stored during the resolution process, which is **O(n)**, where `n` is the number of clauses.
