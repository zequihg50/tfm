#!/usr/bin/env python
import netCDF4, numpy
import time
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()
#print(f'rank: {rank}, nprocs: {nprocs}')

dataset = '/gpfs/users/ecimadevilla/tfm/shared/chunked/tas_AERhr_CNRM-ESM2-1_historical_r1i1p1f2_gr_185001010030-185412312330.nc'
nDataset = netCDF4.Dataset(dataset, mode='r', parallel=True)
ds = nDataset['tas']
ds.set_collective(True) # without this the test takes much more time

step = ds.shape[0]/nprocs + 1
i = int(rank * step)
j = int(i + step)

if rank == nprocs-1:
    j = ds.shape[0]

print(f'rank {rank} from {i} to {j}')

comm.Barrier()
start = time.time()
data = ds[i:j,:,:].sum(axis=0)

results = comm.gather(data, root=0)

if rank == 0:
    v = sum(results).mean() # Just to be sure that value is consistent
    end = time.time()
    print(f'Value: {v} nprocs: {nprocs} Time: {end-start}')

comm.Barrier()
nDataset.close()
