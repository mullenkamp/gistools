# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:28:28 2018

@author: MichaelEK
"""
import pandas as pd
import geopandas as gpd
from gistools import util, rec
from gistools.datasets import get_path

pd.options.display.max_columns = 10

####################################
### Parameters

sites_shp = 'flow_recorders_pareora'
rec_streams_shp = 'rec_streams_pareora'
rec_catch_shp = 'rec_catch_pareora'
catch_shp = 'catchment_pareora'

sites_shp_path = get_path(sites_shp)
rec_streams_shp_path = get_path(rec_streams_shp)
rec_catch_shp_path = get_path(rec_catch_shp)
catch_shp_path = get_path(catch_shp)

sites_col_name = 'SITENUMBER'
poly_col_name = 'Catchmen_1'
line_site_col = 'NZREACH'

#######################################
### Tests

pts = util.load_geo_data(sites_shp_path)
pts['geometry'] = pts.geometry.simplify(1)


def test_catch_delineate():
    poly1 = rec.catch_delineate(sites_shp=sites_shp_path, rec_streams_shp=rec_streams_shp_path, rec_catch_shp=rec_catch_shp_path)
#    poly2 = catch_delineate(sites_shp=sites_shp_path, rec_streams_shp=rec_streams_shp_path, rec_catch_shp=rec_catch_shp_path, site_delineate='between')

    assert (round(poly1.area[0]) == 422889430) & (round(poly1.area[1]) == 528523857)



