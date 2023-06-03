(1) Git clone the repository
```
git clone https://github.com/ZhiangChen/instance_segmentation_remote_sensing.git
```

(2) Build a docker image
```
docker build -t rsisa .
```

(3) Run the docker image in a container
```
docker run -p 8888:8888 -it --name rsisa -v $(pwd)/../:/root/rsisa/ rsisa
```
`$(pwd)/../` should be your repository directory. 

(4) Run jupyter notebook in the container
```
cd
jupyter notebook --allow-root --ip=0.0.0.0
```

(5) Access to a new terminal in the container
```
docker exec -it rsisa bash
```

(6) Start the exited but stopped container
```
docker start rsisa
```

