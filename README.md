# DSA Project

This project generates a map with random points and calculates the shortest path between two points using Dijkstra's algorithm. The map and the shortest path are displayed using Pygame.

## Prerequisites

- Python 3.x
- Pygame library

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd dsaproject/dsa_project
    ```

2. Install the required libraries:
    ```sh
    pip install pygame
    ```

## Usage

1. Generate the map and calculate the shortest path:
    ```sh
    python game.py <start_point> <end_point>
    ```

    Replace `<start_point>` and `<end_point>` with the labels of the points you want to find the shortest path between. For example:
    ```sh
    python game.py 1 10
    ```

2. The map and the shortest path will be displayed in a Pygame window.

## Files

- `game.py`: Main script to generate the map, calculate the shortest path, and display the results.
- `map.txt`: File to store the generated map points.

## Notes

- Ensure that the start and end points exist in the generated map.
- The map is generated randomly each time you run the script.

## License

This project is licensed under the MIT License.