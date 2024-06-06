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
    public int goodNodes(TreeNode root) {
        return checkGoodNodes(root,root.val);
        
    }
    private int checkGoodNodes(TreeNode root, int maxValue){
    if(root==null){
        return 0;
    }

    return (maxValue<=root.val?1:0) + checkGoodNodes(root.left,Math.max(root.val,maxValue))+checkGoodNodes(root.right,Math.max(root.val,maxValue));

}
}