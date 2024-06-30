class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        def canBuildRow(balls, row):
            return balls >= row
        def buildRow(balls, row):
            balls -= row
            return balls
        def maxHeightStartingWithRed(red, blue):
            height = 0
            
            for row in range(1, red + blue + 1):
                if row % 2 == 1:  # Odd rows: red
                    if canBuildRow(red, row):
                        red = buildRow(red, row)
                        height += 1
                    else:
                        break
                else:  # Even rows: blue
                    if canBuildRow(blue, row):
                        blue = buildRow(blue, row)
                        height += 1
                    else:
                        break
            
            return height
        heightStartingWithRed = maxHeightStartingWithRed(red, blue)
        heightStartingWithBlue = maxHeightStartingWithRed(blue, red)
        
        return max(heightStartingWithRed, heightStartingWithBlue)
