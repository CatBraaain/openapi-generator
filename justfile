_:
  @just --list --unsorted

prepare:
  uv run bin/custom/prepare.py
  cp bin/custom/launch.json .vscode/launch.json

build:
  ./mvnw clean package -pl modules/openapi-generator -am -Dmaven.test.skip=true

generate:
  ./bin/generate-samples.sh ./bin/configs/*python*.yaml || exit
