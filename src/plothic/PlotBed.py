#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Author: Zijie Jiang
@Contact: jzjlab@163.com
@File: PlotBed.py
@Time: 2024/12/31 10:45
@Function: Plot HiCPro format data
"""
import os

import numpy as np

from .PlotMTX import plot_matrix
from .logger import logger


def plot_bed(matrix, abs_bed, order_bed="", output='./', genome_name="", fig_size=6, dpi=300,
             bar_min=0,
             bar_max=None, cmap="YlOrRd", log=False, rotation=45, grid=True, out_format="pdf"):
    logger.info(f"Start Plot Hi-C data (HiCPro format):")
    logger.info(f"HiCPro matrix file: {matrix}")
    logger.info(f"HiCPro abs bed file: {abs_bed}")

    # get the matrix data
    data = np.loadtxt(matrix)

    # convert bed to matrix
    max_row = int(data[:, 0].max())
    max_col = int(data[:, 1].max())

    matrix = np.zeros((max_row, max_col))
    for row, col, value in data:
        matrix[int(row) - 1, int(col) - 1] = value
        matrix[int(col) - 1, int(row) - 1] = value

    chr_info = {}  # chromosome information
    pre_label_loci = 0
    with open(abs_bed, 'r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip().split()
            chr_info[line[0]] = {
                "length": int(line[2]),
                "index": int(line[3])
            }

    chr_label_dict = {}  # chrom name: index in the matrix
    for i in chr_info:
        chr_info[i]["loci"] = np.arange(pre_label_loci, chr_info[i]["index"])
        pre_label_loci = chr_info[i]["index"]
        chr_label_dict[i] = chr_info[i]["index"]

    # sort the matrix by the order
    if order_bed != "":
        logger.info(f"Order the matrix by the order file: {order_bed}")

        chr_order = {}  # chrom order: chromosome name
        new_order = []  # new order of the matrix
        chr_label_dict = {}  # chrom name: index in the matrix
        with open(order_bed, 'r') as f:
            for line in f:
                if line.startswith("#" or line == ""):
                    continue
                line = line.strip().split()
                chr_order[line[1]] = line[0]
        chr_order_len = len(chr_order)
        pre_label = 0
        for i in range(1, chr_order_len + 1):
            new_order.extend(chr_info[chr_order[str(i)]]["loci"])
            chr_label_dict[chr_order[str(i)]] = len(chr_info[chr_order[str(i)]]["loci"]) + pre_label
            pre_label = chr_label_dict[chr_order[str(i)]]

        matrix = matrix[np.ix_(new_order, new_order)]
    if os.path.isdir(output):  # output is a directory
        output = os.path.join(output, f"GenomeContact.{out_format}")
    plot_matrix(matrix, chr_info=chr_label_dict, outfile=output, genome_name=genome_name, fig_size=(fig_size, fig_size),
                dpi=dpi,
                bar_min=bar_min,
                bar_max=bar_max, cmap=cmap, log=log, rotation=rotation, grid=grid)

    logger.info(f"Save the plot to {output}")
    logger.info("Finished Plot HiCPro data")


def plot_bed_split(matrix, abs_bed, output='./', fig_size=6, dpi=300,
                   bar_min=0,
                   bar_max=None, cmap="YlOrRd", log=False, rotation=45, out_format="pdf"):
    logger.info(f"Start Plot Hi-C data (HiCPro format) with split chromosomes:")
    logger.info(f"HiCPro matrix file: {matrix}")
    logger.info(f"HiCPro abs bed file: {abs_bed}")

    # get the matrix data
    data = np.loadtxt(matrix)

    # convert the matrix data to a matrix
    max_row = int(data[:, 0].max())
    max_col = int(data[:, 1].max())

    matrix = np.zeros((max_row, max_col))
    for row, col, value in data:
        matrix[int(row) - 1, int(col) - 1] = value
        matrix[int(col) - 1, int(row) - 1] = value

    chr_info = {}  # chrom information
    with open(abs_bed, 'r') as f:
        for line in f:
            if line.startswith("#"):
                continue
            line = line.strip().split()
            chr_info[line[0]] = {
                "index": int(line[3])
            }

    pre_label_loci = 0
    for i in chr_info:
        chr_info[i]["loci"] = np.arange(pre_label_loci, chr_info[i]["index"])

        chr_matrix = matrix[np.ix_(chr_info[i]["loci"], chr_info[i]["loci"])]
        if os.path.isdir(output):  # output is a directory
            chr_output = os.path.join(output, f"{i}.{out_format}")
        else:
            chr_output = os.path.join("./", f"{i}.{out_format}")
        plot_matrix(chr_matrix, outfile=chr_output, genome_name=i, fig_size=(fig_size, fig_size),
                    dpi=dpi,
                    bar_min=bar_min,
                    bar_max=bar_max, cmap=cmap, log=log, rotation=rotation, grid=False)
        pre_label_loci = chr_info[i]["index"]

        logger.info(f"Save the plot to {chr_output}")
    logger.info("Finished Plot HiCPro data with split chromosomes")
