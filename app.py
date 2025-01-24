from flask import Flask, request, render_template, redirect, jsonify, session
import requests
import polars as pl
import subprocess
import os
from flask_session import Session

app = Flask(__name__, template_folder='templates')

app.config['SECRET_KEY'] = 'secret_key'  
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

API_KEY = ''

@app.route('/convert_price', methods=['POST'])
def convert_price():
    price = request.form.get('price')
    rate = request.form.get('rate')
    
    if not rate.replace('.', '', 1).isdigit():
        return jsonify({'error': 'Conversion rate must be a numeric value'}), 400
    
    try:
        result = subprocess.run(['java', 'StockConverter'], input=f"{price}\n{rate}\n", text=True, capture_output=True)
        converted_price = result.stdout.strip()
        
        session['converted_price'] = converted_price
        return redirect('/')  
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def get_stock_data(ticker):
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={ticker}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    
    print(data)
    
    if 'Time Series (Daily)' not in data:
        raise ValueError(f"Error fetching data: {data.get('Error Message', 'Unknown error')}")
    
    time_series = data['Time Series (Daily)']
    records = [{'date': date, **values} for date, values in time_series.items()]
    
    df = pl.DataFrame(records)
    
    df = df.rename({
        '1. open': 'open',
        '2. high': 'high',
        '3. low': 'low',
        '4. close': 'close',
        '5. volume': 'volume'
    })
    
    df = df.with_columns([
        pl.col('date').str.strptime(pl.Date, format='%Y-%m-%d'),
        pl.col('open').cast(pl.Float64),
        pl.col('high').cast(pl.Float64),
        pl.col('low').cast(pl.Float64),
        pl.col('close').cast(pl.Float64),
        pl.col('volume').cast(pl.Int64)
    ])
    
    df = df.sort('date')
    return df

@app.route('/', methods=['GET', 'POST'])
def home():
    stock_data = None
    error = None
    converted_price = session.pop('converted_price', None)  
    rates = {
        'USD': 1.0,
        'EUR': 0.85,
        'JPY': 110.0,
        'GBP': 0.75,
        'AUD': 1.3,
        'CAD': 1.25
    }

    if request.method == 'POST':
        if 'ticker' in request.form:
            ticker = request.form.get('ticker')
            
            if not ticker:
                error = 'Ticker is required'
            else:
                try:
                    df = get_stock_data(ticker)
                    latest_data = df.tail(1)
                    
                    stock_data = {
                        'ticker': ticker.upper(),
                        'currentPrice': latest_data['close'][0],
                        'openPrice': latest_data['open'][0],
                    }
                except Exception as e:
                    error = f'Error fetching data: {str(e)}'

    return render_template('index.html', stock_data=stock_data, error=error, convertedPrice=converted_price, rates=rates)

@app.route('/notify_reports', methods=['GET'])
def notify_reports():
    emails = ['p4504626@gmail.com'] 
    report_type = 'Quarterly GDP, QFR, ECI'
    subject = f"New {report_type} Reports Available"
    body = "The latest quarterly reports for GDP, QFR, and ECI are now available."

    errors = []
    for email in emails:
        try:
            result = subprocess.run(['java', 'EmailSenderService', email, subject, body], capture_output=True, text=True)
            if result.returncode != 0:
                errors.append(f"Failed to send email to {email}")
        except Exception as e:
            errors.append(f"Error for {email}: {str(e)}")

    return jsonify({'status': 'success'}), 200


if __name__ == "__main__":
    app.run(debug=True, port=5001)