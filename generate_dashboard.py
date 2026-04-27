import pandas as pd

# Load data
df = pd.read_csv("data/demand_data.csv")

# Basic aggregation
summary = df.groupby("product_id")["demand"].mean()

# Generate HTML
html_content = f"""
<html>
<head><title>Dashboard</title></head>
<body>
<h1>Demand Summary</h1>
{summary.to_frame().to_html()}
</body>
</html>
"""

# Save output
with open("output/dashboard.html", "w") as f:
    f.write(html_content)

print("Dashboard generated.")
