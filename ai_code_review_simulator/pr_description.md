# Pull Request: Add Automated Code Review Severity Filtering and Risk Score Calculation

## Summary
Implements automated severity filtering and risk score calculation for the Code Review Simulator engine. This feature allows reviewers to filter incoming automated review comments by severity level (low, medium, high, critical) and computes an overall risk score for each submitted Pull Request. Includes new backend utility functions and updated API handling.

## Changes
- **Added `filter_reviews_by_severity()`**: Core logic in `simulator.py` to filter incoming automated feedback items based on specified severity flags.
- **Added `calculate_pr_risk_score()`**: Calculates a weighted risk score (0-100) based on critical issue counts, code churn, and test coverage parameters.
- **Updated API Endpoints**: Enhanced `/api/review/simulate` response payload to include risk metrics and filtered outputs.
- **Added Unit Tests**: Implemented 6 new unit tests in `test_simulator.py` covering severity filtering edge cases and score calculation logic.
- **LOC Impact**: ~140 lines of code added/updated.

## Context
- **Related Issue**: Resolves #18 (Enhance automated risk scoring & noise reduction in AI code review output).
- **Motivation**: Developers needed a way to prioritize critical security and performance warnings while filtering out low-priority style nitpicks in large pull requests.
- **Test Status**: All 12 unit tests (6 existing + 6 new) passed successfully with 100% execution rate.