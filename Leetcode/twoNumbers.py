/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */

const listToStrToNum = (head) => {
    let acc = "";

    let current = head;

    while (current !== null) {
        acc = acc + current.val.toString(); 
        
        current = current.next;
    }

    return parseInt(acc, 10); 
}

const sumStr = (l) => {
    if (l == []) return 0
    else {
        return sumStr(l[0]) + sumStr(l[0+1])
    }
}


function reverseLinkedList(head) {
    let prev = null;
    let current = head;

    while (current) {
        let nextNode = current.next; 
        current.next = prev;     
        prev = current;          
        current = nextNode;      
    }
    return prev; 
}

function arrayToListNode(arr) {
    if (!arr || arr.length === 0) {
        return null;
    }

    const dummyHead = new ListNode(0);
    let current = dummyHead;

    for (const val of arr) {
        const numVal = parseInt(val, 10);
        
        current.next = new ListNode(numVal);
        current = current.next;
    }

    return dummyHead.next;
}

function ListNode(val, next) {
    this.val = (val === undefined ? 0 : val);
    this.next = (next === undefined ? null : next);
}

var addTwoNumbers = function(l1, l2) {
    const dummyHead = new ListNode(0); 
    let current = dummyHead;           
    let carry = 0;                     

    while (l1 !== null || l2 !== null || carry !== 0) {
        const val1 = l1 ? l1.val : 0;
        const val2 = l2 ? l2.val : 0;

        const sum = val1 + val2 + carry;
        carry = Math.floor(sum / 10);
        const digit = sum % 10;

        current.next = new ListNode(digit); 
        current = current.next;

        if (l1) l1 = l1.next;
        if (l2) l2 = l2.next;
    }

    return dummyHead.next; 
};
