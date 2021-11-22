# IWSHM2021_MLP_hardware_implementation:
## Hardware Validation:
In this work, hardware validation is done on a Kintex-7 70T FPGA housed in a NI
cRIO-9035 that also incorporates a CPU running NI Linux Real-Time. Fig. 1 diagrams
how data is collected and processed on the FPGA, as well as how data is transmitted
through the parallel MLP tracks. The sampling rate of the system is set to 25,000 S/s
and is restricted to intervals of the internal clock of the 24-bit ADC used in this project,
a NI-9239 manufactured by NI. Data is passed from the DAQ to a set of 50 registers,
stored in the FPGA’s look-up table memory. The registers make up a software-defined
rolling buffer of the 50 most recent digitized signals. The rolling buffer is sub-sampled
at 5,000 S/s, 6,250 S/s, and 8,333 S/s for the three different MLP tracks. The data
is then normalized, by detecting maximum and minimum values from input data and
ranging the data between -1 to 1. Next, the normalized data is fed through the MLP (i.e.
forward pass) to obtain a prediction that is then passed to the attention layer before a
final prediction of the signal 25 clock cycles (1 ms) into the future is produced.
![flowchart1](https://user-images.githubusercontent.com/60459286/142488752-07980fbc-af0c-421f-89fc-0f8f7b2a07bc.png)
         Figure 1. Flow chart of data collection and processing in parallel MLP tracks

## V4.5.9:
* 3 MLP's
* Main goal: measure computational time for different resources.
* Making SubVI's of large calculation part( Data manipulation MLP 1/2/3, MLP forwardpass for MLP1/2/3, Attention layer and backpropagation).
* One flat sequence inside whole MLP's (case structure). Which has 7 FIFO's for measuring (a) start tick (b) Data In (c) Subsampling (d) Data manipulation (e) MLP forwardpass (f) Attention layer and backpropagation and (g) end tick.
* Run in compile mode.
* Open with 4.5.9.lvproj>host.vi(shows the output) and target.vi(whol MLP algothithum code)
* Used data: \data\data_set_1\data_Vahid_100points.csv
## Result:
The deterministic characteristics of the algorithm are provided by the FPGA implementation, timing, and resource utilization are discussed here. The FPGA’s base clock
is compiled at 80 MHz and a single pass through the algorithm takes 2,005 clock ticks
(25.76 µs). As a new sample is digitized every 40 µs, the system is dormant for 1,195
clock ticks (14.24 µs) between each iteration as it waits for a new data point to be added
to the rolling memory buffer. Fig. 2 reports the timing performance for different aspects
of the process. Resource utilization is presented in Table 1, which reports the resource
utilization in terms of slices used, slice availability, and percentage (%).
![resource](https://user-images.githubusercontent.com/60459286/142489065-2179161a-58b5-4365-bde1-90860abf6e35.png)
        Figure 2. Time required for different aspects of the process.
        
        Table 1. The FPGA elements are shown by device utilization.
 ![image](https://user-images.githubusercontent.com/60459286/142489219-023aa639-a553-4f5b-8f69-f80bcc55eb5c.png)
