# python courses

## course 1: intro

- complex numbers exist, and use `j` for the imaginary versor
- the `**` operator is way cooler than the `pow` function
- `/` is real division, `//` is integer division
- cast with functions like `int()` or `float()`
- bitwise operators: `&`, `|`, `^`, `<<`, `>>`
- you can use `_` in a numeric literal as visual separators, it does nothing
- boolean operators: `and`, `or,` `not`
- bools are uppercase: `True,` `False`
- string literal types:
  - normal string literals: `'something'`, or `"something"`
  - raw string literals: `r'some\nthing'` - ignores character escapes, useful for regex
  - byte string literals: `b'something'` - uses bytes (ASCII characters) instead of UTF-8 characters
  - format string literals: `f'{something}'` - see below
  - multi-line string literals: `'''...'''`, `"""..."""` - useful for long text and documentation
- string formatting:
  - using the `%` operator - similar to C: `'Grade: %d'%10`, `'%d GOTO %d'%(30, 10)`
    - can take a dict argument, and use its keys:

      ```python
      'Name: %(name)8s Grade: %(student_grade)d' % {
        'name': 'Ion', 
        'student_grade': 10
      }
      ```

  - using the `format()` method: `'Hello {}'.format('world!')`
  - using format string literals: `f'Number: {x}'`
    - `F'...'` also works
    - ***todo: format string literal cheat sheet***
- `\` can be used to concatenate program lines or to create multi-line strings
- array/string access:
  - index access: `a[idx]`
    - negative indexes go backwards from the end, `-1` being the last element
  - simple slicing: `a[from:to]`, includes `from`, excludes `to`
    - elements can be missing: `a[:to]` starts from index 0, `a[from:]` goes to the end, and `a[:]` just copies the entire thing
  - slicing with steps: `a[from:to:step]`
    - can go backwards: `a[::-1]`
    - `from` and `to` can be missing, as before; missing `step` assumed to be `1`
- ***todo: string and number method cheat-sheet***
- `string.split(sep)`: split string around separator
- semicolons (`;`) can separate statements on the same line
- `while` and `for` statements can have an `else` block - triggered when the loop condition fails
  
  - `break`ing out will **skip this block**
- `range(from, to, step)` - return an iterable of numbers
- ***todo: common function cheat sheet (`len`, `enumerate`, `filter`, whatever)***
- function parameters can have default values
  
  - these have to come last
- function parameters can have keyword arguments
  
  - these have to come last
- `global` keyword: capture a variable from the global scope
- variable-length parameter: `*args`
- keyword parameter dict: `**kwargs`
- string literals (recommended: multi-line string literals) not assigned to anything are treated as comments or documentation

## course 2: sequences

- lambda functions: `lambda <params>: <return>`
- lambdas will capture variables in their scope
- **list** type: `[]` - mutable
- **tuple** type: `()` - immutable
  
  - empty `(,)` or single-element `(1,)` tuples; parentheses optional: `x = 1, 2`
- can be concatenated amongst themselves and accessed using index/slice operators
- can be nested (beware while copying!)
- can be iterated through and enumerated (to obtain `idx, val` tuples)
- list comprehensions: `[<iterator>]`
- the index and slice operator can modify lists:

  ```python
  a = [1, 2, 3]
  a[1] = 0            # a = [1, 0, 3]
  a[2:] = ['u', 'h']  # a = [1, 0, 'u', 'h']
  a[:2] = [10]        # a = [10, 'u', 'h']
  ```

- the `remove` method and the `del` keyword are equivalent: `a.remove(5)` or `del a[5]`
  - the del keyword can delete slices too: `del a[3:]`
    - `del a[:]` == `a.clear()`
- lists are reference types, use `.copy()` to make a *shallow* copy
- many functions take a `key` keyword argument - don't forget that it's a **keyword** argument
- the `*` operator can separate a list into different elements for a function call

## course 3 - sets and dictionaries

- set elements and dictionary keys have to be *hashable*, which usually just means *immutable*
- `{}` is an empty dict
- set comprehension: `{<iterator>}`
- dict comprehension: `{k:v for ...}`
- set methods/operators:
  - `union()` or `|`
    - `update()` or `|=`
  - `intersection()` or `&`
    - `intersection_update()` or `&=`
  - `difference()` or `-`
    - `difference_update()` or `-=`
  - `symmetric_difference()` or `^`
    - `symmetric_difference_update()` or `^=`
- immutable set type: `frozenset`
- dict access: `d[key]`
  - will error on read if key doesn't exist
- iterate thru dict keys: `key in d` or `key in d.keys()`
- iterate thru dict values: `val in d.values()`
- iterate thru k,v pairs: `k,v in d.items()`
- create k,v tuples: `d.enumerate()`

## course 4: exceptions and modules

### exceptions

- `try`/`except`/`else`:

```python
try:
    # possibly erroneous stuff
except:
    # exception
else:
    # no exception
finally:
    # either way
```

- exception types (derived from `BaseException`): `ArithmeticError`, `BufferError`, `AttributeError`, etc
- `except` keyword:
  - `except`: catch-all
  - `except Type`: catch only Type
  - `except (Type, Type)`: catch more than one type
  - `except Type as e`: catch as variable
  - `except (T1, T2) as e`: catch multiple types as variable
- `raise` keyword
  - `raise Exception(..)` - create and throw exception
  - `raise` - re-throw exception (from except block)
  - `raise Exception(..) from e` - exception chaining
- `assert` keyword: raise error if condition not met
- `pass` keyword: do nothing

### modules

- `import` keyword:
  - `import module`
  - `import module as alias`
  - `from module import object`
  - `from module import *`

#### sys module

- `argv` - get program command-line arguments

#### os module

- `listdir`, `mkdir`, `rmdir`
- `rename`, `remove`
- `path` submodule
  - `join,` `dirname`, `basename`, `splitext`, `exists`, `isdir`, `isfile`, ...
- `walk` - `for (root, dirs, files) in os.walk('.')`
- `system` - basically exec?

### i/o

- `input()`, `input(prompt)`
- `print(*objects, sep='', end='\n', file=sys.stdout, flush=False)`
- `open` -> opens file object
  - defaults to opening in `r`ead mode, but can use other flags: `w`rite, `b`inary, e`x`clusive creation (fail if file exists), `a`ppend, `t`ext, upda`+`e (rw)
  - `close`, `tell` (where am i in the file?), `seek`, `read`, `write,` `readline`, ...
  - `for line in file` - beware the `\n`, use `strip()`

## course 5: modules and packages

### modules

- use `sys.path` to add directories to the path for module importing
- `dir` lists module contents
- `__file__` - path of module file
- `__name__` - module name
  - `'__main__'` if executed directly
- `__package__` - package name
- `__doc__` - object docstring
  - `help(obj)`: print the docstring - useful in interactive sessions

### packages

- a package directory needs an `__init__.py` file
- you can import packages too

### etc

- `importlib` - dynamic imports
- `exec` - execute code dynamically, permits terrifying levels of obfuscation

## course 6: regular expressions

- ***todo: python regex cheat sheet***

- use raw strings to avoid pain

- `compile` a regex object to efficiently reuse it

- `match` checks if match exists

- `search` returns first match

- `findall` returns all matches

- capture groups are important

- `split` around matches
  > if capturing parentheses are used in pattern, then the text of all groups in the pattern are also returned as part of the returning list

  ```python
  re.split(r'(\d\d+', 'color from pixel 20,30 is 123')
  # output:
  # ['color from pixel ', '20', ',', '30', ' is ', '123', '']
  ```

- `sub` - replace matched string
  
  - there's some complicated stuff about a `\<number>` operator idk
  
- `?...` is used for python regexp extensions

  - `?P<name>` to name capture groups
  - `(?i)...` to ignore case
  - `(?s)` makes `.` match everything
  - `(?=...)` - look ahead assertion, match prev exp only if next expr is `...`
  - `(?!...`) - same, but 'not'
  - `(?#...)` - comment for a group

## course 7: serialization, time module, random module, hash functions, zip files

### time

- `time` (`ctime`, `localtime`, `gmtime`)
  - the latter two can take a unix time instead of `time.time()` by default
- `mktime` (obj to float), `asctime` (obj to string)
- `strftime(fmt, obj)` (obj to formatted string)
- `sleep(seconds)`

### hashlib

- md5 stuff
- sha1 stuff

### data serialization

- `json`: `dump`, `dumps`, `load`, `loads`, human readable
- `pickle`: same stuff, python-specific, version dependent
- `marshal`: same stuff, platform dependent

### random

- `random` - float, 0 to 1
- `randint(min, max)`
- `choice(list)`
- `shuffle(list)`
- `sample(list, count)`

### zipfile

- a bunch of stuff who cares

## course 8: networking

### sockets

- same stuff as in C
- `socket(family, type)` creates socket
- `bind((adr, port))`, `listen(queue_len)`
- `(conn, addr) = s.accept()`
- `recv(size)`, `send(what)`
- `gethostbyname(hostname)`, `gethostbyaddr(ip_addr)`
- etc

### other

- `urllib`, `ftplib`, `smtplib`
- `http.server`

### course 9: classes 1

- methods have the first param `self`, static functions do not
- members can be defined in `__init__` or directly in the class definition
  - they are static in the latter case
- classes are really more like fancy dicts, you can add stuff to them post declaration

  ```python
  class Point:
      def __init__(self):
          self.x = 0
          self.y = 0
  
  p1 = Point()
  p1.z = 10
  print(p1.z)
  # 10
  ```

- you can delete a class member with `del`
- a method from another class can be used, but it will refer to the other class' instance's `self`:

  ```python
  class A:
      x = 10
      def f(self):
          return self.x
  class B:
      x = 10
  
  a = A()
  b = B()
  b.f = a.f
  print(b.f())
  # 10
  ```

- normal functions can be used, but will not link `self` correctly:

  ```python
  class A:
      x = 10
  def f(self):
      return self.x
  
  a = A()
  a.f = f
  print(a.f())  # will fail
  ```

- class methods can also be extracted to variables, keeping their `self`:

  ```python
  class A:
      x = 10
      def f(self):
          return self.x
  
  a = A()
  g = a.f
  print(g())
  # 10
  ```

- this works as expected tho:

  ```python
  def fun(self):
      return self.x
  class A:
      x = 10
      fun = f
  ```

  - functions used like this have to be defined in the class body, not in the `__init__` method

- you can use a class as a sort of dict:
  
  ```python
  class A:
    pass
  
  a = A()
  a.x = 10
  a.y = 20
  ```

## course 10 - classes 2

- inheritance: `class Derived(Base):`
- multiple inheritance: `class Derived(Base1, Base2)`
- `isinstance(instance, class)`, `issubclass(derived, base)`
- inheritance does not mean that the superclass' `__init__` is automatically called
  - it needs to be called manually
  
  ```python
  class Base:
    def __init__(self):
      self.x = 10
  
  class Derived(Base):
    def __init__(self):
      # option 1
      Base.__init__(self)
      # option 2
      super().__init__()
  ```

- derived definitions will overwrite base ones
- for multiple inheritance, the base classes are derived right to left, overwriting eachother
- special class methods:
  - `__init__`
  - `__repr__` and `__str__`, for string conversion

## course 11 - threading and synchronization

- two libraries: `_thread` and `threading`

### `_thread`

- `start_new_thread(job, args)`
- `allocate_lock()`
  - `acquire()`, blocks until acquisition
  - `release()`, releases lock
  - can also use a `with` block instead
- unhandled exceptions in a secondary thread will not stop the main one

### `threading`

- class `Thread(target, args)`
  - can be used directly, or derived; if derived one needs to implement:
    - `run` method - code to be executed when thread starts
    - `__init__`
  - `start` method - starts the thread
  - `join(timeout=-1)` - wait for thread to finish
  - `getName`/`setName` - change the `name` attribute
  - `is_alive()`

### `threading` - synchronization

- `Lock` - `acquire(blocking=True, timeout=-1)`, `release()`, and `with`
- `RLock` - reentrant lock - the same thread can lock multiple times, raising a counter
- `Condition` - `acquire`, `release`, `wait` (`wait_for`), `notify`, `notify_all`
- `Semaphore` - `acquire`, `release`, and `with` - provides access to a limited number of threads
- `Timer(delay, job, args)` - an object derived from `Thread`, runs code after a delay
- `Event` - `set`, `clear`, `wait` (blocking), `is_set` (non-blocking)
- `Barrier(parties)` - wait for multiple threads to start at the same time
  - `wait`, `reset`, `abort`
  
## course 12 - c/c++ bindings - struct


- allows packing variables into C/C++ structs for calling C/C++ code
- `pack(fmt, variables)`
- `unpack(fmt, buffer)`
- `calcsize(fmt)` - return the size of the byte buffer that would be obtained by using the format
- ***todo: struct format string cheat sheet?***
- to align a structure to a specific type add the number `0` followed by the letter at the end of the format string
- use `=` to disable alignments and padding for any type
- `s`trings need the number of characters too
- also pascal style strings for some reason

## course 13 - c/c++ bindings - ctype

- create wrappers over c/c++ types
- methods for working with pointers and c-strings
- `c_<type>` for type `<type>`
  - for example, `c_uint` for `unsigned int`
- `value` member 
- beware: normal chars are `byte`s
- `pointer` function: create a pointer from a ctype object
  - `ptr_i.contents.value`
- `byref` function: create a reference - faster, apparently
  - `ref_i._obj.value` ?
- c structures: derive `Structure`
  - `_fields_` - list of `(name, ctype_class)` tuples
  - for each field, `.offset` and `.size` are also methods
  - can use `*` operator for a 1d array: `('n', ctypes.c_long * 10)` is equivalent to `long n[10];`
  - can use `ctyles.POINTER(ctype_class)` to make a pointer for a type
  - you can also have a member that's another `Structure`
  - can use a 3-long tuple to specify... bits or something? `('bit_0', ctypes.c_int, 1)`
- `Union` - same but union
- there is a `cast(var, type)` function
