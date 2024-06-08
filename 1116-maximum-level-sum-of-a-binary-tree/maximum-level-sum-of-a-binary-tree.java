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
    public int maxLevelSum(TreeNode root) {
        int[] arr = new int[10000];
        int height = helper(root, arr, 0);

        int max = arr[0];
        int level = 1;

        for (int i = 0; i < height; i++) {
            if (arr[i] > max) {
                max = arr[i];
                level = i + 1;
            }
        }

        return level;
    }

    int helper(TreeNode root, int[] arr, int level) {
        if (root == null) {
            return 0;
        }

        arr[level] += root.val;

        int left = helper(root.left, arr, level + 1);
        int right = helper(root.right, arr, level + 1);

        return Math.max(left, right) + 1;
    }
}