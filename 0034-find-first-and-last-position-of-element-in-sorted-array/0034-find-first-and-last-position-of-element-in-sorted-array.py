# class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:
#         left = 0    
#         right = len(nums) - 1
#         # first_occurence = -1
#         leftmost=-1
#         rightmost=-1
#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] > target:
#                 right = mid - 1
#             elif nums[mid] < target:
#                 left = mid + 1
#             else:
#                 # first_occurence=mid
#                 leftmost,rightmost=mid,mid
#                 if nums[leftmost-1]==nums[mid]:
#                     right=mid-1
#                     leftmost=right
#                 if nums[rightmost+1]==nums[mid]:
#                     left=mid+1
#                     rightmost=left
#         return [leftmost,rightmost]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        # --- PART 1: FIND THE LEFTMOST INDEX ---
        leftmost = -1
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                # Found target! Record it.
                leftmost = mid
                # CRITICAL: Don't stop! Force the search to the LEFT.
                right = mid - 1
        
        # --- PART 2: FIND THE RIGHTMOST INDEX ---
        rightmost = -1
        left = 0               # <--- RESET POINTERS!
        right = len(nums) - 1  # <--- RESET POINTERS!
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                # Found target! Record it.
                rightmost = mid
                # CRITICAL: Don't stop! Force the search to the RIGHT.
                left = mid + 1
                
        return [leftmost, rightmost]
        

            


        