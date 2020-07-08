#!/usr/bin/env python3
# coding=utf-8
"""This script visualizes caloric intake."""

# wcontrol.py - Caloric intake visualized in terminal
# https://github.szup/wcontrol

import helper as h

VERSION = "0.1"

def main():
    data = h.open_data('data.txt')
    calories_per_day = h.total_calories(data)
    h.cal_plotter(calories_per_day,1600)

if __name__ == "__main__":
    main()
