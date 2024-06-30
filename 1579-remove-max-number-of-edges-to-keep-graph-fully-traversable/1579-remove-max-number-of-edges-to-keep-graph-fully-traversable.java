class Solution {
    int[] parent;
    int[] size;
    int count;

    public int maxNumEdgesToRemove(int n, int[][] edges) {
        parent = new int[n + 1];
        size = new int[n + 1];
        count = n;

        for (int i = 1; i <= n; i++) {
            parent[i] = i;
            size[i] = 1;
        }

        int res = 0;

        for (int[] edge : edges) {
            if (edge[0] == 3) {
                if (!union(edge[1], edge[2])) {
                    res++;
                }
            }
        }

        int[] parentCopy = parent.clone();
        int[] sizeCopy = size.clone();
        int countCopy = count;

        for (int[] edge : edges) {
            if (edge[0] == 1) {
                if (!union(edge[1], edge[2])) {
                    res++;
                }
            }
        }

        if (count != 1) {
            return -1;
        }

        parent = parentCopy;
        size = sizeCopy;
        count = countCopy;

        for (int[] edge : edges) {
            if (edge[0] == 2) {
                if (!union(edge[1], edge[2])) {
                    res++;
                }
            }
        }

        if (count != 1) {
            return -1;
        }

        return res;
    }

    private int find(int x) {
        if (x != parent[x]) {
            parent[x] = find(parent[x]);
        }
        return parent[x];
    }

    private boolean union(int x, int y) {
        int rootX = find(x);
        int rootY = find(y);
        if (rootX == rootY) {
            return false;
        }
        if (size[rootX] < size[rootY]) {
            int temp = rootX;
            rootX = rootY;
            rootY = temp;
        }
        parent[rootY] = rootX;
        size[rootX] += size[rootY];
        count--;
        return true;
    }
}