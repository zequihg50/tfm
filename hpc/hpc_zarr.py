#!/usr/bin/env python
import zarr, numpy
import time
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
nprocs = comm.Get_size()
print(f'rank: {rank}, nprocs: {nprocs}')

store = 'shared/zarr/tas_AERhr_CNRM-ESM2-1_historical_r1i1p1f2_gr_185001010030-185412312330'
ds = zarr.open(store, mode='r')['tas']

if rank == 0:
    start = time.time()

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
    print(f'Value: {v} Time: {end-start}')
