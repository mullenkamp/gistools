How to use gistools
===================

This section will describe how to use the gistools package. The gistools functions depend heavily on the GeoPandas package. Nearly all outputs are either as Pandas DataFrames or GeoPandas GeoDataFrames.

Import base module
------------------

.. code:: python

    import gistools
    import pandas as pd

.. ipython:: python
   :suppress:

   import gistools
   import pandas as pd

General vector
---------------------
The input data can be read into the class at initiatisation or via the param_est function.

We first need to get an example dataset and read it in via pd.read_csv.

.. ipython:: python

    ex1_path = datasets.get_path('example1')
    tsdata = pd.read_csv(ex1_path, parse_dates=True, infer_datetime_format=True, index_col='date')
    tsdata.head()

Now we can run the parameter estimation using the newly loaded in dataset using the default parameters.

.. ipython:: python

    et1.param_est(tsdata)
    et1.ts_param.head()


Calculate ETo
-------------
Now it's just a matter of running the specific ETo function. For example, the FAO ETo.

.. ipython:: python

    eto1 = et1.eto_fao()
    eto1.head()
