<!--
 Copyright (C) 2023 David Jones
 
 This file is part of memex.
 
 memex is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 memex is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with memex.  If not, see <http://www.gnu.org/licenses/>.
-->

# Implementing number scrabble 

Vague idea to implement number scrabble in Svelte for demonstrations etc.

## Design 

- very visual, perhaps use playing cards to represent the numbers 
- the numbers should have different representations that can be switched between 

## Inspirations 

- Get ChatGPT to help write it


## Development Journal 

### 20 May 2023 

Start with number scrabble project with first LLM provided code

Prompt 
> I'd like to implement Number Scrabble as a Javascript application. Can you provide source code as a starting point?

Response was some code including the following additional work 
> To use this code, you'll need to create an HTML file that includes the necessary elements for the game's user interface (e.g., an equation display and score display) and link the JavaScript code to the HTML file. You can style the game elements using CSS to enhance the visual presentation.

Prompt 
> Please provide me with a sample of the required HTML file

The provided HTML file appears correct, but the same error occurs `Uncaught TypeError: gameContainer is null`

Prompt 
> What what you've provided I am getting the error "Uncaught TypeError: gameContainer is null". It appears that your initGame function assumes that there are already tiles within game-contain div, but there aren't any.  Can you please fix your Javascript and HTML?