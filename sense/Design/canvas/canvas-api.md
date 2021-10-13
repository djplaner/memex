## Canvas LMS API

### Resources

- [Canvas LMS API documentation](https://canvas.instructure.com/doc/api/)
- Python wrappers
    - [UCFOpen Canvas API](https://github.com/ucfopen/canvasapi) and [pip install/docs](https://canvasapi.readthedocs.io/en/stable/getting-started.html) - Python API wrapper, used in other projectss e.g. [Canvas Grab](https://github.com/skyzh/canvas_grab) - grab all files on Canvas LMS to local directory
    - [canvas-lms-api](https://pypi.org/project/canvas-lms-api/) - on github enterprise
- Tutorials
    - [Simple Python get script](https://community.canvaslms.com/t5/Canvas-Developers-Group/A-Simple-Python-GET-Script/ba-p/273742) - basic tutorial - fairly limited
    - [Get started with the Canvas API](https://learninganalytics.ubc.ca/for-students/canvas-api/) - from UBC - much better
        - the initial api URL used in this doesn't appear to work    
    - [Canvas APIs: Getting started](https://community.canvaslms.com/t5/Canvas-Developers-Group/Canvas-APIs-Getting-started-the-practical-ins-and-outs-gotchas/ba-p/263685) - better intro, quite detailed

### Details

Anyone, including students can use the API. But only as permitted via the Web interface.

### Process

1. Get access token.
2. Identify the URL/API to be called
3. Make the call
4. Handle requests
