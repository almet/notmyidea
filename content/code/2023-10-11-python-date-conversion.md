---
title: Convert string to duration
tags: python, conversion
---

I found myself wanting to convert a string to a duration (int), for some configuration.

Something you can call like this:

```python
string_to_duration("1d", target="days") # returns 1
string_to_duration("1d", target="hours") # returns 24
string_to_duration("3m", target="hours") # returns 3 * 24 * 30
```

The code :

```python
from typing import Literal


def string_to_duration(value: str, target: Literal["days", "hours"]):
    """Convert a string to a number of hours, or days"""
    num = int("".join(filter(str.isdigit, value)))

    if target == "hours":
        reconvert = True

    if "h" in value:
        if target == "days":
            raise ValueError("Invalid duration value", value)
        num = num
        reconvert = False
    elif "d" in value:
        num = num
    elif "w" in value:
        num = num * 7
    elif "m" in value:
        num = num * 30
    elif "y" in value:
        num = num * 365
    else:
        raise ValueError("Invalid duration value", value)

    if target == "hours" and reconvert:
        num = num * 24

    return num
``````