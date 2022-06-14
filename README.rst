optotrak
++++++++

Read data exported from NDI First Principles. Only tested for use with Optotrak
sensors.


Installation
============

Pip:

.. code::

   pip install optotrak

Conda:

.. code::

   conda install -c otaithleigh optotrak


Usage
=====

Read the example file into a pandas DataFrame:

>>> from optotrak import load_optotrak
>>> load_optotrak('test_optotrak.tsv')
