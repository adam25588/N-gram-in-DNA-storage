#!/usr/env/bin python

import argparse

def get_opt():
    group = argparse.ArgumentParser(description="Translate text or binary file to nt file")
    group.add_argument('-i', '--input_file', help='input file path',required=True)
    group.add_argument('-o', '--output_file', help='output file path', required=True)
    group.add_argument('-T', '--type', help='file type: txt or bin. default=[txt]')
    return group.parse_args()

nt_dict = {'0':['A','C'], '1':['G','T']}

def bit2nt(bit_arr,homo=3):
    nt_arr = []
    for i in range(len(bit_arr)):
        if nt_arr[-(homo-1):] != nt_dict[bit_arr[i]][0]*2:
            nt_arr.append(nt_dict[bit_arr[i]][0])
        else:
            nt_arr.append(nt_dict[bit_arr[i]][1])
    return ''.join(nt_arr)

def txt2bit(txt_line):
    bit_arr = []
    for i in range(len(txt_line)):
        _char_bit = bin(ord(txt_line[i])).replace('0b','')
        _char_bit = '0'*(8-len(_char_bit)) + _char_bit
        bit_arr.append(_char_bit)
    return ''.join(bit_arr)

def encode():
    for i in input:
        i = i.strip()
        if f_type == 'txt':
            bit_arr = txt2bit(i)
        else:
            bit_arr = i
        nt_arr = bit2nt(bit_arr)
        output.write(nt_arr+'\n')

if __name__ == "__main__":
    opts = get_opt()
    input = open(opts.inputfile)
    output = open(opts.outfile,'w')
    f_type = opts.type
    encode()
    input.close()
    output.close()

