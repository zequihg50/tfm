#!/usr/bin/env python
import time
import dask, xarray, zarr

zarr.storage.default_compressor = None

i = 'shared/original/tas_AERhr_CNRM-ESM2-1_historical_r1i1p1f2_gr_185001010030-185412312330.nc'
o = 'shared/zarr/tas_AERhr_CNRM-ESM2-1_historical_r1i1p1f2_gr_185001010030-185412312330'

start = time.time()
ds = xarray.open_dataset(i, engine='netcdf4')
end1 = time.time()

# this will create a zarr array with the following chunking: {'time': 2739, 'lat': 8, 'lon': 32}
ds.to_zarr(o)
end2 = time.time()

print('Time to open: {}. Time to save: {}.'.format(end1 - start, end2 - start))