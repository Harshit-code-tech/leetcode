class SmallestInfiniteSet {
    private final Queue<Integer> minHeap;
    private final Set<Integer> set;
    private int min;

    public SmallestInfiniteSet() {
        this.minHeap = new PriorityQueue<>();
        this.set = new HashSet<>();
        this.min = 1;
    }
    
    public int popSmallest() {
        if(this.minHeap.isEmpty())
            return this.min++;

        final int val = this.minHeap.poll();

        this.set.remove(val);

        return val;
    }
    
    public void addBack(final int num) {
        if(this.min > num && !this.set.contains(num)) {
            this.minHeap.offer(num);
            this.set.add(num);
        }
    }
}

/**
 * Your SmallestInfiniteSet object will be instantiated and called as such:
 * SmallestInfiniteSet obj = new SmallestInfiniteSet();
 * int param_1 = obj.popSmallest();
 * obj.addBack(num);
 */