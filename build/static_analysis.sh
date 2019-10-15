docker build -t "dungeon" .
docker run --rm -w /dndApp "dungeon" tox lint
