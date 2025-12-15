# Generation ID: Hutch_1763800315373_pdf9kv15q (前半)

def myai(board, color):
    """
    オセロの最適な置き位置を返す関数
    """
    size = len(board)
    opponent_color = 3 - color
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    corners = [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]
    
    def count_flips(board, row, col, color, direction):
        """指定した方向で取れる石の数を数える"""
        if board[row][col] != 0:
            return 0
        dr, dc = direction
        count = 0
        r, c = row + dr, col + dc
        while 0 <= r < size and 0 <= c < size:
            if board[r][c] == 0:
                return 0
            if board[r][c] == color:
                return count
            count += 1
            r += dr
            c += dc
        return 0
    
    def get_total_flips(board, row, col, color):
        """その位置での全方向の取れる石の合計"""
        total = 0
        for direction in directions:
            total += count_flips(board, row, col, color, direction)
        return total
    
    def get_opponent_moves(board, opponent_color):
        """相手が置ける位置の数を数える"""
        count = 0
        for r in range(size):
            for c in range(size):
                if get_total_flips(board, r, c, opponent_color) > 0:
                    count += 1
        return count
    
    def get_available_moves(board, color):
        """自分が置ける位置の数を数える"""
        count = 0
        for r in range(size):
            for c in range(size):
                if get_total_flips(board, r, c, color) > 0:
                    count += 1
        return count
    
    best_move = None
    best_score = -float('inf')
    
    # 候補手を評価
    candidates = []
    
    for row in range(size):
        for col in range(size):
            flips = get_total_flips(board, row, col, color)
            if flips > 0:
                candidates.append((row, col, flips))
    
    for row, col, flips in candidates:
        # ボードをシミュレート
        test_board = [r[:] for r in board]
        test_board[row][col] = color
        for direction in directions:
            count = count_flips(board, row, col, color, direction)
            if count > 0:
                dr, dc = direction
                r, c = row + dr, col + dc
                for _ in range(count):
                    test_board[r][c] = color
                    r += dr
                    c += dc
        
        # スコア計算
        score = 0
        
        # 角を取ったか
        if (row, col) in corners:
            score += 1000
        
        # 相手に角を取らせないか
        opponent_can_corner = False
        for cr, cc in corners:
            if get_total_flips(test_board, cr, cc, opponent_color) > 0:
                opponent_can_corner = True
                break
        if not opponent_can_corner:
            score += 500
        
        # 相手の置ける場所を減らす
        opponent_moves = get_opponent_moves(test_board, opponent_color)
        score -= opponent_moves * 10
        
        # 自分の置ける場所を増やす
        my_moves = get_available_moves(test_board, color)
        score += my_moves * 5
        
        # 取れる石の数
        score += flips
        
        if score > best_score:
            best_score = score
            best_move = (col, row)
    
    return best_move

# Generation ID: Hutch_1763800315373_pdf9kv15q (後半)
