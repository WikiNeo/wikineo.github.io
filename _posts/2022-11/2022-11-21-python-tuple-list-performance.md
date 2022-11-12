---
title: 'Python tuple vs list Performance'
published: true
tags: Python
---

## Summary

Tuples tend to perform better than lists in almost every category:

1. Tuples can be constant folded.
2. Tuples can be reused instead of copied.
3. Tuples are compact and don't over-allocate.  
4. Tuples directly reference their elements.

## Tuples can be constant folded

Tuples of constants can be precomputed by Python's peephole optimizer or
AST-optimizer. Lists, on the other hand, get built-up from scratch:

```python
    >>> from dis import dis

    >>> dis(compile("(10, 'abc')", '', 'eval'))
      1           0 LOAD_CONST               2 ((10, 'abc'))
                  3 RETURN_VALUE   
 
    >>> dis(compile("[10, 'abc']", '', 'eval'))
      1           0 LOAD_CONST               0 (10)
                  3 LOAD_CONST               1 ('abc')
                  6 BUILD_LIST               2
                  9 RETURN_VALUE 
```

## Tuples do not need to be copied

Running `tuple(some_tuple)` returns immediately itself. Since tuples are
immutable, they do not have to be copied:

```python
>>> a = (10, 20, 30)
>>> b = tuple(a)
>>> a is b
True
```

In contrast, `list(some_list)` requires all the data to be copied to a new list:

```python
>>> a = [10, 20, 30]
>>> b = list(a)
>>> a is b
False
```

## Tuples do not over-allocate

Since a tuple's size is fixed, it can be stored more compactly than lists
which need to over-allocate to make `append()` operations efficient.

This gives tuples a nice space advantage:

```python
>>> import sys
>>> sys.getsizeof(tuple(iter(range(10))))
128
>>> sys.getsizeof(list(iter(range(10))))
200
```

Here is the comment from Objects/listobject.c that explains what lists are doing:

```c
/* This over-allocates proportional to the list size, making room
 * for additional growth.  The over-allocation is mild, but is
 * enough to give linear-time amortized behavior over a long
 * sequence of appends() in the presence of a poorly-performing
 * system realloc().
 * The growth pattern is:  0, 4, 8, 16, 25, 35, 46, 58, 72, 88, ...
 * Note: new_allocated won't overflow because the largest possible value
 *       is PY_SSIZE_T_MAX * (9 / 8) + 6 which always fits in a size_t.
 */
```

## Tuples refer directly to their elements

References to objects are incorporated directly in a tuple object. In
contrast, lists have an extra layer of indirection to an external array of
pointers.

This gives tuples a small speed advantage for indexed lookups and unpacking:

```bash
$ python3.6 -m timeit -s 'a = (10, 20, 30)' 'a[1]'
10000000 loops, best of 3: 0.0304 usec per loop
$ python3.6 -m timeit -s 'a = [10, 20, 30]' 'a[1]'
10000000 loops, best of 3: 0.0309 usec per loop

$ python3.6 -m timeit -s 'a = (10, 20, 30)' 'x, y, z = a'
10000000 loops, best of 3: 0.0249 usec per loop
$ python3.6 -m timeit -s 'a = [10, 20, 30]' 'x, y, z = a'
10000000 loops, best of 3: 0.0251 usec per loop
```

Here is how the `tuple (10, 20)` is stored:

```c
    typedef struct {
        Py_ssize_t ob_refcnt;
        struct _typeobject *ob_type;
        Py_ssize_t ob_size;
        PyObject *ob_item[2];     /* store a pointer to 10 and a pointer to 20 */
    } PyTupleObject;
```

Here is how the list `[10, 20]` is stored:

```c
    PyObject arr[2];              /* store a pointer to 10 and a pointer to 20 */

    typedef struct {
        Py_ssize_t ob_refcnt;
        struct _typeobject *ob_type;
        Py_ssize_t ob_size;
        PyObject **ob_item = arr; /* store a pointer to the two-pointer array */
        Py_ssize_t allocated;
    } PyListObject;
```

Note that the tuple object incorporates the two data pointers directly while
the list object has an additional layer of indirection to an external array
holding the two data pointers.

## Reference

- [https://stackoverflow.com/questions/68630/are-tuples-more-efficient-than-lists-in-python](https://stackoverflow.com/questions/68630/are-tuples-more-efficient-than-lists-in-python)