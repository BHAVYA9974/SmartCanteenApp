from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__, static_folder='../static')

# Load the menu.csv file
menu_df = pd.read_csv('../model/data/menu.csv')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        query = request.form['query'].lower()
        if "cold" in query and "drink" in query:
            results = menu_df[(menu_df['subcategory'] == 'Cold') & (menu_df['category'] == 'Drinks')]
        elif "spicy" in query:
            results = menu_df[menu_df['spice_level'] > 0]  # Filters items with spice_level > 0
        elif "hot" in query:
            results = menu_df[menu_df['hot'] == 1]  # Filters items marked as hot
        elif "healthy" in query:
            results = menu_df[menu_df['tags'].str.contains('healthy', na=False)]  # Filters by 'healthy' tag
        else:
            results = menu_df  # Default to full menu if no match
        return render_template('results.html', results=results.to_html(), qr_path='/static/gpay_qr.png')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)