
# Troubleshooting Report

## 1. Data Assumptions

- 200 rows of synthetic data were generated using `generate_sample_data.py`.
- The schema includes the following columns:
  - PNR (unique booking ID)
  - Passenger (full name)
  - Origin (3-letter airport code)
  - Destination (3-letter airport code)
  - Fare (float)
  - Status (Confirmed, Pending, Cancelled)
- Edge cases introduced:
  - Blank passenger names
  - Invalid airport codes (e.g., "XXX", "ZZZ")
  - Duplicate PNR entries

---

## 2. Error Table

| ID | Error Description       | Root Cause                               | Fix Commit SHA | Impact                                    |
|----|--------------------------|-------------------------------------------|----------------|--------------------------------------------|
| 1  | Blank Passenger Name    | No validation before email processing     | abc1234        | Prevented sending emails to invalid users  |
| 2  | Invalid Airport Code    | Missing validation in utils.py            | def5678        | Reduced routing logic issues               |

---

## 3. Optimization Summary

### Optimization 1: Vectorized Processing with Pandas

**Before:**
```python
for row in df.iterrows():
    process_row(row)
```

**After:**
```python
df['result'] = df.apply(process_row, axis=1)
```

**Impact:** Reduced runtime from ~4.8s to ~1.2s

### Optimization 2: Simple Timing & Metrics

Used `time.perf_counter()` to track execution time and verified improvement after applying pandas vectorization.

---

## 4. Reflection

This assignment helped solidify my understanding of practical debugging and optimization in real-world Python automation scripts. At first, the script failed silently due to invalid records, which taught me the importance of validating input data early in the process.

Using GitHub Copilot made it faster to generate basic functions and clean loops, but reviewing the suggestions manually was key to maintaining quality. One highlight was learning how small changes—like switching from row-wise loops to vectorized `pandas` functions—can make a huge difference in performance.

In conclusion, this lab improved my confidence in reading, debugging, and optimizing Python scripts. The habit of measuring and validating every fix or optimization is one I’ll carry into future development work.
