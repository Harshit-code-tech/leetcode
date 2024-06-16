class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def isPeak(i):
            return 0 < i < len(nums)-1 and nums[i] > nums[i-1] and nums[i] > nums[i+1]
        peaks = []
        for i in range(1, len(nums)-1):
            if isPeak(i):
                peaks.append(i)
        
        res = []
        for q in queries:
            if q[0] == 1:
                res.append(max(bisect.bisect_left(peaks, q[2]) - bisect.bisect(peaks, q[1]), 0))
            else:
                isPeakBefore = [isPeak(q[1]+i-1) for i in range(3)]
                nums[q[1]] = q[2]
                for i in range(3):
                    idx = q[1]+i-1
                    if isPeak(idx) and not isPeakBefore[i]:
                        bisect.insort(peaks, idx)
                    if not isPeak(idx) and isPeakBefore[i]:
                        j = bisect.bisect_left(peaks, idx)
                        del peaks[j]
        return res