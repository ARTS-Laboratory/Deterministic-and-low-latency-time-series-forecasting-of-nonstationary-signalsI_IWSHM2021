# code/FPGA:
* 3 MLP's
* Main goal: measure computational time for different resources.
* Making SubVI's of large calculation part( Data manipulation MLP 1/2/3, MLP forwardpass for MLP1/2/3, Attention layer and backpropagation).
* One flat sequence inside whole MLP's (case structure). Which has 7 FIFO's for measuring (a) start tick (b) Data In (c) Subsampling (d) Data manipulation (e) MLP forwardpass (f) Attention layer and backpropagation and (g) end tick.
* Run in compile mode.
* Open with project.lvproj>host.vi(shows the output) and target.vi(whole MLP algothithum code)
* Used data: \data\data_set_1\data_100points.csv
