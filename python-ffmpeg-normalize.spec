# Created by pyp2rpm-3.3.4
%global pypi_name ffmpeg_normalize

Name:           python-ffmpeg-normalize
Version:        1.37.3
Release:        %autorelease
Summary:        Normalize audio via ffmpeg

License:        MIT
URL:            https://github.com/slhck/ffmpeg-normalize
Source0:        %{pypi_source}
BuildArch:      noarch

BuildRequires:  python3-devel

%description
A utility for batch-normalizing audio using ffmpeg.
This program normalizes media files to a certain LUFS level using the EBU R128
loudness normalization procedure. It can also perform RMS-based normalization
(where the mean is lifted or attenuated), or peak normalization to a certain
target level.
Batch processing of several input files is possible, including video files.

%package -n     python3-ffmpeg-normalize
Summary:        %{summary}
%{?python_provide:%python_provide python3-ffmpeg-normalize}

Requires:       ffmpeg


%description -n python3-ffmpeg-normalize
A utility for batch-normalizing audio using ffmpeg.
This program normalizes media files to a certain LUFS level using the EBU R128
loudness normalization procedure. It can also perform RMS-based normalization
(where the mean is lifted or attenuated), or peak normalization to a certain
target level.
Batch processing of several input files is possible, including video files.


%prep
%autosetup -n %{pypi_name}-%{version}
sed -i -e '/uv_build/s/<0.9.0/<0.11.0/' -e 's/colorlog==6.7.0/colorlog>=6.7.0/' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l %{pypi_name}


%files -n python3-ffmpeg-normalize -f %{pyproject_files}
%license LICENSE.md
%doc README.md
%{_bindir}/ffmpeg-normalize

%changelog
%autochangelog

