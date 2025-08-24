class Solution:
    def countCollisions(self, directions: str) -> int:
        stack = []
        collisions = 0
        
        for car in directions:
            if not stack:
                stack.append(car)
                continue
            
            # Case 1: R vs L → both stop
            if stack[-1] == 'R' and car == 'L':
                collisions += 2
                stack.pop()
                # Now this becomes stationary
                stack.append('S')
                
            # Case 2: R vs S → R stops
            elif stack[-1] == 'R' and car == 'S':
                collisions += 1
                stack.pop()
                stack.append('S')
                
            # Case 3: S vs L → L stops
            elif stack[-1] == 'S' and car == 'L':
                collisions += 1
                # `S` stays, so no pop-push needed
                
            else:
                # No collision, just push
                stack.append(car)
        
        return collisions
