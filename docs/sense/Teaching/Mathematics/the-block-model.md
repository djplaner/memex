---
backlinks:
- title: Predict Run Investigate Modify Make (PRIMM)
  url: /sense/Teaching/Digital_Technologies/primm.html
- title: Teaching Digital Technologies
  url: /sense/Teaching/Digital_Technologies/teaching-digital-technologies.html
- title: Digital Technologies Structures
  url: /sense/Teaching/Digital_Technologies/digital-technologies-structures.html
- title: My approach to teaching digital technologies
  url: /sense/Teaching/Mathematics/my-approach-to-teaching-digital-technologies.html
tags: teaching-digital-technologies, computing, programming, teaching-programming
title: The block model
type: note
---
Resources:

- [KSU explanation](https://textbooks.cs.ksu.edu/tlcs/4-designing-cs-lessons/06-the-block-model/index.html)
- [Raspberry Pi - quick read](https://raspberrypi-education.s3-eu-west-1.amazonaws.com/Quick+Reads/Pedagogy+Quick+Read+12+-+Block+Model.pdf)

A method to break down the structure of a program to make it easier to understand by students as they read the program. Apparently designed to be directly related with the epistemology of programming and the development of schema.

Useful for understanding how students engage with programs. Novices read bottom up, experts bottom-down.

Based on a duality between 

- structure - text surface and program execution; and,
- function

| Dimensions | Text surface | Program execution (data & control flow) | Function |
|---|---|---|---|
| Macro Structure | Understanding the overall structure of the program | Understanding the 'algorithm' of the program | Understanding the goal/purpose of the program |
| Relations | References between blocks, eg. method calls, object creation, accessing data... | sequence of method calls - 'object sequence diagrams' | Understanding how subgoals relate to goals, how function is achieved by subfunctions |
| Blocks | 'Regions of Interests' (ROI) that syntactically or semantically build a unit | Operation of a block of code, a method, or a ROI (as a sequence of statements) | Purpose of a block of code, possibly seen as a subgoal |
| Atoms | Language elements | Operation of a statement | Purpose of a statement |


## Related activities

| Dimensions | Text surface | Program execution (data & control flow) | Function |
|---|---|---|---|
| Macro structure | <ul> <li> annotate code or draw a diagram to show the overall structure </li> <li> restructure an "untidy" program </li> </ul> | <ul> <li> Identify inputs needed to test all program branches </li> <li> Will line X ever be executed </li> </ul> | <ul> <li> Choose a name for a given program </li> <li> Select/write a sentence that describes a program's purpose </li> </ul> |
| Relationships | <ul> <li> Identify variable scope </li> <li> Highlight function calls </li> <li> Draw the flow of control </li> <li> Find redundant conditional branches </li> <li> Choose a name for a variable/function </li> <li> Are two programs/segments functionally equivalent </li> </ul> |
| Blocks | <ul> <li> Identify block types, such as finite lops 'else' conditions, function definitions, etc. </li> </ul> | <ul> <li> Reordering lines of code </li> <li> Parson's problems </li> </ul> | <ul> <li> Explain the purpose of a block of code </li> </ul> | 
| Atoms | <ul> <li> Identify statement types, such as assignments and conditions </li> </ul> | Trace values through a program | Explain the purpose of a single line |