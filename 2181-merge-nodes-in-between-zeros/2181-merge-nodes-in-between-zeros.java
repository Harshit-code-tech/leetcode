/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeNodes(ListNode head) {
        // Skip the initial zero node as per problem constraints
        head = head.next;

        // New list to store the result
        ListNode newHead = new ListNode(0);
        ListNode currentNewNode = newHead;

        // Variable to store the sum between zeroes
        int sum = 0;

        while (head != null) {
            if (head.val == 0) {
                // When encountering a zero, create a new node with the sum and reset the sum
                currentNewNode.next = new ListNode(sum);
                currentNewNode = currentNewNode.next;
                sum = 0;
            } else {
                // Accumulate the sum
                sum += head.val;
            }
            head = head.next;
        }

        return newHead.next; // The first node is a dummy node
    }
}