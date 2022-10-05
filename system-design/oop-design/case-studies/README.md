# Designing Chess

## Requirements and Goals of the System
1. The system should support two online players to play a game of chess.
2. All rules of chess should be enforced.
3. Each player will be randomly assigned a color (white or black).
4. Both players will play their moves in turns. The white player will play first.
5. Players can't cancel or retract their moves.
6. The system should maintain a log of all moves played in the game.
7. Each side will start with 8 pawns, 2 rooks, 2 knights, 2 bishops, 1 queen and 1 king.
8. The game can finish either in a checkmate, forfeit or stalemate (a draw). or resignation.

## Use cases
we have two actors in our system: 
1. Player: A registered account in the system, who will play the game. The player will play chess moves.
2. Admin: To ban/modify players.

Top use cases for chess:
- player moves a piece
- resign or forfeit a game
- register new account/cancel membership
- update game log

## Class Diagram

- Player
- Account
- Game
- Box
- Board
- Piece
- Move
- Game Controller
- Game View

