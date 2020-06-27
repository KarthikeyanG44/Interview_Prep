class Solution:
    def maxAreaOfIsland(self, grid):
        if not grid:
            return 0

        ###### Let j correspond to horizontal traversals and i correspond to vertical traversals #####

        maxArea = 0

        nRows = len(grid)
        nCols = len(grid[0])

        visitedArray = [[False for j in range(nCols)] for i in range(nRows)]
        #### Initially do iterative solution ######
        for i in range(nRows):
            for j in range(nCols):
                if grid[i][j] == 1 and not visitedArray[i][j]:
                    visitedArray[i][j] = True
                    localGraphStack = []
                    localGraphStack.append((i, j))
                    currentIslandArea = 1
                    while (localGraphStack):
                        m, n = localGraphStack[-1]
                        if m + 1 < nRows and grid[m + 1][n] == 1 and not visitedArray[m + 1][n]:
                            visitedArray[m + 1][n] = True
                            currentIslandArea += 1
                            localGraphStack.append((m + 1, n))
                        elif m - 1 >= 0 and grid[m - 1][n] == 1 and not visitedArray[m - 1][n]:
                            visitedArray[m - 1][n] = True
                            currentIslandArea += 1
                            localGraphStack.append((m - 1, n))
                        elif n + 1 < nCols and grid[m][n + 1] == 1 and not visitedArray[m][n + 1]:
                            visitedArray[m][n + 1] = True
                            currentIslandArea += 1
                            localGraphStack.append((m, n + 1))
                        elif n - 1 >= 0 and grid[m][n - 1] == 1 and not visitedArray[m][n - 1]:
                            visitedArray[m][n - 1] = True
                            currentIslandArea += 1
                            localGraphStack.append((m, n - 1))
                        else:
                            discardNode = localGraphStack.pop()

                    if currentIslandArea > maxArea:
                        maxArea = currentIslandArea

        return maxArea

