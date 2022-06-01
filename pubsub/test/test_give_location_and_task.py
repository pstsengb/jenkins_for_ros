#!/usr/bin/env python
import sys
import time
import unittest
import rospy
import rostest
import json
import tf
from std_srvs.srv import Empty, SetBool
from geometry_msgs.msg import PoseWithCovarianceStamped
import rospkg
from as_module.AS_Actions_Manager import ActionManager

from amcl.srv import GiveLocation, GiveLocationResponse, GiveLocationRequest
from std_msgs.msg import String

class TestGiveLocationAndTask(unittest.TestCase):

    def __init__(self, *args):
        super(TestGiveLocationAndTask, self).__init__(*args)
        rospy.init_node('test_give_location_and_task')
        rospy.loginfo("TestGiveLocationAndTask is initialized.")
        self.manager_state_sub = rospy.Subscriber("ros_manager/robot_state", String, self.managerStateCb)
        self.manager_state = ""

        self.execution_result_sub = rospy.Subscriber("ros_manager/robot_execution_result", String, self.executionResultCb)
        self.execution_result = ""
        
        self.task_cmd_pub = rospy.Publisher("ros_manager/task_cmd", String, queue_size=2)

    def managerStateCb(self, data):
        self.manager_state = json.loads(data.data)

    def executionResultCb(self, data):
        self.execution_result = data.data

    def giveLocation(self):
        try:
            rospy.wait_for_service('ros_manager/give_location',5)
            give_location = rospy.ServiceProxy('ros_manager/give_location', GiveLocation)
            give_location("ware_house", "home")
        except (rospy.ServiceException, rospy.ROSException):
            rospy.logerr("Service call failed --- Clear costmap failed")   

    def assignMockTask(slef):
        try:
            rospy.wait_for_service('/ros_manager/activate_mock_task',5)
            assign_mock = rospy.ServiceProxy('/ros_manager/activate_mock_task', SetBool)
            assign_mock(True)
        except (rospy.ServiceException, rospy.ROSException):
            rospy.logerr("Service call failed --- activate_mock_task failed")   


    def clearCostmap(self):
        try:
            rospy.wait_for_service('move_base/clear_costmaps',5)
            clear_costmap = rospy.ServiceProxy('move_base/clear_costmaps', Empty)
            clear_costmap()
            time.sleep(1.0)
        except (rospy.ServiceException, rospy.ROSException):
            rospy.logerr("Service call failed --- Clear costmap failed")    

    def test_simulation(self):# only functions with 'test_'-prefix will be run!

        while(True):
            '''
            Publish cmd to general manager or do something else here!!!
            '''
            rospy.sleep(1.0)
            break

  

        if(True):
            self.assertTrue(True)
        else:
            self.assertTrue(False)
        
        
if __name__ == '__main__':
    time.sleep(0.75)
    testName = 'test_give_location_and_task'
    try:
        rostest.run('test_give_location_and_task', testName, TestGiveLocationAndTask, sys.argv)
    except KeyboardInterrupt:
        pass
    print("exiting")  
