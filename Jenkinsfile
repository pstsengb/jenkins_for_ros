pipeline {
  agent none
  stages {
  
    stage('Compile the pkg') {
      agent {
        docker {
          image 'ros:melodic-ros-base'
          args ' -v /var/run/docker.sock:/var/run/docker.sock -v /home/pstsengb/Desktop/new_robot_2d_simulation:/ws_ros' 
        }
      }
      
      options {
        skipDefaultCheckout()
      }
      
      steps {
        
        sh '''#!/bin/bash
        mkdir -p /ws_ros/src
        cd /ws_ros/src
        git clone https://github.com/tsengapola/jenkins_ros
        apt update
        cd /ws_ros
        apt install -y ros-melodic-tf2-ros
        #source /opt/ros/melodic/setup.bash && catkin_make
        #rostest jenkins_ros test_give_location_and_task.test;
        '''

      }
      post {
        always {
          sh 'pwd; ls -l'
        }
      }      
    }

  }// Stages
  environment {
    WS_DIR = ''
    CI = true
  }
  
  options {
    buildDiscarder(logRotator(numToKeepStr: '5', artifactDaysToKeepStr: '30'))
    timeout(time: 120, unit: 'MINUTES')
  }
}
 
