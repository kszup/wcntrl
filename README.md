# wcntrl.py
Quick way to visualize caloric intake.

## Motivation
Learning to use Python 3 with pandas, and termgraph.

## Dependencies 
This project uses Python 3.6.10 with the following modules
- pandas v1.0.5
- colorama v0.4.3
- termgraph v0.4.2

wctrl.py also utilizes helper.py to split out functionality.

## Overview
Currently, the script reads in a file named 'data.txt' that starts with 'date,item,calories' on the first line. Below is a sample for data.txt.
```
date,item,calories
20200708,oatmeal,160
20200708,coffee with milk,60
20200709,apple,95
20200709,honey(tbsp),64
```
The script will sum up the total calories per date and then display a graph in the terminal. A threshold can be set to show going over a limit of calories.
```
20200706: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1672.00
20200707: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 1914.00
20200708: ▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇ 737.00
```
## References
- https://dev.to/petercour/draws-graphs-in-the-terminal-with-python-31cg
- https://computingforgeeks.com/termgraph-command-line-tool-draw-graphs-in-terminal-linux/
- https://stackoverflow.com/questions/56360610/sum-column-based-on-another-column-in-pandas-dataframe
