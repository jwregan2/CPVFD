#!/bin/sh

env=${ENV:-test}

echo LOCALE:
locale

if [ "$env" = "test" ]; then
  echo "Building for test..."
  ./build-test.sh
else
  echo "Building for prod..."
  ./build-prod.sh
fi
