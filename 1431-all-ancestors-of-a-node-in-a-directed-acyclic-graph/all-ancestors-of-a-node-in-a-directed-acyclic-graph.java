class Solution {
    public void dfs(ArrayList<Integer> arr[],int p , int c , boolean visited[],List<List<Integer>> ans){
        visited[c]=true;
        for(int ele:arr[c]){
            if(!visited[ele]){
                ans.get(ele).add(p);
                dfs(arr,p,ele,visited,ans);
            }
        }
    }
    public List<List<Integer>> getAncestors(int n, int[][] edges) {
        List<List<Integer>> ans=new ArrayList<>();
        for(int i=0;i<n;i++){
 ans.add(new ArrayList<>());
        }
          ArrayList<Integer>[] adj = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            adj[i] = new ArrayList<>();
        }
        for (int[] ele : edges) {
            adj[ele[0]].add(ele[1]);
        }
        // for(ArrayList<Integer> ele:adj){
        //     System.out.println(ele);
        // }
        for(int i=0;i<n;i++){
  dfs(adj,i,i,new boolean[n],ans);
        }
        for(int i=0;i<n;i++){
            Collections.sort(ans.get(i));
        }
 return ans;      
    }
}