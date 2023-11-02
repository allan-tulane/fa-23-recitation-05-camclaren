# CMPS 2200 Recitation 6
## Answers

**Name:** Cameron McLaren


Place all written answers from `recitation-06.md` here for easier grading.



- **d.**

File | Fixed-Length Coding | Huffman Coding | Huffman vs. Fixed-Length
----------------------------------------------------------------------
**f1.txt** | fixed-length cost: 1340 | huffman cost: 826 | huffman vs. fixed ratio: 1.62

**alice29.txt**    | fixed-length cost: 1039367 | huffman cost: 676374  | huffman vs. fixed ratio: 1.54

**asyoulik.txt**    | fixed-length cost: 876253  | huffman cost: 606448  | huffman vs. fixed ratio: 1.44

**grammar.lsp**    | fixed-length cost: 26047  | huffman cost: 17356  | huffman vs. fixed ratio: 1.50

**fields.c**    | fixed-length cost: 78050  | huffman cost: 52606  | huffman vs. fixed ratio: 1.39



- **e.**

If every character had the same frequency, then the tree that is built would be complete (balanced in number of leaves), and the depth of a given leaf would be based on simply where it's located in the alphabet. Therefore, all characters would have the same expected Huffman encoding cost (you would use lg(n) where n is the total number of characters for the depth since that's how you calculate the depth in a complete binary tree)

