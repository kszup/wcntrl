#!/usr/bin/env python3
# coding=utf-8
"""This script visualizes caloric intake."""

# wcntrl.py - Caloric intake visualized in terminal
# https://github.com/kszup/wcntrl.git

import helper as h

VERSION = "0.1"

def main():
    data = h.open_data('data.txt')
    calories_per_day = h.total_calories(data)
    h.cal_plotter(calories_per_day,1600)

if __name__ == "__main__":
    main()
