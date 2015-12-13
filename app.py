from pandas import DataFrame
import pandas as pd
import requests

from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components 

queryobj = []

app = Flask(__name__)

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index')
def index():
  return render_template('index.html')

@app.route('/query', methods = ['POST'])
def query():
    ticker = request.form['ticker']
    price  = request.form['price']
    queryobj.append(ticker)
    queryobj.append(price)
#    print("The ticker is '"+ticker+"'")
    return redirect('/graph.html') 

@app.route('/graph.html')
def graph():
    r = requests.get('https://www.quandl.com/api/v3/datasets/WIKI/AAPL/data.json?start_date=2015-05-01&end_date=2015-05-27&column_index=2')
    rj = r.json()
    rjdata = rj.get('dataset_data').get('data')
    df = pd.DataFrame(data=rjdata,columns=['Day','Value'])
    dfsort = df.sort('Day')
    dates = dfsort.Day.tolist()
    values = dfsort.Value.tolist()
    fig = figure(title='Data from Quandle WIKI set')
#              x_axis_label='date',
#              x_axis_type='datetime')
#    # Create a polynomial line graph
#    x = list(range(10))
#    fig = figure(title="Polynomial")
#    fig.line(x, [i ** 2 for i in x], line_width=2)
    fig.line(dates,values,line_width=2)
    script, div = components(fig)
    return render_template('graph.html', script=script, div=div)

@app.route('/output.html')
def output():
    return render_template('output.html',queryobj=queryobj)

if __name__ == '__main__':
  app.run(port=33507)
