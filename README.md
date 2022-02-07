# Cross Correlation Model

The project illustrates a DS project that takes in a template bird audio clip and runs it against a set of bird clips of the same species through a cross correlation model that automatically annotates those clips. This project will explore how well the model works on larger sets of data and different species while also obtaining a good amount of automated data for other future uses. The cross correlation model does not use machine learning and runs on the libraries: PyHa* (Python + Piha), Librosa, and Scipy. 

* Pyha: https://github.com/UCSD-E4E/PyHa/blob/main/README.md

## Data 

To use the model, you can edit the file config/data-params.json to change the path/location of the new data file you're trying to test on

## Running

The project assumes the data is stored in the data folder in .wav form with an existing template for each species. To set up the environment with the proper librariesm run the following code: 
`conda env create -f environment.yml`

To activate the environment, run the following code:
`conda activate ccenvironment`

To run the pipeline once the environment is set up, run the following code:
`py run.py test`
