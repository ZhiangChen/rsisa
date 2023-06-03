

from rsisa.annotation_map_split import Tile_Splitter
from rsisa.annotation_map_split import Dataset
from fiona.crs import from_epsg


# split annotation map without tif map
epsg = 32611  # WGS 84 / UTM zone 11N
crs = from_epsg(epsg)
test_config = {'shapefile_path': "/root/rsisa/data/random_generation/ellipses_100_3_300_1000.shp", 
               'save_dir': "/root/rsisa/data/random_generation/split", 
               'crs':crs, 
               'area_x1':0, 
               'area_y1':0, 
               'area_x2':30, # this should be modified for different shapefiles
               'area_y2':30, 
               'tile_size':10, 
               'overlap':1,
               'tif_path': None, 
               'keep_instance_tif': True}

ts = Tile_Splitter(**test_config)
ts.split()

# split annotation map and tif map. (tif map generated by ellipse_instance_generation.py is fake)
test_config = {'shapefile_path': "/root/rsisa/data/random_generation/ellipses_100_3_300_1000.shp", 
               'save_dir': "/root/rsisa/data/random_generation/split_shp_tif", 
               'crs':crs, 
               'area_x1':0, 
               'area_y1':0, 
               'area_x2':30, # this should be modified for different shapefiles
               'area_y2':30, 
               'tile_size':10, 
               'overlap':1,
               'tif_path': '/root/rsisa/data/random_generation/ellipses_100_3_300_1000.tif', 
               'keep_instance_tif': True}

ts = Tile_Splitter(**test_config)
ts.split()

# crop the study area (remove edges)
test_config = {'shapefile_path': "/root/rsisa/data/random_generation/ellipses_100_3_300_1000.shp", 
               'save_dir': "/root/rsisa/data/random_generation/", 
               'crs':crs, 
               'area_x1':0, 
               'area_y1':0, 
               'area_x2':30, 
               'area_y2':30, 
               'tile_size':40, # just change this to the size of study area. here because the ellipses go slightly than the study area, if we set tile_size of 30, the exceeding part will be split into other tiles. thus we have a large tile_size here.
               'overlap':0,
               'tif_path': None, 
               'keep_instance_tif': True}

ts = Tile_Splitter(**test_config)
ts.split()


# create pickle files for training dataset
ellipse_data = Dataset(pixel_size=1000, split_path='/root/rsisa/data/random_generation/split_shp_tif', input_channel=(0,))

ellipse_data.show(11)
ellipse_data.save_pickles()