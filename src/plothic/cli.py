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

from .PlotBed import plot_bed, plot_bed_split
from .PlotHiC import plot_hic, plot_hic_split
from .logger import logger

__version__ = "0.4.5"


def main():
    parser = argparse.ArgumentParser(description='Plot Whole genome Hi-C contact matrix heatmap')
    parser.add_argument('-hic', '--hic-file', type=str, default=None, help='Path to the Hi-C file')
    parser.add_argument('-chr', '--chr-txt', type=str, default=None, help='Path to the chromosome text file')

    parser.add_argument('-matrix', type=str, default=None, help='Path to the HiCPro matrix file')
    parser.add_argument('--abs-bed', type=str, default=None, help='Path to the HiCPro abs bed file')

    parser.add_argument('-o', '--output', type=str, default='./', help='Output directory, default: ./')

    parser.add_argument('-order', action='store_true', help='Order the heatmap by specific order')
    parser.add_argument('--abs-order', type=str, default="", help='Path to the HiCPro abs order file')

    parser.add_argument('--hic-split', type=str, default="", help='Plot the heatmap by split chromosome (hic format)')

    parser.add_argument('--bed-split', action='store_true', help='Plot the heatmap by split chromosome (HiCPro format)')

    parser.add_argument('-g', '--genome-name', type=str, default="", help='Genome name for the heatmap')
    parser.add_argument('-r', '--resolution', type=int, default=None, help='Resolution for Hi-C data')
    parser.add_argument('-d', '--data-type', type=str, default='observed',
                        help='Data type for Hi-C data or "oe" (observed/expected), default: observed')
    parser.add_argument('-n', '--normalization', type=str, default='NONE',
                        help='Normalization method for Hi-C data (NONE, VC, VC_SQRT, KR, SCALE, etc.), default: NONE')
    parser.add_argument('-log', action='store_true', help='Log2 transform the data')

    parser.add_argument('-cmap', type=str, default='YlOrRd', help='Color map for the heatmap, default: YlOrRd')
    parser.add_argument('-format', type=str, default="pdf", help='Output format for the figure, default: pdf')
    parser.add_argument('-f', '--fig-size', type=int, default=10, help='Figure size, default: 10')
    parser.add_argument('-dpi', type=int, default=300, help='DPI for the output figure, default: 300')
    parser.add_argument('--bar-min', type=int, default=0, help='Minimum value for color bar, default: 0')
    parser.add_argument('--bar-max', type=int, default=None, help='Maximum value for color bar')
    parser.add_argument('-rotation', type=int, default=45, help='Rotation for the x and y axis labels, default: 45')
    parser.add_argument('-grid', action='store_false', help='Show grid in the heatmap, Default: True')

    parser.add_argument('-v', '--version', action='version', version=__version__)

    args = parser.parse_args()

    if args.matrix is None and args.hic_file is None:
        logger.error("Please check your input parameters")
        exit(1)

    if args.matrix and args.abs_bed:
        if args.bed_split:
            plot_bed_split(args.matrix, args.abs_bed, output=args.output, fig_size=args.fig_size, dpi=args.dpi,
                           bar_min=args.bar_min,
                           bar_max=args.bar_max, cmap=args.cmap, log=args.log, rotation=args.rotation,
                           out_format=args.format)
        else:
            plot_bed(args.matrix, args.abs_bed, order_bed=args.abs_order, output=args.output,
                     genome_name=args.genome_name,
                     fig_size=args.fig_size, dpi=args.dpi, bar_min=args.bar_min, bar_max=args.bar_max, cmap=args.cmap,
                     log=args.log, rotation=args.rotation, grid=args.grid, out_format=args.format)
    else:
        if args.hic_split != "" and args.hic_file:
            plot_hic_split(args.hic_file, args.hic_split, output=args.output, resolution=args.resolution,
                           data_type=args.data_type,
                           normalization=args.normalization, genome_name=args.genome_name, fig_size=args.fig_size,
                           dpi=args.dpi,
                           bar_min=args.bar_min,
                           bar_max=args.bar_max, cmap=args.cmap, log=args.log, rotation=args.rotation,
                           out_format=args.format)
        elif args.hic_file:
            plot_hic(args.hic_file, chr_txt=args.chr_txt, output=args.output, resolution=args.resolution,
                     data_type=args.data_type, normalization=args.normalization, genome_name=args.genome_name,
                     fig_size=args.fig_size, dpi=args.dpi, bar_min=args.bar_min, bar_max=args.bar_max, cmap=args.cmap,
                     order=args.order, log=args.log, rotation=args.rotation, grid=args.grid, out_format=args.format)
        else:
            logger.error("Please check your input parameters")


if __name__ == '__main__':
    main()
