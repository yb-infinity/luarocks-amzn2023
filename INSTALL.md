# LuaRocks Installation Guide

[![GitHub release](https://img.shields.io/github/release/yb-infinity/luarocks-amzn2023.svg)](https://github.com/yb-infinity/luarocks-amzn2023/releases)
[![Download](https://img.shields.io/github/downloads/yb-infinity/luarocks-amzn2023/total.svg)](https://github.com/yb-infinity/luarocks-amzn2023/releases)

## Installation Options

Choose the installation method that works best for you:

1. **[From Repository](#installation-from-repository)** - Recommended for production
2. **[From GitHub Releases](#installation-from-github-releases)** - Pre-built packages
3. **[Building from Source](#building-from-source)** - Latest development version

## Installation from Repository

### 1. Add the Repository

Create the repository configuration file:

```bash
sudo tee /etc/yum.repos.d/fury.repo << EOF
[fury]
name=Gemfury Repository
baseurl=https://yum.fury.io/drakemazzy/
enabled=1
gpgcheck=0
priority=1
EOF
```

### 2. Install LuaRocks

```bash
# Update package cache
sudo dnf makecache

# Install LuaRocks (no EPEL required for Amazon Linux 2023)
sudo dnf install -y luarocks
```

### 3. Verify Installation

```bash
# Check LuaRocks version
luarocks --version

# Check Lua version
lua -v

# List installed rocks (should be empty initially)
luarocks list
```

## Installation from GitHub Releases

Download pre-built RPM packages from GitHub releases:

```bash
# Download the latest release (replace VERSION with actual version)
wget https://github.com/yb-infinity/luarocks-amzn2023/releases/download/v3.11.1/luarocks-3.11.1-*.rpm

# Install dependencies
sudo dnf install -y lua lua-devel lua-filesystem zip unzip gcc make git curl wget

# Install the downloaded package
sudo dnf install -y ./luarocks-*.rpm
```

## Installation from Local RPM

If you have built the RPM locally or downloaded from releases:

```bash
# Install dependencies
sudo dnf install -y lua lua-devel lua-filesystem zip unzip gcc make git curl wget

# Install the RPM package
sudo dnf install -y ./rpmbuild-output/RPMS/noarch/luarocks-*.rpm
```

## Building from Source

To build the RPM package yourself:

```bash
# Clone the repository
git clone https://github.com/yb-infinity/luarocks-amzn2023.git
cd luarocks-amzn2023

# Build using Docker (recommended)
docker run --rm -v "$PWD":/workspace -w /workspace amazonlinux:2023 /bin/bash -c "
  chmod +x scripts/build-amzn2023.sh
  ./scripts/build-amzn2023.sh
"

# Install the built package
sudo dnf install -y ./rpmbuild-output/RPMS/noarch/luarocks-*.rpm
```

## Basic Usage

### Installing Rocks

```bash
# Install a popular Lua module
luarocks install penlight

# Install commonly needed modules
luarocks install luafilesystem  # File system utilities
luarocks install lua-cjson      # JSON support
luarocks install luasocket      # Network support

# Install a specific version
luarocks install lua-cjson 2.1.0

# Install with user scope (no sudo required)
luarocks install --local penlight
```

### Managing Rocks

```bash
# List installed rocks
luarocks list

# Search for rocks
luarocks search json

# Show rock information
luarocks show penlight

# Remove a rock
luarocks remove penlight
```

### Configuration

LuaRocks is configured with system-wide settings:

- **Config file**: `/etc/luarocks/config-5.4.lua`
- **System rocks**: `/usr/local/lib/luarocks/rocks-5.4/`
- **User rocks**: `~/.luarocks/`

### Environment Setup

For development, you might want to add local paths:

```bash
# Add to your ~/.bashrc or ~/.zshrc
export LUA_PATH="$HOME/.luarocks/share/lua/5.4/?.lua;$HOME/.luarocks/share/lua/5.4/?/init.lua;;"
export LUA_CPATH="$HOME/.luarocks/lib/lua/5.4/?.so;;"
```

## Troubleshooting

### Common Issues

1. **Permission denied**: Use `--local` flag or run with sudo
2. **Missing dependencies**: Install development packages
3. **Compilation errors**: Ensure gcc and make are installed

### Getting Help

```bash
# Show LuaRocks help
luarocks help

# Show help for specific command
luarocks help install

# Check configuration
luarocks config
```

## Development Environment

For Lua development, you might also want:

```bash
# Install additional development tools
sudo dnf install -y lua-devel readline-devel

# Install useful rocks
luarocks install busted        # Testing framework
luarocks install luacheck      # Linter
luarocks install ldoc          # Documentation generator
```

## Package Information

- **Package Name**: luarocks
- **Supported Lua Version**: 5.4
- **Architecture**: noarch (works on x86_64 and ARM64)
- **Dependencies**: Automatically handled by DNF/YUM
- **Target OS**: Amazon Linux 2023 (no EPEL required)

## Amazon Linux 2023 Notes

### Package Availability
- All required dependencies are available in standard Amazon Linux 2023 repositories
- No EPEL repository needed
- lua-filesystem and other common modules should be installed via LuaRocks after installation

### Recommended First Steps
After installing LuaRocks, install commonly needed modules:
```bash
luarocks install luafilesystem
luarocks install luasocket
luarocks install lua-cjson
```
