cmake_minimum_required(VERSION 3.17)
project(cpp_pp)

set(CMAKE_CXX_STANDARD 14)


add_executable(bubblesort src/bubblesort.cpp)
add_executable(insertionsort src/insertionsort.cpp)
add_executable(selectionsort src/selectionsort.cpp)
add_executable(quicksort src/quicksort.cpp)
add_executable(mergesort src/mergesort.cpp)
add_executable(heapsort src/heapsort.cpp)
add_executable(binarytree src/binarytree.cpp)
add_executable(permuations src/permutations.cpp)
add_executable(hanoi src/hanoi.cpp)

add_executable(lrucache
        src/lrucache_main.cpp
        inc/lrucache.h
        src/lrucache.cpp)

target_include_directories(lrucache PUBLIC inc)
