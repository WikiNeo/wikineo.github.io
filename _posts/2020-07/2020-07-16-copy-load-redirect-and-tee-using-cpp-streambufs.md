---
title: "Copy, load, redirect and tee using C++ streambufs"
published: true
---

## Copy streams

```cpp
void stream_copy(std::ostream & dst, std::istream & src)
{
    dst << src.rdbuf();
}
```

How does this work? `std::stream` derives from `std::ios`, and `ios::rdbuf()`
returns a pointer to the source stream's buffer. A suitable specialization of
`ostream::operator<<()` reads from this buffer until the source stream empties.
Note that `stream_copy` typically does no result in the entire content of either
the source or destination stream being held in memory at any one time --
everything goes through the stream buffers in the usual way. Except, of course,
if we're using an in-memory `std::stringstream`, used below to load the content
of a file into a string.

## Load streams

```cpp
// Return a named file's contents as a string
std::string load_file(char const * filepath)
{
    std::ifstream src(filepath);
    std::ostringstream buf;
    buf << src.rdbuf();
    return buf.str();
}
```

I've used this simle recipe in test code to load binary data from a file.

## Redirect streams

To redirect the output of a program to a log file

```bash
$ echo Hello, world! > hello-world.log
$ cat hello-world.log
Hello, world!
```

Stream buffers allow for more flexible stream redirection from within the
program, once again using `ios::rdbuf()`, this time to both get and set a
steam's buffer.

Here's a simple redirecter class, designed for use on the stack, allowing the
constructor and destructor to execute around a block of code

```cpp
#include <ostream>

// Stream redirecter.
class redirecter
{
public:
    // Constructing an instance of this class causes
    // anything written to the source stream to be redirected
    // to the destination stream.
    redirecter(std::ostream & dst, std::ostream & src)
        : src(src)
        , srcbuf(src.rdbuf())
    {
        src.rdbuf(dst.rdbuf());
    }
    
    // The destructor restores the original source stream buffer
    ~redirecter()
    {
        src.rdbuf(srcbuf);
    }
private:
    std::ostream & src;
    std::streambuf * const srcbuf;
};
```

Incidentally, when `ios.rdbuf()` is used in set mode it returns the original
value of the stream's buffer, allowing us to write a slightly more compact
constructor as show in the complete program below.

```cpp
#include <fstream>
#include <iostream>

class redirecter
{
public:
    redirecter(std::ostream & dst, std::ostream & src)
        : src(src), sbuf(src.rdbuf(dst.rdbuf())) {}
    ~redirecter() { src.rdbuf(sbuf); }
private:
    std::ostream & src;
    std::streambuf * const sbuf;
};

void hello_world()
{
    std::cout << "Hello, world!\n";
}

int main()
{
    std::ofstream log("hello-world.log");
    redirecter redirect(log, std::cout);
    hello_world();
    return 0;
}
```

Running this program prints nothing to standard output. Instead the file
`hello-world.log` contains the redirected output, `Hello, world!`.

Note that `redirect` will be destroyed before `log`, thus restoring
`std::cout`'s original buffer. This detail is crucial, since destroying the file
closes it and destroys its stream buffer, so we must not allow `std::cout` to
continue using this buffer.

## Tee streams

You could argue the redirection example is somewhat contrived. if
`hello_world()` had been properly written to accept an `ostream` as a function
argument, rather than rely on the global `std::count`, then we could simply pas
it the `ofstream` of our choice and be done. We could equally pass it an
`ostringstream` and check the contents of this stream to test that
`hello_world()` does indeed print what it's supposed to.

How about teeing streams? In a command shell the standard `tee` connector allows
us to replicate a stream. The snippet blow shows the output from `echo`
appearing on standard output and teed to a log file.

```bash
$ echo Hello, world! | tee hello-world.log
Hello, world!
$ cat hello-world.log 
Hello, world!
```

Within a program, a clever stream buffer customization can do the same job.
Here's the declaration of a minimal teebuf class, which specializes a standard
streambuf. The idea is that we can assign such a teebuf to a stream, causing
anything written to the stream to be derived through both teed output buffers.

```cpp
#include <streambuf>

class teebuf: public std::streambuf
{
public:
    // Construct a streambuf which tees output to both input
    // streambufs.
    teebuf(std::streambuf * sb1, std::streambuf * sb2);
protected:
    virtual int overflow(int char);
private:
    std::streambuf * sb1;
    std::streambuf * sb2;
};
```

Before fleshing out the implementation, I'd like to discuss what lies beneath
the surface of this simple declaration. We're specializing a `std::streambuf`,
which is itself a typdef for `basic_streambuf<char>`. We'll show how to make
this code more generic later.

The base class, `std::streambuf`, despite its name, has no buffer. This base
class provides two public member functions for outputting character data,
`sputc` and `sputn`, which ouput a single character a run of characters
respectively. If the internal buffer is full (always the case here, since there
is no buffer) then the virtual `overflow` method ends up being called. Thus a
suitable override of this method will do the job.

You may wonder why `overflow` deals in `ints` and not `chars`. That's because,
in the case of an error, it returns a sentinel value, `EOF`, which does not fit
in a `char`. (More generically, it deals with `traits::int_types` and returns a
`trait::eof()` to indicate an error condition).

Here's `teebuf` implementation. I have changed both `overflow` to be private
which stops anyone deriving from this class. Any actual buffering will be
delegated to the teed buffers. We've also over-ridden the virtual `sync()`
method: the default implementation does nothing, but here we sync the teed
buffers. I can't see any way the (c == EOF) test could ever return `true` for
instances of this class but I've followed the advice from the footnote in the
standard anyway.

```cpp
#include <streambuf>

class teebuf: public std::streambuf
{
public:
    // Construct a streambuf which tees output to both input
    // streambufs.
    teebuf(std::streambuf * sb1, std::streambuf * sb2)
        : sb1(sb1)
        , sb2(sb2)
    {
    }
private:
    // This tee buffer has no buffer. So every character "overflows"
    // and can be put directly into the teed buffers.
    virtual int overflow(int c)
    {
        if (c == EOF)
        {
            return !EOF;
        }
        else
        {
            int const r1 = sb1->sputc(c);
            int const r2 = sb2->sputc(c);
            return r1 == EOF || r2 == EOF ? EOF : c;
        }
    }
    
    // Sync both teed buffers.
    virtual int sync()
    {
        int const r1 = sb1->pubsync();
        int const r2 = sb2->pubsync();
        return r1 == 0 && r2 == 0 ? 0 : -1;
    }   
private:
    std::streambuf * sb1;
    std::streambuf * sb2;
};
```

Here's a simple helper class to create a tee stream from two input streams.

```cpp
class teestream : public std::ostream
{
public:
    // Construct an ostream which tees output to the supplied
    // ostreams.
    teestream(std::ostream & o1, std::ostream & o2);
private:
    teebuf tbuf;
};

teestream::teestream(std::ostream & o1, std::ostream & o2)
  : std::ostream(&tbuf)
  , tbuf(o1.rdbuf(), o2.rdbuf())
{
}
```

Here's a short program showing how to use these elements

```cpp
#include <fstream>
#include <iostream>
#include <teestream>

int main()
{
    std::ofstream log("hello-world.log");
    teestream tee(std::cout, log);
    tee << "Hello, world!\n";
    return 0;
}
```

Running this program prints the message `Hello, world!` followed by a newline to
standard output, and the file `hello-world.log` contains this same output.

## A generic version

```cpp
template <typename char_type,
          typename traits = std::char_traits<char_type> >
class basic_teebuf:
    public std::basic_streambuf<char_type, traits>
{
public:
    typedef typename traits::int_type int_type;
    
    basic_teebuf(std::basic_streambuf<char_type, traits> * sb1,
                 std::basic_streambuf<char_type, traits> * sb2)
      : sb1(sb1)
      , sb2(sb2)
    {
    }
    
private:    
    virtual int sync()
    {
        int const r1 = sb1->pubsync();
        int const r2 = sb2->pubsync();
        return r1 == 0 && r2 == 0 ? 0 : -1;
    }
    
    virtual int_type overflow(int_type c)
    {
        int_type const eof = traits::eof();
        
        if (traits::eq_int_type(c, eof))
        {
            return traits::not_eof(c);
        }
        else
        {
            char_type const ch = traits::to_char_type(c);
            int_type const r1 = sb1->sputc(ch);
            int_type const r2 = sb2->sputc(ch);
            
            return
                traits::eq_int_type(r1, eof) ||
                traits::eq_int_type(r2, eof) ? eof : c;
        }
    }
    
private:
    std::basic_streambuf<char_type, traits> * sb1;
    std::basic_streambuf<char_type, traits> * sb2;
};

typedef basic_teebuf<char> teebuf;
```

## References

- [http://wordaligned.org/articles/cpp-streambufs#toctee-streams](http://wordaligned.org/articles/cpp-streambufs#toctee-streams)