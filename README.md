# TFM

## Local

Create your environment:

```bash
name=NAME
conda create -n $name -c conda-forge xarray zarr jupyter matplotlib dask nco numcodecs bokeh
conda activate $name
#pip install h5pyd
./local.sh
```

Run jupyter notebook and run `Local.ipynb`.
