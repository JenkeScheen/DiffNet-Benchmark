#### Repository for benchmarking DiffNet vs. LOMAP network generation

- diffnet_loop_benchmark.py loops Diffnet over n nodes

- lomap_scaling/lomap_*.py loops LOMAP over n nodes
- plot_performances.py plots each model's performance over time



- To extract CPU usage run monitor_system.sh in the background.

Benchmarking is run on a 20-core Intel(R) Core(TM) i9-7900X CPU @ 3.30GHz

## Results:

When looping DiffNet over covariance matrices increasing in size, the program crashes at 50 < m < 80; most of the times the crash will cause either a workstation reboot or python to stop responding, but sometimes python crashes with a memory error (*diffnet_MemError.err*). 

The memory error shows that there is some overly large matrix called. For a plot of the parameters versus m, see *diffnet_scaling/output/GsMatrix_plot.png*.

-----------------------------------------------------------------------------------------------------------------------------------------------------------

DiffNet is a Python tool for finding optimal allocations of sampling
in computational or experimental measurements of the individual
quantities and their pairwise differences, so as to minimize the covariance
in the estimated quantities.

Copyright (C) 2018-2019 Huafeng Xu

Huafeng Xu, Optimal measurement network of pairwise differences, 2019, https://arxiv.org/abs/1906.08599.







