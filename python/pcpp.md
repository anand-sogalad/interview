# PCPP interview questions based on the syllabus

- ## Q1. __new__ vs __init__?

  - __new__ allocates and returns the instance; __init__ initializes it.
  - Use __new__ for immutables, singletons, or instance control; __init__ for normal setup.

- ## Q2. Instance vs class variables?

  - Instance variables live on each object; class variables live on the class and are shared unless shadowed.

- ## Q3. Inheritance vs composition?

  - Prefer composition unless there is a strict is-a relationship; composition keeps coupling looser.

- ## Q4. What is MRO?

  - Method Resolution Order defines attribute lookup order; Python uses C3 linearization.

- ## Q5. What is duck typing?

  - Behavior over inheritance: if it quacks like a duck, it can be treated as one.

- ## Q6. Why override __repr__?

  - For clear, unambiguous debug output that helps rebuild the object or understand its state.

- ## Q7. __str__ vs __repr__?

  - __str__ is user-friendly; __repr__ is unambiguous and for developers.

- ## Q8. Why implement __getitem__ and __iter__?

  - To support indexing and iteration on custom containers.

- ## Q9. What is a decorator?

  - A higher-order function that wraps another callable to modify behavior without changing its code.

- ## Q10. How do decorators accept parameters?

  - Use three layers: outer decorator factory (with params) → decorator → wrapper around the function.

- ## Q11. What are class decorators?

  - Functions that take a class and return a modified/replaced class, altering behavior at definition time.

- ## Q12. Why implement __call__?

  - To let objects be invoked like functions (callable instances).

- ## Q13. @classmethod vs @staticmethod?

  - classmethod receives cls and suits factories/alternate constructors; staticmethod is a namespaced utility.

- ## Q14. Why use Abstract Base Classes?

  - To enforce required methods and provide contracts for subclasses.

- ## Q15. Multiple inheritance with ABCs?

  - ABCs can define multiple behaviors; C3 MRO resolves order when combined.

- ## Q16. How private are Python variables?

  - Python uses name mangling (__attr) to discourage access but does not enforce true privacy.

- ## Q17. Shallow vs deep copy?

  - Shallow copies the container and shares inner refs; deep recursively copies contained objects.

- ## Q18. Pickle vs JSON?

  - Pickle is Python-specific and unsafe for untrusted data; JSON is portable, text-based, and safer.

- ## Q19. What is a metaclass?

  - A class that creates classes; it customizes class creation.

- ## Q20. When to use metaclasses?

  - Rarely—framework hooks, registries, validations, or ORM-style transformations.

- ## Q21. What is the event-driven model (tkinter)?

  - A loop dispatches callbacks on user actions or events.

- ## Q22. TCP vs HTTP?

  - TCP is transport-layer, reliable byte stream; HTTP is application-layer protocol built atop TCP.

- ## Q23. REST principles?

  - Stateless, resource-oriented, use HTTP verbs, standardized representations, cacheable responses.

- ## Q24. requests vs urllib?

  - requests is higher-level and ergonomic; urllib is standard library, lower-level.

- ## Q25. Why transactions?

  - To ensure atomic, consistent changes—commit all or none.

- ## Q26. What is ACID?

  - Atomicity, Consistency, Isolation, Durability—core transaction guarantees.

- ## Q27. What is the difference between a class and an instance?

  - A class is a blueprint; an instance is a created object from that blueprint.

- ## Q28. What are instance attributes and class attributes?

  - Instance attrs belong to one object; class attrs are shared across instances unless shadowed.

- ## Q29. How are instance and class data accessed?

  - Access via the instance for per-object data and via the class for shared data; instance lookup falls back to class.

- ## Q30. What are instance, class, and static methods?

  - Instance methods use self; class methods use cls; static methods take no implicit first arg and act as utilities.

- ## Q31. How can you dynamically add attributes?

  - Assign to an instance (obj.new_attr = 10) or class (Class.new_attr = 20) unless __slots__ blocks it.

- ## Q32. What is __init__ and __del__?

  - __init__ runs during construction; __del__ is a destructor called before GC frees the object (timing is not guaranteed).

- ## Q33. Difference between __dict__ and dir()?

  - __dict__ is the instance namespace; dir() lists accessible attributes including inherited ones.

- ## Q34. Demonstrate shallow vs deep copy

  - Shallow shares inner refs; deep copies recursively.

  ```python
  import copy
  a = [[1, 2], [3, 4]]
  b = copy.copy(a)
  c = copy.deepcopy(a)
  ```

- ## Q35. Show shallow vs deep copy effects

  - Mutating inner objects shows the difference: shallow reflects, deep does not.

  ```python
  a = [[1, 2], [3, 4]]
  b = copy.copy(a)
  b[0][0] = 99  # a changes
  c = copy.deepcopy(a)
  c[0][0] = 100  # a stays
  ```

- ## Q36. What is an abstract class?

  - A non-instantiable class with abstract methods defining an interface.

- ## Q37. How do you implement method overriding?

  - Subclass redefines a parent method to change behavior.

- ## Q38. What are special (dunder) methods?

  - Methods like __len__, __add__, __iter__ that integrate objects with Python syntax and protocols.

- ## Q39. Difference between @classmethod and @staticmethod?

  - classmethod receives cls and can touch class state; staticmethod is just namespaced and receives no implicit arg.

- ## Q40. What are __new__ and __init__?

  - __new__ allocates the instance; __init__ initializes it post-allocation.

- ## Q41. What is inheritance?

  - Deriving a class from another to reuse or extend behavior.

- ## Q42. What types of inheritance exist in Python?

  - Single, multiple, multilevel, hierarchical, hybrid.

- ## Q43. What is polymorphism?

  - Same interface, different behavior across types (duck typing or inheritance-based).

- ## Q44. What is encapsulation?

  - Hiding internals; use conventions (_protected, __private) and properties for controlled access.

- ## Q45. What is multiple inheritance and how is ambiguity resolved?

  - A class has multiple bases; MRO (C3) resolves method lookup order.

- ## Q46. How to use super()?

  - Call parent implementations cooperatively, especially in multiple inheritance chains.

- ## Q47. How to define custom exceptions?

  - Subclass Exception and raise them for domain-specific errors.

- ## Q48. What is exception chaining?

  - Raising a new exception while preserving the original via "from" to keep context.

- ## Q49. How do else and finally work in try blocks?

  - else runs when no exception; finally always runs (cleanup).

- ## Q50. How to re-raise exceptions?

  - Use plain raise inside except to propagate.

- ## Q51. What is assert for?

  - Runtime checks for debugging; can be stripped with -O and not for input validation.

- ## Q52. What is pickling?

  - Serializing Python objects to binary with pickle.dump.

- ## Q53. What is unpickling?

  - Loading pickled data back to objects with pickle.load.

- ## Q54. What is the shelve module?

  - A simple persistent key-value store backed by pickled objects.

- ## Q55. Pickle vs shelve?

  - Pickle handles single objects/streams; shelve offers a dict-like interface over pickled data.

- ## Q56. What is a metaclass?

  - A class factory (subclass of type) that customizes class creation.

- ## Q57. Why use metaclasses?

  - Enforce patterns, auto-register classes, validate attributes, or transform classes.

- ## Q58. How does type() relate to metaclasses?

  - type is Python's default metaclass; classes are instances of type.

- ## Q59. How to customize class creation with __new__ in a metaclass?

  - Override __new__ in a metaclass to modify class dict or add attributes before class creation.

- ## Q60. Implement an abstract base class for shapes

  - Use ABC and @abstractmethod to define required methods.

- ## Q61. Demonstrate class variable sharing

  - Class attributes incremented in __init__ show shared state across instances.

- ## Q62. Save and load objects using pickle

  - Dump to a .pkl file then load it back to restore objects.

- ## Q63. Custom metaclass to validate attributes

  - Raise errors in metaclass __new__ if required members are missing.

- ## Q64. What is a class in Python?

  - A blueprint bundling data and behavior for objects.

- ## Q65. How do you define a class and create an object?

  - Declare with class and instantiate like Car(); __init__ sets attributes.

- ## Q66. Where are instance attributes stored?

  - Typically in the instance __dict__ unless __slots__ restricts storage.

- ## Q67. How do class and instance attributes differ?

  - Class attrs live on the class and can be shadowed by instance attrs in __dict__.

- ## Q68. How do you add attributes dynamically?

  - Assign at runtime: obj.attr = value, unless __slots__ blocks it.

- ## Q69. What is the Python data model?

  - The set of dunder methods/protocols that let objects integrate with core syntax.

- ## Q70. How to support len(obj)?

  - Implement __len__ returning a non-negative int.

- ## Q71. __str__ vs __repr__ difference?

  - __str__ is friendly; __repr__ is precise, often evaluable.

- ## Q72. When implement __bool__?

  - To customize truthiness; otherwise __len__ drives it.

- ## Q73. How to make an object hashable?

  - Provide stable __hash__ and consistent __eq__ over immutable state.

- ## Q74. What is MRO?

  - Attribute lookup order; inspect via Class.__mro__ or mro().

- ## Q75. How to inspect MRO?

  - Use Class.__mro__ or Class.mro().

- ## Q76. Multiple inheritance gotcha?

  - Diamond problem; use cooperative super() to follow C3 MRO.

- ## Q77. Proper super() usage in multiple inheritance?

  - Call super() in every class to keep the MRO chain intact.

- ## Q78. How is polymorphism used in Python?

  - Rely on duck typing: implement the needed methods regardless of type.

- ## Q79. How to encapsulate attribute access idiomatically?

  - Use @property for controlled getters/setters.

- ## Q80. Example of validating with a property?

  - Add checks in the setter, raising ValueError on invalid data.

- ## Q81. Are private members enforced?

  - No; name mangling deters but does not prevent access.

- ## Q82. What is a descriptor?

  - An object defining __get__, __set__, or __delete__ to manage attribute access.

- ## Q83. Simple descriptor example?

  - Use __set_name__, __get__, __set__ to control storage and validation.

- ## Q84. How do properties relate to descriptors?

  - property is a built-in data descriptor factory.

- ## Q85. When use a descriptor over a property?

  - When reusing the same access logic across many attributes/classes.

- ## Q86. staticmethod vs classmethod?

  - staticmethod has no implicit arg; classmethod receives cls and can be a factory.

- ## Q87. Alternative constructor with classmethod?

  - Provide a named constructor (e.g., from_hex) that builds an instance from other data.

- ## Q88. What is an ABC and why use it?

  - Defines required methods; useful for contracts and static checking.

- ## Q89. Protocol vs ABC?

  - Protocols are structural (shape-based) and do not require inheritance; ABCs need subclassing.

- ## Q90. Example Protocol usage?

  - Define a Protocol with expected methods; any class with that shape satisfies it for typing.

- ## Q91. Why use dataclasses?

  - Reduce boilerplate by auto-generating __init__, __repr__, __eq__, etc.

- ## Q92. Example frozen dataclass?

  - Use @dataclass(frozen=True) to make immutable value objects.

- ## Q93. When to use __slots__?

  - To save memory and block dynamic attributes for many small instances.

- ## Q94. dataclass with slots?

  - Use @dataclass(slots=True) (Python 3.10+) to combine conveniences with slots.

- ## Q95. Equality contract with hashing?

  - If __eq__ says objects are equal, their __hash__ must match; usually pair with immutability.

- ## Q96. How to implement value semantics?

  - Make fields immutable and define __eq__/__hash__ (or use frozen dataclasses).

- ## Q97. Implement vector addition with operator overloading

  - Define __add__ returning a new instance and __repr__ for clarity.

- ## Q98. When to implement rich comparisons?

  - When a clear ordering exists; functools.total_ordering can fill in remaining methods.

- ## Q99. Custom context manager via __enter__/__exit__?

  - Implement both to manage resources and cleanup with with blocks.

- ## Q100. When return True in __exit__?

  - Only when the exception is fully handled and should be suppressed.

- ## Q101. contextlib.contextmanager helper?

  - Use it for generator-based context managers to simplify setup/teardown.

- ## Q102. Python decorator (language) in one line?

  - A higher-order wrapper that modifies a callable at definition time.

- ## Q103. Example timing decorator?

  - Wrap a function, measure perf_counter delta, print duration, return result.

- ## Q104. Decorator pattern vs Python decorator?

  - Pattern wraps objects to extend behavior; Python decorators wrap callables/classes—conceptually similar but at call/definition time.

- ## Q105. Strategy pattern in Pythonic style?

  - Use a dict mapping names to callables and invoke by key to swap behavior at runtime.

- ## Q106. Factory pattern example?

  - Classmethod that returns subclass/instance based on a kind parameter.

- ## Q107. Adapter pattern example?

  - Wrap an object to expose the expected interface, translating calls as needed.

- ## Q108. Observer pattern example?

  - Event bus storing callbacks per event and notifying subscribers on emit.

- ## Q109. Command pattern example?

  - Encapsulate actions in objects with an execute method.

- ## Q110. How to implement a singleton in Python?

  - Prefer module-level; otherwise override __new__ to return the same instance (mind testability).

- ## Q111. Decorator vs proxy vs wrapper?

  - Decorator adds behavior; proxy controls access; wrapper is a generic term for delegation.

- ## Q112. Why prefer composition over inheritance?

  - Looser coupling, easier testing, and independent evolution of parts.

- ## Q113. What is a mixin?

  - A small class providing focused behavior to be combined via multiple inheritance.

- ## Q114. When choose composition over inheritance?

  - When the relationship is "has-a/uses" or bases would grow deep and brittle.

- ## Q115. Simple dependency injection pattern?

  - Pass dependencies into constructors (composition root wires them).

- ## Q116. Why avoid a service locator?

  - Hidden globals hurt testability and clarity.

- ## Q117. How to load plugins dynamically?

  - Use importlib to import modules/symbols from configured paths at runtime.

- ## Q118. How to design a plugin interface?

  - Define a minimal ABC/Protocol (initialize, execute), discover implementations, and load safely.

- ## Q119. How to safely load third-party plugins?

  - Validate config, isolate errors, sandbox if possible, version contracts, and guard imports.

- ## Q120. How to register plugins without global state?

  - Use explicit registries passed around or configuration-driven maps in the composition root.

- ## Q121. Hot-reload approach for plugins?

  - Watch directories and reload modules with importlib.reload or swap worker processes.

- ## Q122. How do OOP choices affect performance?

  - Many tiny objects and deep call chains add overhead; favor flatter data for hot paths.

- ## Q123. When to use __slots__ for performance?

  - With many small instances where attribute dict memory dominates; measure first.

- ## Q124. Concurrency strategy for CPU-bound OOP services?

  - Use multiprocessing or native extensions; threads mainly help I/O-bound code due to the GIL.

- ## Q125. How does DI help testing?

  - Lets you inject fakes/mocks, isolating units under test.

- ## Q126. How to test class hierarchies effectively?

  - Test via public interfaces and contracts; avoid private details.

- ## Q127. Rule of thumb for testable OOP design?

  - Small classes, pure functions where possible, explicit dependencies, minimal globals.

- ## Q128. Context manager use in frameworks?

  - Wrap external resources to ensure deterministic cleanup with with.

- ## Q129. Where to place retry/backoff logic?

  - As decorators or policy objects separate from core business logic.

- ## Q130. How to apply caching policy?

  - Use functools.lru_cache for pure functions; explicit caches with invalidation for I/O-bound services.

- ## Q131. Configuration strategy?

  - Immutable config objects, layered sources (env/file/CLI), validated at startup.

- ## Q132. Pitfall when overriding __eq__ only?

  - Object becomes unhashable unless __hash__ is defined or set to None intentionally.

- ## Q133. super() in multiple inheritance without cooperation?

  - Skipping super breaks the MRO chain; every class must call super.

- ## Q134. Property and __slots__ interaction?

  - Works if slot names exist; dynamic attributes are blocked unless __dict__ is slotted.

- ## Q135. Why prefer Protocols for libraries?

  - Avoids forcing inheritance; consumers just match the required shape for compatibility.

- ## Q136. Dataclass mutable default trap?

  - Use field(default_factory=...) instead of a mutable default value.

- ## Q137. Pluggable formatter design?

  - Define a Formatter Protocol (format -> str), map names to implementations, inject into report generator.

- ## Q138. Add audit logging to selected services?

  - Wrap with decorator or proxy rather than embedding logging in core logic.

- ## Q139. Feature flags per customer at runtime?

  - Strategy map keyed by flags; inject a FeatureProvider; keep evaluation side-effect-free.

- ## Q140. Versioned serializer for API objects?

  - Factory by version, strategy for encode/decode, and versioned schema modules.

- ## Q141. Safely extend a base Job with new steps?

  - Use Template Method with hooks or a pipeline of composed steps.
