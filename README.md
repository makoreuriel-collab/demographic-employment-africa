# 👥 Demographics & Youth Employment in Africa

> Examining the gap between Africa's rapidly growing youth population and the continent's capacity to generate formal employment — one of the defining development challenges of the coming decades.

---

## Overview

Africa has the world's youngest and fastest-growing population. By 2040, there will be more than 600 million young people aged 15–24 on the continent. That's a potential demographic dividend — but only if labour markets, education systems, and private investment can keep pace.

Right now, they aren't. Formal job creation falls well short of what's needed to absorb new labour market entrants, and youth unemployment in several countries is critically high. This project uses World Bank and ILO data to visualise the relationship between population growth and youth unemployment, and projects the growing gap between Africa's youth population and formal employment capacity through 2040.

---

## Objective

- Compare **youth unemployment rates** and **population growth rates** across 12 African economies
- Project the divergence between **Africa's youth population** and estimated **formal job creation** to 2040
- Identify which countries face the most acute demographic-employment mismatch

---

## Tools

| Tool | Purpose |
|------|---------|
| Python 3.x | Core language |
| pandas | Data manipulation |
| matplotlib | Visualisation |

---

## Data Sources

**World Bank – World Development Indicators (WDI)**
- Youth unemployment rate (% of youth labour force): [`SL.UEM.1524.ZS`](https://data.worldbank.org/indicator/SL.UEM.1524.ZS)
- Population growth (annual %): [`SP.POP.GROW`](https://data.worldbank.org/indicator/SP.POP.GROW)

**ILO – World Employment and Social Outlook**
- Formal employment estimates: [ilo.org/weso](https://www.ilo.org/global/research/global-reports/weso/en/)

Time-series projections based on World Bank and UNDP population forecasts.

---

## How to Run

```bash
pip install pandas matplotlib
python analysis.py
```

Chart is saved to `outputs/demographic_employment_analysis.png`.

---

## Key Findings

- **South Africa** has a youth unemployment rate of **63.9%** — a structural crisis shaped by skills mismatches, spatial inequality, and persistent apartheid-era economic legacies
- Africa's average youth unemployment of **~18%** hides huge variation: Ethiopia sits at 3.5% (informal agriculture absorbs most youth), while South Africa approaches 64%
- **Tanzania and Rwanda**, among the fastest-growing populations in the sample, have limited formal job absorption capacity — most new entrants flow into low-productivity informal work
- By 2040, the **formal employment gap is projected to exceed 475 million** — the difference between the youth population and the jobs being created

---

## Why This Matters for Development Finance

The **AfDB's Jobs for Youth in Africa strategy** aims to create 25 million jobs per year — and this data shows exactly why that target is so urgent. DFIs use this kind of demographic and labour market analysis to identify which sectors should receive investment (agribusiness, light manufacturing, digital economy), where skills development funding is needed most, and how to frame private sector engagement around job creation outcomes.

---

## Output

![Demographics & Employment Chart](outputs/demographic_employment_analysis.png)

---

*Part of a four-project portfolio analysing Africa's development challenges, aligned with the African Development Bank's Four Cardinal Points.*
