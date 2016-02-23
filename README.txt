# Pyflight: Acquire or log data about the flight you're currently on

So far, this only supports flights that have GoGo inflight wireless. Contributions to make it support more types of airline wifi portals are welcome! Just open a pull request. If adding another provider, it would probably make sense to abstract out some common stuff and add a common API.

# How to use

Simplest form right now and best user interface is just to invoke the module pyflight.flightlogger with a parameter of a CSV filename to write the results to. As of now, will overwrite any previously recorded data in the given filename.

    python -m pyflight.flightlogger x.csv
