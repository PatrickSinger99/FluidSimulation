from typing import Tuple, Union, List
from random import randint


class FluidSimulation:
    def __init__(self, world_dimensions: Tuple[int, int], num_of_particles: int):

        # Simulation variables
        self.world_dim = world_dimensions
        self.particle_positions = []
        self.particle_velocities = []
        self.gravity = 0.2

        # Add initial fluid particles
        for _ in range(num_of_particles):
            self.add_particle()

    def add_particle(self, position: Union[None, Tuple[int, int]] = None, velocity: Tuple[int, int] = (0, 0)):
        """
        Add a particle to the simulation
        :param position: Position of particle. If None, random position will be chosen (x, y)
        :param velocity: Initial velocity of the particle. If none given, velocity will be in x and y
        """
        if position is None:
            position = (randint(0, self.world_dim[0]), randint(0, self.world_dim[1]))

        self.particle_positions.append(list(position))
        self.particle_velocities.append(list(velocity))

    def update(self):
        """
        Update the simulation / Step forward in the simulation
        """
        for i in range(len(self.particle_positions)):

            # Add gravity force
            self.particle_velocities[i][1] += self.gravity

            # Update position
            self.particle_positions[i][0] += self.particle_velocities[i][0]
            self.particle_positions[i][1] += self.particle_velocities[i][1]


    def get_state(self):
        """
        Get the current state of the simulation
        :return: List of fluid particle positions
        """
        return self.particle_positions
