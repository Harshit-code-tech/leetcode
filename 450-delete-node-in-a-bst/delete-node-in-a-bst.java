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
    public TreeNode deleteNode(TreeNode root, int key) {
        if (root == null) return null;
        if (root.val == key) {
            // Leaf or single child
            if (root.left == null) return root.right;
            if (root.right == null) return root.left;
            // In-order successor (right subtree's min)
            TreeNode successor = root.right;
            while (successor.left != null) successor = successor.left;
            root.val = successor.val;
            root.right = deleteNode(root.right, successor.val);
        } else if (root.val < key) {
            root.right = deleteNode(root.right, key);
        } else {
            root.left = deleteNode(root.left, key);
        }
        return root;
    }
}
