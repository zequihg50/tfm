FROM jupyter/base-notebook:latest

RUN pip install h5pyd
RUN conda install -y dask xarray netcdf4 matplotlib zarr bokeh h5netcdf s3fs

COPY --chown=jovyan:users notebooks/ /home/$NB_USER/
