# Healthcare Analytics Study

This directory contains an independent healthcare analytics study of [CHI-Bench](https://github.com/actava-ai/chi-bench), developed as part of a healthcare data analytics portfolio.

## Study Scope

The analysis examines how CHI-Bench represents complex healthcare workflows across provider, payer, care-management, end-to-end prior authorization, and longitudinal workflow settings.

The study currently covers:

- **Provider Prior Authorization:** 25 workflows
- **Payer Utilization Management:** 25 workflows
- **Care Management:** 25 workflows
- **Prior Authorization E2E:** 23 workflows
- **Marathon:** 3 extended sessions covering 75 underlying task instances

The analysis focuses on workflow structure, documentation burden, policy complexity, scenario characteristics, and task coverage. It does not claim model performance or clinical prevalence.

## Key Findings

### Provider Prior Authorization

- 25 workflows covering 21 distinct condition titles.
- 324 supporting fixtures across the workflow set.
- 199 policy references, averaging 7.96 policy references per workflow.
- Policy references range from 6 to 10 per workflow.
- 17 of 25 workflows (68%) contain at least 8 policy references.

### Payer Utilization Management

- 25 workflows with 111 request documents, averaging 4.44 documents per workflow.
- 199 policy references, averaging 7.96 per workflow.
- Five workflow stages are represented: nurse review, intake, medical-director review, peer-to-peer, and triage.
- 11 of 25 workflows (44%) contain at least 5 request documents.

### Care Management

- 25 workflows covering 22 distinct condition labels.
- Engagement scenarios vary from tentative or cooperative cases to resistant cases.
- 15 of 25 workflows (60%) use the hard-refusal engagement scenario.
- This provides a useful view of workflow complexity beyond documents and policies by introducing patient-engagement variation.

### Prior Authorization E2E

- 23 end-to-end workflows covering 20 distinct condition titles.
- Provider and payer MCP components are enabled across all 23 workflows.
- Agent timeout is configured at 2,700 seconds, reflecting the longer workflow scope.

### Marathon

- Three extended sessions represent provider, payer utilization-management, and care-management workflows.
- The sessions collectively exercise 75 underlying task instances.
- These are existing benchmark task instances exercised through extended sessions, not 75 additional unique cases.

## Analytical Workflow

The analysis follows a reproducible workflow:

1. Inspect CHI-Bench task and workflow metadata.
2. Extract structured metadata into analysis-ready CSV files.
3. Validate counts, categories, policy references, documents, conditions, and workflow configurations.
4. Analyze the resulting datasets using Python and Jupyter notebooks.
5. Generate focused visualizations for workflow complexity and coverage.
6. Document findings and limitations in Markdown reports.

## Repository Artifacts

- data/ — analysis-ready workflow metadata CSV files.
- notebooks/ — five Jupyter notebooks containing the analytical work.
- figures/ — generated visualizations supporting the findings.
- reports/ — Markdown reports for each workflow family.
- scripts/ — metadata extraction and selected visualization scripts.

### Recommended Reading Order

1. This README for the analytical overview.
2. reports/ for concise findings.
3. notebooks/ to inspect the analysis in detail.
4. data/ to review the derived metadata.
5. scripts/ to inspect reproducibility utilities.


## Skills Demonstrated

- Healthcare workflow analysis
- Healthcare data extraction and validation
- Python and pandas
- Jupyter Notebook-based exploratory analysis
- Structured metadata analysis
- Policy and documentation complexity analysis
- Data visualization and analytical reporting
- Reproducible project organization with Git and GitHub

## Limitations and Responsible Interpretation

- CHI-Bench benchmark tasks should not be interpreted as a dataset of unique patients or real-world population prevalence.
- Workflow counts describe benchmark structure and coverage, not clinical frequency.
- Marathon sessions reuse existing benchmark task instances and should not be counted as additional unique cases.
- This portfolio study analyzes benchmark composition and workflow complexity; it does not report model accuracy, clinical effectiveness, or production-system performance.

## Portfolio Context

This analysis is part of a broader healthcare analytics portfolio focused on applying data analysis, SQL, Python, visualization, and healthcare-domain knowledge to realistic healthcare datasets and workflows.
