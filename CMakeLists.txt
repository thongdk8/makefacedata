cmake_minimum_required (VERSION 3.2)
project(face_recognition_cmake)

find_package(dlib 19.6)
if(${dlib_FOUND})
    message("dlib information:")
    message("  dlib version: ${dlib_VERSION}")

    if (NOT TARGET dlib)
        add_library(dlib INTERFACE IMPORTED GLOBAL)
    endif()
else()
    message(FATAL_ERROR "dlib not found in the system, please install dlib")
endif()


find_package(OpenCV REQUIRED)
message(STATUS "OpenCV library status:")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")
if(CMAKE_VERSION VERSION_LESS "2.8.11")
  # Add OpenCV headers location to your include paths
  include_directories(${OpenCV_INCLUDE_DIRS})
endif()

include_directories("/home/thongpb/works/face_recognition/face_recognition_cmake")

# Declare the executable target built from your sources
add_executable(main main.cpp defineddnn.h facerecognizer.h datamanager.h facerecognizer.cpp)
# Link your application with OpenCV libraries
target_link_libraries(main ${dlib_LIBS} ${OpenCV_LIBS})
