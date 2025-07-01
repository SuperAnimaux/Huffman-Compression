from tree import Huffman_tree
from file import File
import ast

def frequencies_count(string):
    result = {}
    for char in string:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result


def create_huffman_tree(frequencies):
    huffman_tree = [Huffman_tree((char, freq), None, None) for char, freq in frequencies.items()]

    while len(huffman_tree) > 1:
        huffman_tree.sort(key=lambda node: node.node[1])
        left = huffman_tree.pop(0)
        right = huffman_tree.pop(0)
        merged = Huffman_tree((left.node[0] + right.node[0], left.node[1] + right.node[1]), left, right)
        huffman_tree.append(merged)

    return huffman_tree


def create_binary_codes(huffman_tree):
    binary_codes = {}
    file = File()
    file.insertfile((huffman_tree[-1], ""))

    while file.file_len() > 0:

        node, code = file.popfile()

        if node.is_a_leaf():
            binary_codes[node.node[0]] = code

        else:
            if node.left_child != None:
                file.insertfile((node.left_child, code + "0"))
            if node.right_child != None:
                file.insertfile((node.right_child, code + "1"))
    return binary_codes


def compress_text(string):

    char_frequencies = frequencies_count(string)

    huffman_tree = create_huffman_tree(char_frequencies)

    binary_codes = create_binary_codes(huffman_tree)
    print(f"This is the table of codes; keep it because it is necessary to decompress the text: {binary_codes}")

    compress_result = ""

    for char in string:
        compress_result += binary_codes[char]
    
    return compress_result


def decompress(binary_string, code_table):

    inverse_code_table = {v: k for k, v in code_table.items()}

    result = ""
    code = ""

    for bit in binary_string:
        code += bit
        if code in inverse_code_table:
            result += inverse_code_table[code]
            code = ""

    return result


def main():
    print("Welcome to the Huffman compression algorithm ! \n This project implements the Huffman compression algorithm, an efficient lossless coding technique used to reduce the size of textual data. It calculates character frequencies, builds an optimized Huffman tree, and generates corresponding binary codes for each character.")
    while True :
        print("Choose a functionality : \n 1. I want to compress a text ! \n 2. I want to decompress a text ! \n 3. I want ot exit")
        choose = int(input())

        if choose == 1:
            text = input("Enter the text to compress : ")
            binary_text =  ''.join(format(ord(c), '08b') for c in text)
            print(f"----------------\nThe initial binary of your text is: {binary_text} , with a lenght of {len(text)*8} bits.")

            compressed_text = compress_text(text)
            print(f"The compressed text is : {compressed_text} , with a lenght of {len(compressed_text)} bits.")

        elif choose == 2:
            compressed_binary = input("Enter the compressed binary : ")
            codes_table = ast.literal_eval(input("Enter the table of codes : "))

            print(f"The text is : {decompress(compressed_binary, codes_table)}")

        else:
            print("Error")

        

main()