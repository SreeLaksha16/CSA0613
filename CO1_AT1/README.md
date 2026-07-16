# CO1_AT1

## Design and Analysis of Algorithms (DAA)

This repository contains the solutions for the CO1 Assignment. Each question includes the source code, report, and supporting files as required.

---

## Repository Structure

```
CO1_AT1/
│
├── README.md
│
├── Question_21/
│   ├── Source_Code/
│   │   └── master_theorem.c
│   ├── Report/
│   │   ├── Report_Q21.pdf
│   │   ├── Source_Code_Screenshot.png
│   │   ├── Output_Screenshot.png
│   │   └── Analysis_Screenshot.png
│   └── Supporting_Files/
│
└── Question_36/
    ├── Source_Code/
    │   └── search_engine_indexing.c
    ├── Report/
    │   ├── Report_Q36.pdf
    │   ├── Source_Code_Screenshot.png
    │   ├── Output_Screenshot.png
    │   └── Analysis_Screenshot.png
    └── Supporting_Files/
```

---

## Question 21 – Autonomous Vehicle Navigation System

### Problem Statement
Analyze the recurrence relation:

**T(n) = 2T(n/2) + n²**

using the Master Theorem and determine the time complexity.

**Time Complexity:** Θ(n²)

**Space Complexity:** O(log n)

---

## Question 36 – Search Engine Indexing

### Problem Statement
Analyze the recurrence relation:

**T(n) = 2T(n/2) + n²**

using the Master Theorem and explain how indexing time grows as the number of web pages increases.

**Time Complexity:** Θ(n²)

**Space Complexity:** O(log n)

---

## Contents

Each question contains:
- Source Code (.c)
- Report (PDF)
- Source Code Screenshot
- Output Screenshot
- Analysis Screenshot
- Supporting Files (if any)

---

## Conclusion

Both Question 21 and Question 36 are based on the recurrence relation:

**T(n) = 2T(n/2) + n²**

Using the Master Theorem:

- **a = 2**
- **b = 2**
- **f(n) = n²**

Since **f(n)** grows faster than **n^(log₂2)**, **Master Theorem Case 3** applies.

Therefore, the overall time complexity for both problems is:

**Θ(n²)**

---

**Course:** Design and Analysis of Algorithms (DAA)

**Assignment:** CO1_AT1