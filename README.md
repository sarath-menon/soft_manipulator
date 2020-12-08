# Soft Manipulator

Ros package for the three segment soft robotic manipulator

 ## Installation

 Instructions for installing ROS Melodic in Ubuntu 18.04: http://wiki.ros.org/melodic/Installation/Ubuntu
 Instruction for creating catkin_ws: http://wiki.ros.org/catkin/Tutorials/create_a_workspace
 
 ```
 cd catkin_ws/src
 git clone https://github.com/sarath-menon/soft_manipulator.git
 cd ..
 catkin_make
```

To run the example:

The example consists of a soft robotic arm which can be manipualted with mouse interaction

- in a first terminal, "source ros", start roscore
- in a second terminal, "source ros", start python recv.py
- in a third terminal, "source ros", runSofa test_sofaros.py

The data position of this MechanicalObject is published as ros topic "/simulation/sender/position" using a dedicated RosSender (python script controller)

The recv is subscribed to this published ros topic "/simulation/sender/position". Each time a data 
arrive, the recv script just re-emit it into a second ros topic called "/animation/receiver/position".

A RosReceiver is added in the sofa scene to listen to this second topic and propagate the values to 
the second mechanical object. 



