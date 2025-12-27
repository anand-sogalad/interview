# PCAP interview questions based on the syllabus

- ## Q1. What is a module in Python?

  - A module is a reusable .py file containing code (functions, variables, classes) that can be imported.

- ## Q2. What is the difference between a module and a package?

  - Module: single .py file. Package: directory of modules containing an __init__.py file.

- ## Q3. Why use __init__.py?

  - Marks a directory as a package and can control import behavior or run initialization code.

- ## Q4. How do you import modules in Python?

  - import math
  - from math import sqrt
  - from math import pi as PI

- ## Q5. How do you find attributes in a module?

  - Use dir(module), e.g., dir(math).

- ## Q6. How does __name__ == "__main__" work?

  - Lets a file act as both script and importable module; code in that block runs only when executed directly.

- ## Q7. What is PIP?

  - Python’s package manager (pip install, pip uninstall, pip list, pip show).

- ## Q8. How do you create and use a package?

  - Create a folder with __init__.py, add modules, import via import packagename.modulename.

- ## Q9. How are strings represented in Python?

  - Strings are immutable sequences of Unicode characters.

- ## Q10. Why are strings immutable? What is interning?

  - Immutability aids safety and optimization. Interning may reuse identical literals to save memory.

- ## Q11. Common string methods

  - upper, lower, strip, replace, split, join.

- ## Q12. String slicing and formatting

  - s[0:3] for slicing; f"Hello {s}" for f-strings.

- ## Q13. join() vs + for strings

  - join() efficiently concatenates an iterable of strings; + joins two strings creating a new one.

- ## Q14. What is a list in Python?

  - Ordered, mutable collection; stores references (dynamic array under the hood).

- ## Q15. List time complexities (common)

  - Index O(1); append amortized O(1); insert/delete at front O(n); search O(n).

- ## Q16. List vs array

  - Lists hold mixed types as references; arrays are single-type and more memory efficient.

- ## Q17. List slicing: copy or reference?

  - Slicing makes a shallow copy.

- ## Q18. How to copy a list?

  - a[:] or list(a) for shallow copy.

- ## Q19. list.append() vs list.extend()

  - append adds one element; extend adds elements from an iterable.

- ## Q20. sorted() vs .sort()

  - sorted returns a new list; .sort sorts in place.

- ## Q21. List comprehension benefits

  - More readable and often faster for building lists.

- ## Q22. How to remove duplicates from a list?

  - list(set(nums)) (unordered) or list(dict.fromkeys(nums)) to preserve order.

- ## Q23. What is a tuple?

  - Immutable ordered sequence; single-element tuple needs a trailing comma (5,).

- ## Q24. Why use tuples instead of lists?

  - Immutable (safer), can be dict keys, typically faster and lower overhead.

- ## Q25. What is tuple unpacking?

  - Assigning tuple elements to variables in one step.

- ## Q26. What is a set?

  - Unordered collection of unique elements; great for O(1) membership checks.

- ## Q27. Example set operations

  - a & b (intersection), a | b (union), a ^ b (symmetric difference).

- ## Q28. What is a dictionary and why is it fast?

  - Key-value mapping implemented with a hash table (average O(1) lookups).

- ## Q29. Can dict keys be mutable?

  - No; keys must be immutable and hashable.

- ## Q30. dict.get() vs dict[]

  - dict[] raises KeyError when missing; get returns None or a default.

- ## Q31. What are exceptions?

  - Runtime errors that halt execution unless handled.

- ## Q32. Why does exception hierarchy matter?

  - Catch specific exceptions first; controls which errors are handled.

- ## Q33. How do you handle multiple exceptions and use else/finally?

  - try/except ValueError; else for success path; finally for cleanup.

- ## Q34. How to raise custom exceptions?

  - raise ValueError("msg") or define class MyError(Exception): pass and raise it.

- ## Q35. What are custom exceptions used for?

  - Domain-specific errors that improve tracing and intent.

- ## Q36. Why use context managers?

  - Guarantee setup/cleanup (e.g., files) via with blocks.

- ## Q37. What is default argument evaluation?

  - Default arguments are evaluated once at function definition time.

- ## Q38. Why are mutable default arguments risky?

  - The same object is reused across calls, causing shared state.

- ## Q39. *args and **kwargs in Python

  - *args collects arbitrary positional args; **kwargs collects arbitrary keyword args.

- ## Q40. What is the LEGB rule?

  - Name resolution order: Local, Enclosing, Global, Built-in.

- ## Q41. What is the global keyword?

  - Declares that a name refers to a global variable inside a function.

- ## Q42. What is a closure?

  - A nested function that remembers variables from its enclosing scope.

- ## Q43. What is a generator?

  - A function that yields values lazily, producing one value at a time.

- ## Q44. Generators vs lists

  - Generators are lazy and memory efficient; lists store all elements in memory.

- ## Q45. What does yield do?

  - Pauses function state and returns a value; resumes on next iteration.

- ## Q46. What is OOP?

  - Organizes code into classes and objects.

- ## Q47. Define a class and object

  ```python
  class Car:
      def __init__(self, brand):
          self.brand = brand

  c = Car("BMW")
  ```

- ## Q48. Instance, class, and static variables

  - Instance vars per object; class vars shared; static vars are just class attributes not tied to instances.

- ## Q49. Instance methods, class methods, static methods

  - Instance needs self; classmethod uses cls; staticmethod is independent utility.

- ## Q50. What is inheritance?

  - A class can reuse/extend another class’s attributes and methods.

- ## Q51. What is method overriding?

  - Subclass provides its own implementation of a parent method.

- ## Q52. What is encapsulation?

  - Hiding internal details; use naming conventions (_protected, __private) to signal restricted access.

- ## Q53. What is polymorphism?

  - Same method name behaves differently across types (e.g., len on different containers).

- ## Q54. What is operator overloading?

  - Defining special methods like __add__ to customize operator behavior for objects.

- ## Q55. What is multiple inheritance?

  - A class inheriting from more than one base class.

- ## Q56. What is an iterator?

  - Object implementing __iter__() and __next__(); produces items sequentially.

- ## Q57. What is a generator (syntax)?

  - A function with yield that creates an iterator lazily.

- ## Q58. What is a closure (example)?

  - outer returns inner that captures outer’s variables.

- ## Q59. How do you read and write files in Python?

  - Use with open("file", "w") as f: f.write(...); with open("file") as f: f.read().

- ## Q60. Binary vs text files

  - Text handles encoded characters; binary handles raw bytes.

- ## Q61. How is the os module used?

  - os.getcwd(), os.mkdir(), os.remove(), etc., for system operations.

- ## Q62. How do you work with time module?

  - time.time(), time.sleep(), time.ctime().

- ## Q63. How to use datetime

  - datetime.now(), strftime formatting, timedelta arithmetic.

- ## Q64. How to use calendar module

  - calendar.month(year, month), calendar.isleap(year).

- ## Q65. What are text and binary file modes?

  - "r"/"w" for text; "rb"/"wb" for binary.

- ## Q66. What is tuple unpacking?

  - Assign elements of a tuple to variables in one statement.

- ## Q67. What is default argument evaluation timing?

  - Evaluated once when the function is defined (not per call).

- ## Q68. What are custom exceptions used for?

  - Domain-specific error handling and clearer intent.

- ## Q69. Why use context managers?

  - Ensure deterministic cleanup of resources.

- ## Q70. What is a generator expression?

  - Lazy inline generator syntax: (x*x for x in nums).

- ## Q71. Difference between iterator and generator

  - Iterator: any object with __iter__/__next__; Generator: iterator created via yield (function) or generator expression.

- ## Q72. Performance summary: list vs tuple vs set vs dict

  - list: ordered, mutable, allows duplicates, lookup O(n).
  - tuple: ordered, immutable, allows duplicates, lookup O(n).
  - set: unordered, mutable, unique items, lookup O(1) avg.
  - dict: insertion-ordered (3.7+), mutable, unique keys, lookup O(1) avg.

- ## Q73. Two-pointer pattern (when and example)

  - Use when scanning from both ends (e.g., palindrome check).

  ```python
  def is_palindrome(nums):
      l, r = 0, len(nums) - 1
      while l < r:
          if nums[l] != nums[r]:
              return False
          l += 1
          r -= 1
      return True
  ```

- ## Q74. Sliding window pattern

  - For substring/window problems (e.g., max window sum).

  ```python
  def max_window_sum(nums, k):
      window = sum(nums[:k])
      best = window
      for i in range(k, len(nums)):
          window += nums[i] - nums[i-k]
          best = max(best, window)
      return best
  ```

- ## Q75. Hash map frequency pattern

  - Count or group items (e.g., first non-repeating char).

  ```python
  def first_non_repeating(s):
      freq = {}
      for ch in s:
          freq[ch] = freq.get(ch, 0) + 1
      for ch in s:
          if freq[ch] == 1:
              return ch
      return None
  ```

- ## Q76. Stack pattern

  - Use for parsing/parentheses/undo (validate parentheses).

  ```python
  def is_valid(s):
      stack = []
      pairs = {')': '(', ']': '[', '}': '{'}
      for ch in s:
          if ch in pairs.values():
              stack.append(ch)
          elif ch in pairs:
              if not stack or stack.pop() != pairs[ch]:
                  return False
      return not stack
  ```

- ## Q77. Queue / BFS pattern

  - Level-order traversal and nearest search.

  ```python
  from collections import deque

  def level_order(root):
      if not root:
          return []
      q, res = deque([root]), []
      while q:
          level = []
          for _ in range(len(q)):
              node = q.popleft()
              level.append(node.val)
              if node.left:
                  q.append(node.left)
              if node.right:
                  q.append(node.right)
          res.append(level)
      return res
  ```

- ## Q78. Reverse each word in a sentence

  ```python
  s = "Hello World"
  print(" ".join(word[::-1] for word in s.split()))
  ```

- ## Q79. Count character frequency

  ```python
  s = "banana"
  print({ch: s.count(ch) for ch in set(s)})
  ```

- ## Q80. Read file and count lines

  ```python
  with open("data.txt") as f:
      print(len(f.readlines()))
  ```
