#!/usr/env/bin python

import argparse

def get_opt():
    group = argparse.ArgumentParser(description="Translate text or binary file to nt file")
    group.add_argument('-i', '--input_file', help='input file path',required=True)
    group.add_argument('-o', '--output_file', help='output file path', required=True)
    group.add_argument('-T', '--type', help='file type: txt or bin. default=[txt]')
    return group.parse_args()

nt_dict = {'0':['A','C'], '1':['G','T']}

def nt2bit(nt_arr,homo=3):
    bit_arr = []
    for i in range(len(nt_arr)):
        if nt_arr[i] == 'A' or nt_arr[i] == 'C':
            bit_arr.append('0')
        else:
            bit_arr.append('1')
    return ''.join(bit_arr)

def bit2txt(bit_line):
    txt_arr = []
    for i in range(0,len(bit_line),8):
        _char_bit = chr(int(bit_line[i:i+8],2))
        txt_arr.append(_char_bit)
    return ''.join(txt_arr)

def decode():
    for i in input:
        i = i.strip()
        if f_type == 'txt':
            bit_arr = nt2bit(i)
        else:
            bit_arr = i
        txt_arr = bit2txt(bit_arr)
        output.write(txt_arr+'\n')

if __name__ == "__main__":
    opts = get_opt()
    input = open(opts.input_file)
    output = open(opts.output_file,'w')
    f_type = opts.type
    decode()
    input.close()
    output.close()

