# Microarray Analysis

***

**Introduction**

This goal of this project is to create a tool that will pull information out of the [KEGG Pathway](https://www.genome.jp/kegg/pathway.html) database and output the gene pathway of specific genes quickly and easily.

The [ProjectSummary.pdf](https://github.com/MichaelKowal/MicroarrayAnalysis/blob/master/ProjectSummary.pdf) contains a more detailed description of this project and its future uses.

***

**Setup**

To setup this repo, navigate to the folder you want to store the project and run the following commands in the terminal:

    git clone https://github.com/MichaelKowal/MicroarrayAnalysis
    cd MicroarrayAnalysis
    sudo pip install virtualenv
    virtualenv bio_venv
    . bio_venv/bin/activate
    pip install bioservices
    
This will set up the repo and install the necessary packages.

To shut off the virtual environment use

    deactivate
    
at any time while in the venv.
