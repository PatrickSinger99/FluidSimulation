from typing import Tuple
import pygame
from colors import *


class Display:
    def __init__(self, world_dimensions: Tuple[int, int]):

        # Initialize fonts
        self.debug_font = pygame.font.SysFont('Arial', 14)

        self.world_dim = world_dimensions

    def process_events(self):
        """
        Process input events by the user
        :return State of simulation. True = Simulation ended.
        """
        for event in pygame.event.get():

            # CASE: Game closed
            if event.type == pygame.QUIT:
                return True

            elif event.type == pygame.KEYDOWN:
                """KEY PRESS CASES"""
                pass

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._on_mouseclick()

        return False

    def render(self, screen, fluid_simulation, delta_time_last_frame, show_debug_info=True):
        """
        Draw the current state of the simulation to a screen
        :param screen: pygame screen to draw the game objects on
        :param fluid_simulation: FluidSimulation instance
        :param delta_time_last_frame: time since last frame draw. used to display fps in debug infos
        :param show_debug_info: show debug values at top left of screen
        """
        # Get current state of simulation
        particle_positions = fluid_simulation.get_state()

        # Reset screen
        screen.fill(black)

        # Display particles
        for particle_position in particle_positions:
            pygame.draw.circle(screen, white, particle_position, radius=2)

        # Display simulation infos
        if show_debug_info:
            # FPS
            text_surface = self.debug_font.render(f"FPS: {round(1 / delta_time_last_frame)}", True, white)
            screen.blit(text_surface, (2, 0))

    @staticmethod
    def _on_mouseclick():
        mouse_position = pygame.mouse.get_pos()
        print(f"Clicked at {mouse_position}.")
