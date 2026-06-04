import pandas as pd

df = pd.read_csv(
    r"C:\Users\Dell\Desktop\E-Commerce Funnel & Conversion Analytics\Dataset\ecommerce_funnel_50k.csv"
)

print("Dataset Shape:", df.shape)

print("\nEvent Counts:")
print(df["event_type"].value_counts())

print("\nUnique Users:", df["user_id"].nunique())
print("Unique Sessions:", df["session_id"].nunique())

# Funnel Metrics
views = len(df[df["event_type"] == "view"])
carts = len(df[df["event_type"] == "add_to_cart"])
checkouts = len(df[df["event_type"] == "checkout"])
purchases = len(df[df["event_type"] == "purchase"])

print("\nFUNNEL")
print("Views:", views)
print("Add To Cart:", carts)
print("Checkouts:", checkouts)
print("Purchases:", purchases)

print("\nCONVERSION RATES")
print("View → Cart:", round((carts/views)*100,2), "%")
print("Cart → Checkout:", round((checkouts/carts)*100,2), "%")
print("Checkout → Purchase:", round((purchases/checkouts)*100,2), "%")
print("View → Purchase:", round((purchases/views)*100,2), "%")



import pandas as pd

df = pd.read_csv(
    r"C:\Users\Dell\Desktop\E-Commerce Funnel & Conversion Analytics\Dataset\ecommerce_funnel_50k.csv"
)

purchase_df = df[df["event_type"] == "purchase"]

top_categories = (
    purchase_df.groupby("category")
    .size()
    .sort_values(ascending=False)
    .head(10)
)

print("Top Categories by Purchases")
print(top_categories)



top_brands = (
    purchase_df.groupby("brand")["price"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print("\nTop Brands by Revenue")
print(top_brands)




device_revenue = (
    purchase_df.groupby("device")["price"]
    .sum()
    .sort_values(ascending=False)
)

print("\nDevice-wise Revenue")
print(device_revenue)



traffic_revenue = (
    purchase_df.groupby("traffic_source")["price"]
    .sum()
    .sort_values(ascending=False)
)

print("\nTraffic Source Revenue")
print(traffic_revenue)


#Chart 1: Conversion Funne

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    r"C:\Users\Dell\Desktop\E-Commerce Funnel & Conversion Analytics\Dataset\ecommerce_funnel_50k.csv"
)

stages = ["Views", "Add To Cart", "Checkout", "Purchase"]
values = [42315, 3939, 2109, 1215]

conversion_rates = ["100%", "9.31%", "4.98%", "2.87%"]

plt.figure(figsize=(10, 6))
plt.gca().set_facecolor("#081A2F")
plt.gcf().set_facecolor("#081A2F")

bars = plt.barh(stages, values)

plt.title("E-Commerce Conversion Funnel", color="white", fontsize=18, fontweight="bold")
plt.xlabel("Total Events", color="white")
plt.ylabel("Funnel Stage", color="white")

plt.xticks(color="white")
plt.yticks(color="white")

plt.gca().invert_yaxis()

for bar, value, rate in zip(bars, values, conversion_rates):
    plt.text(
        value + 500,
        bar.get_y() + bar.get_height()/2,
        f"{value:,}  ({rate})",
        va="center",
        color="white",
        fontsize=11,
        fontweight="bold"
    )

plt.grid(axis="x", linestyle="--", alpha=0.3)

plt.tight_layout()
plt.show()

# OBSERVATION:- The largest drop-off occurs between the View and Add-to-Cart stages, indicating that product engagement is 
# the primary conversion bottleneck.



# Chart 3: Traffic Source Revenue

import matplotlib.pyplot as plt

traffic_revenue = (
    purchase_df.groupby("traffic_source")["price"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12,6))

ax = plt.gca()
ax.set_facecolor("#0B1220")
plt.gcf().set_facecolor("#0B1220")

bars = plt.bar(
    traffic_revenue.index,
    traffic_revenue.values
)

plt.title(
    "Traffic Source Revenue Analysis",
    fontsize=20,
    fontweight="bold",
    color="white",
    pad=20
)

plt.xlabel("Traffic Source", color="white", fontsize=12)
plt.ylabel("Revenue", color="white", fontsize=12)

plt.xticks(color="white", fontsize=11)
plt.yticks(color="white", fontsize=11)

# Revenue labels
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height + 100000,
        f"{height/1000000:.1f}M",
        ha="center",
        color="white",
        fontsize=10,
        fontweight="bold"
    )

# Highlight top source
bars[0].set_linewidth(3)

plt.grid(axis="y", linestyle="--", alpha=0.25)

# Remove top/right borders
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

ax.spines["bottom"].set_color("white")
ax.spines["left"].set_color("white")

plt.tight_layout()
plt.show()

#   OBSWEVATION :-  Organic traffic generated the highest revenue, making it the most effective acquisition channel.