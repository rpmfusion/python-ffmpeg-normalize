# Created by pyp2rpm-3.3.4
%global pypi_name ffmpeg-normalize

Name:           python-%{pypi_name}
Version:        1.23.0
Release:        1%{?dist}
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
BuildRequires:  python3dist(pytest)

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
* Sun May 01 2022 Leigh Scott <leigh123linux@gmail.com> - 1.23.0-1
- Update to 1.23.0

* Tue Apr 26 2022 Leigh Scott <leigh123linux@gmail.com> - 1.22.10-1
- Update to 1.22.10

* Sun Apr 17 2022 Leigh Scott <leigh123linux@gmail.com> - 1.22.9-1
- Update to 1.22.9

* Mon Apr 11 2022 Leigh Scott <leigh123linux@gmail.com> - 1.22.8-1
- Update to 1.22.8

* Mon Feb 28 2022 Sérgio Basto <sergio@serjux.com> - 1.22.7-1
- Update python-ffmpeg-normalize to 1.22.7

* Wed Feb 09 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 1.22.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Jan 03 2022 Sérgio Basto <sergio@serjux.com> - 1.22.4-1
- Update python-ffmpeg-normalize to 1.22.4

* Tue Aug 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 1.20.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

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
