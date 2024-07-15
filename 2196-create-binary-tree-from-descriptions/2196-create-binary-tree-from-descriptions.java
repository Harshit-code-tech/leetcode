class Solution {
    public TreeNode createBinaryTree(int[][] descriptions) {
        TreeNode parent=new TreeNode();
        TreeNode root=parent;
        Set<Integer>cSet=new HashSet<>();
        Set<Integer>pSet=new HashSet<>();
        Map<Integer,List<int[]>>mp=new HashMap<>();
        for(int description[]:descriptions){
            int curr_parent=description[0];
            int isLeft=description[2];
            int child=description[1];


            // for finding the parent
            if(!cSet.contains(child)){
                cSet.add(child);
            }
            if(!pSet.contains(curr_parent)){
                pSet.add(curr_parent);
            }
            if(pSet.contains(child)){
                pSet.remove(child);
            }
            if(cSet.contains(curr_parent)){
                pSet.remove(curr_parent);
            }
            
            List<int[]>curr=new ArrayList<>();
            curr.add(new int[]{child,isLeft});
            if(!mp.containsKey(curr_parent)){
                mp.put(curr_parent,curr);
            }
            else{
                mp.get(curr_parent).add(new int[]{child,isLeft});
            }
            
        
        }
        for(int num:pSet)parent.val=num;
        dfs(mp,root);
        return parent;
    
        }

         public void dfs(Map<Integer,List<int[]>>mp,TreeNode root){
        
             if(!mp.containsKey(root.val)){
                root.left=null;
                root.right=null;
                return;
             }
            for(int adj[]:mp.get(root.val)){
                int child=adj[0];
                int isLeft=adj[1];

                if(isLeft==1){
                    root.left=new TreeNode(child);
                    dfs(mp,root.left);
                }
                else{
                    root.right=new TreeNode(child);
                    dfs(mp,root.right);
                }
            
            }
        }
        
    
}