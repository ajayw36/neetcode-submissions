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
        ListNode* l1 = list1;
        ListNode* l2 = list2;
        ListNode new_list = ListNode();
        ListNode* l3 = &new_list;

        while (l1 && l2) {
            if (l1->val < l2->val){
                l3->next = l1;
                l3 = l1;
                l1 = l1->next;
            }
            else {
                l3->next = l2;
                l3 = l2;
                l2 = l2 ->next;
            }
        }

        if (l1) {
            l3->next = l1;
        }
        else {
            l3->next = l2;
        }

        return new_list.next;
    }
};
