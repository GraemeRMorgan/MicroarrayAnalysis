![](https://github.com/GraemeRMorgan/MicroarrayAnalysis/blob/master/neet-gif-web2.gif)
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
    python3 -m venv bio_venv
    . bio_venv/bin/activate
    pip install bioservices
    pip install flask
    pip install plotly
    FLASK_APP=app
    FLASK_ENV=development
    
This will set up the repo and install the necessary packages.

To shut off the virtual environment use

    deactivate
    
at any time while in the venv.
![](https://github.com/GraemeRMorgan/MicroarrayAnalysis/blob/master/neet-query2.jpg)
![](https://github.com/GraemeRMorgan/MicroarrayAnalysis/blob/master/neet-query3.jpg)
