# Deviation Analysis Project
This project aims to analyze deviations in floor vs. ceiling corners of a model and compare them with ground truth labels for room names and the number of corners in those rooms. It provides meaningful statistics to evaluate the performance of the model.

## Requirements
Python 3.x
Pandas
Matplotlib

## Installation
1.Clone the repository:

git clone https://github.com/vadzimbudnikau/deviation-analysis.git
cd deviation-analysis

2.Create a virtual environment (optional but recommended):

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3.Install dependencies:

pip install -r requirements.txt

## Usage
1.Ensure you have the required JSON file (deviation.json) in the project directory.
2.Run the Jupyter Notebook to generate and visualize plots:

jupyter notebook Notebook.ipynb

3.The notebook will guide you through the process and display the plots.

## Plots
The generated plots will be saved in the "plots" folder, and their paths will be returned by the draw_plots function.

## Contributing
Feel free to contribute to this project by opening issues or pull requests.

## License
This project is licensed under the MIT License - see the LICENSE file for details.


