---
title:  "C++ rvalue references and move semantics for beginners"
published: true
---

The logic behind *rvalues* is that in C++ you will find such temporary, short-lived values
that you cannot alter in any way.

```cpp
int x = 666;                    // (1)
int y = x + 5;                  // (2)

std::string s1 = "hello ";
std::string s2 = "world";
std::string s3 = s1 + s2;       // (3)

std::string getString() {
  return "hello world";
}
std::string s4 = getString();   // (4)
```

## Introducing the magic of rvalue references

The traditional C++ rules say that you are allowed to take the address of an rvalue only
if you store it in a **const** variable. More technically, *you are allowed to bind a
const lvalue to an rvalue*.

```cpp
int& x = 666;       // Error
const int& x = 666; // OK
```

C++0x has introduced a new type called **rvalue reference**, denoted by placing a double
ampersand `&&` after some type. Such rvalue reference lets you modify the value of a
temporary object: it's like removing the `const` attribute.

```cpp
std::string   s1     = "Hello ";
std::string   s2     = "world";
std::string&& s_rref = s1 + s2;    // the result of s1 + s2 is an rvalue
s_rref += ", my friend";           // I can change the temporary string!
std::cout << s_rref << '\n';       // prints "Hello world, my friend"
```

## Move semantics

Move semantics is a new way of moving resources around in an optimal way by avoid
unnecessary copies of temporary objects, based on rvalue references.

```cpp
class Holder
{
  public:

    Holder(int size)         // Constructor
    {
      m_data = new int[size];
      m_size = size;
    }

    ~Holder()                // Destructor
    {
      delete[] m_data;
    }

  private:

    int*   m_data;
    size_t m_size;
};
```

### Rule of Three

If your class defines one or more of the following methods, it should probably explicitly
define all three

- destructor
- copy constructor
- copy assignment operator

### Implementing the copy constructor

The copy constructor is used to create a new object from another existing object.

```cpp
Holder h1(10000); // regular constructor
Holder h2 = h1;   // copy constructor
Holder h3(h1);    // copy constructor (alternate syntax)
```

```cpp
Holder(const Holder& other)
{
  m_data = new int[other.m_size];  // (1)
  std::copy(other.m_data, other.m_data + other.m_size, m_data);  // (2)
  m_size = other.m_size;
}
```

### Implementing the assignment operator

```cpp
Holder h1(10000);  // regular constructor
Holder h2(60000);  // regular constructor
h1 = h2;           // assignment operator
```

```cpp
Holder& operator=(const Holder& other) 
{
  if(this == &other) return *this;  // (1)
  delete[] m_data;  // (2)
  m_data = new int[other.m_size];
  std::copy(other.m_data, other.m_data + other.m_size, m_data);
  m_size = other.m_size;
  return *this;  // (3)
}
```

### The limitations of our current class design

```cpp
Holder createHolder(int size)
{
  return Holder(size);
}
```

It returns a `Holder` object `by value`. We know that when a function returns an object by
value, the compiler has to create a temporary object (rvalue). Our `Holder` is a
heavy-weight object due to its internal memory allocation, which is a very expensive task:
returning such things by value with our current class design would trigger multiple
expensive memory allocations.

```cpp
int main()
{
  Holder h = createHolder(1000); // Copy constructor
  h = createHolder(500);         // Assignment operator
}
```

### Implementing move semantics with rvalue references

The idea of move semantics is to add new versions of the copy constructor and assignment
operator so that they can take a temporary object in input to steal data from.

#### Rule of Five

Any class for which move semantics are desirable, has to declare two additional member
functions

- the **move constructor** - to constructor new objects by stealing data from temporaries
- the **move assignment operator** - to replace existing objects by stealing data from
  temporaries

### Implementing the move constructor

```cpp
Holder(Holder&& other)     // <-- rvalue reference in input
{
  m_data = other.m_data;   // (1)
  m_size = other.m_size;
  other.m_data = nullptr;  // (2)
  other.m_size = 0;
}
```

### Implementing the move assignment operator

```cpp
Holder& operator=(Holder&& other)     // <-- rvalue reference in input  
{  
  if (this == &other) return *this;

  delete[] m_data;         // (1)

  m_data = other.m_data;   // (2)
  m_size = other.m_size;

  other.m_data = nullptr;  // (3)
  other.m_size = 0;

  return *this;
}
```

```cpp
int main()
{
  Holder h1(1000);                // regular constructor
  Holder h2(h1);                  // copy constructor (lvalue in input)
  Holder h3 = createHolder(2000); // move constructor (rvalue in input) (1) 

  h2 = h3;                        // assignment operator (lvalue in input)
  h2 = createHolder(500);         // move assignment operator (rvalue in input)
}
```

### Can I move lvalues?

```cpp
int main()
{
  Holder h1(1000);     // h1 is an lvalue
  Holder h2(h1);       // copy-constructor invoked (because of lvalue in input)
}
```

```cpp
int main()
{
  Holder h1(1000);           // h1 is an lvalue
  Holder h2(std::move(h1));  // move-constructor invoked (because of rvalue in input)
}
```

References:

- [https://www.internalpointers.com/post/c-rvalue-references-and-move-semantics-beginners](https://www.internalpointers.com/post/c-rvalue-references-and-move-semantics-beginners)