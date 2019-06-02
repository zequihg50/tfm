#!/usr/bin/env python
import sys,time
import dask, xarray, zarr

zarr.storage.default_compressor = None

i = sys.argv[1]
o = sys.argv[2]

ds = xarray.open_dataset(i, engine='netcdf4')
# this will create a zarr array with the following chunking: {'time': 2739, 'lat': 8, 'lon': 32}
ds.to_zarr(o)
