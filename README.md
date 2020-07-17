# ParaViewExportContours
A simple script for automating pedestrian wind contours to use in paraView

This script does not fully work as such it has been written as excerpts of code which can be copied into the Python interpreter within ParaView

A state must be created, current that state is defined as "TWEEDSTATE2.pvsm". Either create a new state and change the code, or create a new state and name it to this.

variable "TWEEDNOpenFOAMFileName" is the variable for the file name that the particular state file looks for. It is dependent on the name of the state file. This is slightly confusing I know...
