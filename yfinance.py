import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

# plt inline


aapl = yf.Ticker('AAPL')

aapl.history()
