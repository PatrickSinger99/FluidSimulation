from typing import Tuple
import pygame
from display import Display
from simulation import FluidSimulation


def run_simulation(world_dimensions: Tuple[int, int], num_of_particles: int, target_fps: int = 60):

    # Initialize pygame and set up the window
    pygame.init()
    pygame.display.set_caption("Simulation")
    screen = pygame.display.set_mode(world_dimensions)

    # Create simulation loop variables
    done = False
    clock = pygame.time.Clock()
    delta_time_last_frame = 1

    # Create simulation and display instances
    simulation = FluidSimulation(world_dimensions=world_dimensions, num_of_particles=num_of_particles)
    display = Display(world_dimensions=world_dimensions)

    """ MAIN GAME LOOP """

    while not done:
        # Run all simulation functions for one step/frame of the simulation
        done = display.process_events()
        simulation.update()
        display.render(screen, simulation, delta_time_last_frame)

        # Display updated screen
        pygame.display.flip()

        # Tick game and save time this frame took to compute
        delta_time_last_frame = clock.tick(target_fps) / 1000


if __name__ == '__main__':
    run_simulation((720, 480), 100)
