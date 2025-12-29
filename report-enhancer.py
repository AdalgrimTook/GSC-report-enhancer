import pandas as pd

df = pd.read_csv("gsc_pages_mock_law_attorneys.csv")

def assign_action(row):
    if row["impressions"] > 10000 and row["ctr"] < 0.01 and row["position"] <= 10:
        return "Improve CTR (title/meta/snippet)"
    elif row["impressions"] > 3000 and 8 < row["position"] <= 15:
        return "Content expansion / optimization"
    elif row["impressions"] < 1000 and row["position"] > 15:
        return "Low priority / monitor"
    else:
        return "No action"

df["seo_action"] = df.apply(assign_action, axis=1)

df_final = df.sort_values(
    by=["seo_action", "impressions"],
    ascending=[True, False]
)

df_final.to_csv("gsc_pages_prioritized_actions.csv", index=False)
