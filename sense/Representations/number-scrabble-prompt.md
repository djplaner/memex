# Prompt exploration for preparing number scrabble

## Initial prompt

As a web developer write a 2-player version of Herb Simon's number scrabble game using HTML, Javascript and CSS.  Provide the HTML, Javascript, and CSS to implement the game. 

The game should take place on a single web page with three main sections: 1) available cards, 2) player 1's selected cards and score, and 3) player 2's selected cards and score. The available cards section should be displayed centered on the top of the page. The two players' sections are displayed underneath the available cards section and displayed next to each other.

At the start of the game, the available cards section will display a horizontal sequence of 9 playing cards numbers 1 to 9. Each players initial score will be 0 and their selected cards list will also be empty.

Each player will take turns choosing one of the available cards. The first player to have 3 cards that add up to 15 wins. Otherwise the game is a tie. 

Visually the cards in the available cards section and the players' selected cards section should resemble playing cards of the diamond suit. The ace card represents the number 1, the 2 card the number to, and so on. 

Each turn consists of a player selecting a card from the available cards selection. They should only be able to select cards that have not already been selected. When a card is selected by a play, the game will complete the following
1. Check if the card's numeric value will cause the player to have more than 15 points. If so, the card should not be selected and the player should be prompted to select another card.
2. Modify the selected card in the available cards section to show the back of the playing card. The back should display the number of player who selected that card.
3. Add the card that was selected to the selected cards section of the player who selected the card.
4. Update the score for the player who selected the card by adding the number value of the selected card.
5. Check if the player who selected the card has 3 cards that add up to 15. If so, the game is over and the player who won should be visually indicated.

The interface of the game must adhere the highest levels WCAG accessibility standards.  The visual design of the game must be heavily inspired by skeuomorphic design.

## Fix the issues 

There are a few limitations of the game provided. Please provide HTML, CSS and Javascript to fix each of the following issues. 

1. The game does not implement turns. First, player 1 gets to select a card, then player 2, then player 1, and so on.
2. When cards are selected the card value is generating a NaN error for both the score and the card value.
3. The selected cards are not displayed in the same way as the available cards. The cards should always be displayed as playing cards using the same visual style.
4. The player 1 and player 2 sections are displayed vertically instead of horizontally. The player 1 section should be displayed to the left of the player 2 section.

## More issues 



Fix this one by prompting
- The playing cards are not shown as obviously playing cards. 
- Nothing obviously skeuomorphic about the design


## Another fresh start 

Number Scrabble was used by Herb Simon to demonstration the importance of representation to design. It is a 2-player game played with a deck of 9 playing cards numbered 1 to 9. The game is played by each player taking turns selecting one of the available cards. The first player to have 3 cards that add up to 15 wins. Otherwise the game is a tie. 

The first representation is that of scrabble tiles. A horizontal row of 9 tiles is displayed. Each tile has a number from 1 to 9. The players must expend cognitive effort to develop a wining strategy as the game progresses.

The second representation is that of a magic square. A 3 by 3 grid of the numbered tiles arranged to mirror the game tic-tac-toe. The magic square is arranged so that all of the horizontal, vertical, and diagonal rows numerically add up to 15. The magic square representation makes it easy for players to develop a winning strategy.

As a web developer you have been employed by a teacher to implement a 2-player version of Herb Simon's Number Scrabble game using HTML, Javascript and CSS. The teacher wants to use the game to teach their students about the importance of representation to design.

The game should take place on a single web page with three main sections: 
1. Available cards section - shows the current representation of the cards and a button to toggle representation
2. player 1's section - includes player 1's selected cards and score
3. player 2's selected - includes player 2's selected cards and score. 

The available cards section should be displayed centered on the top of the page. It will be displayed above the two players' sections. The two players' sections are displayed side-by-side underneath the available cards section. Player 1's section should be displayed to the left of player 2's section.

At the start of the game, the available cards section will display all the 9 cards ready to be selected. Both players' score will be 0. Both players' selected cards section will be empty. 

The game will allow each player to take a turn selecting a card.  First player 1 will select a card, then player 2, then player 1, and so on.  Only cards that have not already been selected, can be selected. Players select cards by clicking on an individual card in the available cards section. 

When a player clicks on an individual card, the game will complete the following:
1. Check if current player's score and the numeric value of the selected card will add up to more than 15. If it does the card should not be selected and the player should be prompted through an alert to select another card.
2. Modify the available cards section by turning the selected card over. Do this by changing the selected card's display to the back of a card.
4. Visually add the selected card to the selected cards section of the relevant player.
5. Add the numeric value of the selected card to the score of the relevant player. 
6. Check if current player's score equals 15 and the current player has 3 cards. If so, the current player has won and the game is over. Generate an alert announcing that the player has won.

In the available cards section and bother players' selected cards section each individual card should use the same visual design. The visual design should resemble a playing card of the diamond suit. 

Each players' selected cards section should display their list of selected cards in a horizontal row using the individual card visual design.

The available cards section will support two different visual representations and a button to toggle between them. The two visual representations are a horizontal row and a magic square. The horizontal row is the default visual representation. The magic square is the alternative visual representation. The magic square representation should be implemented using a grid container.

The available cards section should include a button labelled "Change representation" that switches between the horizontal row and magic square visual representations. The button should be displayed centered on the bottom of the available cards section. 

The HTML and CSS of the game must adhere the highest levels WCAG accessibility standards.  Visually the game should be an effective demonstration of the material design visual style.