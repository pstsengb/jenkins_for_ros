# Jenkins Setup For ROS
Setup jenkins for ROS CI/CD cycle

## Download 2 docker images

One image is for jenkins, and another image is for ROS test in jenkins
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
    
then click install without restart
```
> add a Jenkinsfile on this repo(jenkins system will run this script)
* See Jenkins file in this repo as example, we can add mutiple test, parallel test, etc... 
* In this Jenkins file. We have 2 stages in the test. The first one is the compilation test, in which it creates a workspace and do catkin_make. The second one is a parallel stages template, in which they just echo AA and BB.

### Start Jenkins test - link to public repository
* Following video shows you how to setup a pipeline in jenkins and add public repo for the test
<img src="https://github.com/tsengapola/my_image_repo/blob/main/jenkins_ros/add_repo.gif" width="500" height="300"/>

### Start Jenkins test - link to private repository
`Create a token from your github. Go to your github: setting->Developer settings ->Personal access tokens ,then click Generate new token and record token number`
* Following image shows you how to add the token for the private repo pipeline:
<img src="https://github.com/pstsengb/Image_for_repository/blob/main/jenkin_use/Add.png" width="500" height="300"/>

*  Enter 'user name' and 'Password', the password is the token number
<img src="https://github.com/pstsengb/Image_for_repository/blob/main/jenkin_use/enteruserandpassword.png" width="500" height="300"/>

*  Once you fill the 'user name' and 'Password', in the Credential selection, you should see the name you just created
<img src="https://github.com/pstsengb/Image_for_repository/blob/main/jenkin_use/chosesetting.png" width="500" height="300"/>

* Once the Credential is added,the remain setup is the same as `Start Jenkins test - link to public repository`
> 
## Check Jenkins result
You can now use Blue Ocean to check result

<img src="https://github.com/pstsengb/Image_for_repository/blob/main/jenkin_use/result.png" width="500" height="300"/>  
