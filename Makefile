all:
	@echo "Building..."
	@g++ -o nbody_sh1 nbody_sh1.cpp
	@echo "Done."

figure8:
	./nbody_sh1 -o 1 < figure8.in > figure8.out
