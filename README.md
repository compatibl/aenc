# Autoencoders for Financial Markets (AENC)

## Overview

This package implements specialized autoencoders and related classical methods
for performing dimension reduction in quant models of financial markets. Potential
uses include investment strategy research, portfolio valuation, and risk management.

## Quick Start Guide

Install using:

```shell
pip install aenc
```

## Namespaces

Namespace `aenc.core` implements autoencoders and related
classical methods, including generic (such as PCA) and specialized
(such as Nelson-Siegel). 

The implementation uses PyTorch and can be easily ported to TensorFlow 2
and other machine learning frameworks that support dynamic computational
graphs.

Namespace `aenc.dummy` includes dummy objects and generators for dummy market
data for testing purposes. To perform testing or training on real
market data, provide your own historical market data files in the same
format as the dummy data files, or use pretrained components.

Namespace `aenc.pretrained` includes pretrained components to avoid lengthy
test execution time. Use flags to ignore pretrained parameters
and perform training from scratch (calculation time will increase).

## Licensing

The code in this project is licensed under Apache 2.0 license.
See [LICENSE](https://www.apache.org/licenses/LICENSE-2.0.html) for more information.

## Publications and Links

1. Alexander Sokol, Autoencoder Market Models for Interest Rates, SSRN Working Paper https://ssrn.com/abstract=4300756
2. GitHub repository: https://github.com/compatibl/aenc-py
