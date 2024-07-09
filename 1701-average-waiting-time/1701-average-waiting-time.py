class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        avail_at=0
        summ=0
        for arrival_at,time in customers:
            avail_at=max(avail_at,arrival_at)+time
            summ+=avail_at-arrival_at
        return summ/len(customers)
        