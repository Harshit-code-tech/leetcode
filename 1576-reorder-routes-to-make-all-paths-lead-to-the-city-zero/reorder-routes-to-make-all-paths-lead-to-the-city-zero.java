class Solution {
  public int minReorder(int n, int[][] connections) {
    LinkedList<int[]>[] g = new LinkedList[n];
    for(int i = 0; i != n; ++i) g[i] = new LinkedList<>();  
    for(int[] c: connections){  
      g[c[0]].add(new int[]{c[1], 1});
      g[c[1]].add(new int[]{c[0], 0}); 
    }  

    int[] vis = new int[n];
    int reorderRoads = 0;
    LinkedList<Integer> q = new LinkedList<>();           
    q.add(0);
    while(! q.isEmpty()){                                 
      int city = q.poll();
      if(vis[city] == 1) continue;
      vis[city] = 1;

      for(int[] neib: g[city])
        if(vis[neib[0]] == 0){
          q.add(neib[0]);
          if(neib[1] == 1) ++reorderRoads;
        }
    }

    return reorderRoads;
  }
}