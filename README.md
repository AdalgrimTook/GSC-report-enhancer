# GSC Report Automation: SEO Action Prioritization

An automation exercise that converts a routine SEO analysis workflow from manual spreadsheet work into automated Python code.

## The Problem

When analyzing Google Search Console (GSC) page performance reports, SEO analysts typically need to:

1. Export the pages report from GSC
2. Manually review each page's metrics (impressions, CTR, position)
3. Decide what SEO action each page needs
4. Sort and prioritize the pages for action

For large sites with hundreds or thousands of pages, this manual process is time-consuing and error-prone.

---

## Manual vs Automated: Side-by-Side Comparison

### Manual Spreadsheet Workflow

| Step | Action                                                              | Time     |
| ---- | ------------------------------------------------------------------- | -------- |
| 1    | Export GSC Pages report to CSV/Excel                                | 2 min    |
| 2    | Add a new column "SEO Action"                                       | 1 min    |
| 3    | Copy pre-made formulas from template                                | 2 min    |
| 4    | Adjust thresholds (impressions, CTR, position) based on client size | 5-10 min |
| 5    | Copy-paste formulas across different ranges of data                 | 5-15 min |
| 6    | Sort by action type and priority                                    | 5 min    |
| 7    | Save and share                                                      | 2 min    |

**Total time: ~20-35 minutes** (depending on number of pages and client complexity)

**Common issues:**

- Forgetting to adjust thresholds when switching between clients
- Copy-paste errors when applying formulas to different ranges
- Formula references breaking when pasting across ranges
- Having to redo the whole process when client criteria changes

---

### Automated Python Solution

```python
import pandas as pd

df = pd.read_csv("gsc_pages_report.csv")

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
```

**Total time: ~5 seconds** (after initial setup)

**Benefits:**

- ✅ Consistent rule application across all rows
- ✅ Easy to modify criteria in one place
- ✅ Scales to any number of pages
- ✅ Reproduceble results

---

## SEO Action Logic

The script assigns actions based on these SEO best practices:

| Condition                                   | Action                      | Rationale                                                          |
| ------------------------------------------- | --------------------------- | ------------------------------------------------------------------ |
| Impressions > 10K, CTR < 1%, Position ≤ 10 | **Improve CTR**       | Page ranks well but isn't getting clicks → fix title/meta/h1 etc. |
| Impressions > 3K, Position 8-15             | **Content expansion** | Page has visibility but needs optimization to break into top spots |
| Impressions < 1K, Position > 15             | **Low priority**      | Low visibilty and poor ranking → monitor for now                  |
| Everything else                             | **No action**         | Either performing well or doesn't meet criteria                    |

---

## How to Use

### Requirements

```bash
pip install pandas
```

### Steps

1. **Export your GSC report** from Google Search Console (Pages tab)
2. **Rename the file** to match the expceted input or update the script
3. **Run the script:**
   ```bash
   python report-enhancer.py
   ```
4. **Output:** `gsc_pages_prioritized_actions.csv` with the new `seo_action` column

### Input File Format

The CSV should have these columns:

- `page` - The URL
- `clicks` - Number of clicks
- `impressions` - Number of impressions
- `ctr` - Click-through rate (as decimal, e.g., 0.02 for 2%)
- `position` - Average position in search results

---

## Files

| File                                  | Description                           |
| ------------------------------------- | ------------------------------------- |
| `report-enhancer.py`                | Main automation script                |
| `gsc_pages_prioritized_actions.csv` | Output file with SEO actions assigned |

---

## Time Savings

| Report Size | Manual Time | Automated Time | Savings |
| ----------- | ----------- | -------------- | ------- |
| 100 pages   | ~20 min     | 5 sec          | 99.6%   |
| 500 pages   | ~25 min     | 5 sec          | 99.7%   |
| 1000+ pages | ~35 min     | 5 sec          | 99.8%   |
