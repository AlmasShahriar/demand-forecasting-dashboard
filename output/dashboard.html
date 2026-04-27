"""
Demand Forecasting & Inventory Analysis Dashboard
==================================================
Author  : Almas Shahriar
Degree  : B.Sc. Industrial & Production Engineering, BUET ('26)
GitHub  : github.com/almasshahriar

Generates a standalone HTML dashboard from demand_data.csv.
Techniques: Moving Average, Seasonal Index Forecasting, ABC Analysis.

Usage:
    pip install pandas numpy
    python generate_dashboard.py
    → Open output/dashboard.html in any browser
"""

import csv
import json
import math
import os
from datetime import datetime

# ─────────────────────────────────────────────
# 1. LOAD DATA
# ─────────────────────────────────────────────
MONTHS = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
DATA_FILE = os.path.join(os.path.dirname(__file__), "data", "demand_data.csv")
OUTPUT_FILE = os.path.join(os.path.dirname(__file__), "output", "dashboard.html")
os.makedirs(os.path.join(os.path.dirname(__file__), "output"), exist_ok=True)

items = []
with open(DATA_FILE, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        monthly = [int(row[m]) for m in MONTHS]
        unit_cost = float(row["Unit_Cost"])
        annual_usage = sum(monthly)
        annual_value = annual_usage * unit_cost
        items.append({
            "sku": row["SKU"],
            "desc": row["Description"],
            "unit_cost": unit_cost,
            "monthly": monthly,
            "annual_usage": annual_usage,
            "annual_value": annual_value,
        })

# ─────────────────────────────────────────────
# 2. ABC ANALYSIS
# ─────────────────────────────────────────────
items.sort(key=lambda x: x["annual_value"], reverse=True)
total_value = sum(i["annual_value"] for i in items)
cum = 0
for item in items:
    pct = item["annual_value"] / total_value * 100
    cum += pct
    item["value_pct"] = round(pct, 2)
    item["cum_pct"] = round(cum, 2)
    item["abc"] = "A" if cum - pct < 70 else ("B" if cum - pct < 90 else "C")

count_a = sum(1 for i in items if i["abc"] == "A")
count_b = sum(1 for i in items if i["abc"] == "B")
count_c = sum(1 for i in items if i["abc"] == "C")
val_a   = round(sum(i["annual_value"] for i in items if i["abc"] == "A") / total_value * 100, 1)

# ─────────────────────────────────────────────
# 3. SEASONAL INDEX & FORECASTING (next 6 months)
# ─────────────────────────────────────────────
def seasonal_indices(monthly):
    avg = sum(monthly) / 12
    if avg == 0:
        return [1.0] * 12
    return [m / avg for m in monthly]

def moving_average(series, window=3):
    result = []
    for i in range(len(series)):
        if i < window - 1:
            result.append(None)
        else:
            result.append(round(sum(series[i-window+1:i+1]) / window, 1))
    return result

def forecast_next_6(monthly):
    """Simple seasonal forecast: use seasonal indices × trend-adjusted mean."""
    avg = sum(monthly) / 12
    si = seasonal_indices(monthly)
    # detect trend: compare H2 average to H1 average
    h1 = sum(monthly[:6]) / 6
    h2 = sum(monthly[6:]) / 6
    trend = (h2 - h1) / h1 if h1 > 0 else 0
    forecasts = []
    for k in range(6):
        month_idx = (12 + k) % 12  # Jan–Jun of next year
        projected_avg = avg * (1 + trend * (k + 1) / 6)
        forecasts.append(round(projected_avg * si[month_idx]))
    return forecasts

for item in items:
    item["ma3"]       = moving_average(item["monthly"], 3)
    item["forecast"]  = forecast_next_6(item["monthly"])
    item["si"]        = [round(x, 3) for x in seasonal_indices(item["monthly"])]
    peak_idx          = item["si"].index(max(item["si"]))
    item["peak_month"]= MONTHS[peak_idx]

# ─────────────────────────────────────────────
# 4. SUMMARY STATS
# ─────────────────────────────────────────────
total_units = sum(i["annual_usage"] for i in items)
total_skus  = len(items)
avg_cost    = round(sum(i["unit_cost"] for i in items) / total_skus, 2)
top_sku     = items[0]["sku"]

# Monthly aggregate demand
agg_monthly = [sum(i["monthly"][m] for i in items) for m in range(12)]
agg_forecast = [sum(i["forecast"][m] for i in items) for m in range(6)]
agg_ma3 = moving_average(agg_monthly, 3)

# ─────────────────────────────────────────────
# 5. BUILD HTML DASHBOARD
# ─────────────────────────────────────────────
items_json     = json.dumps(items)
months_json    = json.dumps(MONTHS)
agg_json       = json.dumps(agg_monthly)
agg_ma3_json   = json.dumps(agg_ma3)
agg_fc_json    = json.dumps(agg_forecast)
fc_months_json = json.dumps(["Jan'26","Feb'26","Mar'26","Apr'26","May'26","Jun'26"])

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"/>
<meta name="viewport" content="width=device-width,initial-scale=1.0"/>
<title>Demand Forecasting Dashboard — Almas Shahriar</title>
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.1/chart.umd.min.js"></script>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Barlow:wght@300;400;600;700&family=Barlow+Condensed:wght@700;900&display=swap" rel="stylesheet"/>
<style>
:root{{
  --bg:#0d0f12;--bg2:#13161b;--bg3:#1a1e26;--border:#2a2f3a;
  --accent:#00c2ff;--accent2:#ff6b35;--accent3:#00e5a0;--warn:#f59e0b;
  --text:#e8eaf0;--muted:#6b7280;
  --mono:'Share Tech Mono',monospace;
  --sans:'Barlow',sans-serif;
  --cond:'Barlow Condensed',sans-serif;
}}
*{{margin:0;padding:0;box-sizing:border-box;}}
body{{background:var(--bg);color:var(--text);font-family:var(--sans);min-height:100vh;}}
body::before{{content:'';position:fixed;inset:0;
  background-image:linear-gradient(rgba(0,194,255,0.025) 1px,transparent 1px),
  linear-gradient(90deg,rgba(0,194,255,0.025) 1px,transparent 1px);
  background-size:48px 48px;pointer-events:none;z-index:0;}}
.page{{position:relative;z-index:1;max-width:1200px;margin:0 auto;padding:0 28px 80px;}}

/* HEADER */
header{{padding:48px 0 36px;border-bottom:1px solid var(--border);margin-bottom:40px;}}
.hdr-tag{{font-family:var(--mono);font-size:11px;color:var(--accent);letter-spacing:3px;margin-bottom:10px;display:flex;align-items:center;gap:8px;}}
.hdr-tag::before{{content:'';display:inline-block;width:24px;height:1px;background:var(--accent);}}
h1{{font-family:var(--cond);font-size:clamp(36px,6vw,64px);font-weight:900;text-transform:uppercase;letter-spacing:-1px;line-height:1;}}
h1 span{{color:var(--accent);}}
.hdr-meta{{margin-top:16px;display:flex;gap:12px;flex-wrap:wrap;}}
.pill{{font-family:var(--mono);font-size:11px;color:var(--muted);border:1px solid var(--border);padding:4px 10px;letter-spacing:1px;}}
.pill.hi{{border-color:var(--accent);color:var(--accent);}}

/* KPI STRIP */
.kpi-strip{{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px;margin-bottom:40px;}}
.kpi{{background:var(--bg3);border:1px solid var(--border);border-top:2px solid var(--accent);padding:18px 20px;}}
.kpi.o{{border-top-color:var(--accent2);}}
.kpi.g{{border-top-color:var(--accent3);}}
.kpi.y{{border-top-color:var(--warn);}}
.kpi-label{{font-family:var(--mono);font-size:10px;color:var(--muted);letter-spacing:1.5px;text-transform:uppercase;margin-bottom:6px;}}
.kpi-val{{font-family:var(--cond);font-size:30px;font-weight:900;line-height:1;}}
.kpi-sub{{font-family:var(--mono);font-size:11px;color:var(--muted);margin-top:3px;}}

/* SECTION */
.section-title{{font-family:var(--cond);font-size:20px;font-weight:900;text-transform:uppercase;letter-spacing:2px;margin-bottom:20px;display:flex;align-items:center;gap:12px;}}
.section-title::after{{content:'';flex:1;height:1px;background:var(--border);}}
.section{{margin-bottom:48px;}}

/* CHARTS GRID */
.chart-grid{{display:grid;grid-template-columns:1fr 1fr;gap:20px;}}
.chart-grid.wide{{grid-template-columns:1fr;}}
@media(max-width:700px){{.chart-grid{{grid-template-columns:1fr;}}}}
.chart-box{{background:var(--bg2);border:1px solid var(--border);padding:24px;}}
.chart-title{{font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:2px;text-transform:uppercase;margin-bottom:16px;}}
.chart-wrap{{position:relative;height:260px;}}

/* TABLE */
.tbl-wrap{{overflow-x:auto;}}
table{{width:100%;border-collapse:collapse;font-size:13px;}}
th{{font-family:var(--mono);font-size:10px;letter-spacing:2px;text-transform:uppercase;color:var(--muted);padding:10px 14px;text-align:left;border-bottom:1px solid var(--border);white-space:nowrap;}}
td{{padding:10px 14px;border-bottom:1px solid rgba(42,47,58,0.5);font-family:var(--mono);font-size:12px;}}
tr:last-child td{{border-bottom:none;}}
tr:hover td{{background:rgba(255,255,255,0.02);}}
.badge{{font-family:var(--cond);font-size:13px;font-weight:700;padding:2px 10px;letter-spacing:1px;}}
.A{{background:rgba(0,229,160,0.15);color:var(--accent3);}}
.B{{background:rgba(0,194,255,0.15);color:var(--accent);}}
.C{{background:rgba(107,114,128,0.15);color:var(--muted);}}

/* SKU SELECTOR */
.sku-controls{{display:flex;gap:10px;flex-wrap:wrap;margin-bottom:20px;align-items:center;}}
.sku-controls label{{font-family:var(--mono);font-size:11px;color:var(--muted);letter-spacing:1px;}}
select{{background:var(--bg3);border:1px solid var(--border);color:var(--text);font-family:var(--mono);font-size:13px;padding:8px 12px;outline:none;cursor:pointer;}}
select:focus{{border-color:var(--accent);}}

/* SEASONAL GRID */
.si-grid{{display:grid;grid-template-columns:repeat(12,1fr);gap:6px;}}
.si-cell{{background:var(--bg3);border:1px solid var(--border);padding:10px 6px;text-align:center;}}
.si-month{{font-family:var(--mono);font-size:9px;color:var(--muted);letter-spacing:1px;margin-bottom:4px;}}
.si-val{{font-family:var(--cond);font-size:16px;font-weight:700;}}

/* FOOTER */
footer{{margin-top:60px;padding-top:28px;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;}}
.fn{{font-family:var(--cond);font-size:14px;font-weight:900;letter-spacing:2px;text-transform:uppercase;}}
.fn span{{color:var(--accent);}}
.flinks{{display:flex;gap:16px;}}
.flinks a{{font-family:var(--mono);font-size:11px;color:var(--muted);text-decoration:none;letter-spacing:1px;transition:color .2s;}}
.flinks a:hover{{color:var(--accent);}}
.gen-time{{font-family:var(--mono);font-size:10px;color:var(--muted);}}
</style>
</head>
<body>
<div class="page">

<header>
  <div class="hdr-tag">Demand Forecasting & Inventory Analysis</div>
  <h1>Inventory <span>Intelligence</span><br/>Dashboard</h1>
  <div class="hdr-meta">
    <span class="pill hi">Generated {datetime.now().strftime("%d %b %Y %H:%M")}</span>
    <span class="pill">{total_skus} SKUs</span>
    <span class="pill">12-MONTH HISTORY</span>
    <span class="pill">6-MONTH FORECAST</span>
    <span class="pill">ABC CLASSIFICATION</span>
    <span class="pill">ALMAS SHAHRIAR · BUET IPE</span>
  </div>
</header>

<!-- KPIs -->
<div class="kpi-strip">
  <div class="kpi g">
    <div class="kpi-label">Total Annual Units</div>
    <div class="kpi-val">{total_units:,}</div>
    <div class="kpi-sub">across {total_skus} SKUs</div>
  </div>
  <div class="kpi o">
    <div class="kpi-label">Total Annual Value</div>
    <div class="kpi-val">${total_value:,.0f}</div>
    <div class="kpi-sub">inventory spend</div>
  </div>
  <div class="kpi">
    <div class="kpi-label">Class A SKUs</div>
    <div class="kpi-val">{count_a}</div>
    <div class="kpi-sub">{val_a}% of total value</div>
  </div>
  <div class="kpi y">
    <div class="kpi-label">Class B SKUs</div>
    <div class="kpi-val">{count_b}</div>
    <div class="kpi-sub">medium priority</div>
  </div>
  <div class="kpi">
    <div class="kpi-label">Class C SKUs</div>
    <div class="kpi-val">{count_c}</div>
    <div class="kpi-sub">low priority</div>
  </div>
  <div class="kpi g">
    <div class="kpi-label">Top SKU by Value</div>
    <div class="kpi-val" style="font-size:20px">{top_sku}</div>
    <div class="kpi-sub">{items[0]["desc"][:18]}…</div>
  </div>
</div>

<!-- SECTION 1: AGGREGATE DEMAND -->
<div class="section">
  <div class="section-title">01 — Aggregate Demand & Forecast</div>
  <div class="chart-grid wide">
    <div class="chart-box">
      <div class="chart-title">Total Monthly Demand (All SKUs) + 3-Month MA + 6-Month Forecast</div>
      <div class="chart-wrap"><canvas id="aggChart"></canvas></div>
    </div>
  </div>
</div>

<!-- SECTION 2: ABC -->
<div class="section">
  <div class="section-title">02 — ABC Classification</div>
  <div class="chart-grid">
    <div class="chart-box">
      <div class="chart-title">Annual Value by SKU (Pareto)</div>
      <div class="chart-wrap"><canvas id="paretoChart"></canvas></div>
    </div>
    <div class="chart-box">
      <div class="chart-title">Class Distribution — Count vs Value</div>
      <div class="chart-wrap"><canvas id="abcDonut"></canvas></div>
    </div>
  </div>

  <br/>
  <div class="tbl-wrap">
    <table id="abc-table">
      <thead><tr>
        <th>Rank</th><th>SKU</th><th>Description</th>
        <th>Annual Usage</th><th>Unit Cost ($)</th>
        <th>Annual Value ($)</th><th>% Value</th><th>Cum %</th><th>Class</th>
      </tr></thead>
      <tbody>
        {"".join(f'''<tr>
          <td style="color:var(--muted)">#{i+1}</td>
          <td style="font-weight:600;color:var(--accent)">{item["sku"]}</td>
          <td style="color:var(--muted)">{item["desc"]}</td>
          <td>{item["annual_usage"]:,}</td>
          <td>{item["unit_cost"]:.2f}</td>
          <td>{item["annual_value"]:,.2f}</td>
          <td style="color:var(--muted)">{item["value_pct"]:.2f}%</td>
          <td>{item["cum_pct"]:.1f}%</td>
          <td><span class="badge {item["abc"]}">{item["abc"]}</span></td>
        </tr>''' for i, item in enumerate(items))}
      </tbody>
    </table>
  </div>
</div>

<!-- SECTION 3: SKU DRILL-DOWN -->
<div class="section">
  <div class="section-title">03 — SKU Drill-Down</div>
  <div class="sku-controls">
    <label>SELECT SKU →</label>
    <select id="skuSelect" onchange="updateSKU()">
      {"".join(f'<option value="{i}">{item["sku"]} — {item["desc"]}</option>' for i, item in enumerate(items))}
    </select>
    <span id="sku-abc-badge" class="badge" style="padding:6px 14px;font-size:14px;"></span>
  </div>
  <div class="chart-grid">
    <div class="chart-box">
      <div class="chart-title">Monthly Demand + 3-MA + Forecast</div>
      <div class="chart-wrap"><canvas id="skuDemandChart"></canvas></div>
    </div>
    <div class="chart-box">
      <div class="chart-title">Seasonal Index by Month</div>
      <div class="chart-wrap"><canvas id="skuSIChart"></canvas></div>
    </div>
  </div>
  <br/>
  <div id="sku-si-grid" class="si-grid"></div>
</div>

<!-- SECTION 4: FORECAST TABLE -->
<div class="section">
  <div class="section-title">04 — 6-Month Forecast (Jan–Jun 2026)</div>
  <div class="tbl-wrap">
    <table>
      <thead><tr>
        <th>SKU</th><th>Description</th><th>Class</th>
        <th>Jan'26</th><th>Feb'26</th><th>Mar'26</th>
        <th>Apr'26</th><th>May'26</th><th>Jun'26</th>
        <th>6M Total</th>
      </tr></thead>
      <tbody>
        {"".join(f'''<tr>
          <td style="color:var(--accent)">{item["sku"]}</td>
          <td style="color:var(--muted)">{item["desc"]}</td>
          <td><span class="badge {item["abc"]}">{item["abc"]}</span></td>
          {"".join(f'<td>{v:,}</td>' for v in item["forecast"])}
          <td style="color:var(--accent3);font-weight:700">{sum(item["forecast"]):,}</td>
        </tr>''' for item in items)}
      </tbody>
    </table>
  </div>
</div>

<footer>
  <div class="fn">Almas <span>Shahriar</span> · IPE BUET '26</div>
  <div class="gen-time">Generated by generate_dashboard.py · {datetime.now().strftime("%Y-%m-%d %H:%M")}</div>
  <div class="flinks">
    <a href="https://www.linkedin.com/in/almasshahriar/" target="_blank">LinkedIn</a>
    <a href="mailto:almasalif123@gmail.com">Email</a>
    <a href="https://github.com/almasshahriar" target="_blank">GitHub</a>
  </div>
</footer>
</div>

<script>
const ITEMS = {items_json};
const MONTHS = {months_json};
const AGG = {agg_json};
const AGG_MA3 = {agg_ma3_json};
const AGG_FC = {agg_fc_json};
const FC_MONTHS = {fc_months_json};

const C = {{
  accent:'#00c2ff', accent2:'#ff6b35', accent3:'#00e5a0',
  warn:'#f59e0b', muted:'#6b7280', border:'rgba(42,47,58,0.8)',
  grid:'rgba(42,47,58,0.5)'
}};

Chart.defaults.color = C.muted;
Chart.defaults.borderColor = C.grid;
Chart.defaults.font.family = "'Share Tech Mono', monospace";
Chart.defaults.font.size = 11;

function baseOpts(title='') {{
  return {{
    responsive:true, maintainAspectRatio:false,
    plugins:{{legend:{{display:true,labels:{{boxWidth:10,padding:16,color:C.muted}}}},tooltip:{{backgroundColor:'#13161b',borderColor:C.border,borderWidth:1,titleColor:C.accent,bodyColor:'#e8eaf0',padding:10}}}},
    scales:{{x:{{grid:{{color:C.grid}},ticks:{{color:C.muted}}}},y:{{grid:{{color:C.grid}},ticks:{{color:C.muted}}}}}}
  }};
}}

// ── AGGREGATE CHART ──
const aggCtx = document.getElementById('aggChart').getContext('2d');
new Chart(aggCtx, {{
  type:'line',
  data:{{
    labels:[...MONTHS, ...FC_MONTHS],
    datasets:[
      {{label:'Actual Demand',data:[...AGG,...Array(6).fill(null)],borderColor:C.accent,backgroundColor:'rgba(0,194,255,0.08)',borderWidth:2,pointRadius:3,fill:true,tension:0.3}},
      {{label:'3-Month MA',data:[...AGG_MA3,...Array(6).fill(null)],borderColor:C.warn,borderWidth:2,borderDash:[4,4],pointRadius:0,tension:0.3}},
      {{label:'Forecast',data:[...Array(12).fill(null),...AGG_FC],borderColor:C.accent3,backgroundColor:'rgba(0,229,160,0.08)',borderWidth:2,borderDash:[6,3],pointRadius:4,pointStyle:'triangle',fill:true,tension:0.3}}
    ]
  }},
  options:baseOpts()
}});

// ── PARETO CHART ──
const paretoCtx = document.getElementById('paretoChart').getContext('2d');
const abcColors = ITEMS.map(i => i.abc==='A'?C.accent3:i.abc==='B'?C.accent:C.muted);
new Chart(paretoCtx, {{
  type:'bar',
  data:{{
    labels:ITEMS.map(i=>i.sku),
    datasets:[
      {{label:'Annual Value ($)',data:ITEMS.map(i=>i.annual_value),backgroundColor:abcColors.map(c=>c+'33'),borderColor:abcColors,borderWidth:1,yAxisID:'y'}},
      {{label:'Cumulative %',data:ITEMS.map(i=>i.cum_pct),type:'line',borderColor:C.accent2,borderWidth:2,pointRadius:2,yAxisID:'y1',tension:0.3}}
    ]
  }},
  options:{{...baseOpts(),scales:{{
    x:{{grid:{{color:C.grid}},ticks:{{color:C.muted}}}},
    y:{{grid:{{color:C.grid}},ticks:{{color:C.muted}},title:{{display:true,text:'Annual Value ($)',color:C.muted}}}},
    y1:{{position:'right',grid:{{drawOnChartArea:false}},min:0,max:100,ticks:{{color:C.muted,callback:v=>v+'%'}},title:{{display:true,text:'Cumulative %',color:C.muted}}}}
  }}}}
}});

// ── ABC DONUT ──
const donutCtx = document.getElementById('abcDonut').getContext('2d');
const cntA={count_a}, cntB={count_b}, cntC={count_c};
new Chart(donutCtx, {{
  type:'doughnut',
  data:{{
    labels:['Class A','Class B','Class C'],
    datasets:[
      {{label:'SKU Count',data:[cntA,cntB,cntC],backgroundColor:['rgba(0,229,160,0.25)','rgba(0,194,255,0.25)','rgba(107,114,128,0.2)'],borderColor:[C.accent3,C.accent,C.muted],borderWidth:2}},
    ]
  }},
  options:{{responsive:true,maintainAspectRatio:false,cutout:'55%',
    plugins:{{legend:{{position:'bottom',labels:{{boxWidth:10,padding:14,color:C.muted}}}},tooltip:{{backgroundColor:'#13161b',borderColor:C.border,borderWidth:1,titleColor:C.accent,bodyColor:'#e8eaf0',padding:10}}}}
  }}
}});

// ── SKU DRILL-DOWN ──
let skuDemandChart, skuSIChart;

function updateSKU() {{
  const idx = parseInt(document.getElementById('skuSelect').value);
  const item = ITEMS[idx];

  // Badge
  const badge = document.getElementById('sku-abc-badge');
  badge.textContent = 'Class ' + item.abc;
  badge.className = 'badge ' + item.abc;

  // Seasonal grid
  const grid = document.getElementById('sku-si-grid');
  grid.innerHTML = MONTHS.map((m,i) => {{
    const v = item.si[i];
    const col = v >= 1.1 ? C.accent3 : v >= 0.95 ? C.accent : C.muted;
    return `<div class="si-cell">
      <div class="si-month">${{m}}</div>
      <div class="si-val" style="color:${{col}}">${{v.toFixed(2)}}</div>
    </div>`;
  }}).join('');

  // Demand chart
  if (skuDemandChart) skuDemandChart.destroy();
  const dc = document.getElementById('skuDemandChart').getContext('2d');
  skuDemandChart = new Chart(dc, {{
    type:'line',
    data:{{
      labels:[...MONTHS,...FC_MONTHS],
      datasets:[
        {{label:'Monthly Demand',data:[...item.monthly,...Array(6).fill(null)],borderColor:C.accent,backgroundColor:'rgba(0,194,255,0.08)',borderWidth:2,pointRadius:3,fill:true,tension:0.3}},
        {{label:'3-Month MA',data:[...item.ma3,...Array(6).fill(null)],borderColor:C.warn,borderWidth:2,borderDash:[4,4],pointRadius:0,tension:0.3}},
        {{label:'Forecast',data:[...Array(12).fill(null),...item.forecast],borderColor:C.accent3,borderWidth:2,borderDash:[6,3],pointRadius:4,fill:false,tension:0.3}}
      ]
    }},
    options:baseOpts()
  }});

  // Seasonal index chart
  if (skuSIChart) skuSIChart.destroy();
  const sc = document.getElementById('skuSIChart').getContext('2d');
  const siColors = item.si.map(v => v >= 1.1 ? C.accent3 + '88' : v >= 0.95 ? C.accent + '88' : C.muted + '55');
  const siBorders = item.si.map(v => v >= 1.1 ? C.accent3 : v >= 0.95 ? C.accent : C.muted);
  skuSIChart = new Chart(sc, {{
    type:'bar',
    data:{{
      labels:MONTHS,
      datasets:[
        {{label:'Seasonal Index',data:item.si,backgroundColor:siColors,borderColor:siBorders,borderWidth:1}},
        {{label:'Baseline (1.0)',data:Array(12).fill(1),type:'line',borderColor:C.accent2,borderWidth:1,borderDash:[4,4],pointRadius:0}}
      ]
    }},
    options:{{...baseOpts(),scales:{{
      x:{{grid:{{color:C.grid}},ticks:{{color:C.muted}}}},
      y:{{grid:{{color:C.grid}},ticks:{{color:C.muted}},min:0.5,max:1.6}}
    }}}}
  }});
}}

updateSKU();
</script>
</body>
</html>"""

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(html)

print("=" * 56)
print("  Demand Dashboard — Generated Successfully")
print("=" * 56)
print(f"  SKUs analysed  : {total_skus}")
print(f"  Total units    : {total_units:,}")
print(f"  Total value    : ${total_value:,.2f}")
print(f"  Class A        : {count_a} SKUs ({val_a}% of value)")
print(f"  Class B        : {count_b} SKUs")
print(f"  Class C        : {count_c} SKUs")
print(f"  Output file    : {OUTPUT_FILE}")
print("=" * 56)
print("  Open output/dashboard.html in your browser.")
print("=" * 56)
