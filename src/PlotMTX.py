#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Author: Zijie Jiang
@Contact: jzjlab@163.com
@File: PlotMTX.py
@Time: 2024/11/12 15:47
@Function: Plot Whole genome Hi-C contact matrix heatmap
"""
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.axes_grid1 import make_axes_locatable
from numpy import log2

from ParseHiC import parse_hic
from logger import logger


def plot_matrix(matrix, chr_info=None, genome_name=None, outfile='GenomeContact.pdf', fig_size=(6, 6), dpi=300,
                bar_min=0,
                bar_max=None,
                cmap="YlOrRd",
                axes_len=4,
                axes_wd=1,
                axes_pad=6,
                grid_style='dashed', grid_color='black', grid_width=1, grip_alpha=0.8, bar_size="3%", bar_pad=0.1,
                font_size=10,
                log=False):
    fig, ax = plt.subplots(1, 1, figsize=fig_size, dpi=dpi)

    if chr_info is None:
        labels = []
        pos = []
    else:
        labels = list(chr_info.keys())  # chromosome names
        pos = list(chr_info.values())  # chromosome loci

    ax.set_xticks(pos)
    ax.set_yticks(pos)

    ax.set_xticklabels(labels)
    ax.set_yticklabels(labels)

    # set genome title
    ax.set_title(genome_name, fontsize=20, pad=8, fontstyle='italic')

    ax.grid(color=grid_color, linestyle=grid_style, linewidth=grid_width, alpha=grip_alpha)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize=font_size)
    plt.setp(ax.get_yticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize=font_size)

    ax.tick_params(direction='out', length=axes_len, width=axes_wd, pad=axes_pad)

    color_bar = make_axes_locatable(ax)
    cax = color_bar.append_axes("right", size=bar_size, pad=bar_pad)

    matrix_len = len(matrix)  # matrix length
    lim_extents = matrix_len + 0.5
    ax.set_ylim(0.5, lim_extents)
    ax.set_xlim(0.5, lim_extents)

    matrix = matrix + 1e-9  # avoid log2(0) error
    maxcolor = (np.percentile(matrix, 95))
    if bar_max is None:
        bar_max = maxcolor
        logger.info(f"max color is not set, use the default max color: {bar_max}")
    with np.errstate(divide='ignore'):
        img = ax.imshow(log2(matrix) if log else matrix, cmap=plt.get_cmap(cmap), vmin=bar_min, vmax=bar_max,
                        origin="lower",
                        interpolation="nearest",
                        extent=(0.5, lim_extents, 0.5, lim_extents), aspect='auto')

    cb = fig.colorbar(img, ax=ax, cax=cax, orientation="vertical")
    cb.ax.tick_params(labelsize=font_size)

    plt.savefig(outfile)


def main():
    hic_file = "/home/jzj/projects/PlotHiC/data/Mastacembelus.hic"
    resolution = 250000
    bar_max = 100
    matrix_end = 552000000
    matrix = parse_hic(hic_file, resolution, matrix_end=matrix_end)

    output_file = "/mnt/e/downloads/GenomeContact.pdf"
    chr_info = {'Chr1': 260, 'Chr2': 505, 'Chr3': 5670}

    genome_name = "Mastacembelus"
    # plot_matrix(matrix, outfile=output_file)

    plot_matrix(matrix, chr_info, outfile=output_file, bar_max=bar_max, genome_name=genome_name)


if __name__ == '__main__':
    main()
