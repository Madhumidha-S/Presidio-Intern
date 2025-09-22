# Recursion - Complete Notes

### 1. What Is Recursion?

- A programming technique where a function **calls itself** to solve a problem.
- The problem is broken down into **smaller, similar subproblems** until reaching a simplest form (base case) which can be solved directly.

### 2. Key Components of Recursion

- **Base Case** - Terminates the recursion; smallest instance of the problem.  
  Without a correct base case, recursion can run forever.
- **Recursive Case** - Defines how the problem is reduced toward the base case.

### 3. How Recursion Works (Mechanics)

- Uses a **call stack**: each recursive call pushes onto stack; on reaching base case, returns unwind in LIFO order.
- Local variables are separate in each invocation.

### 4. Examples of Recursive Functions

- **Factorial**  
  `fact(n) = n * fact(n-1)` with `fact(0) = 1` as base case.
- **Fibonacci**  
  `fib(n) = fib(n-1) + fib(n-2)` with `fib(0)=0, fib(1)=1` as base cases.
- **GCD (Euclidean algorithm)**  
  `GCD(a, b) = GCD(b, a mod b)` with base case `b = 0`.
- **Common algorithmic/DS problems**  
  Tree traversals, binary search, reverse a list/array, Tower of Hanoi, permutations, etc.

### 5. Recursion vs Iteration

**Recursion** - A function calls itself within its own definition to solve a problem.
**Iteration** - A block of code is repeatedly executed using loops

### 6. Common Patterns & Techniques

- **Tail Recursion**
- **Memoization / Caching**
- **Divide & Conquer**
- **Backtracking**

### 7. When to Use Recursion

- When problems naturally divide into identical smaller subproblems (divide & conquer).
- When working with recursive data structures (trees, graphs) or hierarchical structures.
- When code clarity and expressiveness are more important than minimal overhead.
