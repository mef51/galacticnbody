all:
	@echo "Building..."
	@g++ -o nbody_sh1 nbody_sh1.cpp
	@echo "Done."

data:
	./nbody_sh1 < figure8.in > figure8.out
