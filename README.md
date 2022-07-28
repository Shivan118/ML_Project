# ML_Project

### Software Requriment for this project

1. [Github Account](https://github.com/)
2. [Heroku Account](https://www.heroku.com/)
3. [VS Code IDE](https://code.visualstudio.com/Download)
4. [Git CLI](https://git-scm.com/downloads)

Create conda envirnment

```
conda create -p venv python==3.7 -y 
```

Actuivate env
```
conda activate venv/
```

To Setup CI/CD Pipeline in heroku we need 3 information
1. Heroku_EMAIl = shivan@ineuron.ai
2. HEROKU_API_KEY = ad0864da-d970-4fa9-a73c-3e7858cc5a11
3. HEROKU_APP_NAME = ml-regression-app122

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tag_name> .
```
> Note: Image name for docker must be lowercase

To List Docker image
```
docker images
```

Run Docker Image
```
docker run -p 5000:5000 -e PORT=5000 <image_id>

To Check Running Container is Docer
```
docker ps
```

To Stop Docker Container
```
dockr stop <container_ids>
```

2h9m.