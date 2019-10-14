## Interview Answers

During your challenge, you will be pulled aside by a PM for a 5 minute interview. During this interview, you will be expected to answer the following two topics:

Explain in detail the workings of a dynamic array:
* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

  **For accessing an array item is runtime of O(1) constant time. However for more complicated functions like add or remove from front can be O(n). For add or remove from back can be less as you are removing/adding to the end and do not need to rearrange all items in the array/list.

* What is the worse case scenario if you try to extend the storage size of a dynamic array?

  **In worse case scenario, extending the storage size of the dynamic array can result in O(n) linear time complexity bceause you would need to set new space in memory and copy each item over to the new space. 

Explain how blockchain networks remain in consensus:
* What does a node do if it gets a message from another in the network with a new block?

  **A Node will follow the defined rules of the blockchain and check the hash validity of the new block. If it is valid, it will be added to the blockchain.

* Why can't someone cheat by changing a transaction from an earlier block to give themselves coins?

  **They can not alter any character in a data set or that would cause the hash for that transaction to completely change and invalidate the block.