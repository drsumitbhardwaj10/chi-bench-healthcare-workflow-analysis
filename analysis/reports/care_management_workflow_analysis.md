\# Care Management Workflow Analysis



\## 1. Objective



This analysis examines the structure of the Care Management domain in CHI-Bench, with a focus on workflow coverage, condition-label diversity, engagement scenarios, and task configuration.



The objective is to understand the benchmark's healthcare workflow design and identify characteristics relevant to healthcare analytics and workflow automation.



This is a benchmark-structure analysis and does not evaluate model performance.



\---



\## 2. Scope



The analysis covers all 25 Care Management workflow entries in:



`data/care\_management/tasks/`



The analysis was derived from task instructions and task configuration metadata.



Hidden evaluation artifacts, including solutions, tests, expectations, rubrics, and canonical evaluation records, were not used for the analytical conclusions.



\---



\## 3. Dataset-Level Metrics



| Metric | Value |

|---|---:|

| Care Management workflows | 25 |

| Distinct condition labels | 22 |

| Verifier timeout | 1,200 seconds |

| Agent timeout | 900 seconds |



All 25 workflows use the same configured verifier and agent timeout values.



\---



\## 4. Engagement Scenario Distribution



The 25 workflows cover six engagement scenarios:



| Engagement scenario | Workflows | Share |

|---|---:|---:|

| hard\_refuses | 15 | 60% |

| moderate\_anxious | 4 | 16% |

| low\_coop | 2 | 8% |

| moderate\_tentative | 2 | 8% |

| low\_tentative | 1 | 4% |

| moderate\_reluctant | 1 | 4% |



The `hard\_refuses` scenario is the largest category, representing 15 of the 25 workflows.



The remaining 10 workflows are distributed across five other engagement scenarios.



These labels describe benchmark scenario construction and should not be interpreted as estimates of real-world patient behavior or prevalence.



\---



\## 5. Condition Coverage



The benchmark contains 22 distinct condition labels across 25 workflows.



Most condition labels occur once. Two labels are repeated:



\- `dm` — 3 workflows

\- `mdd` — 2 workflows



The `dm` workflows cover three different engagement scenarios:



\- `hard\_refuses`

\- `low\_coop`

\- `moderate\_anxious`



The `mdd` workflows cover:



\- `hard\_refuses`

\- `moderate\_reluctant`



This structure provides repeated condition labels with different engagement scenarios, allowing the benchmark to represent variation in workflow context without treating the condition itself as the only defining factor.



\---



\## 6. Multi-Condition Workflow Labels



Three workflow labels explicitly represent combinations of conditions:



\- `complex\_esrd\_dm`

\- `complex\_hf\_afib\_ckd`

\- `complex\_parkinson\_dep`



These cases add multi-condition complexity to the Care Management domain and complement the workflows represented by single-condition labels.



The analysis does not infer clinical severity or patient-level outcomes from these labels.



\---



\## 7. Workflow Perspective



The Care Management task instructions describe a workflow involving:



1\. Care-management intake

2\. Chart review

3\. Patient outreach

4\. Assessment

5\. Finalized care-plan creation



The benchmark therefore represents a workflow-oriented healthcare automation scenario rather than a simple question-answering task.



The task instructions also specify that structured fields should be grounded in chart or outreach evidence and that consent should only be marked as obtained after the relevant consent process has actually occurred.



These requirements emphasize documentation accuracy, evidence grounding, and workflow completion.



\---



\## 8. Key Observations



Several structural characteristics stand out:



\- The domain contains 25 workflows spanning 22 condition labels.

\- Engagement scenarios are deliberately varied, with six different scenario categories.

\- `hard\_refuses` accounts for 60% of the workflows.

\- Diabetes (`dm`) is represented across three different engagement scenarios.

\- Major depressive disorder (`mdd`) is represented across two engagement scenarios.

\- Three workflows explicitly combine multiple conditions.

\- All workflows use the same 1,200-second verifier timeout and 900-second agent timeout.

\- The benchmark combines clinical-condition context with interaction and engagement scenarios.



Overall, the domain is structured to test workflow completion under different care-management interaction conditions rather than simply testing disease-specific knowledge.



\---



\## 9. Interpretation for Healthcare Analytics



From a healthcare analytics perspective, the Care Management domain provides a useful example of workflow-oriented healthcare data.



Potential analytics themes include:



\- Workflow completion tracking

\- Outreach activity monitoring

\- Care-plan documentation

\- Engagement-scenario classification

\- Condition and workflow segmentation

\- Multi-condition case identification

\- Documentation quality monitoring

\- Care-coordination process analysis



These are relevant to healthcare operations, care management, utilization management, and clinical workflow analytics.



The benchmark structure can therefore complement traditional claims or utilization datasets by illustrating how structured workflow states and interaction scenarios can be represented in healthcare automation systems.



\---



\## 10. Limitations



This analysis has several important limitations:



1\. The 25 workflows are benchmark tasks and are not a population sample.

2\. Condition-label counts should not be interpreted as disease prevalence.

3\. Engagement-scenario counts should not be interpreted as patient-behavior statistics.

4\. The analysis does not measure agent accuracy or benchmark performance.

5\. Hidden evaluation artifacts were intentionally excluded.

6\. The analysis is based on task metadata and instructions rather than real-world healthcare utilization data.

7\. Condition labels are benchmark identifiers and may represent simplified or combined workflow categories.



\---



\## 11. Reproducibility



\### Source data



`analysis/data/care\_management\_task\_metadata.csv`



\### Extraction script



`analysis/scripts/extract\_care\_management\_metadata.py`



\### Notebook



`analysis/notebooks/03\_care\_management\_workflow\_analysis.ipynb`



\### Visualization



`analysis/figures/care\_management\_engagement\_scenarios.png`



\### Scope



The analysis covers all 25 Care Management workflow entries.



The extraction and analysis use task identifiers, instruction metadata, engagement-scenario labels, condition labels, and task configuration metadata.



Hidden evaluation artifacts such as solutions, tests, expectations, rubrics, and canonical evaluation records were not used for the analytical conclusions.



\---



\## 12. Project Relevance



The Care Management analysis complements the provider-side and payer-side prior authorization analyses by adding a care-coordination workflow perspective.



The benchmark describes a workflow involving care-management intake, outreach, assessment, and finalized care-plan creation. This makes the domain relevant to healthcare analytics use cases involving workflow monitoring, care coordination, documentation quality, outreach tracking, and structured care-plan generation.



Together, the provider, PA-UM, and Care Management analyses provide three distinct views of healthcare workflow automation within CHI-Bench while keeping benchmark structure separate from model-performance evaluation.



\---



\## 13. Conclusion



The Care Management domain provides 25 structured healthcare workflow tasks covering 22 condition labels and six engagement scenarios.



Its design emphasizes care-management workflow completion, evidence-grounded documentation, patient outreach, assessment, and care-plan generation.



For this project, the analysis establishes the Care Management domain as a complementary component of the broader CHI-Bench workflow analysis alongside provider-side referral and payer-side utilization-management workflows.

