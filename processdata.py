#import libraries 
import csv
import requests
import os #creates new directory source
import pickle #serialise python objects for SP500 to be in a list
import bs4 as bs
import yfinance as yf
import datetime as dt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from sklearn import metrics
from matplotlib import style
from pandas_datareader import data as pdr
from matplotlib.colors import LinearSegmentedColormap
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import RandomizedSearchCV
from sklearn.model_selection import cross_val_score


def download_sp500_data():
    #download available data of the s&p500 index from yahoo finance
    sp500_data = yf.download("^GSPC", start="2017-01-01", end="2021-10-16")
    sp500_df = pd.DataFrame(sp500_data)
    #saves to and creates csv file
    sp500_df.to_csv("sp500_data.csv")

    