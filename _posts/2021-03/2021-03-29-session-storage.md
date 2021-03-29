---
title: 'Window.sessionStorage'
published: true
tags: Web
---

The read-only `sessionStorage` property accesses as session `Storage` object for
the current `origin`. `sessionStorage` is similar to `localStorage`; the
difference is that while data in `localStorage` doesn't expire, data in
`sessionStorage` is cleared when the page session ends.

- Whenever a document is loaded in a particular tab in the browser, a unique
  page session gets created and assigned to that particular tab. That page
  session is valid only for that particular tab.
- A page session lasts as long as the tab or the browser is open and survives
  over page reloads and restores.
- Opening a page in a new tab or window creates a new session with the value of
  the top-level browsing context, which differs from how session cookies work.
- Opening multiple tabs/windows with the same URL creates `sessionStorage` for
  each tab/window.
- Closing a tab/widows ends the session and clears objects in `sessionStorage`

## Example

### Basic usage

```javascript
// Save data to sessionStorage
sessionStorage.setItem('key', 'value');

// Get saved data from sessionStorage
let data = sessionStorage.getItem('key');

// Remove saved data from sessionStorage
sessionStorage.removeItem('key');

// Remove all saved data from sessionStorage
sessionStorage.clear();
```

## Save text between refreshes

```javascript
// Get the text field that we're going to track
let field = document.getElementById("field");

// See if we have an autosave value
// (this will only happen if the page is accidentally refreshed)
if (sessionStorage.getItem("autosave")) {
  // Restore the contents of the text field
  field.value = sessionStorage.getItem("autosave");
}

// Listen for changes in the text field
field.addEventListener("change", function() {
  // And save the results into the session storage object
  sessionStorage.setItem("autosave", field.value);
});
```

## Reference

- [https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/sessionStorage)