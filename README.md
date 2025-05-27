# Fog of War Chess

This project implements a chess variant called **Fog of War Chess** (also known as [Dark Chess](https://en.wikipedia.org/wiki/Dark_chess)), where each player can only see their own pieces and the squares their pieces can legally move to (including any opponent pieces that can be captured). The game is implemented in Python in the [`ChessVar`](ChessVar.py) class.

## Rules

- The game starts with the standard chess setup.
- **White always moves first.**
- Pieces move and capture as in standard chess.
- **No checks, checkmates, castling, en passant, or pawn promotion.**
- Pawns can move two spaces forward on their first move, one space on subsequent moves.
- The game ends when a player's king is captured.
- Players are not informed if their king is in check; moving into or remaining in check is allowed.
- Each player sees only their own pieces and the squares their pieces can legally move to. Opponent pieces are only visible if they can be captured; all other opponent pieces are hidden as `*`.

## Board Representation

- The board is an 8x8 nested list.
- Lowercase letters (`r`, `n`, `b`, `q`, `k`, `p`) represent black pieces.
- Uppercase letters (`R`, `N`, `B`, `Q`, `K`, `P`) represent white pieces.
- Empty squares are `' '`.
- Hidden squares (from a player's perspective) are shown as `'*'`.

### Example: Initial Board (Audience View)

```
[ ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
  ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
  ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'] ]
```

### Example: Initial Board (White's Perspective)

```
[ ['*', '*', '*', '*', '*', '*', '*', '*'],
  ['*', '*', '*', '*', '*', '*', '*', '*'],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
  ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
  ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'] ]
```

## Usage

1. Import or instantiate the [`ChessVar`](ChessVar.py) class.
2. Use `make_move(from_square, to_square)` to make moves (e.g., `'e2'`, `'e4'`).
3. Use `get_board(perspective)` to get the board from `'white'`, `'black'`, or `'audience'` perspective.
4. Use `get_game_state()` to check if the game is `'UNFINISHED'`, `'WHITE_WON'`, or `'BLACK_WON'`.

### Example

```python
from ChessVar import ChessVar

game = ChessVar()
print(game.make_move('d2', 'd4'))
print(game.make_move('g7', 'g5'))
print(game.make_move('c1', 'g5'))
print(game.make_move('e7', 'e6'))
print(game.make_move('g5', 'd8'))
print(game.get_board("audience"))
print(game.get_board("white"))
print(game.get_board("black"))
```

#### Output

```
True
True
True
True
True
[
 ['r', 'n', 'b', 'B', 'k', 'b', 'n', 'r'],
 ['p', 'p', 'p', 'p', ' ', 'p', ' ', 'p'],
 [' ', ' ', ' ', ' ', 'p', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 ['P', 'P', 'P', ' ', 'P', 'P', 'P', 'P'],
 ['R', 'N', ' ', 'Q', 'K', 'B', 'N', 'R']
]
[
 ['*', '*', '*', 'B', '*', '*', '*', '*'],
 ['*', '*', 'p', '*', ' ', '*', ' ', '*'],
 [' ', ' ', ' ', ' ', '*', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', 'P', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 ['P', 'P', 'P', ' ', 'P', 'P', 'P', 'P'],
 ['R', 'N', ' ', 'Q', 'K', 'B', 'N', 'R']
]
[
 ['r', 'n', 'b', 'B', 'k', 'b', 'n', 'r'],
 ['p', 'p', 'p', 'p', ' ', 'p', ' ', 'p'],
 [' ', ' ', ' ', ' ', 'p', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', '*', ' ', ' ', ' ', ' '],
 [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
 ['*', '*', '*', ' ', '*', '*', '*', '*'],
 ['*', '*', ' ', '*', '*', '*', '*', '*']
]
```

## License

MIT License

---

For more details, see [`ChessVar.py`](ChessVar.py).



