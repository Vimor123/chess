# Gameboard coordinates
# Rows:     Columns:
# 1 => 0    A => 0
# 2 => 1    B => 1
# 3 => 2    C => 2
# 4 => 3    D => 3
# 5 => 4    E => 4
# 6 => 5    F => 5
# 7 => 6    G => 6
# 8 => 7    H => 7

# Players
# white - "w", black - "b"

# Pieces
# king - "k", queen - "q", bishop - "b",
# knight - "n", rook - "r", pawn - "p"

# Gameboard state is stored in an 8x8 matrix
# Empty spaces are represented by an empty string
# Occupied spaces are represented by the letter of the piece color
# and the letter of the piece type: e.g. "black knight" => "bn"

# Starting matrix:
#[['wr', 'wn', 'wb', 'wq', 'wk', 'wb', 'wn', 'wr'],
# ['wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp', 'wp'],
# ['', '', '', '', '', '', '', ''],
# ['', '', '', '', '', '', '', ''],
# ['', '', '', '', '', '', '', ''],
# ['', '', '', '', '', '', '', ''],
# ['bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp', 'bp'],
# ['br', 'bn', 'bb', 'bq', 'bk', 'bb', 'bn', 'br']]


def can_move_piece(gameboard, piece_position):
    pass

def get_legal_moves(gameboard, piece_position):
    pass

def check_for_checks(gameboard, turn):
    pass

def check_for_win(gameboard, turn):
    pass

def check_for_draw(gameboard, turn):
    pass
