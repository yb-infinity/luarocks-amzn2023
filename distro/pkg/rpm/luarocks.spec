%global luaver 5.4

Name:           luarocks
Version:        {{ rpm_version }}
Release:        {{ release }}%{?dist}
Summary:        A deployment and management system for Lua modules

License:        MIT
URL:            https://luarocks.org/
Source0:        https://luarocks.org/releases/%{name}-{{ source_version }}.tar.gz

BuildArch:      noarch
BuildRequires:  lua >= %{luaver}
BuildRequires:  lua-devel >= %{luaver}
BuildRequires:  lua-filesystem
BuildRequires:  zip
BuildRequires:  unzip
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  git
BuildRequires:  curl
BuildRequires:  wget
BuildRequires:  which

Requires:       lua >= %{luaver}
Requires:       lua-filesystem
Requires:       zip
Requires:       unzip
Requires:       gcc
Requires:       make
Requires:       git
Requires:       curl
Requires:       wget
Requires:       which

%description
LuaRocks is a deployment and management system for Lua modules. It allows
you to create and install Lua modules as self-contained packages called
rocks. You can download and install rocks, along with their dependencies,
from a local or remote repository. You can also create and upload rocks,
along with their documentation, to a repository.

This package includes lua-filesystem as a dependency for better file system support.

%prep
%setup -q -n %{name}-{{ source_version }}

%build
./configure \
    --prefix=%{_prefix} \
    --sysconfdir=%{_sysconfdir}/luarocks \
    --with-lua=%{_prefix} \
    --with-lua-bin=%{_bindir} \
    --with-lua-include=%{_includedir} \
    --with-lua-lib=%{_libdir} \
    --lua-version=%{luaver} \
    --versioned-rocks-dir

make build

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Create version-specific symlinks
ln -s luarocks %{buildroot}%{_bindir}/luarocks-%{luaver}
ln -s luarocks-admin %{buildroot}%{_bindir}/luarocks-admin-%{luaver}

# Create system rocks directory
mkdir -p %{buildroot}/usr/local/lib/luarocks/rocks-%{luaver}
mkdir -p %{buildroot}/usr/local/share/lua/%{luaver}
mkdir -p %{buildroot}/usr/local/lib/lua/%{luaver}

%files
%license COPYING
%doc README.md CHANGELOG.md
%{_bindir}/luarocks
%{_bindir}/luarocks-%{luaver}
%{_bindir}/luarocks-admin
%{_bindir}/luarocks-admin-%{luaver}
%dir %{_sysconfdir}/luarocks
%dir %{_sysconfdir}/luarocks/luarocks
%config(noreplace) %{_sysconfdir}/luarocks/luarocks/config-%{luaver}.lua
%{_datadir}/lua/%{luaver}/luarocks/
/usr/local/lib/luarocks/
/usr/local/share/lua/%{luaver}/
/usr/local/lib/lua/%{luaver}/

%changelog
* {{ now }} DrakeMazzy <drake@mazzy.rv.ua> - {{ rpm_version }}-{{ release }}
- Updated to version {{ source_version }}
- Built for Amazon Linux 2023
- Added support for Lua %{luaver}
- Configured with versioned rocks directory
- Added system-wide configuration file
