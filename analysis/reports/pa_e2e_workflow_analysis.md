# Prior Authorization E2E Workflow Analysis

## Overview

This analysis examines the 23 Prior Authorization End-to-End (E2E) workflows in CHI-Bench.

The E2E workflows represent provider-to-payer prior authorization scenarios. Unlike the provider-only and payer-only workflow families, these tasks expose both provider and payer interfaces and are designed to evaluate the interaction across the two sides of the authorization process.

The analysis uses task instructions and task metadata only. Hidden evaluation artifacts, solution files, and expectation files are not used.

## Dataset Coverage

| Metric | Result |
|---|---:|
| E2E workflows | 23 |
| Distinct condition titles | 20 |
| Provider MCP available | 23/23 (100%) |
| Payer MCP available | 23/23 (100%) |
| Verifier timeout | 1,200 sec |
| Agent timeout | 2,700 sec |

All 23 workflows provide access to both provider and payer MCP interfaces.

## Condition Diversity

The 23 workflows cover 20 distinct condition titles.

Three conditions occur twice:

- Obstructive sleep apnea — 2
- Headache — 2
- Rheumatoid arthritis — 2

The remaining 17 condition titles occur once each.

This provides broad clinical scenario coverage while retaining a small number of repeated conditions across the E2E workflow set.

## Workflow Structure

The defining characteristic of the E2E workflow family is the presence of both provider-side and payer-side interfaces.

| Capability | Workflows | Coverage |
|---|---:|---:|
| Provider MCP | 23 | 100% |
| Payer MCP | 23 | 100% |

This distinguishes the E2E workflows from single-actor provider and payer workflows.

The structure supports analysis of cross-role coordination rather than isolated work performed by only one side of the prior authorization process.

## Execution Requirements

All 23 E2E workflows use the same timeout configuration:

- Verifier timeout: **1,200 seconds**
- Agent timeout: **2,700 seconds**

The 2,700-second agent timeout is three times the 900-second timeout used by the provider and payer workflow families.

This longer execution allowance is consistent with the broader scope of an end-to-end workflow involving interactions across provider and payer roles.

## Key Findings

### 1. Cross-role workflow design

All 23 E2E tasks expose both provider and payer MCP interfaces.

This makes the E2E family structurally different from provider-only and payer-only prior authorization workflows and provides a benchmark setting for evaluating cross-role workflow execution.

### 2. Broad condition coverage

The E2E workflow set contains 20 distinct condition titles across 23 workflows.

The repeated conditions are:

- Obstructive sleep apnea
- Headache
- Rheumatoid arthritis

Each appears twice, while the remaining conditions appear once.

### 3. Higher execution allowance

The E2E workflows provide a 2,700-second agent timeout, compared with 900 seconds for the provider and payer workflow families.

This gives E2E agents three times the execution window and reflects the additional scope of cross-role workflow execution.

### 4. Consistent environment configuration

Every E2E workflow has the same provider/payer MCP availability and timeout configuration.

This consistency makes workflow structure and condition diversity the primary observable differences within this task family.

## Portfolio Interpretation

From a healthcare analytics perspective, the E2E workflow family is useful for studying how AI systems handle processes that cross organizational and functional boundaries.

A prior authorization process can require information to move from clinical documentation on the provider side to utilization-management decision-making on the payer side. An E2E benchmark therefore evaluates more than isolated clinical reasoning: it also tests workflow coordination, information transfer, and role-specific tool use.

These findings describe the structure of the CHI-Bench benchmark and should not be interpreted as real-world prevalence of diseases, payer behavior, or clinical workflow frequency.

## Limitations

This analysis is based on benchmark task metadata and task instructions.

It does not measure:

- Agent accuracy
- Benchmark scores
- Clinical outcomes
- Real-world prior authorization performance
- Patient prevalence
- Payer approval rates in actual healthcare settings

The 23 E2E workflows are benchmark workflow entries and should not be interpreted as 23 unique patients.

## Conclusion

The CHI-Bench Prior Authorization E2E subset contains 23 provider-to-payer workflows covering 20 distinct condition titles.

Its defining structural feature is dual access to provider and payer MCP interfaces across all workflows. The E2E tasks also receive a substantially larger agent execution window than the single-role prior authorization workflows.

Together, these characteristics make the E2E subset a useful benchmark component for studying AI performance in multi-role healthcare workflow coordination.