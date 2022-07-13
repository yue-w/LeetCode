

# %%
## f(x) = (x - 4) ** 2
def dw_prime(w):
     return 2 * w - 8

def dw2_prime(w):
    return 2

counter = 0
total = 20
alpha = 1
w = 1
epsilon = 1e-6
while counter < total:
    counter += 1
    wcp = w
    w = w - alpha * dw_prime(w)/dw2_prime(w)
    if abs(wcp - w) < epsilon:
         break

print(w)


# %%
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse(head):
    """
    Reverse the linked list with head "head"
    """ 
    prev = None
    curr = head
    while curr:
        nxtcp = curr.next
        curr.next = prev
        prev = curr
        curr = nxtcp
    return prev

head = ListNode(0)
head.next = ListNode(1)
head.next.next = ListNode(2)
head.next.next.next = ListNode(3)
head = reverse(head)
while(head):
    print(head.val)
    head = head.next
# %%
'b' - 'a'
# %%
import math
math.ceil(2.5)
# %%
-2 % 10
# %%
M = int(1e9 + 7)
print(472391999 % M)

# %%
chr(ord('B') ^ 32)
# %%
ord('A')
# %%
ord('a')
# %%
a = ['a'] * 4
a[1] = 'b'
print(a)
# %%
20 % 10
# %%
