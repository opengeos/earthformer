# Earthformer

[![image](https://img.shields.io/pypi/v/earthformer.svg)](https://pypi.python.org/pypi/earthformer)
[![image](https://img.shields.io/conda/vn/conda-forge/earthformer.svg)](https://anaconda.org/conda-forge/earthformer)
[![Open In Studio Lab](https://studiolab.sagemaker.aws/studiolab.svg)](https://studiolab.sagemaker.aws/import/github/opengeos/earthformer/blob/main/docs/examples/earthnet2021.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/opengeos/earthformer/blob/main/docs/examples/earthnet2021.ipynb)

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

## Disclaimer

I am not the author of the original implementation. This repository is a Python package that wraps the original implementation into a package. If you have any questions about the original implementation, please refer to the [amazon-science/earth-forecasting-transformer](https://github.com/amazon-science/earth-forecasting-transformer). The original implementation is licensed under the Apache License, Version 2.0.
