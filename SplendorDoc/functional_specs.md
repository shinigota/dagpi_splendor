# Functional specifications
---

## GameBoard
  
## GameRules

## Display

## RessourceType

## Tile

## TokenStack

## Card

## Player

## AI
* Focusing on a specific strategy
  * Winning nobles by purchasing cheap cards
  * Buying expensive card, targeting a lot of points
* Examinating all **his** next **X** *(depth)* turns, choosing the best path leading to the strategy
  * Depth determines the AI's difficulty
* AI based on early game, mid game, end game times
  * AI's income (from mines) determines the state of the game
  * AI begins by reserving a tier 3 card
  * Based on the card's cost to value ratio, AI will
  	* (5 points) Tiles strategy, until late game, then buy its reserved card
  	* (4 points) If the cost is low, tiles strategy and buy the card in the end game. Otherwise, tiles strategy and gnot obliged to buy the card
  	* (3 points) Tiles strategy
