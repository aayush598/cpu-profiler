# Reference URL: https://learn.arm.com/install-guides/perf/

# Update the package list
sudo apt update

# Install the required packages
sudo apt install -y \
    make \
    gcc \
    flex \
    bison \
    pkg-config \
    linux-tools-generic \
    linux-tools-$(uname -r) \
    libzstd1 \
    libdwarf-dev \
    libdw-dev \
    binutils-dev \
    libcap-dev \
    libelf-dev \
    libnuma-dev \
    python3 \
    python3-dev \
    python3-setuptools \
    libssl-dev \
    libunwind-dev \
    libdwarf-dev \
    zlib1g-dev \
    liblzma-dev \
    libaio-dev \
    libtraceevent-dev \
    debuginfod \
    libpfm4-dev \
    libslang2-dev \
    systemtap-sdt-dev \
    libperl-dev \
    binutils-dev \
    libbabeltrace-dev \
    libiberty-dev \
    libzstd-dev

# Clone the Linux repository
git clone --depth=1 --branch v6.8 git://git.kernel.org/pub/scm/linux/kernel/git/stable/linux.git

# Build perf
cd linux
make -C tools/perf

# Install perf
sudo cp tools/perf/perf /usr/local/bin