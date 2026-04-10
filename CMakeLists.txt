cmake_minimum_required(VERSION 3.8 FATAL_ERROR)
project(CNPY)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

option(ENABLE_STATIC "Build static (.a) library" ON)

find_package(ZLIB REQUIRED)

add_library(cnpy SHARED "cnpy.cpp")
target_link_libraries(cnpy ZLIB::ZLIB)
install(TARGETS "cnpy" LIBRARY DESTINATION lib PERMISSIONS OWNER_READ OWNER_WRITE OWNER_EXECUTE GROUP_READ GROUP_EXECUTE WORLD_READ WORLD_EXECUTE)

if(ENABLE_STATIC)
    add_library(cnpy-static STATIC "cnpy.cpp")
    set_target_properties(cnpy-static PROPERTIES OUTPUT_NAME "cnpy")
    target_link_libraries(cnpy-static ZLIB::ZLIB)
    install(TARGETS "cnpy-static" ARCHIVE DESTINATION lib)
endif(ENABLE_STATIC)

install(FILES "cnpy.h" DESTINATION include)

add_executable(test test/gen.cpp)
target_include_directories(test PRIVATE ${CMAKE_SOURCE_DIR})
target_link_libraries(test cnpy)

add_custom_command(
    OUTPUT ${CMAKE_BINARY_DIR}/critic
    COMMAND ${CMAKE_COMMAND} -E copy ${CMAKE_SOURCE_DIR}/test/critic.py ${CMAKE_BINARY_DIR}/critic
    COMMAND chmod +x ${CMAKE_BINARY_DIR}/critic
    DEPENDS ${CMAKE_SOURCE_DIR}/test/critic.py
)
add_custom_target(critic ALL DEPENDS ${CMAKE_BINARY_DIR}/critic)
