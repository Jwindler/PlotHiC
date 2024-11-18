#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Author: Zijie Jiang
@Contact: jzjlab@163.com
@File: cli.py
@Time: 2024/11/15 11:47
@Function: Main function of PlotHiC
"""
import argparse

from plothic.PlotHiC import plot_hic


def main():
    parser = argparse.ArgumentParser(description='Plot Whole genome Hi-C contact matrix heatmap')
    parser.add_argument('-hic', '--hic-file', type=str, help='Path to the Hi-C file', required=True)
    parser.add_argument('-chr', '--chr-txt', type=str, help='Path to the chromosome text file', required=True)
    parser.add_argument('-o', '--output', type=str, default='GenomeContact.pdf', help='Output file name')
    parser.add_argument('-r', '--resolution', type=int, default=None, help='Resolution for Hi-C data')
    parser.add_argument('-d', '--data-type', type=str, default='observed',
                        help='Data type for Hi-C data or "oe" (observed/expected)')
    parser.add_argument('-n', '--normalization', type=str, default='NONE',
                        help='Normalization method for Hi-C data (NONE, VC, VC_SQRT, KR, SCALE, etc.)')
    parser.add_argument('-g', '--genome-name', type=str, default=None, help='Genome name')
    parser.add_argument('-f', '--fig-size', type=tuple, default=(6, 6), help='Figure size')
    parser.add_argument('--dpi', type=int, default=300, help='DPI for the output figure')
    parser.add_argument('--bar_min', type=int, default=0, help='Minimum value for color bar')
    parser.add_argument('--bar_max', type=int, default=None, help='Maximum value for color bar')
    parser.add_argument('--cmap', type=str, default='YlOrRd', help='Color map for the heatmap')

    args = parser.parse_args()

    plot_hic(args.hic_file, chr_txt=args.chr_txt, output=args.output, resolution=args.resolution,
             data_type=args.data_type, normalization=args.normalization, genome_name=args.genome_name,
             fig_size=args.fig_size, dpi=args.dpi, bar_min=args.bar_min, bar_max=args.bar_max, cmap=args.cmap)


if __name__ == '__main__':
    main()
