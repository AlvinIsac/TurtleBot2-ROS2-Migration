cmake_minimum_required(VERSION 3.5)
project(kobuki_launch_pkg)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(kobuki_node REQUIRED) 

install(
  DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

ament_package()

