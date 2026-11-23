class ListNode:
  def __init__(self, val = 0, next = None):
    self.val = val
    self.next = next

#Construct the Linked List
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

print("==== Performing Different Operations ====")
#Display original Linked List
curr = head
print("\nOriginal Singly Linked List: ")
while curr:
  print(curr.val, end = " -> ")
  curr = curr.next
print(None)


#Insert New Node
new_node = ListNode(10)
new_node.next = head
head = new_node
print("\nInsert a new Node: 10.")
curr = head
while curr:
  print(curr.val, end = " -> ")
  curr = curr.next
print(None)


#Delete a Node;
print("\nDelete that Inserted Node: 10.")
head = head.next
curr = head
while curr:
  print(curr.val, end = " -> ")
  curr = curr.next
print(None)


#Reverse Linked List
prev = None
curr = head
while curr:
  next_node = curr.next
  curr.next = prev
  prev = curr
  curr = next_node

print("\nAfter Reserve Singly Linked List: ")
curr = prev 
while curr:
  print(curr.val, end = " -> ")
  curr = curr.next
print(None)
