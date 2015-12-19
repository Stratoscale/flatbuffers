%define longhash %(git log | head -1 | awk '{print $2}')
%define shorthash %(echo %{longhash} | dd bs=1 count=12)

Name:           flatbuffers
Version:        1.2.0
Release:        2.strato.%{shorthash}
Summary:        Memory Efficient Serialization Library from Google
Packager:       Stratoscale Ltd.
License:        ASL 2.0
URL:            http://google.github.io/flatbuffers/
BuildRequires:  cmake

%description
FlatBuffers is a serialization library for games and other memory constrained apps.
FlatBuffers allows you to directly access serialized data without unpacking/parsing
it first, while still having great forwards/backwards compatibility.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}
Provides:       %{name}-static = %{version}-%{release}
%description    devel
%{summary}.

%package        python
Summary:        Python module for %{name}
Requires:       %{name} = %{version}-%{release}
%description    python
%{summary}.

%build
cp %{TOP}/build/strato/flatc .
cp %{TOP}/build/strato/flathash .
cp %{TOP}/LICENSE.txt .
cp %{TOP}/readme.md .
cp %{TOP}/include/flatbuffers/flatbuffers.h .
cp -r %{TOP}/python .
pushd python
python setup.py build
echo "__version__ = '%{version}-%{release}'" >> build/lib/flatbuffers/version.py
popd


%install
mkdir -p %{buildroot}/%{_bindir}
mkdir -p %{buildroot}/%{_includedir}/flatbuffers
mkdir -p %{buildroot}/%{python2_sitelib}
install -m 755 flatc %{buildroot}/%{_bindir}
install -m 755 flathash %{buildroot}/%{_bindir}
install -m 644 flatbuffers.h %{buildroot}/%{_includedir}/flatbuffers
cp -r python/build/lib/flatbuffers %{buildroot}/%{python2_sitelib}/

%files
%license LICENSE.txt
%doc readme.md

%files devel
%{_bindir}/flatc
%{_bindir}/flathash
%{_includedir}/flatbuffers

%files python
%{python2_sitelib}/flatbuffers

%changelog

* Sat Dec 19 2015 Rafael Buchbinder <rafi@stratoscale.com> - 1.2.0-2
- Updated to latest master to take the Python binding fixes that
  didn't make it to v1.2.0
* Thu Nov 19 2015 Rafael Buchbinder <rafi@stratoscale.com> - 1.2.0-1
- Initial version
