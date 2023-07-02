#!/usr/bin/env bash
# Post install script for the UI .rpm to place symlinks in places to allow the CLI to work similarly in both versions

set -e

ln -s /opt/platinum/resources/app.asar.unpacked/daemon/platinum /usr/bin/platinum || true
ln -s /opt/platinum/platinum-blockchain /usr/bin/platinum-blockchain || true
