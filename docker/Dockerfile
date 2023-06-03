FROM ubuntu:focal

RUN apt update \
	&& apt install ffmpeg libsm6 libxext6  -y \
	&& apt install software-properties-common -y \
	&& apt install python3-pip -y \
	&& add-apt-repository ppa:ubuntugis/ppa \
	&& apt install gdal-bin -y \
	&& apt install git -y \
	&& pip3 install rasterio fiona pyproj matplotlib Shapely tqdm rioxarray opencv-python notebook geopandas

RUN pip3 install --upgrade numpy


