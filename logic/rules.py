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


def get_piece_moves(gameboard, piece_position, last_move_positions):
    i = piece_position[0]
    j = piece_position[1]
    piece = gameboard[i][j]
    moves = []
    if piece == "":
        pass
    
    elif piece.endswith("p"):
        if piece == "wp":
            if gameboard[i+1][j] == "":
                moves.append((i+1, j))
                if i == 1 and gameboard[i+2][j] == "":
                    moves.append((i+2, j))
            if j > 0 and gameboard[i+1][j-1].startswith("b"):
                moves.append((i+1, j-1))
            if j < 7 and gameboard[i+1][j+1].startswith("b"):
                moves.append((i+1, j+1))
            # En passant
            last_moved_piece = gameboard[last_move_positions[1][0]][last_move_positions[1][1]]
            if (last_moved_piece == "bp" and last_move_positions[0][0] == 6 and
                last_move_positions[1][0] == 4 and i == 4
                and abs(last_move_positions[1][1] - j) == 1):
                moves.append((i+1, last_move_positions[1][1]))

        else:
            if gameboard[i-1][j] == "":
                moves.append((i-1, j))
                if i == 6 and gameboard[i-2][j] == "":
                    moves.append((i-2, j))
            if j > 0 and gameboard[i-1][j-1].startswith("w"):
                moves.append((i-1, j-1))
            if j < 7 and gameboard[i-1][j+1].startswith("w"):
                moves.append((i-1, j+1))
            # En passant
            last_moved_piece = gameboard[last_move_positions[1][0]][last_move_positions[1][1]]
            if (last_moved_piece == "wp" and last_move_positions[0][0] == 1 and
                last_move_positions[1][0] == 3 and i == 3
                and abs(last_move_positions[1][1] - j) == 1):
                moves.append((i-1, last_move_positions[1][1]))

    elif piece.endswith("r"):
        increments = ((1, 0), (-1, 0), (0, 1), (0, -1))
        for increment_pair in increments:
            new_position = [i + increment_pair[0], j + increment_pair[1]]
            while new_position[0] in range(8) and new_position[1] in range(8):
                if gameboard[new_position[0]][new_position[1]] == "":
                    moves.append(tuple(new_position))
                elif gameboard[new_position[0]][new_position[1]][0] != piece[0]:
                    moves.append(tuple(new_position))
                    break
                else:
                    break
                new_position[0] += increment_pair[0]
                new_position[1] += increment_pair[1]

    elif piece.endswith("n"):
        jumps = ((2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2))
        for jump in jumps:
            if i + jump[0] in range(8) and j + jump[1] in range(8):
                if (gameboard[i+jump[0]][j+jump[1]] == "" or
                    gameboard[i+jump[0]][j+jump[1]][0] != piece[0]):
                    moves.append((i+jump[0], j+jump[1]))

    elif piece.endswith("b"):
        increments = ((1, 1), (1, -1), (-1, -1), (-1, 1))
        for increment_pair in increments:
            new_position = [i + increment_pair[0], j + increment_pair[1]]
            while new_position[0] in range(8) and new_position[1] in range(8):
                if gameboard[new_position[0]][new_position[1]] == "":
                    moves.append(tuple(new_position))
                elif gameboard[new_position[0]][new_position[1]][0] != piece[0]:
                    moves.append(tuple(new_position))
                    break
                else:
                    break
                new_position[0] += increment_pair[0]
                new_position[1] += increment_pair[1]

    elif piece.endswith("q"):
        increments = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1))
        for increment_pair in increments:
            new_position = [i + increment_pair[0], j + increment_pair[1]]
            while new_position[0] in range(8) and new_position[1] in range(8):
                if gameboard[new_position[0]][new_position[1]] == "":
                    moves.append(tuple(new_position))
                elif gameboard[new_position[0]][new_position[1]][0] != piece[0]:
                    moves.append(tuple(new_position))
                    break
                else:
                    break
                new_position[0] += increment_pair[0]
                new_position[1] += increment_pair[1]

    elif piece.endswith("k"):
        increments = ((1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1))
        for increment_pair in increments:
            new_position = (i + increment_pair[0], j + increment_pair[1])
            if new_position[0] in range(8) and new_position[1] in range(8):
                if (gameboard[new_position[0]][new_position[1]] == "" or
                    gameboard[new_position[0]][new_position[1]][0] != piece[0]):
                    moves.append(tuple(new_position))

    return moves


def check_for_checks(gameboard, turn, last_move_positions):
    king_position = (-1, -1)
    opponents_pieces_positions = []
    for i in range(8):
        for j in range(8):
            if gameboard[i][j] == turn + "k":
                king_position = (i, j)
            elif not gameboard[i][j].startswith(turn) and gameboard[i][j] != "":
                opponents_pieces_positions.append((i, j))

    check = False
    for piece_position in opponents_pieces_positions:
        if king_position in get_piece_moves(gameboard, piece_position, last_move_positions):
            check = True
            break

    return check


def get_legal_moves(gameboard, turn, piece_position, last_move_positions):
    possible_moves = get_piece_moves(gameboard, piece_position, last_move_positions)
    legal_moves = []
    for move in possible_moves:
        new_gameboard = []
        for gameboard_row in gameboard:
            new_gameboard.append(gameboard_row.copy())
        piece = new_gameboard[piece_position[0]][piece_position[1]]
        new_gameboard[piece_position[0]][piece_position[1]] = ""
        new_gameboard[move[0]][move[1]] = piece

        new_last_move_positions = ((piece_position[0], piece_position[1]), (move[0], move[1]))

        is_move_illegal = check_for_checks(new_gameboard, turn, new_last_move_positions)

        if not is_move_illegal:
            legal_moves.append(move)

    return legal_moves


def check_for_game_over(gameboard, turn, last_move_positions):
    game_over = True
    winner = "n"
    
    pieces_positions = []
    for i in range(8):
        for j in range(8):
            if gameboard[i][j].startswith(turn):
                pieces_positions.append((i, j))

    for piece_position in pieces_positions:
        legal_moves = get_legal_moves(gameboard, turn, piece_position, last_move_positions)
        if len(legal_moves) > 0:
            game_over = False
            break

    if game_over:
        if check_for_checks(gameboard, turn, last_move_positions):
            if turn == "w":
                winner = "b"
            else:
                winner = "w"

    return game_over, winner
