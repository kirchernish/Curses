#!/bin/bash

# Переключаемся на ветку dev
git checkout dev

# Получаем последний коммит из dev
last_commit=$(git rev-parse HEAD)

# Переключаемся на ветку prd
git checkout prd

# Сливаем изменения из dev в prd
git merge dev

# Устанавливаем тэг для последнего коммита
git tag -a "release-$(date "+%Y-%m-%d-%H-%M-%S")" $last_commit -m "Release deploy"

# Отправляем изменения в удаленный репозиторий
git push --tags
