Usage project Sales
============================


# ``read_data(file)``
# ``report(file,report)``

Example usage
-------------

.. code-block:: python

    from sales import read_data, report

    data = read_data("sales.csv")
    report(data, "report.txt")