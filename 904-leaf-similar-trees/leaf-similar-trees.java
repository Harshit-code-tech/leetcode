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
        StringBuilder seq1 = new StringBuilder();
        StringBuilder seq2 = new StringBuilder();

        buildSeq(root1, seq1);
        buildSeq(root2, seq2);

        return seq1.toString().equals(seq2.toString());
    }
    private void buildSeq(TreeNode root, StringBuilder seq){
         if(root == null)return;
         if(root.left == null && root.right == null){
             seq.append(Integer.toString(root.val) + " ");
             return;
         }
         buildSeq(root.left, seq);
         buildSeq(root.right, seq);
    }
}