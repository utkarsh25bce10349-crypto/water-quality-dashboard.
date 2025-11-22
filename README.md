# Water_quality_dashboard.
## About the Project
This project calculates the Water Quality Index (WQI) based on three basic water parameters: pH, turbidity, and dissolved oxygen. The WQI helps to understand how clean or polluted the water is by giving a score and category like Good, Fair, or Poor.

User can enter details for multiple water samples, and the program will save the results and show a simple graph of the water quality trends across your samples.

## What It Does
- Takes input for pH, turbidity, and dissolved oxygen for each sample.
- Calculates the WQI score using assigned weights to each parameter.
- Shows the water quality category based on the score.
- Saves all sample results in a CSV file (`WQI_results.csv`).
- Draws a chart to show how water quality changes over the samples.

## Tools Used
- Python 3
- `csv` for saving data in a spreadsheet-friendly format
- `matplotlib` for making the graphs

## How to Use
1. Make sure Python 3 is installed on user's computer.
2. Install matplotlib library by running:
pip install matplotlib

text
3. Run the Python script:
python your_script.py

text
4. Enter the number of samples you want to evaluate.
5. Enter the values for pH, turbidity, and dissolved oxygen for each sample.
6. See the WQI results and view the trend graph.
7. Results will be saved in `WQI_results.csv` automatically.

## What I Learned
- How to work with user input and handle multiple entries.
- Basic calculations and data normalization.
- Writing data to files using the CSV format.
- Creating simple visualizations with matplotlib.
- Applying programming skills to a real-life environmental problem.

---

**Author:** Utkarsh Agrawal
**Date:** 23 November 2025
