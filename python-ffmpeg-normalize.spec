# Created by pyp2rpm-3.3.4
%global pypi_name ffmpeg-normalize

Name:           python-%{pypi_name}
Version:        1.20.1
Release:        4%{?dist}
Summary:        Normalize audio via ffmpeg

License:        MIT
URL:            https://github.com/slhck/ffmpeg-normalize
Source0:        https://pypi.python.org/packages/source/f/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)
# Nedded for tests
BuildRequires:  ffmpeg >= 3.1
BuildRequires:  python3dist(tqdm) >= 4.38

%description
A utility for batch-normalizing audio using ffmpeg.
This program normalizes media files to a certain LUFS level using the EBU R128
loudness normalization procedure. It can also perform RMS-based normalization
(where the mean is lifted or attenuated), or peak normalization to a certain
target level.
Batch processing of several input files is possible, including video files.

%package -n     python3-%{pypi_name}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       ffmpeg >= 3.1


%description -n python3-%{pypi_name}
A utility for batch-normalizing audio using ffmpeg.
This program normalizes media files to a certain LUFS level using the EBU R128
loudness normalization procedure. It can also perform RMS-based normalization
(where the mean is lifted or attenuated), or peak normalization to a certain
target level.
Batch processing of several input files is possible, including video files.


%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e 's@colorama>=0.4.3@colorama>=0.4.1@g' setup.py

%build
%py3_build

%install
%py3_install

%check
%{python3} test/test.py

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md
%{_bindir}/ffmpeg-normalize
%{python3_sitelib}/ffmpeg_normalize
%{python3_sitelib}/ffmpeg_normalize-%{version}-py%{python3_version}.egg-info

%changelog
* Tue Jun 15 2021 Leigh Scott <leigh123linux@gmail.com> - 1.20.1-4
- Rebuild for python-3.10

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.20.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Aug 18 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.20.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Jul 25 2020 Leigh Scott <leigh123linux@gmail.com> - 1.20.1-1
- Update to 1.20.1

* Wed Jul 15 2020 Leigh Scott <leigh123linux@gmail.com> - 1.20.0-1
- Update to 1.20.0

* Mon Jun 01 2020 Leigh Scott <leigh123linux@gmail.com> - 1.19.0-1
- Initial package.
