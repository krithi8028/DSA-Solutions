class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # Sets to keep track of used numbers
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize the sets with the existing board
        empty_cells = []
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty_cells.append((i, j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + j // 3].add(val)

        def backtrack(index):
            # If all empty cells are filled, the Sudoku is solved
            if index == len(empty_cells):
                return True

            row, col = empty_cells[index]
            box_index = (row // 3) * 3 + col // 3

            for num in "123456789":
                if num not in rows[row] and num not in cols[col] and num not in boxes[box_index]:
                    # Place the number
                    board[row][col] = num
                    rows[row].add(num)
                    cols[col].add(num)
                    boxes[box_index].add(num)

                    # Recur for the next cell
                    if backtrack(index + 1):
                        return True

                    # Undo the move (backtrack)
                    board[row][col] = "."
                    rows[row].remove(num)
                    cols[col].remove(num)
                    boxes[box_index].remove(num)

            return False

        # Start the backtracking process
        backtrack(0)
