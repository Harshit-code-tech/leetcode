/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean leafSimilar(TreeNode root1, TreeNode root2) {
        if(root1.left == null && root1.right == null && root2.left == null && root2.right == null) return root1.val == root2.val;
        List<Integer> firstList = new ArrayList<>();
        List<Integer> secondList = new ArrayList<>();
        addLastLayer(root1,firstList);
        addLastLayer(root2,secondList);
        if(firstList.size() != secondList.size()){
            return false;
        }
        for( int i = 0; i < firstList.size(); i++){
            if(!firstList.get(i).equals(secondList.get(i))){
                return false;
            }
        }
        return true;
    }
     public void addLastLayer(TreeNode root, List<Integer> listToAdd){
        if(root == null) return;
        if(root.left == null && root.right == null){
            listToAdd.add(root.val );
            return;
        }
        addLastLayer(root.left, listToAdd);
        addLastLayer(root.right, listToAdd);
    }
}