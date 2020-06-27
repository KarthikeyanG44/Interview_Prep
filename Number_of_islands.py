"""
This solution uses BFS for counting number of islands in the given grid.
Runtime: 144 ms, faster than 72.31% of Python3 online submissions for Number of Islands.
Memory Usage: 15.6 MB, less than 7.69% of Python3 online submissions for Number of Islands.

"""

class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        nRows = len(grid)
        nCols = len(grid[0])
        visitedArray = [[False for i in range(nCols)] for j in range(nRows)]

        numIslands = 0
        graphStack = []
        count = 0

        for landIdx in landIndices:
            i, j = landIdx
            graphStack = []
            if (grid[i][j] == "1" and not visitedArray[i][j]):
                visitedArray[i][j] = True
                graphStack.append((i, j))
                count += 1

            while (graphStack):
                top_i, top_j = graphStack[-1]
                if top_j + 1 < nCols and grid[top_i][top_j + 1] == "1" and not visitedArray[top_i][top_j + 1]:
                    visitedArray[top_i][top_j + 1] = True
                    graphStack.append((top_i, top_j + 1))
                elif top_i + 1 < nRows and grid[top_i + 1][top_j] == "1" and not visitedArray[top_i + 1][top_j]:
                    visitedArray[top_i + 1][top_j] = True
                    graphStack.append((top_i + 1, top_j))
                elif top_i - 1 >= 0 and grid[top_i - 1][top_j] == "1" and not visitedArray[top_i - 1][top_j]:
                    visitedArray[top_i - 1][top_j] = True
                    graphStack.append((top_i - 1, top_j))
                elif top_j - 1 >= 0 and grid[top_i][top_j - 1] == "1" and not visitedArray[top_i][top_j - 1]:
                    visitedArray[top_i][top_j - 1] = True
                    graphStack.append((top_i, top_j - 1))
                else:
                    discard_node = graphStack.pop()

        return count


if __name__ == "__main__":
    islandCounter = Solution()
    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    numIslands = islandCounter.numIslands(grid)
    print(numIslands)