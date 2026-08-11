/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode dummy = ListNode();
        ListNode* l3 = &dummy;

        while (list1 && list2) {
            if (list1->val < list2->val){
                l3->next = list1;
                l3 = list1;
                list1 = list1->next;
            }
            else {
                l3->next = list2;
                l3 = list2;
                list2 = list2 ->next;
            }
        }

        if (list1) {
            l3->next = list1;
        }
        else {
            l3->next = list2;
        }

        return dummy.next;
    }
};
