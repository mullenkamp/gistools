# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:28:28 2018

@author: MichaelEK
"""
import os
import pandas as pd
import geopandas as gpd
from gistools import util, rec
# from gistools.datasets import get_path

pd.options.display.max_columns = 10

####################################
### Parameters

data_dir = os.path.join(os.path.split(os.path.realpath(os.path.dirname(__file__)))[0], 'datasets', 'shapefiles')

sites_shp = 'flow_recorders_pareora.shp'
rec_streams_shp = 'rec_streams_pareora.shp'
rec_catch_shp = 'rec_catch_pareora.shp'
catch_shp = 'catchment_pareora.shp'

sites_shp_path = os.path.join(data_dir, sites_shp)
rec_streams_shp_path = os.path.join(data_dir, rec_streams_shp)
rec_catch_shp_path = os.path.join(data_dir, rec_catch_shp)
catch_shp_path = os.path.join(data_dir, catch_shp)

sites_col_name = 'SITENUMBER'
poly_col_name = 'Catchmen_1'
line_site_col = 'NZREACH'

#######################################
### Tests

pts = util.load_geo_data(sites_shp_path)
pts['geometry'] = pts.geometry.simplify(1)


def test_catch_delineate():
    poly1 = rec.catch_delineate(sites=sites_shp_path, rec_streams=rec_streams_shp_path, rec_catch=rec_catch_shp_path, stream_order_col='ORDER', segment_id_col='NZREACH', from_node_col='NZFNODE', to_node_col='NZTNODE')

    assert (round(poly1.area[0]) > 420000000) & (round(poly1.area[1]) > 520000000)
