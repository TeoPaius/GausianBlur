#!/usr/bin/env python
"""
Parallel Hello World
"""
import math
from mpi4py import MPI
from Core import Core
import numpy as np
import cv2

# MPI
nrProcs = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
# nrProcs = 4
# rank = 0

# Core
core = Core()
core.readFile('cactusmic.png')


def masterSplitWork():
    linesEachProcess = math.ceil( core.img.shape[0] / nrProcs)

    # Send the work to each process
    for i in range(nrProcs):
        fr = linesEachProcess * i
        to = min(linesEachProcess * (i + 1), int(core.img.shape[0]) - 1)

        MPI.COMM_WORLD.send(fr,   dest = i,   tag = 0)
        MPI.COMM_WORLD.send(to,   dest = i,   tag = 1)

def masterCollectWork():
    # Receive work from each process
    resultImg = np.zeros(core.img.shape)
    for i in range(nrProcs):
        print("Receiving form proc: ", i)
        receivedImg = MPI.COMM_WORLD.recv(source = i, tag = 0)

        for x in range(core.img.shape[0]):
            for y in range(core.img.shape[1]):
                for z in range(core.img.shape[2]):
                    if receivedImg[x][y][z] != 0 :
                        resultImg[x][y][z] = receivedImg[x][y][z]

        print("Received form proc: ", i)

    # Save the image
    cv2.imwrite("cactusmic_rez.png", resultImg)

def slaveDoWork():
    # Read commands
    fr = MPI.COMM_WORLD.recv(source = 0, tag = 0)
    to = MPI.COMM_WORLD.recv(source = 0, tag = 1)

    # Execute the multiplications
    zeros = np.zeros(core.img.shape)
    for i in range(fr, to + 1):
        for j in range(core.img.shape[1]):
            for h in range(3):
                zeros[i][j][h] = core.multiplyPx(i, j, h)

    # Send the result
    MPI.COMM_WORLD.isend(zeros, dest=0, tag=0)

if rank == 0:
    masterSplitWork()
    slaveDoWork()
    masterCollectWork()
else:
    slaveDoWork()