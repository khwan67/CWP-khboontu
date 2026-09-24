def checkmate(board_str):
    
    board = board_str.strip().split('\n')
    Row = len(board)

    for r in range(Row):
        if len(board[r]) != Row:
            print("Error")
            return
        
    size = len(board)
    king = None
    king_count = 0
    for r in range(size):
        for c in range(size):
            if board[r][c] == 'K':
                king_count += 1
                king = (r, c)
                break
        
    if king_count != 1 or king_count == 0:
        print("Error")
        return

    kr, kc = king
    chess = ('K', 'Q', 'R', 'B', 'P','N')


    straight_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diagonal_dirs = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
   
    for dr, dc in straight_dirs:
        r, c = kr + dr, kc + dc
        while r >= 0 and r < size and c >= 0 and c < size:
            current = board[r][c]
            if current in ('R', 'Q'):
                print("Success")
                return
            elif current in chess:
                break  
            r += dr
            c += dc

    for dr, dc in diagonal_dirs:
        r, c = kr + dr, kc + dc
        while r >= 0 and r < size and c >= 0 and c < size:
            current = board[r][c]
            if current in ('B', 'Q'):
                print("Success")
                return
            elif current in chess:
                break  
            r += dr
            c += dc

    
    pawn = [(kr + 1, kc - 1), (kr + 1, kc + 1)]
    for r, c in pawn:
        if r >= 0 and r < size and c >= 0 and c < size:
            if board[r][c] == 'P':
                print("Success")
                return

    knight = [(kr + 2 , kc - 1),(kr + 1 , kc - 2),(kr - 1 , kc - 2),(kr - 2, kc - 1),(kr - 2 , kc + 1),(kr - 1 , kc + 2),(kr + 1 , kc + 2),(kr + 2,kc + 1)]
    for r,c in knight:
        if 0 <= r < size and 0 <= c < size:
            if board[r][c] == 'N':
                print("Success")
                return

    print("Fail")