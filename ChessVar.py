# Author: Ethan Van Hao
# GitHub username: Evhevh
# Date: 12/8/2024
# Description: This code creates a game of Fog-of-War chess with multiple rules that are accounted for in the methods.
# There are methods to show perspectives based on the player with fog-of-war to hide pieces that the player is not
# directly able to capture. All the pieces from chess are coded to make sure that they work accordingly to their
# traditional moves in the normal game of chess. The code handles turn swapping, game_state checking, and legal
# move checking in the code created.


class ChessVar:
    """
    A class that represents a Chess game played by two players denoted as WHITE or BLACK. WHITE will
    always go first. Manages the moves of the board and checks for legal moves and victory of players.
    """

    def __init__(self):
        """
        Constructor for the ChessVar class and initializes the board, game_state, and gives the first turn to white.
        Takes no parameters and all data members are private.
        """

        #initial board state
        self._board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]

        self._game_state = 'UNFINISHED'  #game starts 'UNFINISHED'
        self._turn = 'WHITE' #white starts first


    def get_game_state(self):
        """
        Returns the game state and returns either 'UNFINISHED', 'WHITE_WON', 'BLACK_WON'.
        """

        return self._game_state


    def get_board(self, perspective):
        """
        Returns the board state from the perspective of the audience or either player. Hides the pieces of the
        opponent if called from the perspective of a player by using '*' as a censor. Audience can see the whole
        board.
        :param perspective: A value of 'audience', 'white', or 'black' that denotes what board the individual should
        see
        :return: A nested list that represents a chessboard showing the perspective of the board from either the
        audience or a player
        """

        #displays the board from the audience's perspective
        if perspective == 'audience':
            return self._board

        #initializes a new board and row for the player's perspective
        player_board = []

        #displays the board from the white player's perspective
        if perspective == 'white':
            for row in range(8):
                player_row = []
                for col in range(8):
                    piece = self._board[row][col]
                    if piece == ' ':
                        player_row.append(' ')
                    elif piece.isupper():
                        player_row.append(piece)
                    elif piece.islower():
                        if self.is_piece_in_range(row, col):
                            player_row.append(piece)
                        else:
                            player_row.append('*')
                player_board.append(player_row)


        #displays the board from the black player's perspective
        if perspective == 'black':
            for row in range(8):
                player_row = []
                for col in range(8):
                    piece = self._board[row][col]
                    if piece == ' ':
                        player_row.append(' ')
                    elif piece.islower():
                        player_row.append(piece)
                    elif piece.isupper():
                        if self.is_piece_in_range(row, col):
                            player_row.append(piece)
                        else:
                            player_row.append('*')
                player_board.append(player_row)

        return player_board


    def make_move(self, moved_from, moved_to):
        """
        Makes a move on the board and checks for legal moves, if the piece belongs to the player, and if the
        game is over. If all is accounted for, then it will make the move, remove any captured piece, update the game
        state and switch turns.
        :param moved_from:  a string denoting the initial notation of piece being moved
        :param moved_to:    a string denoting the notation of square a piece is being moved to
        :return:    True if move is made successfully and game is updated, false if move is not legal
        """
        #check for game_state; false if game_state is 'unfinished'
        if self._game_state != 'UNFINISHED':
            return False

        #gather the start and end indices of both notations; 4 parameters of start row, end row, start col, end col
        start_row, start_col = self.convert_notation_to_index(moved_from)
        end_row, end_col = self.convert_notation_to_index(moved_to)

        #get the piece that is on the initial spot
        piece = self._board[start_row][start_col]

        #check for player turn; false if wrong piece is being used by wrong player
        if self._turn == 'WHITE' and piece.islower() or self._turn == 'BLACK' and piece.isupper():
            return False

        #check if move is legal using the 4 parameters gained above
        if not self.is_legal_move(moved_from, moved_to):
            return False

        #checks if the king is at the end spot before moving the piece
        if self._board[end_row][end_col] == 'k' and self._turn =='WHITE':
            self._game_state = 'WHITE_WON'

        if self._board[end_row][end_col] == 'K' and self._turn == 'BLACK':
            self._game_state = 'BLACK_WON'

        #move the piece and update the board; replace old spot with an empty spot
        self._board[end_row][end_col] = self._board[start_row][start_col]
        self._board[start_row][start_col] = ' '

        #switch turns if game is still going
        self.switch_turn()

        return True

    def convert_notation_to_index(self, notation):
        """
        Converts algebraic notation to a board index.
        :param notation: notation of the square of the chess board
        :return: the row and column of the list that the notation pertains to
        """

        # converts the column to an index using the difference in Unicode
        col = ord(notation[0]) - ord('a')

        # converts the row to an index by subtracting 8 by the row number
        row = 8 - int(notation[1])

        return row, col

    def is_legal_move(self, moved_from, moved_to):
        """
        Checks if a move from a chess piece is legal by checking what the piece is and calling the individual piece's
        legality function to check if it is legal.
        :param moved_from: a string denoting the starting location of a piece on a chessboard
        :param moved_to:    a string denoting the final location of a piece on a chessboard
        :return: True if the piece is making a legal move, false otherwise
        """

        piece = self._board[self.convert_notation_to_index(moved_from)[0]][self.convert_notation_to_index(moved_from)[1]]
        start_row, start_col = self.convert_notation_to_index(moved_from)
        end_row, end_col = self.convert_notation_to_index(moved_to)

        if not(0 <= start_row < 8 and 0 <= start_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8):
            return False

        if piece.lower() == 'p':
            return self.is_pawn_move_legal(start_row, start_col, end_row, end_col)
        if piece.lower() == 'r':
            return self.is_rook_move_legal(start_row, start_col, end_row, end_col)
        if piece.lower() == 'n':
            return self.is_knight_move_legal(start_row, start_col, end_row, end_col)
        if piece.lower() == 'b':
            return self.is_bishop_move_legal(start_row, start_col, end_row, end_col)
        if piece.lower() == 'q':
            return self.is_queen_move_legal(start_row, start_col, end_row, end_col)
        if piece.lower() == 'k':
            return self.is_king_move_legal(start_row, start_col, end_row, end_col)


    def is_pawn_move_legal(self, start_row, start_col, end_row, end_col):
        """
        Checks if a pawn's move is legal. Can move forward two squares if on initial tile or move one in a straight
        line. Can capture diagonally 1 square.
        :param start_row: starting row index acquire from convert_notation_to_index()
        :param start_col: starting column index acquire from convert_notation_to_index()
        :param end_row: end row index acquire from convert_notation_to_index()
        :param end_col: end column index acquire from convert_notation_to_index()
        :return: True if piece movement is legal, false otherwise
        """

        piece = self._board[start_row][start_col]

        if piece == 'P'and start_col == end_col: #checks black pawn movement
            if start_row == 6 and end_row == 4 and self._board[end_row][end_col] == ' ': #checks initial double move
                return True
            if start_row - 1 == end_row and self._board[end_row][end_col] == ' ': # checks single move and empty spot
                return True
        elif piece == 'p' and start_col == end_col: #checks white pawn movement
            if start_row == 1 and end_row == 3 and self._board[end_row][end_col] == ' ':
                return True
            if start_row + 1 == end_row and self._board[end_row][end_col] == ' ':
                return True

        if piece == 'P' and abs(start_col - end_col) == 1 and start_row - 1 == end_row:
            if self._board[end_row][end_col].islower():
                return True
        elif piece == 'p' and abs(start_col - end_col) == 1 and start_row + 1 == end_row:
            if self._board[end_row][end_col].isupper():
                return True

        return False

    def is_rook_move_legal(self, start_row, start_col, end_row, end_col):
        """
        Checks if a rook's move is legal. Can move horizontally or vertically without limit, but cannot jump
        over pieces.
        :param start_row: starting row index acquire from convert_notation_to_index()
        :param start_col: starting column index acquire from convert_notation_to_index()
        :param end_row: end row index acquire from convert_notation_to_index()
        :param end_col: end column index acquire from convert_notation_to_index()
        :return: True if piece movement is legal, false otherwise
        """

        if start_row == end_row or start_col == end_col:
            return self.is_path_clear(start_row, start_col, end_row, end_col)

        return False

    def is_knight_move_legal(self, start_row, start_col, end_row, end_col):
        """
        Checks if a knight's move is legal. Can move in an "L" shape where it moves 2 squares in one direction
        and 1 square in a perpendicular direction.
        :param start_row: starting row index acquire from convert_notation_to_index()
        :param start_col: starting column index acquire from convert_notation_to_index()
        :param end_row: end row index acquire from convert_notation_to_index()
        :param end_col: end column index acquire from convert_notation_to_index()
        :return: True if piece movement is legal, false otherwise
        """

        if ((abs(start_row - end_row) == 2 and abs(start_col - end_col) == 1) or (abs(start_row - end_row) == 1 and abs(start_col - end_col) == 2)):
            starting_piece = self._board[start_row][start_col]
            target_piece = self._board[end_row][end_col]

            if target_piece == ' ' or (starting_piece.isupper() != target_piece.isupper()):
                return True

        return False

    def is_bishop_move_legal(self, start_row, start_col, end_row, end_col):
        """
        Checks if a bishop's move is legal. Can move diagonally without limit, but cannot jump over pieces.
        :param start_row: starting row index acquire from convert_notation_to_index()
        :param start_col: starting column index acquire from convert_notation_to_index()
        :param end_row: end row index acquire from convert_notation_to_index()
        :param end_col: end column index acquire from convert_notation_to_index()
        :return: True if piece movement is legal, false otherwise
        """

        if abs(start_row - end_row) == abs(start_col - end_col):
            return self.is_path_clear(start_row, start_col, end_row, end_col)

        return False

    def is_queen_move_legal(self, start_row, start_col, end_row, end_col):
        """
        Checks if a queen's move is legal. Can move horizontally, vertically, or diagonally without limit, but cannot
        jump over pieces.
        :param start_row: starting row index acquire from convert_notation_to_index()
        :param start_col: starting column index acquire from convert_notation_to_index()
        :param end_row: end row index acquire from convert_notation_to_index()
        :param end_col: end column index acquire from convert_notation_to_index()
        :return: True if piece movement is legal, false otherwise
        """

        return (self.is_rook_move_legal(start_row, start_col, end_row, end_col) or
                self.is_bishop_move_legal(start_row, start_col, end_row, end_col))

    def is_king_move_legal(self, start_row, start_col, end_row, end_col):
        """
        Checks if a king's move is legal. Can move 1 square in any direction.
        :param start_row: starting row index acquire from convert_notation_to_index()
        :param start_col: starting column index acquire from convert_notation_to_index()
        :param end_row: end row index acquire from convert_notation_to_index()
        :param end_col: end column index acquire from convert_notation_to_index()
        :return: True if piece movement is legal, false otherwise
        """

        if abs(start_row - end_row) <= 1 and abs(start_col - end_col) <= 1:
            return self.is_path_clear(start_row, start_col, end_row, end_col)

        return False

    def is_path_clear(self, start_row, start_col, end_row, end_col):
        """
        Checks if the path is clear for pieces that cannot jump over pieces.
        :param start_row: starting row index acquire from convert_notation_to_index()
        :param start_col: starting column index acquire from convert_notation_to_index()
        :param end_row: end row index acquire from convert_notation_to_index()
        :param end_col: end column index acquire from convert_notation_to_index()
        :return: True if path is not obstructed, false otherwise
        """

        row_direction = 0
        col_direction = 0

        if start_row == end_row:    #Horizontal movement
            if start_col < end_col:
                col_direction = 1
            else:
                col_direction = -1

        elif start_col == end_col:    #Vertical movement
            if start_row < end_row:
                row_direction = 1
            else:
                row_direction = -1

        elif abs(start_row - end_row) == abs(start_col - end_col):    #Diagonal Movement
            if start_row < end_row:
                row_direction = 1
            else:
                row_direction = -1
            if start_col < end_col:
                col_direction = 1
            else:
                col_direction = -1

        row, col = start_row + row_direction,  start_col + col_direction
        while (row != end_row) or (col != end_col):
            if self._board[row][col] != ' ':
                return False
            row += row_direction
            col += col_direction

        starting_piece = self._board[start_row][start_col]
        target_piece = self._board[end_row][end_col]

        if target_piece != ' ':
            if ((starting_piece.isupper() and target_piece.isupper()) or
                    (starting_piece.islower() and target_piece.islower())):
                return False

        return True

    def switch_turn(self):
        """
        Gives the turn to the other player after a player has made a move.
        """

        if self._turn == 'WHITE':
            self._turn = 'BLACK'
        else:
            self._turn = 'WHITE'

    def is_piece_in_range(self, row, col):
        """
        Checks if a piece is in range of an enemy piece by iterating through the board and checking legality of moves
        from enemy pieces.
        :param row: Row position of the piece being checked
        :param col: Column position of the piece being checked
        :return: True if in range, false is not
        """

        for r in range(8):
            for c in range (8):
                piece = self._board[r][c]

                if piece != ' ' and ((piece.isupper() and self._board[row][col].islower())
                        or (piece.islower() and self._board[row][col].isupper())):
                    piece_index = chr(c + ord('a')) + str(8 - r)
                    target_index = chr(col + ord('a')) + str(8 - row)

                    if self.is_legal_move(piece_index, target_index):
                        return True

        return False