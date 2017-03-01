all:
	@echo "Building..."
	@g++ -o nbody_sh1 nbody_sh1.cpp
	@echo "Done."

simdir = simulations

figure8:
	./nbody_sh1 -o 0.01 < $(simdir)/figure8.in > $(simdir)/figure8.out

flingout:
	./nbody_sh1 -o 0.01 < $(simdir)/flingout.in > $(simdir)/flingout.out

flingout2:
	./nbody_sh1 -o 0.01 < $(simdir)/flingout2.in > $(simdir)/flingout2.out

chaos:
	./nbody_sh1 -o 0.01 < $(simdir)/chaos.in > $(simdir)/chaos.out

chaos2:
	./nbody_sh1 -o 0.01 < $(simdir)/chaos2.in > $(simdir)/chaos2.out

chaos3:
	./nbody_sh1 -o 0.01 < $(simdir)/chaos3.in > $(simdir)/chaos3.out

rings:
	./nbody_sh1 -o 0.01 < $(simdir)/rings.in > $(simdir)/rings.out
