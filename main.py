import pygame as pg
import sys
import asyncio
import time
import asyncio

from settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from sound import *
from pathfinding import *


class Game:
    def __init__(self):
        pg.init()

        try:
            pg.mouse.set_visible(False)
        except:
            pass  # Not all platforms support this (e.g., web browsers)

        self.screen = pg.display.set_mode(RES)

        try:
            pg.event.set_grab(True)
        except:
            pass  # Not all platforms support mouse grab (e.g., web browsers)

        self.clock = pg.time.Clock()

        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 40)

        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)

        self.weapon = Weapon(self)

        self.sound = Sound(self)

        self.pathfinding = PathFinding(self)

        try:
            if pg.mixer.get_init():
                pg.mixer.music.play(-1)
        except:
            pass

    def check_events(self):
        self.global_trigger = False

        for event in pg.event.get():

            if event.type == pg.QUIT:
                return False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    return False

            if event.type == self.global_event:
                self.global_trigger = True

            self.player.single_fire_event(event)

        return True

    def update(self):
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()


    def draw(self):
        self.object_renderer.draw()
        self.weapon.draw()

    async def run(self):
        running = True
        target_dt = 1 / FPS

        while running:
            frame_start = time.perf_counter()

            running = self.check_events()

            self.update()
            self.draw()

            pg.display.flip()

            # update internal clock without blocking
            self.clock.tick(0)

            # maintain target FPS cooperatively
            elapsed = time.perf_counter() - frame_start
            sleep_time = max(0, target_dt - elapsed)
            if sleep_time > 0:
                await asyncio.sleep(sleep_time)

            pg.display.set_caption(f"FPS Game | {self.clock.get_fps():.1f}")

        pg.quit()
        sys.exit()


if __name__ == "__main__":
    try:
        asyncio.run(Game().run())
    except Exception as e:
        import traceback
        traceback.print_exc()
        input("\nGame crashed. Press Enter to exit...")
