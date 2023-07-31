# Earthformer

[![image](https://img.shields.io/pypi/v/earthformer.svg)](https://pypi.python.org/pypi/earthformer)

<!-- [![image](https://img.shields.io/conda/vn/conda-forge/earthformer.svg)](https://anaconda.org/conda-forge/earthformer) -->

**A Python package for Earth forecasting transformer**

-   Free software: Apache Software License 2.0
-   Documentation: <https://opengeos.github.io/earthformer>

## Introduction

This repository turns the [amazon-science/earth-forecasting-transformer](https://github.com/amazon-science/earth-forecasting-transformer) repository into a Python package, making it easier to install and use. To learn more about Earthformer, please refer to the NeurIPS 2022 paper: [Earthformer: Exploring Space-Time Transformers for Earth System Forecasting](https://www.amazon.science/publications/earthformer-exploring-space-time-transformers-for-earth-system-forecasting). Credits to the authors and their [repository](https://github.com/amazon-science/earth-forecasting-transformer) for the original implementation.

## Installation

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
