# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:28:28 2018

@author: MichaelEK
"""
import os
import pandas as pd
import geopandas as gpd
from gistools import util, rec

pd.options.display.max_columns = 10

####################################
### Parameters

base_dir = os.path.realpath(os.path.dirname(__file__))

sites_shp = 'flow_recorders_pareora.shp'
rec_streams_shp = 'rec_streams_pareora.shp'
rec_catch_shp = 'rec_catch_pareora.shp'
catch_shp = 'catchment_pareora.shp'

sites_shp_path = os.path.join(base_dir, sites_shp)
rec_streams_shp_path = os.path.join(base_dir, rec_streams_shp)
rec_catch_shp_path = os.path.join(base_dir, rec_catch_shp)
catch_shp_path = os.path.join(base_dir, catch_shp)

sites_col_name = 'SITENUMBER'
poly_col_name = 'Catchmen_1'
line_site_col = 'NZREACH'

#######################################
### Tests

pts = util.load_geo_data(sites_shp_path)
pts['geometry'] = pts.geometry.simplify(1)


def test_catch_del():
    poly1 = rec.catch_del(sites_shp_path, rec_streams_shp_path, rec_catch_shp_path, sites_col=sites_col_name, buffer_dis=400)
    poly1.area

    assert (round(poly1.area[0]) == 422889430) &(round(poly1.area[1]) == 527399098)



