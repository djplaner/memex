---
title: "Number Scrabble - web implementation"
type: "note"
tags: teaching, number-scrabble 
---

See also: [[number-scrabble]], [[teaching]], [[teaching-implementation]]

Aim here is to explore if/how to implement a web app/component that allows me to demonstrate (perhaps play) [[number-scrabble]] as part of a lesson. Plan is to split development into 

1. [x] Visuals only - no game play/logic, just allow two players to play on a web page
2. [x] [Two player game play](./html/card-deck-1.html) should work
3. Single player game play

## Visuals only

### Resources

- [CSS playing cards](https://selfthinker.github.io/CSS-Playing-Cards/) - [blog post](https://blog.selfthinker.org/2010/08/23/css-playing-cards/) - 13 year old but quite interesting
- [CodePens labelled "playing cards"](https://codepen.io/tag/playing-cards)

    - [playing cards in CSS](https://codepen.io/chris22smith/pen/MzPrYe)
    - [playing cards no JS](https://codepen.io/rlbaxter/pen/jdjEow) some animation to turn over

Javascript

- [Medium article (part of series) on playing cards with JS](https://medium.com/@pakastin/javascript-playing-cards-part-2-graphics-cd65d331ad00)

    - related to [deck of cards site](https://deck.of.cards/) which is almost what I need
    - [repo](https://github.com/deck-of-cards/deck-of-cards)
    - Could be the one - Javascript mostly functional

- [Cards JS](http://richardschneider.github.io/cardsJS/)
- [CardTS](https://github.com/e-lements/CARDTS) - card web components

Other

- [Deck of Cards API](https://github.com/crobertsbmw/deckofcards) - fairly up to date

### Experiment 1 - [Deck of Cards](https://github.com/deck-of-cards/deck-of-cards)

In theory, I should be able to use one of the example bits of code and replace the local css/js with a CDN and [this web page](./html/card-deck-1.html) should work

All that's required now is to write Javascript that

- [x] shows up turned cards from 1 to 15
- [x] allow dragging and dropping of the cards

### Experiment 2 - Two player game play

- [x] Add a player 1 and player 2 space for dragging cards
- [x] as cards dragged there update a count for that player

    Could be interesting.  How to get an event that fires when a card is dropped on a player space?

    For each card add an event listener on stop moving that looks for location


[//begin]: # "Autogenerated link references for markdown compatibility"
[number-scrabble]: ..%2FRepresentations%2Fnumber-scrabble "Number scrabble (aka Fifteen)"
[teaching]: ..%2FTeaching%2Fteaching "Teaching"
[teaching-implementation]: ..%2FTeaching%2FImplementation%2Fteaching-implementation "Teaching implementation"
[//end]: # "Autogenerated link references"