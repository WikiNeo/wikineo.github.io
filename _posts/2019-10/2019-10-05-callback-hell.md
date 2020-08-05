---
title: "Managing Node.js Callback Hell with Promises, Generators and Other Approaches"
published: true
tags: Node.js
---

## The problem

Let's say we want to write a module that finds the largest file within a directory

```javascript
var findLargest = require('./findLargest')
findLargest('./path/to/dir', function (er, filename) {
  if (er) return console.error(er)
  console.log('largest file was:', filename)
})
```

Let's break down the steps to accomplish this:

- Read the files in the provided directory
- Get the stats on each file in the directory
- Determine which is largest (pick one if multiple have the same size)
- Callback with the name of the largest file

If an error occurs at any point, callback with that error instead. We also should never
call the callback more than once.

## A nested approach

```javascript
var fs = require('fs')
var path = require('path')

module.exports = function (dir, cb) {
  fs.readdir(dir, function (er, files) { // [1]
    if (er) return cb(er)
    var counter = files.length
    var errored = false
    var stats = []

    files.forEach(function (file, index) {
      fs.stat(path.join(dir,file), function (er, stat) { // [2]
        if (errored) return
        if (er) {
          errored = true
          return cb(er)
        }
        stats[index] = stat // [3]

        if (--counter == 0) { // [4]
          var largest = stats
            .filter(function (stat) { return stat.isFile() }) // [5]
            .reduce(function (prev, next) { // [6]
              if (prev.size > next.size) return prev
              return next
            })
          cb(null, files[stats.indexOf(largest)]) // [7]
        }
      })
    })
  })
}
```

- Read all the files inside the directory
- Gets the stats on each file. This is done in parallel so we are using a **counter** to
  track when all the I/O has finished. We are also using a **errored** boolean to prevent
  the provided callback (**cb**) from being called more than once if an error occurs.
- Collect the stats for each file. Notice we are setting up a parallel array here.
- Check to see if all parallel operations have completed.
- Only grab regular files (not links or directories, etc).
- Reduce the list to the largest file.
- Pull the filename associated with the stat and callback.

This may be a perfectly fine approach to solving this problem. However, its tricky to
manage the parallel operation and ensure we only callback once.

## A modular approach

Our nested approach can be broken out into tree modular units:

- Grabbing the files from a directory.
- Grabbing the stats for those files.
- Processing the stats and files to determine the largest.

```javascript
unction getStats (paths, cb) {
  var counter = paths.length
  var errored = false
  var stats = []
  paths.forEach(function (path, index) {
    fs.stat(path, function (er, stat) {
      if (errored) return
      if (er) {
        errored = true
        return cb(er)
      }
      stats[index] = stat
      if (--counter == 0) cb(null, stats)
    })
  })
}
```

```javascript
function getLargestFile (files, stats) {
  var largest = stats
    .filter(function (stat) { return stat.isFile() })
    .reduce(function (prev, next) {
      if (prev.size > next.size) return prev
      return next
    })
    return files[stats.indexOf(largest)]
}
```

```javascript
var fs = require('fs')
var path = require('path')

module.exports = function (dir, cb) {
  fs.readdir(dir, function (er, files) {
    if (er) return cb(er)
    var paths = files.map(function (file) { // [1]
      return path.join(dir,file)
    })

    getStats(paths, function (er, stats) {
      if (er) return cb(er)
      var largestFile = getLargestFile(files, stats)
      cb(null, largestFile)
    })
  })
```

- Generate a list of paths from the files and directory

A modular approach makes the reusing and testing method easier. The main export is easier
to reason about as well. However, we are still manually managing the parallel stat task.

## An async Approach

```javascript
var fs = require('fs')
var async = require('async')
var path = require('path')

module.exports = function (dir, cb) {
  async.waterfall([ // [1]
    function (next) {
      fs.readdir(dir, next)
    },
    function (files, next) {
      var paths =
       files.map(function (file) { return path.join(dir,file) })
      async.map(paths, fs.stat, function (er, stats) { // [2]
        next(er, files, stats)
      })
    },
    function (files, stats, next) {
      var largest = stats
        .filter(function (stat) { return stat.isFile() })
        .reduce(function (prev, next) {
        if (prev.size > next.size) return prev
          return next
        })
        next(null, files[stats.indexOf(largest)])
    }
  ], cb) // [3]
}
```

- `async.waterfall` provides a series flow of execution where data from one operation can
  be passed to the next function in the series using the **next** callback.
- `async.map` let us run fs.stat over a set of paths in parallel and calls back with an
  array (with order maintained) of the results.
- The **cb** function will be called either after the last step has completed or if any
  error has occurred along the way. It will only be called once.

The async module guarantees only one callback will be fired. It also propagates errors and
manages parallelism for us.

## A promises approach

```javascript
var fs = require('fs')
var path = require('path')
var Q = require('q')
var fs_readdir = Q.denodeify(fs.readdir) // [1]
var fs_stat = Q.denodeify(fs.stat)

module.exports = function (dir) {
  return fs_readdir(dir)
    .then(function (files) {
      var promises = files.map(function (file) {
        return fs_stat(path.join(dir,file))
      })
      return Q.all(promises).then(function (stats) { // [2]
        return [files, stats] // [3]
      })
    })
    .then(function (data) { // [4]
      var files = data[0]
      var stats = data[1]
      var largest = stats
        .filter(function (stat) { return stat.isFile() })
        .reduce(function (prev, next) {
        if (prev.size > next.size) return prev
          return next
        })
      return files[stats.indexOf(largest)]
    })
```

- Since Node core functionality isn't promise-aware, we make it so.
- `Q.all` will run all the stat calls in parallel and the result array order is maintained.
- Since we want to pass files and stats to the next **then** function, it's the last thing
  returned.

```javascript
var findLargest = require('./findLargest')
findLargest('./path/to/dir')
  .then(function (filename) {
    console.log('largest file was:', filename)
  })
  .catch(console.error)
```

## A generators approach

```javascript
var co = require('co')
var thunkify = require('thunkify')
var fs = require('fs')
var path = require('path')
var readdir = thunkify(fs.readdir)
var stat = thunkify(fs.stat)

module.exports = co(function* (dir) { // [2]
  var files = yield readdir(dir) // [3]
  var stats = yield files.map(function (file) { // [4]
    return stat(path.join(dir,file))
  })
  var largest = stats
    .filter(function (stat) { return stat.isFile() })
    .reduce(function (prev, next) {
      if (prev.size > next.size) return prev
      return next
    })
  return files[stats.indexOf(largest)] // [5]
})
```

- Since node core functionality isn't "thunk"-aware, we make it so.
- `co` takes a generator function which can be suspended at anytime using the **yield**
  keyword.
- The generator function will suspend until readdir returns. The result value is assigned
  to the **files** variable.
- `co` can also handle arrays a set of parallel operations to perform. A result array with
  order maintained is assigned to **stats**.
- The final result is returned.

```javascript
try {
  var files = yield readdir(dir)
} catch (er) {
  console.error('something happened whilst reading the directory')
}
```

References:

- [https://strongloop.com/strongblog/node-js-callback-hell-promises-generators/](https://strongloop.com/strongblog/node-js-callback-hell-promises-generators/)
