# AI Conda Environment Setup

## To list the environments you have

``` Bash
conda info -e
```

## Initial Setup for a new AI environment

``` Bash
conda create --name AI python=3.11
conda activate AI
conda install pandas
conda install console_shortcut
conda install -c conda-forge jupyterlab
conda install scikit-learn
conda install matplotlib
pip install python-dotenv
pip install nltk
pip install transformers
pip install sentence-transformers
pip install tensorflow
pip install keras-tuner
pip install tf-keras
pip install gradio
pip install iprogress
pip install jupyter --upgrade
pip install openai
pip install langchain
pip install langchain-openai
```

## Create the kernel for VS Code/Jupyter

``` Bash
python -m ipykernel install --user --name <other-env> --display-name "Python (<other-env>)"
For example,
python -m ipykernel install --user --name AI --display-name "Python (AI)"
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

PC:  From the Anaconda Prompt (AI):

``` Bash
jupyter lab
```

Mac:  From the Terminal:

``` Bash
conda activate AI
jupyter lab
```
