#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Author: Zijie Jiang
@Contact: jzjlab@163.com
@File: PlotHiC.py
@Time: 2024/9/29 17:08
@Function: Plot Whole genome Hi-C contact matrix heatmap
"""

from ParseHiC import parse_hic
from PlotMTX import plot_matrix


def plot_hic(hic, resolution, chr_info=None, asy=None):
    pass


def main():
    hic_file = "/home/jzj/projects/PlotHiC/data/Mastacembelus.hic"
    resolution = 50000
    vmax = 100
    matrix = parse_hic(hic_file, resolution)

    output_file = "/mnt/e/downloads/GenomeContact.pdf"
    chr_info = {'Chr1': 260, 'Chr2': 505, 'Chr3': 5670}
    plot_matrix(matrix, chr_info, outfile=output_file, vmax=vmax)


if __name__ == '__main__':
    main()
