#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Author: Zijie Jiang
@Contact: jzjlab@163.com
@File: PlotHiC.py
@Time: 2024/11/12 15:47
@Function: main program entry
"""
import logging

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from mpl_toolkits.axes_grid1 import make_axes_locatable
from numpy import log2


def plot(matrix, chr_info, outfile='GenomeContact.pdf', fig_size=(6, 6), dpi=300, cmap=3, start=1, axes_len=4,
         axes_wd=1,
         axes_pad=6,
         grid_st='dashed', grid_color='black', grid_lw=1, grip_ap=0.8, cp_size="0.5%", cp_pad=0.05, font_size=6,
         log=False):
    """
    Plot Whole genome Hi-C contact matrix heatmap
    Args:
        matrix:
        chr_info:
        outfile:
        fig_size:
        dpi:
        cmap:
        start:
        axes_len:
        axes_wd:
        axes_pad:
        grid_st:
        grid_color:
        grid_lw:
        grip_ap:
        cp_size:
        cp_pad:
        font_size:
        log:

    Returns:

    """
    cmaps = ['Greys', 'Reds', 'YlOrBr', 'YlOrRd', 'hot']

    params = {'font.family': 'serif',
              'font.serif': 'Times New Roman',
              'font.style': 'italic',
              'font.weight': 'normal',
              'font.size': font_size
              }

    (w, h) = fig_size

    fig = plt.figure(figsize=(int(w), int(h)), dpi=dpi)
    ax = plt.subplot2grid((1, 4), (0, 0), rowspan=1, colspan=4)

    try:
        rcParams.update(params)
    except Warning:
        logging.info("You should install serif font family if possible" + '\n')

    labels = list(chr_info.keys())  # chromosome names
    pos = list(chr_info.values())  # chromosome loci

    ax.set_xticks(pos)
    ax.set_xticklabels(labels)

    ax.set_yticklabels(labels)
    ax.set_yticks(pos)

    ax.grid(color=grid_color, linestyle=grid_st, linewidth=grid_lw, alpha=grip_ap)

    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize=font_size)
    plt.setp(ax.get_yticklabels(), rotation=45, ha="right", rotation_mode="anchor", fontsize=font_size)

    ax.tick_params(direction='out', length=axes_len, width=axes_wd, pad=axes_pad)

    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size=cp_size, pad=cp_pad)
    length = len(matrix)
    ax.set_ylim(int(start or 1) - 0.5, int(start or 1) + length - 0.5)
    ax.set_xlim(int(start or 1) - 0.5, int(start or 1) + length - 0.5)

    if log:
        with np.errstate(divide='ignore'):
            img = ax.imshow(log2(matrix), cmap=plt.get_cmap(cmaps[cmap]), origin="lower", interpolation="nearest",
                            extent=(int(start or 1) - 0.5, int(start or 1) + length - 0.5, int(start or 1) - 0.5,
                                    int(start or 1) + length - 0.5),
                            aspect='auto')  # solve log2 Divide by zero error encountered error
        cb = fig.colorbar(img, ax=ax, cax=cax,
                          orientation="vertical")
        cb.ax.tick_params(labelsize=font_size)

    else:
        with np.errstate(divide='ignore'):
            img = ax.imshow(matrix, cmap=plt.get_cmap(cmaps[cmap]), origin="lower", interpolation="nearest",
                            extent=(int(start or 1) - 0.5, int(start or 1) + length - 0.5, int(start or 1) - 0.5,
                                    int(start or 1) + length - 0.5),
                            aspect='auto')  # solve log2 Divide by zero error encountered error
        fig.colorbar(img, ax=ax, cax=cax, orientation="vertical")

    plt.savefig(outfile)


def main():
    print("")


if __name__ == '__main__':
    main()
