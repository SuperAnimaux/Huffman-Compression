from tree import Huffman_tree
from file import File
import ast
import json
import os

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


def compress_text(string, file=False):

    char_frequencies = frequencies_count(string)

    huffman_tree = create_huffman_tree(char_frequencies)

    binary_codes = create_binary_codes(huffman_tree)
    if file:
        print("----------------\ncode_table.json is the file containing the table of codes; keep it because it is necessary to decompress the file")
        with open("code_table.json", "w") as f:
            json.dump(binary_codes, f)
    else:
        print(f"----------------\nThis is the table of codes; keep it because it is necessary to decompress the text: {binary_codes}")

    compress_result = ""

    for char in string:
        compress_result += binary_codes[char]
    
    return compress_result


def read_file(file):

    if not os.path.isfile(file):
        print(f"Error: The file '{file}' does not exist.")
        return None
    
    with open(f"{file}", "r", encoding="utf-8") as f:
        content = f.read()
    return content

def read_compressed_file(filename):
    with open(filename, "rb") as f:
        byte_data = f.read()
    bits = "".join(f"{byte:08b}" for byte in byte_data)
    return bits


def load_json(json_file):
    if not os.path.isfile(json_file):
        print(f"Error: The JSON file '{json_file}' does not exist.")
        return None
    try:
        with open(json_file, "r") as f:
            code_table = json.load(f)
    except json.JSONDecodeError:
        print("Error: JSON file is corrupted or not valid.")
        return None
    return code_table


def compress_file(content):
    compressed_file = compress_text(content, True)
    compressed_bytes = bits_to_bytes(compressed_file)
    with open("compressed_file.bin", "wb") as f:
        f.write(compressed_bytes)


def decompress_file_bin(bin_filename, json_filename):
    compressed_bits = read_compressed_file(bin_filename)
    if compressed_bits is None:
        return
    code_table = load_json(json_filename)
    if code_table is None:
        return
    decompressed_text = decompress(compressed_bits, code_table)
    with open("decompressed.txt", "w", encoding="utf-8") as f:
        f.write(decompressed_text)


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



def bits_to_bytes(bits):
    b = bytearray()
    for i in range(0, len(bits), 8):
        byte = bits[i:i+8]
        if len(byte) < 8:
            byte = byte.ljust(8, '0')
        b.append(int(byte, 2))
    return bytes(b)


def main():
    print("Welcome to the Huffman compression algorithm ! \n This project implements the Huffman compression algorithm, an efficient lossless coding technique used to reduce the size of textual data. It calculates character frequencies, builds an optimized Huffman tree, and generates corresponding binary codes for each character.")
    while True :
        print("----------------\nChoose a functionality : \n 1. I want to compress a text ! \n 2. I want to decompress a text ! \n 3. I want to compress a file (only .txt)\n 4. I want to decompress a file (only .txt).\n 5. I want to exit")
        
        try:
            choose = int(input("Choose an option: "))
            if choose not in [1, 2, 3, 4, 5]:
                print("Please enter a valid option number (1-5).")
                continue
            
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        if choose == 1:
            text = input("Enter the text to compress : ")
            binary_text =  ''.join(format(ord(c), '08b') for c in text)
            print(f"----------------\nThe initial binary of your text is: {binary_text} , with a length of {len(text)*8} bits.")

            compressed_text = compress_text(text)
            print(f"----------------\nThe compressed text is : {compressed_text} , with a length of {len(compressed_text)} bits.")

        elif choose == 2:
            compressed_binary = input("Enter the compressed binary : ")
            codes_table = ast.literal_eval(input("Enter the table of codes : "))

            print(f"----------------\nThe text is : {decompress(compressed_binary, codes_table)}")

        elif choose == 3:
            print("Please make sure the file is in the same directory")
            file = input("Enter the filename with the .txt : ")
            file_content = read_file(file)

            compress_file(file_content)

        elif choose == 4:
            print("Please make sure the file and the .json are in the same directory")
            file = input("Enter the filename with the .bin : ")
            json_file = input("Enter the filename with the .json : ")

            decompress_file_bin(file, json_file)

        elif choose == 5:
            break

        

if __name__ == "__main__": main()