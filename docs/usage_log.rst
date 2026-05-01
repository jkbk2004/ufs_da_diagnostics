JEDI Log Diagnostics
====================

The log diagnostics subsystem parses a full JEDI variational DA log file
and produces a comprehensive text report summarizing:

- Configuration metadata (cost type, analysis time, resolutions)
- Observation counts (loaded, total, assimilated, per-variable)
- Jo/n evolution across outer loops
- Cost-function convergence (J, Jb, JoJc)
- Departures (Min/Max/RMS)
- Observation error statistics
- Chi-squared consistency diagnostics

This tool is designed for FV3-JEDI DA workflows and provides a compact,
human-readable summary suitable for DA monitoring and experiment comparison.


Overview
--------

The log parser reads a single JEDI log file and extracts structured
diagnostic information using pattern-based parsing. The output is a
multi-section text report that can be printed to the terminal or saved
to a file.

The parser is robust to ordering differences across JEDI versions and
supports all standard variational DA logs (3DVar, 4DVar, hybrid).


Command-Line Usage
------------------

The CLI entry point is:

.. code-block:: bash

    ufsda-parse-jedi-log <jedi_log_file> [--output report.txt]

Examples:

.. code-block:: bash

    # Print report to terminal
    ufsda-parse-jedi-log jedi.log

    # Save report to a file
    ufsda-parse-jedi-log jedi.log --output diag_report.txt


YAML-Free Operation
-------------------

Unlike other diagnostics subsystems, the log parser does **not** require
a YAML configuration file. All information is extracted directly from
the JEDI log.


Report Structure
----------------

The generated report contains the following sections:

1. **Configuration Summary**
   - Cost type
   - Analysis datetime
   - Time window begin/length
   - Outer and inner resolutions
   - Number of vertical levels
   - Static and ensemble weights
   - Ensemble size
   - Minimizer algorithm
   - Inner-loop structure

2. **Observation Counts**
   - Loaded locations (nlocs)
   - Total obs before QC
   - Assimilated obs (used in Jo)
   - Rejected obs
   - Assimilation percentage
   - Per-variable counts (e.g., AMSUA brightness temperatures)

3. **Jo/n Evolution**
   - Jo/n for each obs type across outer loops
   - Total Jo reduction percentage

4. **Cost Function Convergence**
   - J, Jb, JoJc for each inner iteration
   - Grouped by outer loop

5. **Chi-Squared Consistency**
   - Jo, P, Jo/P for each obs type
   - Calibration status (OK, R too large, R too small)

6. **Departures**
   - Min, Max, RMS for each obs type/variable

7. **Observation Error Statistics**
   - Min, Max, RMS of diagonal R entries


Example Output (Excerpt)
------------------------

Below is a shortened example of the generated report:

.. code-block:: text

    ================================================================================
      JEDI Variational DA - Diagnostic Report
    ================================================================================
    
    ----------------------------------------
      1. CONFIGURATION SUMMARY
    ----------------------------------------
      Cost Type                     : 3D-Var
      Analysis Time                 : 2024-01-01T00:00:00Z
      Outer Resolution              : C96
      Inner Resolution              : C48
      Ensemble Members              : 80
      Minimizer                     : DRIPCG
    
    ----------------------------------------
      2. OBSERVATION COUNTS
    ----------------------------------------
      Obs Type                     Locations   Total Obs   Assimilated   Rejected   Assim%
      AMSUA                         12,345      98,765       95,432        3,333     96.6%
        +-- brightness_temperature                95,432
    
    ----------------------------------------
      3. Jo/n EVOLUTION ACROSS OUTER ITERATIONS
    ----------------------------------------
      Obs Type                     Outer 0     Outer 1       Delta
      AMSUA                         1.2345     0.9876      -0.2469


Python API Usage
----------------

The parser can also be used programmatically:

.. code-block:: python

    from ufs_da_diagnostics.log.parse_jedi_log import (
        parse_configuration,
        parse_obs_counts,
        parse_jo_evolution,
        parse_cost_convergence,
        parse_departures,
        parse_obs_errors,
        generate_report,
    )

    with open("jedi.log") as f:
        lines = f.readlines()

    config = parse_configuration(lines)
    obs_counts = parse_obs_counts(lines)
    jo_data, jo_total = parse_jo_evolution(lines)
    convergence = parse_cost_convergence(lines)
    departures = parse_departures(lines)
    obs_errors = parse_obs_errors(lines)

    report = generate_report(
        config, obs_counts, jo_data, jo_total,
        convergence, departures, obs_errors
    )

    print(report)


File Locations
--------------

The log parser is implemented in:

``ufs_da_diagnostics/log/parse_jedi_log.py``

The CLI entry point is defined in ``pyproject.toml`` under:

``ufsda-parse-jedi-log``


See Also
--------

- :doc:`../api/log`
- :doc:`../usage_increment`
- :doc:`../usage_obs`
- :doc:`../usage_spectra`
