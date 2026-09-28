#!/bin/sh
set -e
alembic upgrade head
fastapi run --port 8080
