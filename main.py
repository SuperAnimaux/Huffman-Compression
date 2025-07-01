from tree import Huffman_tree
from file import File

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

    compress_result = ""

    for char in string:
        compress_result += binary_codes[char]
    
    return compress_result



