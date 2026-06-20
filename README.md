# TurtleBot2 ROS2 Migration Project

[![ROS2](https://img.shields.io/badge/ROS2-Humble-blue)](https://docs.ros.org/en/humble/)
[![Platform](https://img.shields.io/badge/Platform-Kobuki-green)](https://iclebo-kobuki.readthedocs.io/en/latest/index.html)

A comprehensive migration of TurtleBot2 (Kobuki base) from ROS1 to ROS2 Humble, featuring custom sensor configurations with Hokuyo LiDAR and Kinect depth camera.

<!--
## 📺 Demo Video

<div align="center">


### 🎥 Watch the TurtleBot2 running on ROS2 Humble!

[![TurtleBot2 ROS2 Demo](https://img.youtube.com/vi/Wfc_RwKe6ok/maxresdefault.jpg)](https://youtu.be/Wfc_RwKe6ok)

**Click the image above to watch the demonstration video**

[▶️ Direct Link: TurtleBot2 ROS2 Demo Video](https://youtu.be/Wfc_RwKe6ok)
-->

</div>

## 📄 Project Presentation

A detailed presentation about this project is available: [Presentation_Alvin Isac PREM SUNDER_Taichi HARAGUCHI_2024.pdf](./« Presentation_Alvin Isac PREM SUNDER_Taichi HARAGUCHI_2024.pdf)

---

## 🎯 Project Overview

This project provides a complete ROS2 implementation for the TurtleBot2 platform, including:
- **Kobuki base controller** with remapped topics for easier integration
- **Custom robot description** with Hokuyo and Kinect sensors
- **Full sensor stack** including LiDAR and depth camera drivers
- **Complete migration** of ECL libraries and Kobuki drivers to ROS2

## 📦 Repository Structure

The project consists of three main packages:

```
TurtleBot2_Migration/
├── kobuki_launch_pkg-main/      # Launch configurations for Kobuki + sensors
├── turtlebot2_description-main/ # URDF/Xacro robot description files
└── turtlebot2_ros2-main/        # Core ROS2 packages (Kobuki drivers, ECL libraries)
```

### 1. kobuki_launch_pkg
Launch package that starts the Kobuki node and Hokuyo LiDAR with standardized topic names.

**Topics Remapped:**
- `/commands/velocity` → `/cmd_vel`
- Various command topics (`/cmd/led1`, `/cmd/led2`, etc.)

### 2. turtlebot2_description
Robot description package with customizable URDF models for visualization and simulation.

**Features:**
- Support for multiple sensor configurations
- Customizable TF prefix (default: `turtlebot/`)
- RViz visualization launch files

### 3. turtlebot2_ros2
Core packages including Kobuki drivers, ECL libraries, and ROS2 interfaces.

**Includes:**
- `kobuki_core` - Low-level Kobuki driver
- `kobuki_node` - ROS2 node wrapper
- `kobuki_ros_interfaces` - Custom messages and actions
- `cmd_vel_mux` - Velocity command multiplexer
- `ecl_core` & `ecl_lite` - ECL library ports

## 🚀 Quick Start

### Prerequisites

- ROS2 Humble
- Ubuntu 22.04 (recommended)
- Kobuki base with USB connection
- Hokuyo URG LiDAR (optional)
- Microsoft Kinect (optional)

### Installation

1. **Create a workspace:**
```bash
mkdir -p ~/turtlebot2_ws/src
cd ~/turtlebot2_ws/src
```

2. **Clone this repository:**
```bash
# Clone the main repository containing all packages
git clone https://github.com/AlvinIsac/TurtleBot2-ROS2-Migration.git
cd TurtleBot2-ROS2-Migration
```

The repository contains three packages:
- `kobuki_launch_pkg-main/` - Kobuki and sensor launch files
- `turtlebot2_description-main/` - Robot URDF description
- `turtlebot2_ros2-main/` - Core Kobuki drivers and ECL libraries

3. **Install dependencies:**
```bash
cd ~/turtlebot2_ws
rosdep install --from-paths src --ignore-src -r -y
```

4. **Build the workspace:**
```bash
colcon build --symlink-install
source install/setup.bash
```

5. **Set up udev rules (for Kobuki):**
```bash
sudo cp src/TurtleBot2-ROS2-Migration/turtlebot2_ros2-main/kobuki_core/60-kobuki.rules /etc/udev/rules.d/
sudo udevadm control --reload-rules && sudo udevadm trigger
```

### Running the Robot

1. **Launch Kobuki with sensors:**
```bash
ros2 launch kobuki_launch_pkg kobuki_launch.py
```

2. **Visualize in RViz:**
```bash
ros2 launch turtlebot2_description display_with_kinect_hokuyo.launch.py
```

3. **Test robot control:**
```bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

## 📋 Available Topics

After launching, the following topics are available:

**Control:**
- `/cmd_vel` - Velocity commands (geometry_msgs/Twist)

**Sensors:**
- `/odom` - Odometry data
- `/scan` - LiDAR scan data
- `/imu` - IMU data from Kobuki
- `/sensors/bumper` - Bumper events
- `/sensors/cliff` - Cliff sensor data
- `/sensors/wheel_drop` - Wheel drop events

**Status:**
- `/sensors/core` - Battery and sensor core data
- `/sensors/dock_ir` - Docking IR sensor

## 🔧 Configuration

### Customizing Sensor Positions

Edit the URDF files in `turtlebot2_description/robots/` to adjust sensor mounting positions.

### Changing TF Prefix

Modify the prefix in `kobuki_hexagons_kinect_hokuyo.urdf.xacro`:
```xml
<xacro:property name="prefix" value="your_prefix/"/>
```

### Kobuki Parameters

Edit `kobuki_node/config/kobuki_node_params.yaml` to customize:
- Device port
- Base frame
- Odom frame
- Command timeout

## 🛠️ Hardware Setup

**Tested Configuration:**
- Kobuki base platform
- Hokuyo URG-04LX-UG01 LiDAR
- Microsoft Kinect (Xbox 360)
- Custom hexagon plates for sensor mounting

**Connections:**
- Kobuki: USB connection (typically `/dev/kobuki`)
- Hokuyo: USB connection (typically `/dev/ttyACM0`)
- Kinect: USB connection

## 📝 License

- **kobuki_launch_pkg**: Apache-2.0
- **turtlebot2_description**: Apache 2.0
- **turtlebot2_ros2**: MIT/BSD (see individual packages)

## 🙏 Acknowledgments

This project builds upon and adapts code from:
- [idorobotics/turtlebot2_ros2](https://github.com/idorobotics/turtlebot2_ros2)
- [igrak34/turtlebot2-ros2](https://github.com/igrak34/turtlebot2-ros2)
- Original TurtleBot project

## 👤 Author

- **Alvin Isac PREMSUNDER**
- **Taichi HARAGUCHI**

## 📚 Additional Resources

- [ROS2 Humble Documentation](https://docs.ros.org/en/humble/)
- [Kobuki Documentation](https://kobuki.readthedocs.io/)
- [TurtleBot Official Site](https://www.turtlebot.com/)

---

**Note:** Make sure to adjust serial port configurations (`/dev/ttyACM0`, etc.) according to your hardware setup.
