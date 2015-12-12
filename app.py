from flask import Flask, render_template, request, redirect

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
#    print("The ticker is '"+ticker+"'")
    return redirect('/output.html') 

@app.route('/output.html')
def output():
    return render_template('output.html',ticker=ticker, price=price)

if __name__ == '__main__':
  app.run(port=33507)
