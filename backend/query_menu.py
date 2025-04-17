import pandas as pd

menu_df = pd.read_csv('../model/data/menu.csv')
print("Menu loaded successfully!")

def search_menu(query):
    query = query.lower()
    if "spicy" in query and "hot" in query:
        return menu_df[(menu_df['is_hot'] == 1) & (menu_df['spice_level'] > 2)]
    elif "cold" in query and "drink" in query:
        return menu_df[(menu_df['subcategory'] == 'Cold') & (menu_df['category'] == 'Drinks')]
    elif "healthy" in query:
        return menu_df[menu_df['tags'].str.contains('healthy', na=False)]
    else:
        return menu_df  

query = input("Ask about the menu (e.g., 'spicy hot items'): ")
results = search_menu(query)
print(results)