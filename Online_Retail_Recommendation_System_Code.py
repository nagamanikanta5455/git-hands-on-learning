import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules
import matplotlib.pyplot as plt
import seaborn as sns
from itertools import combinations

def load_and_clean_data(path):
    df = pd.read_excel(path)
    df = df.dropna(subset=['CustomerID', 'Description'])
    df = df[df['Quantity'] > 0]
    df = df[df['Country'] == "United Kingdom"]
    item_counts = df['Description'].value_counts()
    common_items = item_counts[item_counts > 10].index
    df = df[df['Description'].isin(common_items)]
    return df

def create_basket_matrix(df):
    basket = df.groupby(['InvoiceNo', 'Description'])['Quantity'].sum().unstack().fillna(0).astype(int)
    return basket.gt(0)

def generate_rules(basket_sets, min_support=0.02, min_lift=1.0, min_confidence=0.5):
    itemsets = apriori(basket_sets, min_support=min_support, use_colnames=True)
    rules = association_rules(itemsets, metric="lift", min_threshold=min_lift)
    rules = rules[rules['confidence'] >= min_confidence]
    return rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']].sort_values(by=['lift', 'confidence'], ascending=False)

def format_rules(rules_df, top_n=10):
    return [
        f"If a customer buys [{', '.join(list(row['antecedents']))}], they are likely to buy [{', '.join(list(row['consequents']))}] "
        f"(Support: {row['support']:.2f}, Confidence: {row['confidence']:.2f}, Lift: {row['lift']:.2f})"
        for _, row in rules_df.head(top_n).iterrows()
    ]

def plot_top_items(df):
    top_items = df['Description'].value_counts().head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=top_items.values, y=top_items.index, color="skyblue")
    plt.title("Top 10 Frequently Purchased Items")
    plt.xlabel("Number of Purchases")
    plt.ylabel("Product")
    plt.tight_layout()
    plt.show()

def plot_rule_scatter(rules_df):
    plt.figure(figsize=(10,6))
    sns.scatterplot(data=rules_df.head(20), x='support', y='confidence', size='lift', legend=False, hue='lift', palette='coolwarm')
    plt.title("Top 20 Rules: Support vs Confidence (size = Lift)")
    plt.xlabel("Support")
    plt.ylabel("Confidence")
    plt.tight_layout()
    plt.show()

def plot_co_occurrence_heatmap(basket_sets, top_n=10):
    top_items = basket_sets.sum().sort_values(ascending=False).head(top_n).index
    co_matrix = pd.DataFrame(0, index=top_items, columns=top_items)
    for _, row in basket_sets[top_items].iterrows():
        items = row[row].index
        for item1, item2 in combinations(items, 2):
            co_matrix.loc[item1, item2] += 1
            co_matrix.loc[item2, item1] += 1
    plt.figure(figsize=(8,6))
    sns.heatmap(co_matrix, annot=True, fmt="d", cmap="YlGnBu")
    plt.title("Co-occurrence Heatmap of Top Frequent Items")
    plt.tight_layout()
    plt.show()

df = load_and_clean_data("OnlineRetail (1).xlsx")
basket_sets = create_basket_matrix(df)
rules_df = generate_rules(basket_sets)

print("Top Product Recommendations:\n")
for rec in format_rules(rules_df, top_n=15):
    print(rec)

rules_df.to_excel("Top_Product_Recommendations.xlsx", index=False)

plot_top_items(df)
plot_rule_scatter(rules_df)
plot_co_occurrence_heatmap(basket_sets)
