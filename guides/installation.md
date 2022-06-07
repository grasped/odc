## ⚙️ Open Data Cube Installation and Diwata-2 SMI Indexing

This document presents the process for installing Open Data Cube (ODC) into a local machine and proper indexing of Diwata-2 SMI dataset.

### 1. Install dependencies
The following are software requirements in order to run ODC.
#### Anaconda
The Anaconda serves an environment for ODC. Install Anaconda or Mini Conda from https://www.anaconda.com/products/individual.
#### PostgreSQL
ODC requires a database and the PostreSQL is recommended. Install it from https://www.postgresql.org/download/.
#### AWS CLI
The AWS CLI is needed in order to index data that are from the S3 service. Install the version 2 from here https://docs.aws.amazon.com/cli/v1/userguide/install-windows.html and follow the configuration steps here https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html.

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
conda install jupyter matplotlib scipy ipyleaflet geopandas scikit-learn-intelex
```

### 3. Create database
If it is the first time installing PostgreSQL, it is need to create a user.

Once a user is present e.g. `postgres`, a database should be created after the user:
```
createdb -h localhost -U postgres datacube

password: ******
```

The next step is creating an integration configuration. The following text can be copied and saved to the directory `C:\Users\odc_user\.datacube_integration.conf ` (example):
```
[datacube]
db_hostname: localhost
db_database: datacube
db_username: postgres
db_password: ******
```

Finally in the ODC environment, the database can be initialized using the following:
```
datacube -v system init
```

### 3. Prepare indexing tools
If the data source is coming from AWS S3, some tools are needed to index the data. Starting with `boto` and `awscli`. Install them using:

```
conda install aiobotocore[boto3,awscli]
```
or (if pip)
```
pip install aiobotocore[boto3,awscli]
```
The next package is the ODC tools itself:
```
pip install odc-apps-dc-tools
```

### 4. Add the product definition
The Diwata-2 SMI dataset product definition can be added using the following. This document describes the dataset which includes projection and measurement properties of the SMI products.
```
datacube product add s3://diwata-missions/Diwata-2/SMI/collection/diwata_2_smi.yaml
```
or
```
datacube product add https://diwata2-odc.s3.us-east-2.amazonaws.com/eo3-product/diwata2_smi_l1c.odc-product.yaml
```

### 5. Add the product definition
Finally, the dataset documents are metadata for each data. Each one describes the capture time and location of individual band files. They can be recursively added using the following:
```
s3-to-dc --no-sign-request s3://diwata-missions/Diwata-2/SMI/collection/*.odc-metadata.yaml diwata_2_smi
```
or
```
s3-to-dc --no-sign-request https://diwata2-odc.s3.us-east-2.amazonaws.com/eo3/*.odc-metadata.yaml diwata2_smi_l1c

s3-to-dc --no-sign-request s3://diwata2-odc/eo3/*.odc-metadata.yaml diwata2_smi_l1c
```

### 6. Install DEA Tools
```
pip install dea-tools
```


### Misc. Shortcut
```
conda create --name odc_env --channel conda-forge python=3.8 datacube jupyter matplotlib scipy ipyleaflet geopandas scikit-learn aiobotocore[boto3,awscli] dask-ml rasterstats geopy pydotplus

pip install odc-apps-dc-tools dea-tools
```

## 📌 Links
* [Main page](https://gitlab.com/grasped/odc-notebook)
* [Table of contents](../README.md#-table-of-contents)