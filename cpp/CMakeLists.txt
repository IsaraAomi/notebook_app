cmake_minimum_required(VERSION 2.8.12)
project(step1)
set(SOURCE_FILE main.cpp)

# Load the configuration file for building OpenCV
find_package(OpenCV REQUIRED)

# Set the include directory paths for OpenCV
include_directories(
    ${OpenCV_INCLUDE_DIRS}
)

# Set the executable file name
add_executable(main
    ${SOURCE_FILE}
)

# Link the required libraries
target_link_libraries(main
    ${OpenCV_LIBRARIES}
)
