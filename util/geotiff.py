
import rasterio
from rasterio.plot import show
#fp = r'/Users/davidjones/Downloads/SKYWATCH_S2_MS_20200416T0208_TC_Tile_0_0_2K3eZmYj.tif'
fp = r'/Users/davidjones/Downloads/SKYWATCH_S2_MS_20250227T0002_ALL_Tile_0_0_c3d5 (1).tif'
img = rasterio.open(fp)
show(img)