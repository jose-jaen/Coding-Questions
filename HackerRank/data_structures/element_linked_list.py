class SinglyLinkedListNode:
    pass


def print_linked_list(head: 'SinglyLinkedListNode') -> None:
    while head:
        if head.data is not None:
            print(head.data)
        head = head.next
