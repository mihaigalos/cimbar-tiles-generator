import json
import math


class Hamming:

    def __init__(self, tile_size, default_tiles):
        self.tile_size = tile_size  # NxN pixels per tile
        self.tiles = self._remove_tile_first_newline(default_tiles)
        self.min_hamming_distance = 1000000000
        self.max_hamming_distance = 0

    def _remove_tile_first_newline(self, tiles):
        result = []
        for tile in tiles:
            tile = tile[1:]
            result.append(tile)
        return result

    def compute_distances(self):
        hamming_distances = {}
        i = 0
        for tile1 in self.tiles:
            one_distance = {}
            j = 0
            for tile2 in self.tiles:
                if i != j:
                    one_distance[j] = self._diff_tile(tile1, tile2)
                    if self.max_hamming_distance < one_distance[j]:
                        self.max_hamming_distance = one_distance[j]
                    if self.min_hamming_distance > one_distance[j]:
                        self.min_hamming_distance = one_distance[j]
                j += 1

            hamming_distances[i] = one_distance
            i += 1
        return hamming_distances

    def to_json(self):
        json_object = json.dumps(self.compute_distances(), indent=4)
        print(json_object)

    def print(self):
        self.to_json()
        print(
            f"min: {self.min_hamming_distance}, log2(min) = {math.log2(self.min_hamming_distance)} bits")
        print(
            f"max: {self.max_hamming_distance}, log2(max) = {math.log2(self.max_hamming_distance)} bits")

    def _diff_tile(self, tile1, tile2) -> int:
        hamming_distance = 0
        for pixel1 in tile1:
            if pixel1 == '\n' or pixel1 == '\r':
                continue
            for pixel2 in tile2:
                if pixel2 == '\n' or pixel2 == '\r':
                    continue
                if pixel1 != pixel2:
                    hamming_distance += 1
        return hamming_distance
