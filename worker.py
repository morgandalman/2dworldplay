# worker.py - Simulates a region of the world with global coordinates

import redis
import json

import time
import random
import argparse

from region import Region
from world import World

REGION_SIZE = 400  # Fixed region width
NUMBER_OF_ENTITIES = 5000
world = World(size=REGION_SIZE, region_count=2)

r = redis.Redis(host='localhost', port=6379, db=0)



def build_cell_hash(entities):
    cells = {}
    for entity_id, entity in entities.items():
        key = (entity['x'], entity['y'])
        cells[key] = entity

    return cells

def run_worker(region_index):

    region = Region(region_index, REGION_SIZE)
    r.delete(region_index)

    # Entities managed by this region
    entities = {
        region_index * 100000 + i: {
            "x": random.randint(region.min_x(), region.max_x()),
            "y": random.randint(region.min_y(), region.max_y()),
            "red": random.randint(0, 255),
            "blue": random.randint(0, 255),
            "green": random.randint(0, 255)
        }
        for i in range(NUMBER_OF_ENTITIES)
    }

    print(f"Worker {region_index} running...")

    while True:
        pipe = r.pipeline()

        start_time = time.time()
        cells = build_cell_hash(entities)

        # Move entities randomly
        for entity_id, entity in list(entities.items()):
            new_x = entity["x"] + random.choice([-1, 0, 1])
            new_y = entity["y"] + random.choice([-1, 0, 1])

            if world.in_x_bounds(new_x):
                entity["x"] = new_x

            if world.in_y_bounds(new_y):
                entity["y"] = new_y

            key = (entity["x"], entity["y"])
            if key in cells:
                other_entity = cells[key]
                # if other_entity != entity:
                #     print(f"collision: {key}")


            # print(entity)
            # Publish entity's global position
            msg = f"ENTITY_POS {entity_id} {entity['x']} {entity['y']} {region.index} {entity['red']} {entity['blue']} {entity['green']}"
            pipe.hset('entity_positions', f'{entity_id}', msg)

            # Handle exits to neighboring regions
            if not region.in_x_bounds(entity["x"]):
                new_region = world.region_for(entity["x"], entity["y"])
                msg = f"EXIT {entity_id} {entity['x']} {entity['y']} {new_region} {entity['red']} {entity['blue']} {entity['green']}"
                # print(msg)
                pipe.rpush(new_region, msg)
                del entities[entity_id]

        pipe.execute()
        # Receive incoming entities
        message = r.lpop(region_index)
        while message:
            parts = message.split()
            _, entity_id, x, y, new_region, red, blue, green = parts

            if int(new_region) == region_index:
                entities[int(entity_id)] = {"x": int(x), "y": int(y), region: region_index, "red": red, "blue": blue, "green": green}
                # print(f"Entity {entity_id} entered region {region_index} at global ({x}, {y})")

            message = r.lpop(region_index)

        total_time = time.time() - start_time
        print(total_time)
        # time.sleep(0.01)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--region", required=True, type=int, help="Region index (e.g., 0, 1, 2)")
    args = parser.parse_args()

    run_worker(int(args.region))
