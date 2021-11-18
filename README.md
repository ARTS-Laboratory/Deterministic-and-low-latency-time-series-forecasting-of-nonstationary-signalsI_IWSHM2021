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
