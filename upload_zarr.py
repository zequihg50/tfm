#!/usr/bin/env python

import s3fs, zarr, xarray

fs = s3fs.S3FileSystem(
  client_kwargs=dict(endpoint_url='ENDPOINT'),
  anon=False,
  key='KEY',
  secret='SECRET')

store = s3fs.S3Map(root='zarr/tas_AERhr_CNRM-ESM2-1_historical_r1i1p1f2_gr_185001010030-185412312330', s3=fs, check=False)
ds = xarray.open_zarr('dataset/zarr/tas_AERhr_CNRM-ESM2-1_historical_r1i1p1f2_gr_185001010030-185412312330')
#zarr_fs = zarr.open('dataset/zarr/tas_AERhr_CNRM-ESM2-1_historical_r1i1p1f2_gr_185001010030-185412312330', mode='r')
ds.to_zarr(store)

