---
title: "JavaScript Adapter"
published: false
---

The adapter pattern allows us to access the functionality of an object using a
different interface. As the name suggests, it adapts an object so that if can be
used by components  expecting a different interface.

The Adapter is essentially a wrapper for the Adaptee, exposing a different
interface. The operations of the Adapter can also be a composition of one or
more method invocations on the Adaptee.

## Using LevelUP through the filesystem API

We are now going to build an Adapter around the LevelUP API, transforming it
into an interface that is compatible with the core `fs` module. In particular,we
will  make sure that every call to `readFile()` and `writeFile()` will translate
into calls to `db.get()` and `db.put()`; this way we will be able to use a
LevelUP database as a storage backend for simple filesystem operation.

```javascript
const path = require('path')

module.exports = function createFsAdapter(db){
    const fs = {}

    fs.readFile = (filename, options, callback) => {
        if(typeof options === 'function'){
            callback = options
            options = {}
        } else if (typeof options === 'string'){
            options = {encoding: options}
        }

        db.get(path.resolve(filename), {
            valueEncoding: options.encoding
        }, (err, value) => {
            if(err) {
                if (err.type === 'NotFoundError'){
                    err = new Error(`ENOENT, open "${filename}"`)
                    err.code = 'ENOENT'
                    err.errno = 34
                    err.path = filename
                }
                return callback && callback(err)
            }
            callback && callback(null, value)
        })
    }

    fs.writeFile = (fileName, contents, options, callback) => {
        if(typeof options === 'function'){
            callback = options
            options = {}
        } else if (typeof options === 'string'){
            options = {encoding: options}
        }

        db.put(path.resolve(filename), contents, {
            valueEncoding: options.encoding
        }, callback);
    }

    return fs;
}
```

Our new adapter is now ready; we now write a small test module.

```javascript
const fs = require('fs')

fs.writeFile('file.txt', 'Hello!', () => {
    fs.readFile('file.txt', {encoding: 'utf8'}, (err, res) => {
        console.log(res)
    })
})

// try to read a missing file
fs.readFile('missing.txt', {encoding: 'utf8'}, (err, res) => {
    console.log(err)
})
```

Now, we can try to replace the `fs` module with our adapter

```javascript
const levelup = require('level')
const fsAdapter = require('./fsAdapter')
const db = levelup('./fsDB', {valueEncoding: 'binary'});
const fs = fsAdapter(db);
```

## References

- Node.js Design Patterns
