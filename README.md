The AI implemented in this Tic Tac Toe game is based on the Minimax algorithm with alpha-beta pruning. The Minimax algorithm is a decision-making algorithm used in two-player games, where the goal is to find the optimal move for a player while assuming that the opponent also plays optimally. It is commonly used in games like Tic Tac Toe, Chess, and Connect Four.

The AI has four difficulty levels: Easy, Medium, Hard, and Impossible. Each difficulty level corresponds to a different AI strategy for making moves on the game board.

1. Easy (ai_move_easy):
   
- The AI at this level makes random moves. It selects an empty position on the board randomly and places its mark (X or O) on that position.

2. Medium (ai_move_medium):

- The Medium-level AI attempts to play strategically by checking if it can win on the next move. If it finds a position where it can win, it places its mark there.
- If there is no winning move for the AI, it checks if the opponent (human player) can win on their next move and tries to block them by placing its mark in the blocking position.
- If neither a winning move nor a blocking move is possible, it falls back to making a random move.

3. Hard (ai_move_hard):

- The Hard-level AI uses the Minimax algorithm to search for the best possible move at each turn.
- It recursively explores all possible moves and their outcomes (by simulating both AI's and the opponent's moves) up to a certain depth, assuming that both players play optimally.
- The AI assigns a score to each board configuration based on the outcome of the game (win, loss, or draw) and the depth of the search tree.
- It chooses the move that leads to the highest score, indicating the best possible move for the AI.
- This AI is more challenging to beat as it looks ahead several moves to anticipate the human player's moves and reacts accordingly.

4. Impossible (ai_move_impossible):

- The Impossible-level AI uses the Minimax algorithm with alpha-beta pruning, an optimization to reduce the number of unnecessary branches in the search tree.
- Similar to the Hard AI, it recursively searches for the best possible move, but alpha-beta pruning allows it to eliminate certain branches when it knows they will not lead to a better outcome.
- This optimization significantly speeds up the search process and makes it even harder for the human player to win.
- The Impossible AI is expected to play perfectly, making it nearly impossible for the human player to win.

