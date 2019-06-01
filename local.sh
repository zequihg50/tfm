#!/bin/bash

# Dataset: https://esg1.umr-cnrm.fr/thredds/catalog/esgcet/27/CMIP6.CMIP.CNRM-CERFACS.CNRM-ESM2-1.historical.r1i1p1f2.AERhr.tas.gr.v20181206.html#CMIP6.CMIP.CNRM-CERFACS.CNRM-ESM2-1.historical.r1i1p1f2.AERhr.tas.gr.v20181206

mkdir -p shared/{original,chunked,zarr}

url='https://esg1.umr-cnrm.fr/thredds/fileServer/CMIP6_CNRM/CMIP/CNRM-CERFACS/CNRM-ESM2-1/historical/r1i1p1f2/AERhr/tas/gr/v20181206/tas_AERhr_CNRM-ESM2-1_historical_r1i1p1f2_gr_185001010030-185412312330.nc'
file="${url##*/}"

if [ ! -f "shared/original/$file" ]; then
  wget -O "shared/original/$file" "$url"
fi

echo "Rechunking..."
time nccopy -d 0 -4 -c "time/2739,lat/8,lon/32" shared/original/"$file" shared/chunked/"$file"

echo "Converting NetCDF to Zarr..."
./netcdf-to-zarr.py
