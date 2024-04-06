from flask import Flask, redirect, url_for, request, jsonify
from Secret import *
import requests

URI_newsapi_org = f'https://newsapi.org/v2/everything?apiKey={KEY_newsapi_org}&q='

app = Flask(__name__)

@app.route('/')
def index():
    return 'Main point!'

@app.route('/success/<name>')
def success(name):
   return 'welcome %s' % name

@app.route('/search', methods=['POST'])
def search():
    # Получаем данные из запроса
    param_value = request.args.get('param')
   
    # Проверяем наличие параметра в запросе
    if param_value is not None:
        ulr = URI_newsapi_org+param_value
        res=get_news_data(ulr)
        return jsonify({"message": f"Received for parameter: {param_value} values: {res}"}), 200
    else:
        return jsonify({"error": "Parameter 'param' is missing"}), 400
    
def get_news_data(url):   
    try:
        response = requests.get(url)
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Assuming the response is JSON, you can parse it using .json()
            data = response.json()
            return data
        else:
            # If the request was unsuccessful, print the error code
            print("Request failed with status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == '__main__':
    app.run(debug=True,port=8080)