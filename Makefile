all:
	@echo "Building..."
	@g++ -o nbody_sh1 nbody_sh1.cpp
	@echo "Done."

simdir = simulations

figure8:
	./nbody_sh1 -o 0.01 < $(simdir)/figure8.in > $(simdir)/figure8.out

flungout:
	./nbody_sh1 -o 0.01 < $(simdir)/flungout.in > $(simdir)/flungout.out

flungout2:
	./nbody_sh1 -o 0.01 < $(simdir)/flungout2.in > $(simdir)/flungout2.out

chaos:
	./nbody_sh1 -o 0.01 < $(simdir)/chaos.in > $(simdir)/chaos.out

chaos2:
	./nbody_sh1 -o 0.01 < $(simdir)/chaos2.in > $(simdir)/chaos2.out

chaos3:
	./nbody_sh1 -o 0.01 < $(simdir)/chaos3.in > $(simdir)/chaos3.out

rings:
	./nbody_sh1 -o 0.01 < $(simdir)/rings.in > $(simdir)/rings.out
