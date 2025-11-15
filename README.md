# Project Overview: Motorcycle Fatality Analysis (NHTSA FARS)

The goal of this project is to conduct a detailed analysis of factors contributing to motorcycle crash fatalities in the United States.

##### 

### Introduction



##### Data Source

We utilize the Fatality Analysis Reporting System (FARS), a comprehensive national census maintained by the National Highway Traffic Safety Administration (NHTSA) that details all traffic crashes resulting in a fatality within 30 days.

##### 

##### Objective

This analysis focuses on identifying compounding risk factors (e.g., specific interactions between rider behavior, environmental conditions, and crash dynamics). The resulting insights aim to describe complex hazardous scenarios, moving beyond simple causation to support data-driven policy decisions and targeted awareness campaigns.





### Installation \& Setup



This project requires Miniconda (or Miniforge) and the Mamba environment manager. Mamba is a fast, drop-in replacement for the conda command.



###### **1. Prerequisites (Miniconda / Mamba)**

**Install Miniconda:** Download and install the latest version of Miniconda for your operating system from the official Miniconda website. Accept the default options during installation.



**Install Mamba:** Once Miniconda is installed and activated (you should see (base) in your terminal prompt), install Mamba, which we will use for environment management:



$ conda install -c conda-forge mamba -y $





###### **2. Environment Setup**

The next step is to create a new, isolated environment with the exact software dependencies required by this project.



1. **Create the Environment:** Use Mamba to create a new environment named fars-env with the specified packages. The packages are pinned to ensure the code runs exactly as tested:
   	$ mamba create -n fars-env python=3.14 jupyter pandas = 2.3.3 matplotlib=3.10.7 -y $
2. **Activate the Environment:** You must activate this environment every time you work on the project:
   	$ mamba activate fars-env $



###### **3. Running the Analysis**

Once the environment is active, you can launch the Jupyter Notebook interface to view and run the analysis files.



1. Navigate to the Repository:
   	$ cd /path/to/your/repository
2. Launch Jupyter Notebook:
   	$ jupyter notebook $





&nbsp;	



