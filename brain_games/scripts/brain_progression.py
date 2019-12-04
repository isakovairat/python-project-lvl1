#!/usr/bin/env python3
from brain_games.engine import play_the_game
from brain_games.games import brain_progression


def main():
    play_the_game(brain_progression)


if __name__ == "__main__":
    main()
