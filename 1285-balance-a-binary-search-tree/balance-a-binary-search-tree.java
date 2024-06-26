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
public class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
  // In-order traversal to collect node values
  private List<Integer> inOrder(TreeNode root) {
    List<Integer> values = new ArrayList<>();
    if (root != null) {
      values.addAll(inOrder(root.left));
      values.add(root.val);
      values.addAll(inOrder(root.right));
    }
    return values;
  }
  
  // Build balanced BST from sorted array (helper function)
  private TreeNode buildBalancedBST(List<Integer> values, int start, int end) {
    if (start > end) {
      return null;
    }
    int mid = start + (end - start) / 2;
    TreeNode root = new TreeNode(values.get(mid));
    root.left = buildBalancedBST(values, start, mid - 1);
    root.right = buildBalancedBST(values, mid + 1, end);
    return root;
  }

  public TreeNode balanceBST(TreeNode root) {
    if (root == null) {
      return null;
    }
    // In-order traversal to get sorted list of values
    List<Integer> values = inOrder(root);
    // Build balanced BST from the sorted values
    return buildBalancedBST(values, 0, values.size() - 1);
  }
}