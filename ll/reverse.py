

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = None  # Capital 'N' for None
        curr = head
        
        # 2. Iterate through the list
        while curr:
            next_node = curr.next  # Save next
            curr.next = prev       # Reverse link
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward
            
        # 3. Return the new head (which is prev)
        return prev
