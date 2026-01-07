# APEPM-pre-QM-geometric-bond-feasibility-screening
This code implements the APEPM model found on chemrxiv, and is intended to ideally be used either as a pre-QM screening method to see if bonds are geometrically possible (not energetically)(if overlap radius = 0, then there can be no bond), or see if a bond is possible at all based on distance between electron radii of 2 atoms. APEPM model paper available here: [10.26434/chemrxiv-2026-bvl0v](https://doi.org/10.26434/chemrxiv-2026-9swcr)


# Please Note:
This model and paper relies on AREECM notation, the code already comes with the digital AREECM dictionary, but for the "+1" rule seen here that applies to AREECM notation, for a better understanding of AREECM, the AREECM paper can be found here on chemrxiv: https://doi.org/10.26434/chemrxiv-2025-jq84z-v3


# Why Industry Should Care

High-throughput QM and DFT workflows often evaluate candidate structures that are geometrically incapable of bonding. These cases are typically identified only after electronic structure calculations have already been performed, resulting in unnecessary computational cost.

APEPM provides a simple geometric check that can be applied before those methods.

# What APEPM Provides

Early identification of geometrically infeasible bonds based on electron cloud overlap

Reduction of wasted QM / DFT calculations on impossible or highly strained structures

Millisecond-scale evaluation, even for large systems

Closed-form, non-iterative calculations with no convergence or numerical tuning

Straightforward integration as a lightweight pre-screening step in existing workflows

# Additionally, APEPM enables:

Geometry-based validation of declared or hypothesized bonds in modified, generated, or user-defined structures

Continuous feasibility feedback under bond stretching, compression, or angular distortion (e.g., during optimization, sampling, or manual editing)

Use as an interpretable geometric constraint layer independent of force fields or energetic models

Real-time applicability in interactive modeling or visualization environments due to its analytic, parameter-free formulation

A clear separation between geometric admissibility and energetic favorability, reducing ambiguity in downstream analysis

# Typical Use
Candidate structure

   ↓
   
APEPM geometric screening

   ↓
   
QM / DFT / ML (applied to feasible geometries)


# Summary

APEPM is a fast, geometry-based screening and interpretive layer that helps identify infeasible bonding configurations early, providing structural context and reducing unnecessary downstream computation.
