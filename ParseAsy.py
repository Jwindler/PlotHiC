#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Author: Zijie Jiang
@Contact: jzjlab@163.com
@File: ParseAsy.py
@Time: 2024/11/12 15:54
@Function: Parse assembly file to get the chromosome information
"""


def parse_assembly(assembly_file):
    """
    Parse assembly file to get the chromosome information
    Args:
        assembly_file: assembly file

    Returns:
        chr_info: chromosome information

    """
    scaffold_info = {}  # scaffold information
    chr_info = {}  # chromosome information

    # Parse assembly file
    with open(assembly_file, 'r') as f:
        chr_count = 1  # chromosome number
        for line in f:
            stripped_line = line.strip()
            if stripped_line.startswith('>'):
                parts = stripped_line.split(" ")
                scaffold_name = parts[0][1:]
                scaffold_index = int(parts[1])
                scaffold_asy_len = int(parts[2])
                scaffold_info[scaffold_index] = {
                    "scaffold_name": scaffold_name,
                    "scaffold_asy_len": scaffold_asy_len
                }
            else:
                chr_info[chr_count] = {
                    "scaffold_index": stripped_line
                }
                chr_count += 1

    # Calculate each chromosome length
    for chr_num, info in chr_info.items():
        scaffold_indices = map(int, info["scaffold_index"].split(" "))
        chr_len = sum(scaffold_info[abs(index)]["scaffold_asy_len"] for index in scaffold_indices)
        chr_info[chr_num]["chr_len"] = chr_len

    return chr_info


def main():
    asy_file = "/home/jzj/projects/HiCPlot/Mastacembelus.assembly"
    temp_result = parse_assembly(asy_file)
    print(temp_result)


if __name__ == '__main__':
    main()