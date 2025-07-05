
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df = pd.read_excel("OnlineRetail (1).xlsx")
df.dropna(subset=['CustomerID', 'Description'], inplace=True)  # Remove missing customer or item
df = df[df['Quantity'] > 0]  # Remove returns and invalid transactions
df = df[df['Country'] == "United Kingdom"]  # Focus on a single market for clarity

basket = (
    df.groupby(['InvoiceNo', 'Description'])['Quantity']
    .sum().unstack().reset_index().fillna(0)
    .set_index('InvoiceNo')
)

basket_sets = basket.applymap(lambda x: 1 if x > 0 else 0)

frequent_itemsets = apriori(basket_sets, min_support=0.02, use_colnames=True)

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

strong_rules = rules[['antecedents', 'consequents', 'support', 'confidence', 'lift']]\
    .sort_values(by='lift', ascending=False)

print("Top Product Recommendations:")
print(strong_rules.head(10))
