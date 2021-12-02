# Installation

This document presents the process for installing Open Data Cube (ODC) into a local machine and proper indexing of Diwata-2 SMI dataset.

### 1. Install dependencies
The following are software requirements in order to run ODC.
#### Anaconda
The Anaconda serves an environment for ODC. Install Anaconda or Mini Conda from https://www.anaconda.com/products/individual.
#### PostgreSQL
ODC requires a database and the PostreSQL is recommended. Install it from https://www.postgresql.org/download/.

### 2. Install Python and packages
Conda environments are used to isolate ODC from other software development projects.

Add conda-forge to package channels:
```
conda config --append channels conda-forge
```

Create a conda environment named `odc_env` and install python
```
conda create --name odc_env python=3.8 datacube
```

Activate the `odc_env` conda environment:
```
conda activate odc_env
```

Install other packages needed by ODC.
```
conda install jupyter matplotlib scipy
```