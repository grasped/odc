# Installation

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
conda install jupyter matplotlib scipy
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
db_password: awserd12
```

Finally in the ODC environment, the database can be initialized using the following:
```
datacube -v system init
```

### 3. Prepare indexing tools
If the data source is coming from AWS S3, some tools are needed to index the data. Starting with `boto` and `awscli`.
