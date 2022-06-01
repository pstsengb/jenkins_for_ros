#include "ros/ros.h"
#include "std_msgs/String.h"
#include "geometry_msgs/Twist.h"
#include "sensor_msgs/LaserScan.h"
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>
#include <tf2_ros/transform_listener.h>
#include <geometry_msgs/TransformStamped.h>
#include <geometry_msgs/PointStamped.h>
#include <math.h>
#include <geometry_msgs/PoseArray.h>

class VShapeSegmentation{

  public:
    void doSegmentation();
  
  private:
    int a;

};


class MySub{

    public:
        MySub(ros::NodeHandle m_nh);
        void scanCb(const sensor_msgs::LaserScan::ConstPtr& msg);

    private:
        ros::Subscriber sub_;
        ros::Publisher pub_;
        ros::NodeHandle nh_;

        tf2_ros::Buffer tfBuffer_;
        geometry_msgs::TransformStamped trans_pad2laser_;

};

MySub::MySub(ros::NodeHandle m_nh){

  nh_ = m_nh;
  sub_ = nh_.subscribe("scan", 10, &MySub::scanCb, this);
  pub_ = nh_.advertise<geometry_msgs::PoseArray>("points", 2);

  tf2_ros::TransformListener tfListener(tfBuffer_);

  
  while (ros::ok()){
    try{
      trans_pad2laser_ = tfBuffer_.lookupTransform("charging_pad", "laser",
                                ros::Time(0), ros::Duration(1.0));
    }
    catch (tf2::TransformException &ex) {
      ROS_WARN("%s",ex.what());
      ros::Duration(1.0).sleep();
      continue;
    }
  }


}

void MySub::scanCb(const sensor_msgs::LaserScan::ConstPtr& msg)
{

  double m_angle_min = msg->angle_min;
  double m_angle_increment = msg->angle_increment; 
  int m_cnt = 0;
  
  geometry_msgs::PoseArray pose_for_visualization;
  pose_for_visualization.header.frame_id = "charging_pad";

  for(auto it=msg->ranges.begin();it!=msg->ranges.end();it++){

    geometry_msgs::Pose a_beam_pose_laser, a_beam_pose_pad;

    a_beam_pose_laser.position.x = (*it)*cos(m_angle_min + m_cnt*m_angle_increment);
    a_beam_pose_laser.position.y = (*it)*sin(m_angle_min + m_cnt*m_angle_increment);

    tf2::doTransform(a_beam_pose_laser, a_beam_pose_pad, trans_pad2laser_);
    m_cnt++;

  }

}




int main(int argc, char **argv)
{

  ros::init(argc, argv, "test_node");

  ros::NodeHandle n;

  MySub sub_obj(n);

  ros::Rate loop_rate(10);

  while (ros::ok())
  {

    ros::spinOnce();

    loop_rate.sleep();
  }


  return 0;
}

