# Assuming the ListNode class is defined as before

class Solution:
    def addTwoNumbersForward(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []

        # Step 1: Populate the stacks
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next

        carry = 0
        # This will be the head of our resulting list, built backwards
        result_head = None 

        # Step 2: Add digits by popping from stacks
        while stack1 or stack2 or carry != 0:
            val1 = stack1.pop() if stack1 else 0
            val2 = stack2.pop() if stack2 else 0

            total_sum = val1 + val2 + carry
            digit = total_sum % 10
            carry = total_sum // 10

            # Step 3: Create the new node and insert it at the beginning of the list
            new_node = ListNode(digit)
            new_node.next = result_head
            result_head = new_node
            
        return result_head
