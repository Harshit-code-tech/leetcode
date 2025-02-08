class NumberContainers {
    Map<Integer, Integer> data;
    Map<Integer, PriorityQueue<Integer>> indices;

    public NumberContainers() {
        data = new HashMap<>();
        indices = new HashMap<>();
    }
    
    public void change(int index, int number) {
        data.put(index, number);
        indices.computeIfAbsent(number, _ -> new PriorityQueue<>()).offer(index);
    }
    
    public int find(int number) {
        PriorityQueue<Integer> pq = indices.computeIfAbsent(number, _ -> new PriorityQueue<>());
        while (!pq.isEmpty()) {
            int index = pq.peek();
            if (data.get(index) == number) {
                return index;
            } else {
                pq.poll();
            }
        }
        return -1;
    }
}


/**
 * Your NumberContainers object will be instantiated and called as such:
 * NumberContainers obj = new NumberContainers();
 * obj.change(index,number);
 * int param_2 = obj.find(number);
 */