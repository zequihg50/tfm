## Local

Create your environment:

```bash
name=NAME
conda create -n $name -c conda-forge xarray zarr jupyter matplotlib dask
conda activate $name
pip install h5pyd
```

Set up environment:

```bash
cd notebooks
./local.sh
```

Run jupyter notebook and run `Local.ipynb`.
