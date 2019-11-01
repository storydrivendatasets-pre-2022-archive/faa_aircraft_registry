#!/bin/sh

for i in $(seq 2008 2017); do
    echo http://registry.faa.gov/database/yearly/ReleasableAircraft.${i}.zip
    curl -Lo data/stashed/ReleasableAircraft.${i}.zip \
        http://registry.faa.gov/database/yearly/ReleasableAircraft.${i}.zip
done
