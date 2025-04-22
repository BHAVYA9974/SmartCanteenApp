from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__, static_folder='../static')

# Load the menu.csv file
menu_df = pd.read_csv('../model/data/menu.csv')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query']
        if "cold" in query.lower() and "drink" in query.lower():
            results = menu_df[(menu_df['subcategory'] == 'Cold') & (menu_df['category'] == 'Drinks')]
        else:
            results = menu_df
        return render_template('results.html', results=results.to_html(), qr_path='../static/gpay_qr.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)