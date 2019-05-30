FROM jupyter/base-notebook:latest

RUN pip install h5py h5pyd
RUN conda install -y dask xarray netcdf4 matplotlib zarr

COPY --chown=jovyan:users notebooks/ /home/$NB_USER/
