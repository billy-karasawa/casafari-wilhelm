# Data operations cost structure (26 Oct 2026)

**Goal:** current monthly cost of data collection & processing, split by pipeline
(A DQA research/job creation · B DC parsers · C crawling · D ingestion/processing "MVP"),
by country and by residential/commercial — to support rebuilding data ops as one agent per pipeline.
Billy asked to run it "in a cheap way – smallest possible model without loss of quality".

**Inputs:** payroll xlsx (DQA & DC), DQA new-source & fix-job CSVs, DC jobs-by-status CSV,
crawling settings xlsx (~8,900 sources), Drive folder `15beyh7kd1h0Qdg5LP6tcNcOKRyYT4-sl`
(Oxylabs SoW + invoices, BrightData order form + invoices, `gcp costs.xlsx`).

**Result: €43,899 / month**

| Line | €/month |
|---|---|
| A new-source | 2,256 |
| A fix | 9,061 |
| B1 new build | 171 |
| B2 maintenance | 9,916 |
| C Proxy IPs | 6,354 |
| C Unblocker services | 9,744 |
| D servers | 4,056 |
| D people | 2,341 |

Crawling contract floor ≈ €16.1k/month (BrightData $9.5k commit; Oxylabs €8k minimum).
Top countries by cost: FR, DE, ES, PT, IT. Unit costs: ~€58.60/new-source job, ~€48.76/fix job (A);
~€3.99/counted DC job, €5.00/done job (B).

**Decisions by Billy:** monthly not annual; FX 1.17 USD/EUR placeholder; listings as country×type proxy
for crawling; leavers' jobs carry no cost; GCP column C → D; no "AI" wording for crawling (use invoice
terms); DC closed rule (only config-change + fixed-comment jobs count — removed 21,134 auto-closed jobs).

**Open:** D people is a floor (DS/platform staff not in payroll); 49 new jobs on closed rows excluded
(unconfirmed); Netnut/Zenrows/GoProxies costs unknown; files never uploaded to Drive.

**Output:** `data_ops_cost_structure.xlsx` + summary md, sent as chat attachments (v4 final).
