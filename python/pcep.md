# PCEP interview questions based on the syllabus

- ## Q1. What is Python and why is it popular?

  - High-level, interpreted, dynamically typed; valued for simplicity and readability.
  - Key features: simple syntax, interpreted and portable, large standard library, OO and functional support, cross-platform.

- ## Q2. What is the difference between a compiler and an interpreter?

  - Compiler: translates entire code before execution (e.g., C, C++).
  - Interpreter: executes code line by line (e.g., Python, JavaScript).

- ## Q3. What are keywords in Python?

  - Reserved words with predefined meanings; cannot be used as identifiers.

- ## Q4. What are Python’s main features?

  - Interpreted, dynamically typed, object-oriented, portable, rich standard library.

- ## Q5. What is PEP 8?

  - Python’s style guide for naming and formatting readable code.

- ## Q6. Is python interpreted or compiled?

  - Source compiles to bytecode (.pyc) then the VM interprets it.

- ## Q7. Why is python considered dynamically typed?

  - Types are not declared on variables; decided at runtime.

- ## Q8. What is a variable and identifier in Python?

  - Variable: name referring to a value in memory. Identifier: name for entities like variables, functions, classes.

- ## Q9. Are variables typed in python?

  - Variables hold references and have no fixed type; objects have types.

- ## Q10. What happens when a python file is executed?

  - Code is parsed, compiled to bytecode, executed by the interpreter.

- ## Q11. What is script and module in python?

  - Script: run directly. Module: imported and reused.

- ## Q12. Why is indentation mandatory?

  - Defines blocks for functions, classes, conditionals, loops.

- ## Q13. SyntaxError vs RuntimeError?

  - SyntaxError: grammar issues. RuntimeError: occurs during execution from data/conditions.

- ## Q14. What does “everything in Python is an object” mean?

  - Even int/str/bool are objects from classes.

- ## Q15. What is id() in Python?

  - Returns an object’s memory reference (unique identifier).

  ```python
  x = 10
  print(id(x))
  ```

- ## Q16. Difference between is and ==?

  - == compares values; is compares identity (same object).

- ## Q17. What is immutability?

  - Immutable objects cannot change after creation; lists/dicts/sets are mutable, ints/floats/strs/tuples/bools are immutable.

- ## Q18. Why immutability matters?

  - Improves safety, predictability, and hashability.

- ## Q19. What is interning?

  - Python may reuse small immutable objects (e.g., small ints, some strings) to save memory.

- ## Q20. What happens when we do x = x + 1?

  - Creates a new int object; original is unchanged.

- ## Q21. Mutable vs Immutable types?

  - Mutable: list, dict, set. Immutable: int, float, str, tuple, bool, frozenset.

- ## Q22. Can a tuple contain mutable objects?

  - Yes; mutability belongs to the contained object, not the tuple.

  ```python
  t = (1, [2, 3])
  t[1].append(4)
  ```

- ## Q23. How are variables created in Python?

  - By assignment; dynamic typing (e.g., x = 10, name = "Alice").

- ## Q24. What are Python’s built-in data types?

  - Numeric: int, float, complex; Sequence: str, list, tuple, range; Mapping: dict; Set: set, frozenset; Boolean: bool; NoneType.

- ## Q25. How does Python handle input and output?

  - Input via input(); output via print().

  ```python
  name = input("Enter your name: ")
  print("Hello,", name)
  ```

- ## Q26. What is type casting in Python?

  - Converting types: int("5"), str(10), float(3).

- ## Q27. What is the difference between = and ==?

  - = assigns; == compares values.

- ## Q28. Difference between / and //?

  - / float division; // floor division.

- ## Q29. What does ** do?

  - Exponentiation: 2**3 = 8.

- ## Q30. What does += do?

  - Immutable: creates new value. Mutable: may modify in place.

- ## Q31. What are Python’s basic operators?

  - Arithmetic, comparison, logical, assignment, membership (in/not in), identity (is/is not).

- ## Q32. What is short-circuit evaluation?

  - Logical expressions stop once the result is known.

- ## Q33. What are Boolean values?

  - True and False.

- ## Q34. Explain conditional statements

  ```python
  if x > 10:
      print("Greater")
  elif x == 10:
      print("Equal")
  else:
      print("Smaller")
  ```

- ## Q35. Python has which conditional keywords?

  - if, elif, else.

- ## Q36. How does Python handle indentation?

  - Indentation defines blocks; no braces.

- ## Q37. What are loops in Python?

  - for iterates over a sequence; while repeats while a condition is true.

- ## Q38. for vs while?

  - for when iterating known items; while when condition-driven.

- ## Q39. Difference between break, continue, pass?

  - break exits loop; continue skips iteration; pass is a no-op placeholder.

- ## Q40. What does for x in range(5) do?

  - Iterates over 0,1,2,3,4.

- ## Q41. Explain bitwise operators

  - &: AND; |: OR; ^: XOR; ~: NOT; <<: left shift; >>: right shift.

- ## Q42. Bitwise operators example

  ```python
  5 & 3  # 1
  5 | 3  # 7
  5 ^ 3  # 6
  ~5     # -6
  5 << 1 # 10
  5 >> 1 # 2
  ```

- ## Q43. Explain lists and their common operations

  - Example: nums = [1, 2, 3]; nums.append(4); nums.remove(2); nums.sort().
  - Common methods: append, insert, remove, pop, sort, reverse, count, len.

- ## Q44. What is list slicing?

  - Access sublists with [start:end:step].

  ```python
  nums = [10, 20, 30, 40, 50]
  print(nums[1:4])
  ```

- ## Q45. What is list comprehension?

  - Concise list creation: [x*x for x in range(5)].

- ## Q46. Define a function in Python

  ```python
  def greet(name):
      return f"Hello {name}"
  ```

- ## Q47. How do you define and call a function?

  ```python
  def add(a, b):
      return a + b

  print(add(3, 4))
  ```

- ## Q48. Explain local and global variables

  - Assignment inside a function is local unless declared global; globals live at module level.

- ## Q49. What are default arguments?

  - Parameters with preset values.

- ## Q50. Why avoid mutable default arguments?

  - Default is created once; mutations persist across calls.

- ## Q51. What is *args and **kwargs?

  - *args collects positional extras; **kwargs collects keyword extras.

- ## Q52. What is recursion?

  - A function calling itself.

- ## Q53. Why can recursion be slow in Python?

  - Call overhead and recursion depth limit.

- ## Q54. How to optimize recursive functions?

  - Memoization or converting to iteration.

- ## Q55. What are tuples? How different from lists?

  - Tuples are immutable sequences using (); lists are mutable using [].

- ## Q56. What is a dictionary?

  - Key-value mapping.

  ```python
  person = {"name": "John", "age": 25}
  print(person["name"])
  ```

- ## Q57. How do you iterate through a dictionary?

  ```python
  for key, value in person.items():
      print(key, value)
  ```

- ## Q58. What is None in Python?

  - Represents no value / null.

- ## Q59. What are lambda functions?

  - Anonymous single-line functions, e.g., square = lambda x: x * x.

- ## Q60. What are common data processing functions?

  - len, sum, max, min, sorted, map, filter, zip.

- ## Q61. Explain map() and filter()

  ```python
  nums = [1, 2, 3, 4]
  squares = list(map(lambda x: x*x, nums))
  evens = list(filter(lambda x: x % 2 == 0, nums))
  ```

- ## Q62. What are docstrings?

  - String literals documenting functions/classes.

- ## Q63. How do you handle exceptions?

  ```python
  try:
      risky_code()
  except ValueError:
      handle()
  ```

- ## Q64. What is finally used for?

  - Always runs for cleanup.

- ## Q65. How to raise custom exceptions?

  ```python
  class MyError(Exception):
      pass

  raise MyError("Something went wrong")
  ```

- ## Q66. Difference between Exception and BaseException?

  - BaseException is the root (includes SystemExit, KeyboardInterrupt); catch Exception in user code.

- ## Q67. What is exception propagation?

  - Unhandled exceptions bubble up to the caller.

- ## Q68. What is variable shadowing?

  - A local variable hides a global variable with the same name.

- ## Q69. Explain LEGB rule

  - Lookup order: Local, Enclosing, Global, Built-in.

- ## Q70. Pure function vs impure function?

  - Pure: no side effects. Impure: modifies external state.

- ## Q71. How does Python manage memory?

  - Reference counting plus cyclic garbage collector.

- ## Q72. How does Python call stack work?

  - Each function call creates a new stack frame.

- ## Q73. How does Python handle parameter passing?

  - Pass-by-object-reference: the reference to the object is passed.

- ## Q74. What is a frame object?

  - Holds execution state: locals, instruction pointer, etc.

- ## Q75. What is a code object?

  - Compiled bytecode representation of Python code.

- ## Q76. How to view bytecode?

  ```python
  import dis
  dis.dis(func)
  ```

- ## Q77. What is the GIL?

  - A mutex allowing only one thread to execute Python bytecode at a time.

- ## Q78. When does GIL matter?

  - Hurts CPU-bound threading; I/O-bound threading is less impacted.

- ## Q79. How to bypass GIL?

  - Use multiprocessing, C extensions, Numba, or PyPy.

- ## Q80. What is duck typing?

  - Behavior-based typing: if it quacks like a duck, treat it as a duck.

- ## Q81. Explain dynamic dispatch

  - Method chosen at runtime based on the object's type.

- ## Q82. Check if a number is prime

  ```python
  num = int(input("Enter a number: "))
  for i in range(2, num):
      if num % i == 0:
          print("Not Prime")
          break
  else:
      print("Prime")
  ```

- ## Q83. Reverse a string

  ```python
  def reverse(s):
      return s[::-1]
  ```

- ## Q84. Count vowels in a string

  ```python
  s = input("Enter string: ")
  count = sum(1 for ch in s if ch.lower() in "aeiou")
  print("Vowels:", count)
  ```
