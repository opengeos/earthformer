# Installation

## Install from PyPI

The `earthformer` package is available on PyPI. To install it, run:

```bash
pip install earthformer
```

Earthformer has several optional dependencies. It is recommended to create a new conda environment and install the dependencies with conda:

```bash
conda create -n earthformer python=3.10
conda activate earthformer
conda install -c conda-forge mamba
mamba install -c conda-forge pytorch torchvision pytorch-lightning==1.7.7
mamba install -c conda-forge nvidia-apex omegaconf
mamba install -c conda-forge xarray netcdf4 opencv
pip install earthnet earthformer
```

## From sources

To install earthformer from sources, run this command in your terminal:

```bash
pip install git+https://github.com/opengeos/earthformer
```
