First of all connect to Advance desktop on Oscar with 8 cores and 256 GB memory allocation for faster and nonstop work. Set the time for 72 hours.
Tutorial is modified from this github repository https://github.com/r-barnes/Barnes2020-FillSpillMerge


Fill-spill-merge
Ensure you have a working compiler.
The following compilers are known to work: GCC7.5.0, GCC8.4.0, GCC9.3.0
The following compilers are known to be too old: GCC5.4.0
Although GDAL is not required to use the library, it is needed to run the example program.
Install the prerequisites
To install on linux:
Go to terminal and follow these steps:
```
git clone --recurse-submodules -j8 https://github.com/r-barnes/Barnes2020-FillSpillMerge for downloading attached repositories
git submodule update --init --recursive
```
To compile type these on terminal
```
mkdir build
cd build
cmake -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ -DGDAL_INCLUDE_DIR=/gpfs/runtime/opt/gdal/3.5.0/include/ -DCMAKE_INSTALL_PREFIX=/users/nwagle/Barnes2020-FillSpillMerge ..
```
Use your prefix and the location of your compilers
Binaries are located in “/users/nwagle/Barnes2020-FillSpillMerge/build”

Make sure there is your name in the biraries file

To run fill spill merge :
```
./fsm.exe "DEM_FILE.tif" "Resultant_filled_dem.tif" <ocean level> --swl <run_off depth>
```
Replace the ocean level and runoff depth with your value

To run fill spill merge with the runoff depth of raster grid rather than single value:
```
./fsm.exe "DEM_FILE.tif" "Resultant_filled_dem.tif" <ocean level> --swf “runoff.tif”
```

For other works:
You will need 
xarray

rasterio

gdal

white box tools
