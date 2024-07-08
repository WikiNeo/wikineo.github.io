---
title: "Bluebird - Why Promises?"
published: true
tags: Node.js
---

You should use promises to turn this:

```javascript
fs.readFile("file.json", function (err, val) {
    if (err) {
        console.error("unable to read file");
    }
    else {
        try {
            val = JSON.parse(val);
            console.log(val.success);
        }
        catch (e) {
            console.error("invalid json in file");
        }
    }
});
```

Into this:

```javascript
fs.readFileAsync("file.json").then(JSON.parse).then(function (val) {
    console.log(val.success);
})
.catch(SyntaxError, function (e) {
    console.error("invalid json in file");
})
.catch(function (e) {
    console.error("unable to read file");
});
```

You might notice that the promise approach looks very similar to using
synchronous I/O:

```javascript
try {
    var val = JSON.parse(fs.readFileSync("file.json"));
    console.log(val.success);
}
// Gecko-only syntax; used for illustrative purposes
catch (e if e instanceof SyntaxError) {
    console.error("invalid json in file");
}
catch (e) {
    console.error("unable to read file");
}
```

This is the point - to have something that works like the `return` and `throw`
in synchronous code.

You can also use promises to improve code that was written with callbacks:

```javascript
//Copyright Plato https://stackoverflow.com/a/19385911/995876
//CC BY-SA 2.5
mapSeries(URLs, function (URL, done) {
    var options = {};
    needle.get(URL, options, function (error, response, body) {
        if (error) {
            return done(error);
        }
        try {
            var ret = JSON.parse(body);
            return done(null, ret);
        }
        catch (e) {
            done(e);
        }
    });
}, function (err, results) {
    if (err) {
        console.log(err);
    } else {
        console.log('All Needle requests successful');
        // results is a 1 to 1 mapping in order of URLs > needle.body
        processAndSaveAllInDB(results, function (err) {
            if (err) {
                return done(err);
            }
            console.log('All Needle requests saved');
            done(null);
        });
    }
});
```

This is far more readable when done with promise:

```javascript
Promise.promisifyAll(needle);
var options = {};

var current = Promise.resolve();
Promise.map(URLs, function (URL) {
    current = current.then(function () {
        return needle.getAsync(URL, options);
    });
    return current;
}).map(function (responseAndBody) {
    return JSON.parse(responseAndBody[1]);
}).then(function (results) {
    return processAndSaveAllInDB(results);
}).then(function () {
    console.log('All Needle requests saved');
}).catch(function (e) {
    console.log(e);
});
```

## References

- [https://bluebirdjs.com/docs/why-promises.html](https://bluebirdjs.com/docs/why-promises.html)