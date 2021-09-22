# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        i = l1
        j = l2
        rows = []
        addon = 0
        while i is not None or j is not None:
            row = 0
            if i is not None and j is not None:
                row = i.val + j.val + int(addon)
            elif i is None and j is not None:
                row = j.val + addon
            elif i is not None and j is None:
                row = i.val + addon
            row = list(str(row))
            if len(row) == 1:
                rows.append(int(row[0]))
                addon = 0
            elif len(row) == 2:
                rows.append(int(row[1]))
                addon = int(row[0])
            i = i.next if i is not None else None
            j = j.next if j is not None else None
        if int(addon) > 0:
            rows.append(addon)
        nodes = []
        for i in list(range(len(rows)))[::-1]:
            if len(nodes) == 0:
                node = ListNode(val=rows[i], next=None)
            else:
                node = ListNode(val=rows[i], next=nodes[-1])
            nodes.append(node)
        return nodes[-1]



