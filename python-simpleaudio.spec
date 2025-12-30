%define module simpleaudio

Summary:	A simple audio playback Python extension
Name:		python-%{module}
Version:	1.0.4
Release:	3
License:	MIT
Group:		Development/Python
Url:		https://github.com/hamiltron/py-simple-audio
Source:		https://files.pythonhosted.org/packages/source/s/%{module}/%{module}-%{version}.tar.gz

BuildRequires:	pkgconfig(python3)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	python3dist(pytest)
BuildRequires:	python3dist(setuptools)

%description
The simplaudio package provides cross-platform, dependency-free audio playback
capability for Python 3.

%files
%license LICENSE.txt
%doc README.rst
%{python_sitearch}/%{module}/
%{python_sitearch}/%{module}-%{version}-py%{pyver}.egg-info/

#----------------------------------------------------------------------------

%prep
%autosetup -n %{module}-%{version}

%build
%py_build

%install
%py_install

