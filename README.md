# Hello App for Docker
 **Description**
  - This is a beginner friendly Docker basic hello world app to get familiar with the basic structure.

  ## Setup:
  ### 1. Building Docker Image
  ``` docker build -t <your dockerhub username>/hello-app . ```  *you can run without username also in local system

  ### 2. Run the Container
  ``` docker run -p 5000:5000 hello-app ```

  ### 3. Webpage Access
   Open your browse and search:
  
   ``` http://localhost:5000 ```
   
   You will see: Hello World from Docker

   ---
# Docker Commands Every Beginner Should Know
 ## Basic Setup and info:
 - ```docker --version```

   Check your installed Docker version.

 - ```docker info```

    View system-wide Docker details.

## Working with Images:
- ```docker pull <image_name>```

  Download an image from Docker Hub (e.g., docker pull python:3.10).

- ```docker images```

  List all downloaded images.

- ```docker rmi <image_name>```

  Remove an image.

## Running Containers:
- ```docker run <image_name>```

  Run a container from an image (e.g., docker run hello-world).

- ```docker run -it <image_name> /bin/bash``` 
  
  Start an interactive shell inside a container.

- ```docker run -p <host_port>:<container_port> <image_name>```

  Map ports for web apps (e.g., Jupyter: -p 8888:8888).

- ```docker run -v <host_path>:<container_path> <image_name>```

  Mount local folders into the container.

## Managing Containers:
- ```docker ps```

  List running containers.

- ```docker ps -a```

  List all containers (including stopped ones).

-  ```docker stop <container_id>```

  Stop a running container.

- ```docker start <container_id>```

  Start a stopped container.

- ```docker rm <container_id>``

  Remove a container.

## Building Custom Images:
- ```docker build -t <image_name> .```

  Build an image from a Dockerfile.

- ```docker tag <image_id> <repo>:<tag>```

  Tag an image for sharing.

- ```docker push <repo>:<tag>```

  Push an image to Docker Hub.
----
# Dockerfile Basics
```
FROM python:3.10                       #FROM python:<version>-<variant>
WORKDIR /app                           #WORKDIR /<your-app-directory>
COPY requirements.txt .                #COPY . /<your-app-directory>
RUN pip install -r requirements.txt    #RUN Install dependencies from requirements.txt                               
CMD ["python", "main.py"]              #CMD ["python", "<your-app-file>.py"]
```
