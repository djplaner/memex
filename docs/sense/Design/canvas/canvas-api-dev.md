﻿---
title: Canvas API dev
---
Resources and approaches to using the Canvas API.

[Canvas Live API](https://lms.griffith.edu.au/doc/api/live)

## How to, guides and tutorials

### [ubccapico/getting-started-with-the-canvas-api-with-node](https://github.com/ubccapico/getting-started-with-the-canvas-api-with-node)

Script and tutorial to get started with node/javascript.
 
Possibly not an approach usable within the browser - question of API token

## Javascript libraries 

### [beardon/canvas-lms-api](https://github.com/beardon/canvas-lms-api)

Another promise wrapper. Perhaps a bit more along the way than following. But is aging, no longer maintained by the company.

### [artevelde-uas/canvas-lms-api](https://github.com/artevelde-uas/canvas-lms-api)

Simple(istic?) promise wrapper. Might be bare bones enough?

From Arevelde University (Belgium), one developer

### [ubccapico/node-canvas-api](https://github.com/ubccapico/node-canvas-api)

Specifically for Node.js. Appears to be more widely used. UBC is source

## Exploration

Using [where-am-i](https://github.com/msdlt/canvas-where-am-I/blob/master/canvas-where-am-I.js) as example.

uses function ```ou_getCsrfToken``` to apparently get the necessary token and then uses fetch as a basis for promise driven.

Which extracts the token from the users cookies

```Javascript
  function ou_getCsrfToken() {
        var csrfRegex = new RegExp('^_csrf_token=(.*)$');
        var csrf;
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            var match = csrfRegex.exec(cookie);
            if (match) {
                csrf = decodeURIComponent(match[1]);
                break;
            }
        }
        return csrf;
    }
```