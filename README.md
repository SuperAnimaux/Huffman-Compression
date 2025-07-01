# Huffman Compression Algorithm

This project implements the Huffman compression algorithm, a popular and efficient lossless data compression technique. It calculates character frequencies from the input, builds an optimized Huffman tree, generates corresponding binary codes, and uses these codes to compress and decompress textual data.

---

## Features

- Compress plain text input into a binary string using Huffman coding.
- Decompress a binary string back to the original text using the code table.
- Compress `.txt` files to a binary file (`.bin`) along with a JSON code table.
- Decompress binary files using the associated JSON code table.
- Interactive command-line interface to choose the desired functionality.

---

## How it works

1. **Frequency calculation:** Counts occurrences of each character in the input.

2. **Huffman tree construction:** Builds a binary tree where more frequent characters have shorter codes.

3. **Binary code generation:** Traverses the tree to assign a unique binary code for each character.

4. **Compression:** Converts the original text into a binary string based on the code table.

5. **Decompression:** Converts the binary string back to text using the inverse code table.

---

## Usage

Run the main script:

```bash
python main.py
```


You will be prompted to choose one of the following options:

1. Compress a text string.

2. Decompress a binary string.

3.Compress a .txt file.

4. Decompress a binary file (.bin) with its .json code table.

5. Exit the program.

## Files generated

* **compressed_file.bin** : The compressed binary output for files.
* **code_table.json** : JSON file containing the Huffman codes needed for decompression.
* **decompressed.txt** : The output text file after decompression.

## Requirements

* Python 3
* Modules: json, ast
* The tree.py and file.py modules (custom modules for the Huffman tree and file structure)

## Notes

* Make sure your .txt files and the corresponding .json code tables are in the same directory when decompressing.
* Compression of very small files or texts may sometimes result in larger outputs due to overhead.
* This implementation uses a simple file-based queue (File class) for breadth-first traversal.

# How the Huffman Algorithm Works ?

Huffman coding is a popular **lossless data compression** technique that reduces the size of textual data by assigning shorter binary codes to more frequent characters and longer codes to less frequent ones.

## Step-by-step process:

1. **Frequency Counting**
    First, the algorithm counts how many times each character appears in the input text. This frequency information is crucial to build the Huffman tree.

2. **Building the Huffman Tree**
    Each character is represented as a leaf node with its frequency. The algorithm repeatedly merges the two nodes with the smallest frequencies into a new node whose frequency is the sum of the two. This process continues until there is only one node left — the root of the Huffman tree.

3. **Generating Binary Codes**
    The algorithm traverses the Huffman tree from the root to each leaf node. Moving to the left child appends a "0" to the code, and moving to the right child appends a "1". Each character thus gets a unique binary code based on its position in the tree.

4. **Compression**
    The original text is then encoded by replacing each character with its corresponding binary code, producing a compressed binary string.

5. **Decompression**
    To decompress, the binary string is decoded by traversing the Huffman tree: reading bits one by one, moving left or right until a leaf node (character) is reached, then outputting that character and restarting from the root for the next bits.

This approach ensures the most frequent characters use fewer bits, which leads to overall data size reduction without losing any information.
