class RecentCounter {
    int [] times ;
    int size = 0;
    public RecentCounter() {
        this.times = new int[10000];
    }
    
    public int ping(int t) {
        times[size++] = t;
        int count = 0;
        for (int i = size - 1; i >= 0; i--) {
            if (t - times[i] <= 3000) {
                count++;
            }
            else break;
        }
        return count ;
    }
}

/**
 * Your RecentCounter object will be instantiated and called as such:
 * RecentCounter obj = new RecentCounter();
 * int param_1 = obj.ping(t);
 */