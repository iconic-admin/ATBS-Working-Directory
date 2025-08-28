def isValidChessBoard(boardDict):
    print()
    # check to make sure there are exactly one black
    # king and one white king(value)
    numberOfKingsCheck = list(boardDict.values())
    blackKings = 0
    whiteKings = 0
    for i in range(len(numberOfKingsCheck)):
        if numberOfKingsCheck[i] == 'bK':
            blackKings += 1
        elif numberOfKingsCheck[i] == 'wK':
            whiteKings += 1
    if blackKings == 1 and whiteKings == 1:
        print('Kings check, check.')
    else:
        print('Kings check fail.')

    # check that each player has 16 pieces or less(value)
    numberOfPiecesCheck = list(boardDict.values())
    whitePieces = 0
    blackPieces = 0
    for i in range(len(numberOfPiecesCheck)):
        piecesString = numberOfPiecesCheck[i]
        if piecesString[0] == 'b':
            blackPieces += 1
        elif piecesString[0] == 'w':
            whitePieces += 1
    if blackPieces <= 16 and whitePieces <= 16:
        print('Number of white and black pieces, check.')
    else:
        print('White or black has too many pieces.')

    # check that each player has 8 pawns or less(value)
    numberOfPawnsCheck = list(boardDict.values())
    whitePawns = 0
    blackPawns = 0
    for i in range(len(numberOfPawnsCheck)):
        pawnsString = numberOfPawnsCheck[i]
        if pawnsString[0] == 'b' and pawnsString[1] == 'P':
            blackPawns += 1
        elif pawnsString[0] == 'w' and pawnsString[1] == 'P':
            whitePawns += 1
    if blackPawns <= 8 and whitePawns <= 8:
        print('Number of pawns check, check.')
    else:
        print('Black or white has too many pawns.')
    
    # check that all pieces are on a valid square (key)
    validSquareCheck = list(boardDict.keys())
    goodSquares = ['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8',
                   'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b7', 'b8',
                   'c1', 'c2', 'c3', 'c4', 'c5', 'c6', 'c7', 'c8',
                   'd1', 'd2', 'd3', 'd4', 'd5', 'd6', 'd7', 'd8',
                   'e1', 'e2', 'e3', 'e4', 'e5', 'e6', 'e7', 'e8',
                   'f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8',
                   'g1', 'g2', 'g3', 'g4', 'g5', 'g6', 'g7', 'g8',
                   'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'h7', 'h8',]
    if set(validSquareCheck).issubset(goodSquares):
        print('Valid square check, check.')
    else:
        print('One or more pieces are on an invalid square.')

# GPT 5 used to generate test board sets to test the function.
# I later had to correct the simulated board sets from GPT
# bad GPT...

# Missing white king
invalid_board_1 = {
    'e8': 'bK',
    'd1': 'wQ'
}

# Two white kings
invalid_board_2 = {
    'e1': 'wK',
    'd1': 'wK',
    'e8': 'bK'
}

# Too many pawns (9 white pawns)
invalid_board_3 = {
    'e1': 'wK',
    'e8': 'bK',
    'a1': 'wP',
    'a2': 'wP',
    'a3': 'wP',
    'a4': 'wP',
    'a5': 'wP',
    'a6': 'wP',
    'a7': 'wP',
    'a8': 'wP',
    'h3': 'wP'  # extra ninth pawn
}

# Too many pieces overall (17 black pieces)
invalid_board_4 = {
    'e1': 'wK',
    'e8': 'bK',
    'a8': 'bR',
    'b8': 'bN',
    'c8': 'bB',
    'd8': 'bQ',
    'f8': 'bB',
    'g8': 'bN',
    'h8': 'bR',
    'a1': 'bR',
    'a2': 'bR',
    'a3': 'bR',
    'a4': 'bR',
    'a5': 'bR',
    'f1': 'bR',
    'a7': 'bR',
    'a8': 'bR',
    'f7': 'bR',
    'a6': 'bP'  # pushes black over 16
}

# Invalid square name
invalid_board_5 = {
    'e1': 'wK',
    'e8': 'bK',
    'z9': 'wQ'
}

# Minimal but valid: one king each
valid_board_1 = {
    'e1': 'wK',
    'e8': 'bK'
}

# Typical: kings + a few other legal pieces
valid_board_2 = {
    'e1': 'wK',
    'e8': 'bK',
    'a2': 'wP',
    'b2': 'wP',
    'c2': 'wP',
    'a7': 'wP',
    'b7': 'wP',
    'c7': 'bP',
    'd8': 'bQ'
}

# Max pawns, still valid
valid_board_3 = {
    'e1': 'wK',
    'e8': 'bK',
    **{f"{f}2": "wpawn" for f in "abcdefgh"},
    **{f"{f}7": "bpawn" for f in "abcdefgh"},
}

print('Invalid Board 1.')
isValidChessBoard(invalid_board_1)
print()
print()
print('Invalid Board 2.')
isValidChessBoard(invalid_board_2)
print()
print()
print('Invalid Board 3.')
isValidChessBoard(invalid_board_3)
print()
print()
print('Invalid Board 4.')
isValidChessBoard(invalid_board_4)
print()
print()
print('Invalid Board 5.')
isValidChessBoard(invalid_board_5)
print()
print()
print('Valid board 1.')
isValidChessBoard(valid_board_1)
print()
print()
print('Valid board 2.')
isValidChessBoard(valid_board_2)
print()
print()
print('Valid board 3.')
isValidChessBoard(valid_board_3)
print()
print()