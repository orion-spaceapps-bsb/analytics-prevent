# Introduction

Repository of algorithms to analyze data about prediction of rain correlated to runoff from rain excess. The goal is to develop an APIto feed a react native based app. Our goal is to predict flood using this data.

This is a single file server, the dataset used in the development was the daily accumulated precipitation since 1998-2018 in millimetres. It can be accessed by this [link](https://disc.gsfc.nasa.gov/datasets/TRMM_3B42_Daily_7/summary).

## To run

You need to ```pip install``` **all dependencies listed** in the ```server.py``` file.

Run ```pip install netCDF4```.<br />
Run ```pip install numpy```.<br />
Run ```pip install matplotlib```.<br />
Run ```pip install flask```.<br />
Run ```pip install codecs```.<br />
Run ```pip install pandas```.<br />

Run ```python3 server.py```, this up the server to acess endpoints.

## Using data
After download all the data, add them to /data folder to use.

Please check if the files are saved with correct extension .nc4 and if files are not saved like ".nc4.nc4". Please save them as ```<name_of_the_file>.nc4```.
