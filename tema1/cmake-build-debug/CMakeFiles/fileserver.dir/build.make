# CMAKE generated file: DO NOT EDIT!
# Generated by "Unix Makefiles" Generator, CMake Version 3.10

# Delete rule output on recipe failure.
.DELETE_ON_ERROR:


#=============================================================================
# Special targets provided by cmake.

# Disable implicit rules so canonical targets will work.
.SUFFIXES:


# Remove some rules from gmake that .SUFFIXES does not remove.
SUFFIXES =

.SUFFIXES: .hpux_make_needs_suffix_list


# Suppress display of executed commands.
$(VERBOSE).SILENT:


# A target that is always out of date.
cmake_force:

.PHONY : cmake_force

#=============================================================================
# Set environment variables for the build.

# The shell in which to execute make rules.
SHELL = /bin/sh

# The CMake executable.
CMAKE_COMMAND = /usr/bin/cmake

# The command to remove a file.
RM = /usr/bin/cmake -E remove -f

# Escaping for special characters.
EQUALS = =

# The top-level source directory on which CMake was run.
CMAKE_SOURCE_DIR = /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1

# The top-level build directory on which CMake was run.
CMAKE_BINARY_DIR = /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/cmake-build-debug

# Include any dependencies generated for this target.
include CMakeFiles/fileserver.dir/depend.make

# Include the progress variables for this target.
include CMakeFiles/fileserver.dir/progress.make

# Include the compile flags for this target's objects.
include CMakeFiles/fileserver.dir/flags.make

CMakeFiles/fileserver.dir/server.cpp.o: CMakeFiles/fileserver.dir/flags.make
CMakeFiles/fileserver.dir/server.cpp.o: ../server.cpp
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_1) "Building CXX object CMakeFiles/fileserver.dir/server.cpp.o"
	/usr/bin/c++  $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -o CMakeFiles/fileserver.dir/server.cpp.o -c /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/server.cpp

CMakeFiles/fileserver.dir/server.cpp.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing CXX source to CMakeFiles/fileserver.dir/server.cpp.i"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -E /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/server.cpp > CMakeFiles/fileserver.dir/server.cpp.i

CMakeFiles/fileserver.dir/server.cpp.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling CXX source to assembly CMakeFiles/fileserver.dir/server.cpp.s"
	/usr/bin/c++ $(CXX_DEFINES) $(CXX_INCLUDES) $(CXX_FLAGS) -S /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/server.cpp -o CMakeFiles/fileserver.dir/server.cpp.s

CMakeFiles/fileserver.dir/server.cpp.o.requires:

.PHONY : CMakeFiles/fileserver.dir/server.cpp.o.requires

CMakeFiles/fileserver.dir/server.cpp.o.provides: CMakeFiles/fileserver.dir/server.cpp.o.requires
	$(MAKE) -f CMakeFiles/fileserver.dir/build.make CMakeFiles/fileserver.dir/server.cpp.o.provides.build
.PHONY : CMakeFiles/fileserver.dir/server.cpp.o.provides

CMakeFiles/fileserver.dir/server.cpp.o.provides.build: CMakeFiles/fileserver.dir/server.cpp.o


CMakeFiles/fileserver.dir/load_svc.c.o: CMakeFiles/fileserver.dir/flags.make
CMakeFiles/fileserver.dir/load_svc.c.o: ../load_svc.c
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --progress-dir=/mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_2) "Building C object CMakeFiles/fileserver.dir/load_svc.c.o"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -o CMakeFiles/fileserver.dir/load_svc.c.o   -c /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/load_svc.c

CMakeFiles/fileserver.dir/load_svc.c.i: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Preprocessing C source to CMakeFiles/fileserver.dir/load_svc.c.i"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -E /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/load_svc.c > CMakeFiles/fileserver.dir/load_svc.c.i

CMakeFiles/fileserver.dir/load_svc.c.s: cmake_force
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green "Compiling C source to assembly CMakeFiles/fileserver.dir/load_svc.c.s"
	/usr/bin/cc $(C_DEFINES) $(C_INCLUDES) $(C_FLAGS) -S /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/load_svc.c -o CMakeFiles/fileserver.dir/load_svc.c.s

CMakeFiles/fileserver.dir/load_svc.c.o.requires:

.PHONY : CMakeFiles/fileserver.dir/load_svc.c.o.requires

CMakeFiles/fileserver.dir/load_svc.c.o.provides: CMakeFiles/fileserver.dir/load_svc.c.o.requires
	$(MAKE) -f CMakeFiles/fileserver.dir/build.make CMakeFiles/fileserver.dir/load_svc.c.o.provides.build
.PHONY : CMakeFiles/fileserver.dir/load_svc.c.o.provides

CMakeFiles/fileserver.dir/load_svc.c.o.provides.build: CMakeFiles/fileserver.dir/load_svc.c.o


# Object files for target fileserver
fileserver_OBJECTS = \
"CMakeFiles/fileserver.dir/server.cpp.o" \
"CMakeFiles/fileserver.dir/load_svc.c.o"

# External object files for target fileserver
fileserver_EXTERNAL_OBJECTS =

fileserver: CMakeFiles/fileserver.dir/server.cpp.o
fileserver: CMakeFiles/fileserver.dir/load_svc.c.o
fileserver: CMakeFiles/fileserver.dir/build.make
fileserver: CMakeFiles/fileserver.dir/link.txt
	@$(CMAKE_COMMAND) -E cmake_echo_color --switch=$(COLOR) --green --bold --progress-dir=/mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/cmake-build-debug/CMakeFiles --progress-num=$(CMAKE_PROGRESS_3) "Linking CXX executable fileserver"
	$(CMAKE_COMMAND) -E cmake_link_script CMakeFiles/fileserver.dir/link.txt --verbose=$(VERBOSE)

# Rule to build all files generated by this target.
CMakeFiles/fileserver.dir/build: fileserver

.PHONY : CMakeFiles/fileserver.dir/build

CMakeFiles/fileserver.dir/requires: CMakeFiles/fileserver.dir/server.cpp.o.requires
CMakeFiles/fileserver.dir/requires: CMakeFiles/fileserver.dir/load_svc.c.o.requires

.PHONY : CMakeFiles/fileserver.dir/requires

CMakeFiles/fileserver.dir/clean:
	$(CMAKE_COMMAND) -P CMakeFiles/fileserver.dir/cmake_clean.cmake
.PHONY : CMakeFiles/fileserver.dir/clean

CMakeFiles/fileserver.dir/depend:
	cd /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/cmake-build-debug && $(CMAKE_COMMAND) -E cmake_depends "Unix Makefiles" /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1 /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1 /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/cmake-build-debug /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/cmake-build-debug /mnt/c/Users/GeorgeMD/Documents/Facultate/sprc/tema1/cmake-build-debug/CMakeFiles/fileserver.dir/DependInfo.cmake --color=$(COLOR)
.PHONY : CMakeFiles/fileserver.dir/depend

