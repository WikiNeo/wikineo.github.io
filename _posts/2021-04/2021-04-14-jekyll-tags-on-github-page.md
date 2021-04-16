---
title: 'Jekyll Tags on Github Page'
published: false
tags: Web
---

## 0. Introduction

We try to add tag/tags to the post and show the list of tags on the left of the
Github Page website.

## 1. Add tag/tags to the post

Add tag to front matter section.

```markdown
---
title: 'Jekyll Tags on Github Page'
published: true
tags: Web
---
```

Multiple tags are separated by white space.

## 2. Collect tags of all posts

We need a list named `site.tags`. We will use
[Liquid](https://shopify.github.io/liquid/) to do this.

In the `_includes` folder, add an html file called `collecttags.html`

```html
{% assign rawtags = "" %}
{% for post in site.posts %}
  {% assign ttags = post.tags | join:'|' | append:'|' %}
  {% assign rawtags = rawtags | append:ttags %}
{% endfor %}
{% assign rawtags = rawtags | split:'|' | sort %}

{% assign site.tags = "" %}
{% for tag in rawtags %}
  {% if tag != "" %}
    {% if tags == "" %}
      {% assign tags = tag | split:'|' %}
    {% endif %}
    {% unless tags contains tag %}
      {% assign tags = tags | join:'|' | append:'|' | append:tag | split:'|' %}
    {% endunless %}
  {% endif %}
{% endfor %}
```

## 3. Execute the script

Insert the folllowing to `_includes/head.html`

```html
{% if site.tags != "" %}
  {% include collecttags.html %}
{% endif %}
```

## 4. Display tag/tags of a post

Add the following to `_layouts/post`

```html
<span>[
  {% for tag in page.tags %}
    {% capture tag_name %}{{ tag }}{% endcapture %}
    <a href="/tag/{{ tag_name }}"><code class="highligher-rouge"><nobr>{{ tag_name }}</nobr></code>&nbsp;</a>
  {% endfor %}
]</span>
```

## 5. Generate the tag page

Clicking on the tag should navigate to a tag page.

### 5.1 Define the layout of tag page

`_layouts/tagpage.html`

```html
---
layout: default
---
<div class="post">
    <h1>Tag: {{ page.tag }}</h1>
    <ul>
        {% for post in site.tags[page.tag] %}
        <li>{{ post.date | date: "%Y-%m-%d " }}<a href="{{ post.url }}">{{ post.title }}</a> <br>
            {{ post.description }}
        </li>
        {% endfor %}
    </ul>
</div>
<hr>
```

### 5.2 Auotmatic tag page creation

Read all tags in folder `_posts/` and generate tag page at `/tag`.

## Reference

- [https://longqian.me/2017/02/09/github-jekyll-tag/](https://longqian.me/2017/02/09/github-jekyll-tag/)