%if ! (0%{?fedora} > 12 || 0%{?rhel} > 5)
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif
%{!?python_version: %global python_version %(%{__python} -c "from distutils.sysconfig import get_python_version; print(get_python_version())")}

Name: libtdb
Version: 1.3.8
Release: 3%{?dist}.2
Group: System Environment/Daemons
Summary: The tdb library
License: LGPLv3+
URL: http://tdb.samba.org/
Source: http://samba.org/ftp/tdb/tdb-%{version}.tar.gz
BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

BuildRequires: autoconf
BuildRequires: libxslt
BuildRequires: docbook-style-xsl
BuildRequires: python-devel

%description
A library that implements a trivial database.

%package devel
Group: Development/Libraries
Summary: Header files need to link the Tdb library
Requires: libtdb = %{version}-%{release}
Requires: pkgconfig

%description devel
Header files needed to develop programs that link against the Tdb library.

%package -n tdb-tools
Group: Development/Libraries
Summary: Developer tools for the Tdb library
Requires: libtdb = %{version}-%{release}

%description -n tdb-tools
Tools to manage Tdb files

%package -n python-tdb
Group: Development/Libraries
Summary: Python bindings for the Tdb library
Requires: libtdb = %{version}-%{release}

%description -n python-tdb
Python bindings for libtdb

%prep
%setup -q -n tdb-%{version}

%build
%configure --disable-rpath \
           --bundled-libraries=NONE \
           --builtin-libraries=replace
make %{?_smp_mflags} V=1

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

# Shared libraries need to be marked executable for
# rpmbuild to strip them and include them in debuginfo
find $RPM_BUILD_ROOT -name "*.so*" -exec chmod -c +x {} \;

rm -f $RPM_BUILD_ROOT%{_libdir}/libtdb.a

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_libdir}/libtdb.so.*

%files devel
%defattr(-,root,root)
%{_includedir}/tdb.h
%{_libdir}/libtdb.so
%{_libdir}/pkgconfig/tdb.pc
%doc docs/README
%doc docs/tracing.txt

%files -n tdb-tools
%defattr(-,root,root,-)
%{_bindir}/tdbbackup
%{_bindir}/tdbdump
%{_bindir}/tdbtool
%{_bindir}/tdbrestore
%{_mandir}/man8/tdbbackup.8*
%{_mandir}/man8/tdbdump.8*
%{_mandir}/man8/tdbtool.8*
%{_mandir}/man8/tdbrestore.8*

%files -n python-tdb
%defattr(-,root,root,-)
%{python_sitearch}/tdb.so
%{python_sitearch}/_tdb_text.py*

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post -n python-tdb -p /sbin/ldconfig

%postun -n python-tdb -p /sbin/ldconfig

%changelog
* Thu Apr 21 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.3.8-3.2
- Move _tdb_text.py to python-tdb subpackage
- Resolves: rhbz#1329664 - tdb mispackaged tdb_text.py file

* Fri Apr  1 2016 Jakub Hrozek <jhrozek@redhat.com> - 1.3.8-1
- Rebase libtdb to 1.3.8
- related: #1322689

* Thu Aug 02 2012 Jakub Hrozek <jhrozek@redhat.com> - 1.2.10-1
- Resolves: rhbz#766334 - Rebase libtdb to match the version required
                          by Samba4
- Enable the Python bindings to satisfy samba4 BuildRequirements
- Obsoletes tdb-1.2.9-limit-tdb_expand.patch

* Tue Apr 05 2011 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-3
- Resolves: rhbz#692251 - tdb_extend() can cause a memory-usage explosion if
-                         the size of its entries are very large

* Thu Feb 25 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.1-2
- Remove unnecessary --prefix argument to configure

* Wed Feb 24 2010 Simo Sorce <ssorce@redhat.com> - 1.2.1-1
- New upstream bugfix release
- Package manpages too

* Tue Feb 23 2010 Stephen Gallagher <sgallagh@redhat.com> - 1.2.0-2
- Add README and tracing.txt
- Fix rpmlint errors

* Tue Dec 15 2009 Simo Sorce <ssorce@redhat.com> - 1.2.0-1
- New upstream release

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Simo Sorce <ssorce@redhat.com> - 1.1.5-1
- Original tarballs had a screw-up, rebuild with new fixed tarballs from
  upstream.

* Tue Jun 16 2009 Simo Sorce <ssorce@redhat.com> - 1.1.5-0
- New upstream release

* Wed May 6 2009 Simo Sorce <ssorce@redhat.com> - 1.1.3-15
- First public independent release from upstream
