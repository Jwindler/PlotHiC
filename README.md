# PlotHiC

`PlotHiC` is an extension of [AutoHiC](https://github.com/Jwindler/AutoHiC) that is used to visualize global interaction heatmaps after genome scaffolding.

**Note: PlotHiC is currently under development. If you have any questions, please [Open Issues](https://github.com/Jwindler/PlotHiC/issues/new) or provide us with your comments via the email below.**

Author: Zijie Jiang

Email: [jzjlab@163.com](mailto:jzjlab@163.com)



## Content 

- [PlotHiC](#plothic)
  - [Content](#content)
  - [Citations](#citations)
  - [Installation](#installation)
    - [pip](#pip)
  - [Usage](#usage)
    - [Input file](#input-file)
    - [example](#example)
    - [other parameter](#other-parameter)
    - [Color map](#color-map)
  - [Dev](#dev)





## Citations

**If you used PlotHiC in your research, please cite us:**

Zijie Jiang, Zhixiang Peng, Zhaoyuan Wei, Jiahe Sun, Yongjiang Luo, Lingzi Bie, Guoqing Zhang, Yi Wang, A deep learning-based method enables the automatic and accurate assembly of chromosome-level genomes, Nucleic Acids Research, 2024;, gkae789, https://doi.org/10.1093/nar/gkae789



## Installation

- Dependency : `python = "^3.10"`



### pip

```bash
# pip install 
pip install plothic

```



## Usage

### Input file

- `hic`

This file is taken directly from `3d-dna`, you need to select the final `hic` file (which has already been error adjusted and chromosome boundaries determined).



- **Chromosome txt**

This file is used for heatmap labeling. The first column is the name of the chromosome and the second column is the length of the chromosome (this length is the length of the hic file in Juicebox and can be manually determined from Juicebox).

**Note: **the length is in .hic file, not true base length.

```sh
# name length
Chr1 24800000
Chr2 44380000
Chr3 63338000
Chr4 81187000
Chr5 97650000
```



### example

```sh
plothic -hic test.hic -chr chr.txt -r 100000

# -hic > .hic file 
# -chr > chromosome length (in .hic file)
# -r > resolution to visualization

```

![](https://s2.loli.net/2024/11/15/3rmOLU5IPa6vywo.png)



### other parameter

![](https://s2.loli.net/2024/11/18/dmuXrbsB9DRhlyt.png)



### Color map

**PlotHiC** uses `YlOrRd` by default, you can choose more colors from [Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html).

![](https://s2.loli.net/2024/11/13/MYZe56Vy2BT1tDp.png)



## Dev

Currently only use `hic` and `chr txt` are supported for visualization, and `assembly` files will be supported in the future. However, from the perspective of usage, using `chr txt` files seems to be more convenient. If you have better suggestions or other requirements, please [Open Issues](https://github.com/Jwindler/PlotHiC/issues/new).

