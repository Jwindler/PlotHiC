#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Author: Zijie Jiang
@Contact: jzjlab@163.com
@File: ParseHiC.py
@Time: 2024/11/12 19:33
@Function: Parse Hi-C data
"""

import hicstraw
import numpy as np

from logger import logger


def parse_hic(hic, resolution=None, data_type="observed", normalization="NONE"):
    hic_obj = hicstraw.HiCFile(hic)

    # genome_id = hic_obj.getGenomeID()
    # logger.info(f"Genome ID: {genome_id}")

    resolutions = hic_obj.getResolutions()
    logger.info(f"This Hi-C data has resolutions: {resolutions}")

    # check resolution
    if resolution is None:
        resolution = resolutions[-1]
        logger.info(f"Resolution not set, use the default max resolution: {resolution}")
    elif resolution not in resolutions:
        logger.error(f"Resolution {resolution} not in {resolutions}")
        resolution = resolutions[-1]
    logger.info(f"Resolution: {resolution}")

    chr_info = {}
    for chrom in hic_obj.getChromosomes():
        chr_info[chrom.name] = chrom.length
    hic_max_len = chr_info["assembly"]
    logger.info(f"HiC data assembly chromosome length: {hic_max_len}")

    res_max_len = resolution * 1400

    matrix_obj = hic_obj.getMatrixZoomData('assembly', 'assembly', data_type, normalization, "BP", resolution)

    # contact_matrix = None  # contact matrix
    if res_max_len > hic_max_len:
        contact_matrix = matrix_obj.getRecordsAsMatrix(0, hic_max_len, 0, hic_max_len)
    else:
        extract_times = int(hic_max_len / res_max_len) + 1  # extract times
        iter_len = np.linspace(0, hic_max_len, extract_times + 1)  # iteration length
        incr_distance = iter_len[1]  # increment distance
        final_matrix = None

        for i in iter_len[1:]:
            temp_matrix = None
            for j in iter_len[1:]:
                contact_matrix = matrix_obj.getRecordsAsMatrix(int(i - incr_distance), int(i), int(j - incr_distance),
                                                               int(j))
                temp_matrix = contact_matrix if temp_matrix is None else np.hstack((temp_matrix, contact_matrix))

            final_matrix = temp_matrix if final_matrix is None else np.vstack((final_matrix, temp_matrix))

        # Remove all zero rows and columns
        non_zero_rows = final_matrix[~np.all(final_matrix == 0, axis=1)]
        contact_matrix = non_zero_rows[:, ~np.all(non_zero_rows == 0, axis=0)]

    return contact_matrix


def main():
    hic_file = "/home/jzj/projects/PlotHiC/data/Mastacembelus.hic"
    resolution = 1000
    temp_result = parse_hic(hic_file, resolution)
    print(temp_result.shape)


if __name__ == '__main__':
    main()
