#!/usr/env/bin python

import argparse

begin_map = {'C':'0', 'G':'1', 'T':'2'}
pre_A = {'C':'0', 'G':'1', 'T':'2'}
pre_C = {'G':'0', 'T':'1', 'A':'2'}
pre_G = {'T':'0', 'A':'1', 'C':'2'}
pre_T = {'A':'0', 'C':'1', 'G':'2'}

def get_opt():
    group = argparse.ArgumentParser(description="Translate text or binary file to nt file")
    group.add_argument('-i', '--input_file', help='input file path',required=True)
    group.add_argument('-o', '--output_file', help='output file path', required=True)
    group.add_argument('-d', '--dict_file', help='code dict file path', required=True)
    return group.parse_args()

def nt2bit(nt_str):
    bit_str = []
    for i in range(len(nt_str)):
        if i == 0:
            bit_str.append(begin_map[nt_str[i]])
        elif nt_str[i-1] == 'A':
            bit_str.append(pre_A[nt_str[i]])
        elif nt_str[i-1] == 'T':
            bit_str.append(pre_T[nt_str[i]])
        elif nt_str[i-1] == 'C':
            bit_str.append(pre_C[nt_str[i]])
        elif nt_str[i-1] == 'G':
            bit_str.append(pre_G[nt_str[i]])
    return ''.join(bit_str)

def decode(nt_str):
    txt_str = []
    num = 8
    while nt_str and num > 0:
        if nt_str[:num] in codes.keys():
            txt_str.append(codes[nt_str[:num]])
            nt_str = nt_str[num:]
            num = 8
        else:
            num -= 1
    return ''.join(txt_str)

if __name__ == '__main__':
    opts = get_opt()
    input = open(opts.input_file, encoding='utf-8')
    output = open(opts.output_file, 'w', encoding='utf-8')
    codes_file = open(opts.dict_file, encoding='utf-8')
    codes = dict()
    for i in codes_file:
        i = i.strip("\n").split("\t")
        codes[str(i[1])]  = i[0]
    for nt_str in input:
        bit_str = nt2bit(nt_str.strip())
        output.write( decode(bit_str) + '\n')
    input.close()
    output.close()
    codes_file.close()