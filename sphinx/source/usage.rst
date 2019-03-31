How to use gistools
===================

This section will describe how to use the gistools package. The gistools functions depend heavily on the GeoPandas package. Nearly all outputs are either as Pandas DataFrames or GeoPandas GeoDataFrames.

Import base module
------------------
Import the base modules and necessary parameters for the examples.

.. code:: python

    import gistools

    ####################################
    ### Parameters

    sites_shp = 'flow_recorders_pareora'
    rec_streams_shp = 'rec_streams_pareora'
    rec_catch_shp = 'rec_catch_pareora'
    catch_shp = 'catchment_pareora'

    sites_shp_path = gistools.datasets.get_path(sites_shp)
    rec_streams_shp_path = gistools.datasets.get_path(rec_streams_shp)
    rec_catch_shp_path = gistools.datasets.get_path(rec_catch_shp)
    catch_shp_path = gistools.datasets.get_path(catch_shp)

    sites_col_name = 'SITENUMBER'
    poly_col_name = 'Catchmen_1'
    line_site_col = 'NZREACH'

.. ipython:: python
   :suppress:

   import gistools

   ####################################
   ### Parameters

   sites_shp = 'flow_recorders_pareora'
   rec_streams_shp = 'rec_streams_pareora'
   rec_catch_shp = 'rec_catch_pareora'
   catch_shp = 'catchment_pareora'

   sites_shp_path = gistools.datasets.get_path(sites_shp)
   rec_streams_shp_path = gistools.datasets.get_path(rec_streams_shp)
   rec_catch_shp_path = gistools.datasets.get_path(rec_catch_shp)
   catch_shp_path = gistools.datasets.get_path(catch_shp)

   sites_col_name = 'SITENUMBER'
   poly_col_name = 'Catchmen_1'
   line_site_col = 'NZREACH'


General vector tools
---------------------
A utility function provides a similar function to the GeoPandas read_file, but also works with pdsql.

.. ipython:: python

    pts = gistools.util.load_geo_data(sites_shp_path)
    pts['geometry'] = pts.geometry.simplify(1)

Converting a DataFrame with x and y coordinates to a GeoDataFrame:

.. ipython:: python

    pts_df = pts[[sites_col_name, 'geometry']].copy()
    pts_df['x'] = pts_df.geometry.x
    pts_df['y'] = pts_df.geometry.y
    pts_df.drop('geometry', axis=1, inplace=True)

    pts3 = gistools.vector.xy_to_gpd(sites_col_name, 'x', 'y', pts_df)

Selecting points from within a polygon:

.. ipython:: python

    pts1 = gistools.vector.sel_sites_poly(sites_shp_path, rec_catch_shp_path, buffer_dis=10)

Joining the attributes of a polygon to points:

.. ipython:: python

    pts2, poly2 = gistools.vector.pts_poly_join(sites_shp_path, catch_shp_path, poly_col_name)

Find the closest line segment to points:

.. ipython:: python

    line1 = gistools.vector.closest_line_to_pts(sites_shp_path, rec_streams_shp_path, line_site_col, buffer_dis=100)

Catchment delineation of NIWA REC network
-----------------------------------------
There are several functions that build to the final catch_delineate function. I will only provide an example of the final catchment delineation function. For each point, a polygon is created to represent the delineated catchment above that point.

.. ipython:: python

    poly1 = gistools.rec.catch_delineate(sites_shp_path, rec_streams_shp_path, rec_catch_shp_path, sites_col=sites_col_name, buffer_dis=400)
