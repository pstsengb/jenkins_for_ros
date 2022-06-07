pipeline {
  agent none
  stages {
  
    stage('Compile the pkg') {
      agent {
        docker {
          image 'ubuntu20.04_ros_noetic_rlab:latest'
          args ' -v /var/run/docker.sock:/var/run/docker.sock -v /home/pstsengb/Desktop/new_robot_2d_simulation:/ws_ros' 
        }
      }
      
      options {
        skipDefaultCheckout()
      }
      
      steps {
        
        sh '''#!/bin/bash
        cd /ws_ros
        catkin_make -DCMAKE_BUILD_TYPE=Release
        source devel/setup.bash
        rostest fsm_manager test_cmd.test;
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
 
