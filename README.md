# Earthformer

[![image](https://img.shields.io/pypi/v/earthformer.svg)](https://pypi.python.org/pypi/earthformer)
[![image](https://img.shields.io/conda/vn/conda-forge/earthformer.svg)](https://anaconda.org/conda-forge/earthformer)

**A Python package for Earth forecasting transformer**

-   Free software: Apache License, Version 2.0 (Apache-2.0)
-   Documentation: <https://opengeos.github.io/earthformer>

## Introduction

This repository turns the [amazon-science/earth-forecasting-transformer](https://github.com/amazon-science/earth-forecasting-transformer) repository into a Python package, making it easier to install and use. To learn more about Earthformer, please refer to the NeurIPS 2022 paper: [Earthformer: Exploring Space-Time Transformers for Earth System Forecasting](https://www.amazon.science/publications/earthformer-exploring-space-time-transformers-for-earth-system-forecasting). Credits to the authors and their [repository](https://github.com/amazon-science/earth-forecasting-transformer) for the original implementation.

## Installation

The `earthformer` package is available on [PyPI](https://pypi.org/project/earthformer). To install it, run:

```bash
pip install earthformer
```

The `earthformer` package is also available on [conda-forge](https://anaconda.org/conda-forge/earthformer). To install it, run:

```bash
conda create -n earthformer python=3.10
conda activate earthformer
conda install -c conda-forge mamba
mamba install -c conda-forge earthformer
```
