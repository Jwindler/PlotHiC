#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Author: Zijie Jiang
@Contact: jzjlab@163.com
@File: PlotHiC.py
@Time: 2024/9/29 17:08
@Function: Plot Whole genome Hi-C contact matrix heatmap
"""

import hicstraw

from plothic.ParseHiC import parse_hic
from plothic.PlotMTX import plot_matrix
from plothic.logger import logger


def plot_hic(hic, chr_txt, output='GenomeContact.pdf', resolution=None, data_type="observed",
             normalization="NONE", genome_name=None, fig_size=(6, 6), dpi=300,
             bar_min=0,
             bar_max=None, cmap="YlOrRd"):
    logger.info(f"Start Plot Hi-C data: {hic}")

    # get hic object
    hic_obj = hicstraw.HiCFile(hic)

    # get resolutions
    resolutions = hic_obj.getResolutions()
    logger.info(f"This Hi-C data has resolutions: {resolutions}")

    # choose resolution
    if resolution is None:
        resolution = resolutions[-3]
        logger.info(f"Resolution not set, use the default max resolution: {resolution}")
    elif resolution not in resolutions:
        logger.error(f"Resolution {resolution} not in {resolutions}")
        resolution = resolutions[-3]
    logger.info(f"Use the resolution: {resolution}")
    logger.info(f"Use the {data_type} data type and {normalization} normalization method")

    # plot with chr txt

    chr_info = {}
    last_chr_len = 0
    with open(chr_txt, 'r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip().split()
            chr_info[line[0]] = int(line[1]) // int(resolution)

            # get the last chromosome length
            if int(line[1]) > last_chr_len:
                last_chr_len = int(line[1])
    logger.info(f"Chromosome information: {chr_info}")
    # sort chromosome information
    chr_info_sorted = dict(sorted(chr_info.items(), key=lambda item: item[1]))
    matrix = parse_hic(hic, resolution, matrix_end=last_chr_len, data_type=data_type, normalization=normalization)

    plot_matrix(matrix, chr_info=chr_info_sorted, outfile=output, genome_name=genome_name, fig_size=fig_size, dpi=dpi,
                bar_min=bar_min,
                bar_max=bar_max, cmap=cmap)

    logger.info(f"Save the plot to {output}")
    logger.info("Finished Plot Hi-C data")
