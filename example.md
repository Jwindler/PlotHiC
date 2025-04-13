# Example data usage of PlotHiC

This document shows how to run `PlotHiC` on the **example data (as follows)**.

- hic format data
    - at.hic
    - chr_default.txt
    - chr_order.txt
- bed format data
    - at.matrix
    - at_asb_re.bed
    - bed_order.txt

The data used in the examples can be obtained from [google drive](https://drive.google.com/drive/folders/1G2HRe09j_aIaEDpSNCn6el52Lmet5JBx?usp=sharing).

---

**If you have any questions, please [Open Issues](https://github.com/Jwindler/PlotHiC/issues/new) or provide us with your comments via the email below.**

Email: [jzjlab@163.com](mailto:jzjlab@163.com)



## Install

- Dependency : `python = "^3.10"`

### pip (recommend)

```sh
# pip install 
pip install plothic

plothic -v
```



### conda

```sh
# create plothic enviorment and install plothic
conda env create -n plothic -c bioconda  -c conda-forge plothic

# mamba env create -n plothic -c bioconda  -c conda-forge plothic

# then
conda activate plothic

plothic -v
```



## .hic format

The `at.hic`, `chr_default.txt` and `chr_order.txt` data used in the examples can be obtained from [google drive](https://drive.google.com/drive/folders/1G2HRe09j_aIaEDpSNCn6el52Lmet5JBx?usp=sharing).



### default

```sh
plothic -hic at.hic -chr chr_default.txt -r 100000 -format png --bar-max 200
```

- `-hic`: hic format file (**at.hic**).
- `-chr`: hic format chromosome config file (**chr_default.txt**).
- `-r`: set the resolution to **100000**.
- `-format`: set the output format to **png**, the default is **pdf**.
- `--bar-max`: set the maximum color threshold to **200**.



The output result is as follows:

![](https://s2.loli.net/2025/04/13/kvK1NIdqa2OxZle.png)



### sort by chromosome length

```sh
plothic -hic at.hic -chr chr_order.txt -r 100000 -format png --bar-max 200 -order
```

- `-order`: set the output to be sorted by chromosome length from **chr_order.txt**.



The output result is as follows:

![](https://s2.loli.net/2025/04/13/LRhKtVgPicf9zWH.png)



## bed format

The `at.hic`, `chr_default.txt` and `chr_order.txt` data used in the examples can be obtained from [google drive](https://drive.google.com/drive/folders/1G2HRe09j_aIaEDpSNCn6el52Lmet5JBx?usp=sharing).



### default

```sh
plothic -matrix at.matrix --abs-bed at_abs_re.bed -format png -cmap viridis --bar-max 20
```

- `-matrix`: bed format matrix file (**at.matrix**).
- `--abs-bed `: bed format position file (**at_abs_re.bed**).
- `-format`: set the output format to **png**, the default is **pdf**.
- `-cmap`: set color map to **viridis**, `PlotHiC` uses `YlOrRd` by default, you can choose more colors from [Matplotlib](https://matplotlib.org/stable/users/explain/colors/colormaps.html).
- `--bar-max`: set the maximum color threshold to **20**.



The output result is as follows:

![](https://s2.loli.net/2025/04/13/1hBjsnq95XFLvIc.png)



### sort by chromosome length

```sh
plothic -matrix at.matrix --abs-bed at_abs_re.bed -format png -cmap viridis --bar-max 20 --abs-order bed_order.txt
```

`--abs-order`: bed format chromosome config file (**bed_order.txt**).



The output result is as follows:

![](https://s2.loli.net/2025/04/13/ueXcLrMHv9q1kh6.png)



---

The above is just for demonstration and example visualization. For more personalized settings, please refer to [README](https://github.com/Jwindler/PlotHiC?tab=readme-ov-file#usage) or [Wiki](https://github.com/Jwindler/PlotHiC/wiki).
