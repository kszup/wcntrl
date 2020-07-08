# wcntrl.py
Quick way to visualize caloric intake.

## Motivation
Learning to use Python 3 with pandas, and termgraph.

## Dependencies 
This project uses Python 3.6.10 with the following modules
- pandas v1.0.5
- colorama v0.4.3
- termgraph v0.4.2

wctrl.py also utilizes helper.py to split out functionality. Not sure I need this though.

## Overview
Currently, the script reads in a file named 'data.txt' that starts with 'date,item,calories' on the first line.
- Sample data:

date,item,calories
20200708,oatmeal,160
20200708,coffee with milk,60
20200709,apple,95
20200709,honey(tbsp),64

- The script will sum up the total calories per date and then display a graph in the terminal. A threshold can be set to show going over a limit of calories.

## References
https://dev.to/petercour/draws-graphs-in-the-terminal-with-python-31cg
https://computingforgeeks.com/termgraph-command-line-tool-draw-graphs-in-terminal-linux/
https://stackoverflow.com/questions/56360610/sum-column-based-on-another-column-in-pandas-dataframe
