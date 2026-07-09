class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Create a dummy head to easily build and return the new list
        dummy_head = ListNode(0)
        current = dummy_head
        carry = 0
        
        # Traverse both lists directly until both are exhausted and carry is 0
        while l1 is not None or l2 is not None or carry > 0:
            # Get the values from the current nodes, or 0 if a list is exhausted
            val1 = l1.val if l1 is not None else 0
            val2 = l2.val if l2 is not None else 0
            
            # Calculate the total for this column
            total = val1 + val2 + carry
            
            # Determine the carry and the digit to store
            carry = total // 10
            new_digit = total % 10
            
            # Create a new node with the digit and attach it
            current.next = ListNode(new_digit)
            
            # Advance the current pointer for the result list
            current = current.next
            
            # Advance the pointers for l1 and l2 if they still have nodes
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next
                
        # The actual result starts after the dummy head
        return dummy_head.next

# --- HELPER FUNCTIONS FOR LOCAL TESTING ---

def create_linked_list(arr):
    """Converts a standard Python list into a Linked List of ListNodes."""
    dummy = ListNode(0)
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(node):
    """Traverses a Linked List and prints its values as a standard array."""
    result = []
    while node is not None:
        result.append(node.val)
        node = node.next
    print(result)

# --- MAIN EXECUTION BLOCK ---

def main():
    l1_head = create_linked_list([2, 4, 3]) 
    l2_head = create_linked_list([5, 6, 4]) 

    # 2. Create an instance of the Solution class
    sol = Solution()

    # 3. Call the function and store the resulting head node
    result_head = sol.addTwoNumbers(l1_head, l2_head)

    # 4. Print the result
    # 342 + 465 = 807, which is stored in reverse as [7, 0, 8]
    print("Output:")
    print_linked_list(result_head)

if __name__ == "__main__":
    main()