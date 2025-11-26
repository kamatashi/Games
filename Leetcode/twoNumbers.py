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

var addTwoNumbers = function(l1, l2) {
    const l1Reverse = reverseLinkedList(l1);
    const l2Reverse = reverseLinkedList(l2);

    const sum = listToStrToNum(l1Reverse) + listToStrToNum(l2Reverse)

    const result = sum.toString()

    const resultStringArr = sum.toString().split(''); 
    const reversedResultArr = resultStringArr.reverse();

    return arrayToListNode(reversedResultArr);


};
