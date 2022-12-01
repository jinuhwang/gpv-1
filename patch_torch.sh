#!/bin/bash
cp adam.patch /opt/conda/lib/python3.8/site-packages
cd /opt/conda/lib/python3.8/site-packages
patch -p1 < adam.patch
