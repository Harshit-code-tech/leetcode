class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        friends = list(range(1, n+1))
        current_position = 0

        # Till 1 friend is left
        while n > 1:
            # Current position after k move, (k-1) to include current friend.
            current_position = (current_position + (k-1)) % n
            # Remove picked friend
            friends.pop(current_position)
            # Decrement total friends
            n -= 1

        # Return last friend
        return friends[0]