# Jenkins Setup For ROS
Tutorial for running ROS test in jenkins and how to setup.

## Download 2 docker images

```
docker pull ros:melodic-ros-base
docker pull jenkins/jenkins:lts
```

## Start Jenkins using Docker

```
docker run --name jenkins -u root -p 8080:8080 -v $(which docker):/usr/bin/docker -v /var/run/docker.sock:/var/run/docker.sock jenkins/jenkins:lts
```

> Remember the password for future login, you will see something in terminal:
```
Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:

483d1d6cd3de49db86f76efae8d8fd5f

This may also be found at: /var/jenkins_home/secrets/initialAdminPassword
```

> open browser and go to localhost:8080
* intall suggested pkgs and wait finish


> go to Manage Jenkins-->Manage Plugins-->Available--> search docker
```
install following
    --> Docker
    --> Docker Commons
    --> Docker Pipeline
    --> docker-build-step 
    --> Docker Compose Build Step 
    --> Docker API 
click install without restart
```
> add Jenkins file
* See Jenkins file in this repo as example, we can add mutiple test, parallel test, etc... 
* In this Jenkins file, I only test if package can be compiled or not. You can see a comment line that runs rostest for your reference.

> Setup testing
<img src="https://github.com/tsengapola/my_image_repo/blob/main/jenkins_ros/add_repo.gif" width="600" height="400"/>

> Generate token
got to your github: setting->Developer settings
Create a token
<img src="https://github.com/pstsengb/Image_for_repository/blob/main/jenkin_use/how_to_getting_token.gif" width="600" height="400"/>
> When select github in credential part add token and provide the token
