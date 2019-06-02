# TFM

## Local (1 file)

Create your environment:

```bash
name=NAME
conda create -n $name -c conda-forge xarray zarr jupyter matplotlib dask nco numcodecs bokeh
conda activate $name
./local.sh
```

Run jupyter notebook and run `local/Local.ipynb`.

## Local (full dataset)

```bash
find $(pwd)/original -type f | parallel nccopy -d 0 -4 -c "time/2739,lat/8,lon/32" {} chunked/{/}
```

## Remote

```bash
pip install h5pyd
hsload -u USER -p PASS NETCDF DEST
```
