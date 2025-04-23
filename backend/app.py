from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__, static_folder='../static')

# Load the menu.csv file
menu_df = pd.read_csv('../model/data/menu.csv')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query'].lower()
        print(f"Received query: {query}")  # Debug line
        if "cold" in query and "drink" in query:
            results = menu_df[(menu_df['subcategory'] == 'Cold') & (menu_df['category'] == 'Drinks')]
        elif "spicy" in query:
            results = menu_df[menu_df['tags'].str.contains('spicy', na=False)]
            if results.empty:
                results = pd.DataFrame([["No spicy items found. Try 'healthy' or 'hot'?", "", "", "", "", "", "", "", "", ""]], columns=menu_df.columns)
        elif "hot" in query:
            results = menu_df[menu_df['is_hot'] == 1]
        elif "healthy" in query:
            results = menu_df[menu_df['tags'].str.contains('healthy', na=False)]
        else:
            results = menu_df
        return render_template('results.html', results=results.to_html(), qr_path='/static/gpay_qr.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)