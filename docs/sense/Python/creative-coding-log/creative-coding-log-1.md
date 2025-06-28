---
backlinks:
- title: Creative coding log 2
  url: /memex/sense/Python/creative-coding-log/creative-coding-log-2.html
tags: creativeCoding, python
title: Creative coding log 1
type: note
---
## Getting set up

1. New repo
2. Virtual environment with venv
3. Project structure [following this advice](https://packaging.python.org/en/latest/tutorials/packaging-projects/)

    Which is probably over kill

## First program

Following the [getting started tutorial](https://docs.manim.community/en/stable/tutorials/quickstart.html)

??? note "Structure of manim code"

    At a minimum, Manim code needs to have a class that inherits from `Scene` and a method called `construct`. The `construct` method is where the animation is written.

    Calling the `play` method appropriately contributed to animation.

    Tutorial uses `scene.py` reinforcing this is about producing animations and in particular a scene


## Manim conceptual model

- `Scene` describes/creates the video produced by Manim. 

    Your video is a class that inherits from `Scene`. The constructor will populate the scene. 
    
- _Mobjects_ are added (displayed) and removed from the scene 
- any/every animation has to be _played_ using the Scene's `play` method
- `wait` specifies a period of time where no change happens
    and eventually use the `play` method to play a particular animation (and produce the video or other outputs).  All of the uses of the `play` method are animated in sequence as they appear in the constructor.

Scenes can contain one or more `Mobjects` (mathematical objects).

_Creating_ a `Mobject` creates the object, but does not show it in the scene. It appears you need to call a `Create` function with the object as an argument.

| Concept | Description |
| --- | --- |
| `Scene` | Describes/creates the video produced by Manim. Your video is a class that inherits from `Scene`. The constructor will populate the scene and eventually use the `play` method to play a particular animation (and produce the video or other outputs).  All of the uses of the `play` method are animated in sequence as they appear in the constructor. |
| [`Mobject`](https://docs.manim.community/en/stable/tutorials/building_blocks.html#mobjects) | (Mathematical) object that can be displayed. |
| Sections | Way to split a Scene into multiple output videos |

### Coordinate system

(0,0) in Manim is the centre of the screen

### Output settings

`manim -pql hello.py SquareToCircle` is one of the example command lines above

- `-pql` are the output settings
- `hello.py` is the Python file I created
- `SquareToCircle` is one of the classes in the Python file

| Setting | Description |
| --- | --- |
| `p` | Preview the animation once it renders |
| `ql` | Render at a low quality (480p15 fps) |
| `qm` | Render at a medium quality (720p30) |
| `qh` | Render at a high quality (1080p60) |
| `a` | Render all scenes (as separate videos)

See [configuration guide](https://docs.manim.community/en/stable/guides/configuration.html) for more

### Manipulating Mobjects

#### Adding them

Not visible until added to the scene

- `self.add` - `Scene` method, can take multiple mobjects
- `self.play( Create(<mobject>))` - playing the animation of creating it

#### Mobject properties

##### Coordinates

There are methods to get the coordinators of a mobject (e.g., `get_center`)

#### Moving mobjects


#### Styling mobjects

#### Animating objects

Animation is done by interpolation. Any property of a mobject that can be changed, can be animated (by adding `.animate` before the call to change the property ).

Create custom annimations by extending the `Animation` class and overriding the `interpolate_mobject` method.

`Transform` function will transform one mobject into another.

## Plugins

There are [plugins](https://plugins.manim.community/) - but not many and early exploration finds them all in early days.  

[RevalJS plugin](https://pypi.org/project/manim-revealjs/) looks interesting.