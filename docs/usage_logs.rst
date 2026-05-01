JEDI Log Tools
==============

This page describes the log‑parsing utilities included in
``ufs-da-diagnostics``. These tools extract useful information from
FV3‑JEDI run logs, including iteration summaries, cost‑function
components, and QC statistics.


Basic Usage
-----------

To parse a JEDI log:

.. code-block:: python

    from ufs_da_diagnostics.logs.log_parser import LogParser

    parser = LogParser("jedi.log")
    summary = parser.extract_iteration_summary()

    print(summary)


Available Functions
-------------------

- ``extract_iteration_summary()``  
  Returns iteration number, cost function values, and convergence info.

- ``extract_qc_summary()``  
  Summarizes QC pass/fail counts by observation type.

- ``extract_timing()``  
  Reports wall‑clock timing for major JEDI components.


Example
-------

.. code-block:: python

    parser = LogParser("jedi.log")
    qc = parser.extract_qc_summary()
    print(qc)


Notes
-----

- The parser is robust to multi‑line log entries.
- Missing fields are skipped gracefully.
- Output is returned as Python dictionaries for easy downstream use.
