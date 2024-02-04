# AI Conda Environment Setup

## To list the environments you have

``` Bash
conda info -e
```

## Initial Setup for a new Llama 2 environment

``` Bash
conda create --name llama2 python=3.12
conda activate llama2
conda install pandas
conda install console_shortcut
conda install -c conda-forge jupyterlab
conda install matplotlib
pip install streamlit
conda install langchain
conda install replicate
pip install python-dotenv
pip install -U langchain-community
```

## Create the kernel for VS Code/Jupyter

``` Bash
python -m ipykernel install --user --name <other-env> --display-name "Python (<other-env>)"
For example,
python -m ipykernel install --user --name llama2 --display-name "Python (Llama2)"
```
### To remove a Kernel from Jupyter, simply run the following code:

``` Bash
jupyter kernelspec uninstall "Python 3.7.1 64-bit"
```

### To list the Kernel's you have defined

``` Bash
jupyter kernelspec list
```

## Occasionally:

Run this from time-to-time to update Anaconda

``` Bash
conda update -n base -c defaults conda
```

Run this from time-to-time to update pip

``` Bash
python.exe -m pip install --upgrade pip
```

## To Remove a Corrupted Environment

``` Bash
conda env remove -n ENV_NAME
```

### To Launch Jupyter Lab

PC:  From the Anaconda Prompt (Llama2):

``` Bash
jupyter lab
```

Mac:  From the Terminal:

``` Bash
conda activate llama2
jupyter lab
```
