---
title: Returning objects from an arrow function
tags: Javascript
---

When using an arrow function in JavaScript, I was expecting to be able to return objects, but ended up with returning `undefined` values.

Turns out it's not possible to return directly objects from inside the arrow function because they're confused as statements.

This is [covered by MDN](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions#function_body).

To return an object, I had to **put it inside parenthesis, like this**:

```js
latlngs.map(({ lat, lng }) => ({ lat, lng }))
```
