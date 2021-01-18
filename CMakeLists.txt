cmake_minimum_required(VERSION 3.17)
project(cpp_pp)

set(CMAKE_CXX_STANDARD 14)

add_executable(linked_list c/linked_list.c)
add_executable(cpp_pp main.c)