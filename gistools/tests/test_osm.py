# -*- coding: utf-8 -*-
"""
Created on Fri Aug  3 15:28:28 2018

@author: MichaelEK
"""
import pandas as pd
import geopandas as gpd
from gistools import util, osm
from gistools.datasets import get_path

#import osm
#from datasets import get_path
#import requests

pd.options.display.max_columns = 10

####################################
### Parameters

sites_shp = 'flow_recorders_pareora'

sites_shp_path = get_path(sites_shp)

id_col = 'SITENUMBER'

#sites_shp = 'opihi_limit_points'
#
#sites_shp_path = get_path(sites_shp)
#
#id_col = 'Management'

#id_col = 'SITENUMBER'
#gdf_from = pts.copy()
#max_distance=500
#waterway_name=True
#
#n0 = ways1[0]['nodes']
#n1 = 1213916012
#
#osm_nodes_from = res1.copy()

#######################################
### Tests

gdf_from = util.load_geo_data(sites_shp_path)
gdf_from['geometry'] = gdf_from.geometry.simplify(1)

#q1 = get_nearest_waterways(pts.loc[[0]], sites_col_name)
#
#op_endpoint = 'http://hp1802:12345/api/interpreter'
#
#data = b'data=%5Bout%3Ajson%5D%3B%28way%5B%27waterway%27~%27%28river%7Cstream%7Ctidal_channel%29%27%5D%28around%3A500%2C+-44.41173986213191%2C+171.05708873335843%29%3B+node%28around%3A500%2C+-44.41173986213191%2C+171.05708873335843%29%28w%29%3B%29%3Bout+body%3B'


def test_get_nearest():
    pts1 = osm.get_nearest_waterways(gdf_from, id_col)

    assert (len(pts1) == 2) & isinstance(pts1, gpd.GeoDataFrame)

pts1 = osm.get_nearest_waterways(gdf_from, id_col)


def test_get_waterways():
    waterways, nodes = osm.get_waterways(pts1)

    assert (len(waterways) >= 3) & (len(nodes) >= 318)

waterways, nodes = osm.get_waterways(pts1)


def test_waterway_delineation():
    site_delin = osm.waterway_delineation(pts1, waterways, 'between')

    assert (len(site_delin) == 2)

site_delin = osm.waterway_delineation(pts1, waterways, 'between')


def test_to_osm():
    osm_delin = osm.to_osm(site_delin, nodes)

    assert (len(osm_delin) == 2)

osm_delin = osm.to_osm(site_delin, nodes)


def test_to_gdf():
    gdf1 = osm.to_gdf(osm_delin)

    assert (len(gdf1) == 4) & isinstance(gdf1, gpd.GeoDataFrame)


def test_pts_to_waterway_delineation():
    pts1, gdf1 = osm.pts_to_waterway_delineation(gdf_from, id_col, 500, 'natural', 'between')

    assert (len(gdf1) == 4) & isinstance(gdf1, gpd.GeoDataFrame)
