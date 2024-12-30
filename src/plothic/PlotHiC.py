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
import numpy as np

from .ParseHiC import parse_hic
from .PlotMTX import plot_matrix
from .logger import logger


def plot_hic(hic, chr_txt, output='GenomeContact.pdf', resolution=None, data_type="observed",
             normalization="NONE", genome_name=None, fig_size=6, dpi=300,
             bar_min=0,
             bar_max=None, cmap="YlOrRd", order=False):
    logger.info(f"Start Plot Hi-C data: {hic}")

    # get hic object
    hic_obj = hicstraw.HiCFile(hic)

    # get resolutions
    resolutions = hic_obj.getResolutions()
    logger.info(f"This Hi-C data has resolutions: {resolutions}")

    # choose resolution
    if resolution is None:
        resolution = resolutions[-4]
        logger.info(f"Resolution not set, use the default max resolution: {resolution}")
    elif resolution not in resolutions:
        logger.error(f"Resolution {resolution} not in {resolutions}")
        resolution = resolutions[-4]
    logger.info(f"Use the resolution: {resolution}")
    logger.info(f"Use the {data_type} data type and {normalization} normalization method")

    # plot with chr txt
    chr_info = {}
    chr_start = 0
    last_chr_len = 0

    with (open(chr_txt, 'r') as f):
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip().split()
            chr_info[line[2]] = {
                "length": int(line[1]) - chr_start,
                "name": line[0],
                "hic_loci": int(line[1])
            }
            chr_start = int(line[1])

            # get the last chromosome length
            if int(line[1]) > last_chr_len:
                last_chr_len = int(line[1])

    logger.info(f"Chromosome information: {chr_info}")

    matrix = parse_hic(hic, resolution, matrix_end=last_chr_len, data_type=data_type, normalization=normalization)
    matrix_len = len(matrix)

    chr_label_dict = {}
    for i in chr_info:
        chr_label_dict[chr_info[i]["name"]] = chr_info[i]["hic_loci"] * matrix_len // last_chr_len

    if order:
        chr_dict_length = len(chr_info)

        # cal the new order
        for i in chr_info:
            chr_info[i]["index"] = (chr_info[i]["hic_loci"] * matrix_len) // last_chr_len

        new_order = []

        pre_label_loci = 0
        for i in range(1, chr_dict_length):
            temp_order = np.arange(chr_info[str(i + 1)]["index"], chr_info[str(i)]["index"])
            new_order.extend(temp_order)
            chr_info[str(i)]["label_loci"] = len(temp_order) + pre_label_loci
            pre_label_loci = chr_info[str(i)]["label_loci"]

        new_order.extend(np.arange(0, chr_info[str(chr_dict_length)]["index"]))
        chr_info[str(chr_dict_length)]["label_loci"] = matrix_len

        matrix = matrix[new_order, :][:, new_order]

        chr_label_dict = {}
        for i in chr_info:
            chr_label_dict[chr_info[i]["name"]] = chr_info[i]["label_loci"]
    fig_size = (fig_size, fig_size)
    plot_matrix(matrix, chr_info=chr_label_dict, outfile=output, genome_name=genome_name, fig_size=fig_size,
                dpi=dpi,
                bar_min=bar_min,
                bar_max=bar_max, cmap=cmap)

    logger.info(f"Save the plot to {output}")
    logger.info("Finished Plot Hi-C data")
