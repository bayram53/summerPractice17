#!/usr/bin/env python
import sys
import rospy
from moveit_commander import RobotCommander,MoveGroupCommander, PlanningSceneInterface, roscpp_initialize, roscpp_shutdown
from geometry_msgs.msg import PoseStamped

if __name__=='__main__':

    roscpp_initialize(sys.argv)
    rospy.init_node('moveit_py_demo', anonymous=True)
    
    scene = PlanningSceneInterface()
    robot = RobotCommander()
    eef =  MoveGroupCommander("endeffector")
    rospy.sleep(1)

    # clean the scene
    scene.remove_world_object("pole")
    scene.remove_world_object("table")
    scene.remove_world_object("part")

    # publish a demo scene
    p = PoseStamped()
    p.header.frame_id = robot.get_planning_frame()

    p.pose.position.x = 0.748724
    p.pose.position.y = 0.612035
    p.pose.position.z = 0.0122832
    scene.add_box("part", p, (0.1, 0.1, 0.1))

    rospy.sleep(1)

    # pick an object
    robot.manipulator.pick("part")

    rospy.spin()
roscpp_shutdown()
