def inside(r, c, rows, cols):
    # check if (r,c) is inside the board
    return 0 <= r < rows and 0 <= c < cols

def is_piece(ch):
    # check if a QRBP piece (not .)
    return ch != '.'

def is_attacker(ch):
    # check if current piece is QRBP
    return ch in {'Q', 'R', 'B', 'P'}

def validate_board(lines):
    # check all input characters are valid
    allowed = {'.', 'K', 'Q', 'R', 'B', 'P'}
    for row in lines:
        for ch in row:
            if ch not in allowed:
                print("Error (Character not allowed)")
                return False
    return True

def checkmate(board):
    lines = board.strip().splitlines()

    rows = len(lines)
    if rows == 0:
        print("Error (Empty board)")
        return

    cols = len(lines[0])
    for row in lines:
        if len(row) != cols:
            print("Error (Not Square)")
            return
        
    if not validate_board(lines):
        return
    
    board = []
    for row in lines:
        board.append(list(row))

    kings = []
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'K':
                kings.append((r, c))

    if len(kings) != 1:
        print("Error (Kings not == 1)")
        return
    kr, kc = kings[0]

    for r in range(rows):
        for c in range(cols):
            ch = board[r][c]
            if not is_attacker(ch):
                continue

            # Pawn
            if ch == 'P':
                for dr, dc in [(-1, -1), (-1, 1)]:
                    rr, cc = r + dr, c + dc
                    if inside(rr, cc, rows, cols) and (rr, cc) == (kr, kc):
                        print("Success")
                        return

            # Rook
            if ch == 'R':
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    rr, cc = r + dr, c + dc
                    while inside(rr, cc, rows, cols):
                        cell = board[rr][cc]
                        if is_piece(cell):
                            if (rr, cc) == (kr, kc):
                                print("Success")
                                return
                            break
                        rr += dr
                        cc += dc

            # Bishop
            if ch == 'B':
                for dr, dc in [(1,1), (1,-1), (-1,1), (-1,-1)]:
                    rr, cc = r + dr, c + dc
                    while inside(rr, cc, rows, cols):
                        cell = board[rr][cc]
                        if is_piece(cell):
                            if (rr, cc) == (kr, kc):
                                print("Success")
                                return
                            break
                        rr += dr
                        cc += dc

            # Queen
            if ch == 'Q':
                for dr, dc in [
                    (1,0), (-1,0), (0,1), (0,-1),
                    (1,1), (1,-1), (-1,1), (-1,-1)
                ]:
                    rr, cc = r + dr, c + dc
                    while inside(rr, cc, rows, cols):
                        cell = board[rr][cc]
                        if is_piece(cell):
                            if (rr, cc) == (kr, kc):
                                print("Success")
                                return
                            break
                        rr += dr
                        cc += dc

    print("Fail")