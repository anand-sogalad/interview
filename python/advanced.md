# Advanced interview questions: threading, multiprocessing, asyncio, context managers, design patterns

- ## Q1. What is a thread?

  - A thread is the smallest schedulable unit within a process; threads in the same process share memory and resources.

- ## Q2. What is multithreading in Python?

  - Running multiple threads concurrently, mainly effective for I/O-bound tasks.

  ```python
  import threading, time

  def worker(name):
    print(f"Thread {name} starting")
    time.sleep(2)
    print(f"Thread {name} done")

  t1 = threading.Thread(target=worker, args=("A",))
  t2 = threading.Thread(target=worker, args=("B",))
  t1.start(); t2.start()
  t1.join(); t2.join()
  ```

- ## Q3. What is the Global Interpreter Lock (GIL)?

  - Only one thread executes Python bytecode at a time; good for I/O-bound work, limits CPU-bound parallelism.

- ## Q4. How can you overcome the GIL?

  - Use multiprocessing for CPU-bound tasks; C extensions (NumPy, Cython) or asyncio for concurrency.

- ## Q5. How do you synchronize threads?

  - Use `Lock`, `RLock`, `Semaphore`, or `Condition` from `threading`.

  ```python
  import threading

  lock = threading.Lock()
  count = 0

  def safe_increment():
    global count
    with lock:
      count += 1
  ```

- ## Q6. Difference between daemon and non-daemon threads?

  - Daemon threads exit when the main thread exits; non-daemon threads block termination until done.

  ```python
  t = threading.Thread(target=worker)
  t.daemon = True
  t.start()
  ```

- ## Q7. What is multiprocessing?

  - Multiple processes with independent memory and interpreters enable true parallelism (bypass GIL).

  ```python
  from multiprocessing import Process

  def worker(n):
    print(f"Processing {n}")

  if __name__ == "__main__":
    p1 = Process(target=worker, args=(1,))
    p1.start(); p1.join()
  ```

- ## Q8. Threading vs multiprocessing

  - Memory: threads share; processes are independent.
  - Parallelism: threads GIL-limited; processes are true parallel.
  - Overhead: threads lower; processes higher.
  - Use case: threads/asyncio for I/O-bound; processes for CPU-bound.

- ## Q9. How do you share data between processes?

  - Use `multiprocessing.Queue`, `Pipe`, or `Manager`.

  ```python
  from multiprocessing import Process, Queue

  def f(q):
    q.put("Hello")

  if __name__ == "__main__":
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())
    p.join()
  ```

- ## Q10. How do you create a process pool?

  ```python
  from multiprocessing import Pool

  def square(x): return x*x

  if __name__ == "__main__":
  with Pool(4) as p:
  print(p.map(square, [1,2,3,4]))
  ```

- ## Q11. What is asyncio?

  - Asynchronous, single-threaded concurrency with `async`/`await` and an event loop.

- ## Q12. Example: async function with await

  ```python
  import asyncio

  async def greet(name):
  await asyncio.sleep(1)
  print(f"Hello {name}")

  async def main():
  await asyncio.gather(greet("A"), greet("B"), greet("C"))

  asyncio.run(main())
  ```

- ## Q13. Difference between concurrency and parallelism

  - Concurrency: manage multiple tasks (not necessarily simultaneous).
  - Parallelism: execute multiple tasks at the same time on hardware.

- ## Q14. When to use asyncio vs threading vs multiprocessing

  - I/O-bound, many network requests: asyncio or threading.
  - CPU-bound: multiprocessing.
  - Heavy computation: `ProcessPoolExecutor`.
  - Mixed workloads: combine appropriately.

- ## Q15. Asyncio tasks and event loop

  ```python
  import asyncio

  async def fetch_data():
  print("Fetching...")
  await asyncio.sleep(2)
  return 42

  async def main():
  task = asyncio.create_task(fetch_data())
  result = await task
  print(result)

  asyncio.run(main())
  ```

- ## Q16. What is a context manager?

  - Object defining setup/teardown via `__enter__` and `__exit__` for deterministic cleanup.

  ```python
  class FileManager:
  def __init__(self, filename): self.filename = filename
  def __enter__(self): self.file = open(self.filename, "w"); return self.file
  def __exit__(self, exc_type, exc_val, exc_tb): self.file.close()

  with FileManager("test.txt") as f:
  f.write("Hello Context Manager")
  ```

- ## Q17. What does the with statement do?

  - Automates resource management; equivalent to structured `try/finally` for setup and cleanup.

- ## Q18. How to create a context manager using contextlib?

  ```python
  from contextlib import contextmanager

  @contextmanager
  def managed_resource():
  print("Setup")
  yield
  print("Cleanup")

  with managed_resource():
  print("Using resource")
  ```

- ## Q19. What are design patterns?

  - Proven solutions to recurring design problems; improve reuse, scalability, and maintainability.

- ## Q20. Common design pattern categories

  - Creational: Singleton, Factory, Builder.
  - Structural: Adapter, Decorator, Facade.
  - Behavioral: Observer, Strategy, Command.

- ## Q21. Singleton pattern

  ```python
  class Singleton:
  _instance = None
  def __new__(cls):
  if not cls._instance:
  cls._instance = super().__new__(cls)
  return cls._instance
  ```

- ## Q22. Factory pattern

  ```python
  class Dog:
  def speak(self): return "Woof"
  class Cat:
  def speak(self): return "Meow"

  def pet_factory(pet_type):
  if pet_type == "dog": return Dog()
  elif pet_type == "cat": return Cat()
  raise ValueError("unknown")
  ```

- ## Q23. Decorator pattern

  ```python
  def uppercase_decorator(func):
  def wrapper():
  result = func()
  return result.upper()
  return wrapper

  @uppercase_decorator
  def greet(): return "hello"

  print(greet())  # HELLO
  ```

- ## Q24. Observer pattern

  ```python
  class Subject:
  def __init__(self): self.observers = []
  def attach(self, obs): self.observers.append(obs)
  def notify(self, msg):
  for obs in self.observers: obs.update(msg)

  class Observer:
  def update(self, msg): print(f"Received: {msg}")

  s = Subject(); o1, o2 = Observer(), Observer()
  s.attach(o1); s.attach(o2)
  s.notify("Event triggered!")
  ```

- ## Q25. Strategy pattern

  ```python
  class Strategy:
  def execute(self, a, b): pass

  class Add(Strategy):
  def execute(self, a, b): return a + b

  class Subtract(Strategy):
  def execute(self, a, b): return a - b

  def context(strategy, a, b): print(strategy.execute(a, b))

  context(Add(), 5, 3); context(Subtract(), 5, 3)
  ```

- ## Q26. ThreadPoolExecutor & ProcessPoolExecutor

  ```python
  from concurrent.futures import ThreadPoolExecutor, as_completed

  def work(x): return x * 2

  with ThreadPoolExecutor(max_workers=3) as executor:
  futures = [executor.submit(work, i) for i in range(5)]
  for f in as_completed(futures):
  print(f.result())
  ```

- ## Q27. Combining asyncio and threading

  ```python
  import asyncio, time

  def blocking_task():
  time.sleep(2)
  return "Done"

  async def main():
  loop = asyncio.get_running_loop()
  result = await loop.run_in_executor(None, blocking_task)
  print(result)

  asyncio.run(main())
  ```

- ## Q28. What is an iterable in Python?

  - Object that can return its elements one at a time; implements `__iter__()`.

- ## Q29. What is an iterator?

  - Object with `__iter__()` and `__next__()` yielding items on demand.

- ## Q30. How does a for loop work internally?

  ```python
  it = iter(obj)
  while True:
  try:
  value = next(it)
  except StopIteration:
  break
  ```

- ## Q31. Make a custom iterator

  ```python
  class Countdown:
  def __init__(self, n): self.n = n
  def __iter__(self): return self
  def __next__(self):
  if self.n <= 0: raise StopIteration
  self.n -= 1
  return self.n + 1
  ```

- ## Q32. When do iterators get exhausted?

  - After `StopIteration` is raised; recreate to iterate again.

- ## Q33. What is a generator?

  - Function using `yield` to produce values lazily.

- ## Q34. Difference between return and yield

  - `yield` pauses/resumes state; `return` exits the function.

- ## Q35. Generator expression example

  ```python
  squares = (x*x for x in range(5))
  ```

- ## Q36. When to use generators?

  - Large streams, pipelines, or when avoiding storing entire results.

- ## Q37. Turn a function into a generator

  ```python
  def fib(n):
  a,b = 0,1
  for _ in range(n):
  yield a
  a,b = b, a+b
  ```

- ## Q38. What is a context manager used for?

  - Managing resources with guaranteed cleanup (files, locks, DB connections).

- ## Q39. Two ways to implement a context manager

  - `__enter__` / `__exit__` methods.
  - `contextlib.contextmanager` decorator.

- ## Q40. Example using contextlib

  ```python
  from contextlib import contextmanager

  @contextmanager
  def db_session(conn):
  try:
  yield conn
  conn.commit()
  except:
  conn.rollback()
  raise
  ```

- ## Q41. When should __exit__ return True?

  - Only when the exception is handled and should be suppressed.

- ## Q42. Why do frameworks prefer context managers?

  - Centralized setup/cleanup reduces leaks and simplifies resource handling.

- ## Q43. What is a closure?

  - Function that remembers variables from its enclosing scope via `nonlocal` or captured names.

- ## Q44. Closure example

  ```python
  def make_counter():
  count = 0
  def inc():
  nonlocal count
  count += 1
  return count
  return inc
  ```

- ## Q45. When do closures help?

  - Stateful callbacks, decorators, lazy evaluation, factories.

- ## Q46. What is shallow copy?

  - Copies the outer container; inner objects are shared references.

- ## Q47. What is deep copy?

  - Recursively copies contents, producing independent sub-objects.

- ## Q48. Demonstrate shallow vs deep copy

  ```python
  import copy
  a = [[1,2], [3,4]]
  b = copy.copy(a)
  c = copy.deepcopy(a)

  a[0].append(99)
  # b reflects change, c does not
  ```

- ## Q49. When should you avoid deepcopy?

  - Large/cyclic graphs; prefer tailored clone logic for performance and control.

- ## Q50. What is pickle used for?

  - Serializing Python object graphs (including custom classes) to binary.

- ## Q51. What is the risk with pickle?

  - Unpickling untrusted input can execute arbitrary code; never use with untrusted data.

- ## Q52. When to use JSON?

  - Cross-language text-based interchange of standard types.

- ## Q53. Key differences: pickle vs JSON

  - Portability: pickle is Python-only; JSON is multi-language.
  - Security: pickle unsafe for untrusted input; JSON safe.
  - Custom objects: pickle supports; JSON needs custom encoders.

- ## Q54. Custom JSON encoding example

  ```python
  import json

  class User:
  def __init__(self,name): self.name=name

  def encode(obj):
  if isinstance(obj, User):
  return {"name": obj.name}
  raise TypeError

  json.dumps(User("Ana"), default=encode)
  ```

- ## Q55. What is a metaclass?

  - A class that creates classes (customizes class creation and behavior).

- ## Q56. What is the default metaclass?

  - `type`.

- ## Q57. How is a class created with type?

  ```python
  MyClass = type("MyClass", (Base,), {"attr": 10})
  ```

- ## Q58. Why use metaclasses?

  - Enforce patterns, auto-registration, validation, API contracts, automatic mixins.

- ## Q59. Simple metaclass example

  ```python
  class Registry(type):
  registry = {}
  def __new__(mcls, name, bases, attrs):
  cls = super().__new__(mcls, name, bases, attrs)
  Registry.registry[name] = cls
  return cls

  class Base(metaclass=Registry): pass
  class A(Base): pass
  class B(Base): pass
  # Registry.registry now tracks subclasses
  ```

- ## Q60. Metaclass vs decorator

  - Decorators modify one class/function; metaclasses affect all classes using them.

- ## Q61. Metaclass vs inheritance

  - Inheritance shapes instance behavior; metaclasses shape class-level behavior.

- ## Q62. Convert a generator to a list

  ```python
  list(gen)
  ```

- ## Q63. Detect if object is iterable

  ```python
  import collections.abc
  isinstance(obj, collections.abc.Iterable)
  ```

- ## Q64. Write an infinite generator

  ```python
  def naturals():
  n = 0
  while True:
  yield n
  n += 1
  ```

- ## Q65. Use yield inside a context manager

  - See `contextlib.contextmanager` pattern (Q40) for generator-based managers.

- ## Q66. Why is generator-based pipelining efficient?

  - Avoids materializing intermediates; reduces memory and improves streaming.

- ## Q67. When to use context managers in test automation?

  - Browser sessions, DB handles, sockets, temp directories.

- ## Q68. When is a metaclass overkill?

  - When a decorator or factory suffices; prefer the simplest tool.

- ## Q69. Real cases where metaclasses shine

  - Auto-register test cases, enforce field definitions (ORMs), plugin loaders.

- ## Q70. Which advanced features power Django's ORM models?

  - Metaclasses and descriptors.
