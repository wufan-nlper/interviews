"""1.13一面"""

"""成对反转链表"""


def reverse(head):
    if not head or not head.next:
        return head
    new_head = head.next
    head.next = reverse(new_head.next)
    new_head.next = head
    return new_head


"""break"""