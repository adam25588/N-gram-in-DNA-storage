#!/usr/env/bin python
# -*- coding: utf-8 -*-

import argparse

begin_map = {'0':'C', '1':'G', '2':'T'}
pre_A = {'0':'C', '1':'G', '2':'T'}
pre_C = {'0':'G', '1':'T', '2':'A'}
pre_G = {'0':'T', '1':'A', '2':'C'}
pre_T = {'0':'A', '1':'C', '2':'G'}

def get_opt():
    group = argparse.ArgumentParser(description="Translate text or binary file to nt file")
    group.add_argument('-i', '--input_file', help='input file path',required=True)
    group.add_argument('-o', '--output_file', help='output file path', required=True)
    return group.parse_args()

class Node:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight
        self.left = None
        self.right = None
        self.mid = None
        self.father = None
    def is_left_child(self):
        return self.father.left == self
    def is_right_child(self):
        return self.father.right == self

def create_prim_nodes(data_set, labels):
    if(len(data_set) != len(labels)):
        raise Exception('数据和标签不匹配！')
    nodes = []
    for i in range(len(labels)):
        nodes.append(Node(labels[i], data_set[i]))
    return nodes

def create_HF_tree(nodes):
    tree_nodes = nodes.copy()
    while len(tree_nodes) > 2:
        tree_nodes.sort(key=lambda node: node.weight)
        new_left = tree_nodes.pop(0)
        new_right = tree_nodes.pop(0)
        new_mid = tree_nodes.pop(0)
        new_node = Node(None, (new_left.weight + new_right.weight + new_mid.weight))
        new_node.left = new_left
        new_node.right = new_right
        new_node.mid = new_mid
        new_mid.father = new_left.father = new_right.father = new_node
        tree_nodes.append(new_node)
    tree_nodes[0].father = None
    return tree_nodes[0]

def get_huffman_code(nodes):
    codes = {}
    for node in nodes:
        code = ''
        name = node.name
        while node.father != None:
            if node.is_left_child():
                code = '0' + code
            elif node.is_right_child():
                code = '1' + code
            else:
                code = '2' + code
            node = node.father
        codes[name] = code
    return codes

def encode(txt_str):
    bit_str = []
    for i in txt_str:
        bit_str.append(codes[i])
    return ''.join(bit_str)

def bit2nt(bit_str):
    nt_str = []
    for i in range(len(bit_str)):
        if i == 0:
            nt_str.append(begin_map[bit_str[i]])
        elif nt_str[-1] == 'A':
            nt_str.append(pre_A[bit_str[i]])
        elif nt_str[-1] == 'T':
            nt_str.append(pre_T[bit_str[i]])
        elif nt_str[-1] == 'C':
            nt_str.append(pre_C[bit_str[i]])
        elif nt_str[-1] == 'G':
            nt_str.append(pre_G[bit_str[i]])
    return ''.join(nt_str)
     
if __name__ == '__main__':
    opts = get_opt()
    input = open(opts.input_file, encoding='utf-8')
    output = open(opts.output_file,'w')
    codes_dict = open('code_dict.txt', 'w', encoding='utf-8')  ## 创建一个密码子本
    all_cont = ''
    labels = []
    data_set = []
    all_input = []
    for i in input:
        all_cont = all_cont + i.strip()
        all_input.append(i)
    
    for i in set(all_cont):
        labels.append(i)
        data_set.append(all_cont.count(i))
    nodes = create_prim_nodes(data_set, labels)
    root = create_HF_tree(nodes)
    codes = get_huffman_code(nodes)
    for i in codes.keys():
        codes_dict.write(i + "\t" + codes[i] + '\n')

    for txt_str in all_input:
        txt_str = txt_str.strip()
        bit_str = encode(txt_str)
        nt_str = bit2nt(bit_str)
        output.write(nt_str + '\n')
    input.close()
    output.close()
    codes_dict.close()
    