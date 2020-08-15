# Blogs

## Start

```bash
docker-compose up
```

## Generate Tags

Note the extra `/` for Windows

```bash
docker run --rm -v /"$PWD"://usr/src/app -w //usr/src/app python:3 python tag_generator.py
```

## References

- [github/personal-website](https://github.com/github/personal-website)
- [Jekyll Tags on Github Pages](https://longqian.me/2017/02/09/github-jekyll-tag/)