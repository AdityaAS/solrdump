Summary:    Export SOLR fields.
Name:       solrtab
Version:    0.1.2
Release:    0
License:    GPL
BuildArch:  x86_64
BuildRoot:  %{_tmppath}/%{name}-build
Group:      System/Base
Vendor:     Leipzig University Library, https://www.ub.uni-leipzig.de
URL:        https://github.com/ubleipzig/solrtab

%description

Export SOLR fields.

%prep

%build

%pre

%install
mkdir -p $RPM_BUILD_ROOT/usr/local/sbin
install -m 755 solrtab $RPM_BUILD_ROOT/usr/local/sbin

%post

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_tmppath}/%{name}
rm -rf %{_topdir}/BUILD/%{name}

%files
%defattr(-,root,root)

/usr/local/sbin/solrtab

%changelog
* Thu Dec 6 2016 Martin Czygan
- 0.1.2 initial release
