# TFM

Notebooks, scripts and figures for the three access methods, local, remote, hpc, are available in the folders with the same name.

Create your environment:

```bash
name=NAME
conda create -n $name -c conda-forge xarray zarr jupyter matplotlib dask nco numcodecs bokeh
conda activate $name
./local.sh # generate data for analysis
```

Run jupyter notebook and run `local/Local.ipynb`.

## Notes for HSDS

```bash
pip install h5pyd
hsload -u USER -p PASS NETCDF DEST
```
