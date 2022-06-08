pipeline {
  agent none
  stages {
  
    stage('test Compile the pkg') {
      agent {
        docker {
          image 'ros:melodic-ros-base'
          args "${MOUNT_DIRS}"
        }
      }
      
      options {
        skipDefaultCheckout()
      }
    
      steps {
        
        sh '''#!/bin/bash
	mkdir -p /ws_ros/src
	cd /ws_ros
	source /opt/ros/melodic/setup.bash
	catkin_make 
        '''

      }
      post {
        always {
          sh 'pwd; ls -l'
        }
      }      
    }

    stage('Test the parallel') {
      parallel {
        
        stage('A') {
          agent {
            docker {
              image 'ros:melodic-ros-base'
              args "${MOUNT_DIRS}"
            }
          }
          
          options {skipDefaultCheckout()}
          
          steps {
             
            sh '''#!/bin/bash
                  echo "AA"
                  '''        
          }
          post {
            always {
              sh 'pwd; ls -l'
            }
          }      
        }

        stage('B') {
          agent {
            docker {
              image 'ros:melodic-ros-base'
              args "${MOUNT_DIRS}"
            }
          }
          
          options {skipDefaultCheckout()}
          
          steps {
             
            sh '''#!/bin/bash
                cd /ws_ros
		source /opt/ros/melodic/setup.bash
                roscore
                  '''      
          }
          post {
            always {
              sh 'pwd; ls -l'
            }
          }      
        }
      } //parallel
    } //stage

  
  }// Stages
  environment {
    MOUNT_DIRS = ' -v /var/run/docker.sock:/var/run/docker.sock' 
    //WS_DIR = '/home/dfl-sim01/rlab_navigation_stack'
    CI = true
  }
  options {
    buildDiscarder(logRotator(numToKeepStr: '5', artifactDaysToKeepStr: '30'))
    timeout(time: 120, unit: 'MINUTES')
  }
}
