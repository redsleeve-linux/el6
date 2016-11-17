Name:           libqb
Version:        0.17.1
Release:        2%{?dist}.0
Summary:        An IPC library for high performance servers

Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.libqb.org
Source0:        https://fedorahosted.org/releases/q/u/quarterback/%{name}-%{version}.tar.xz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# need this to build on rhel5 build boxes
Patch1:         01-build-on-brew.patch
Patch2:		bz1276345-increase-socket-field-len.patch

ExclusiveArch: i686 x86_64 s390 %{arm}
# not ppc at this point

BuildRequires:  libtool doxygen procps check-devel automake

#Requires: <nothing>

%description
libqb provides high performance client server reusable features.
Initially these are IPC and poll.

%prep
%setup -q

%patch1 -p1
%patch2 -p1

%build
./autogen.sh
%configure --disable-static ac_cv_func_epoll_create1=no ac_cv_func_epoll_create=no
make %{?_smp_mflags}

%check
make check

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -name '*.la' -exec rm -f {} ';'
rm -rf $RPM_BUILD_ROOT/%{_docdir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING
%{_sbindir}/qb-blackbox
%{_libdir}/libqb.so.*

%package        devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires:       %{name} = %{version}-%{release} pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files          devel
%defattr(-,root,root,-)
%doc COPYING README.markdown
%{_includedir}/qb/
%{_libdir}/libqb.so
%{_libdir}/pkgconfig/libqb.pc
%{_mandir}/man3/qb*3*
%{_mandir}/man8/qb-blackbox.8.gz

%changelog
* Tue Sep 06 2016 Bjarne Saltbaek <bjarne@redsleeve.org> - 0.17.1-2.0
- Added patch from Jacco
- Add ARM architectures

* Fri Nov 27 2015 Christine Caulfield <ccaulfie@redhat.com> - 0.17.1-2
- Increase size of the buffer where we make the socket name to allow for longer PIDs 
  Resolves: rhbz#1276345

* Mon Jan 19 2015 David Vossel <dvossel@redhat.com> - 0.17.1-1
- Rebase to libqb v0.17.1
  Resolves: rhbz#1110042

* Wed Jul 25 2013 David Vossel <dvossel@redhat.com> - 0.16.0-2
- Re-add fix required to build under brew.
  Resolves: rhbz#950403

* Wed Jul 25 2013 David Vossel <dvossel@redhat.com> - 0.16.0-1
- rebase to v0.16.0
  Resolves: rhbz#950403

* Mon Nov 19 2012 David Vossel <dvossel@redhat.com> - 0.14.2-3
- Additional upstream work to address 100% cpu usage bug in
  realtime environment.
  cpu usage during certain situations. (#869446)

* Wed Oct 24 2012 David Vossel <dvossel@redhat.com> - 0.14.2-2
- Fixes issue with qb_ipcc_recv() that resulted in nearly 100%
  cpu usage during certain situations. (#869446)

* Wed Sep 12 2012 David Vossel <dvossel@redhat.com> - 0.14.2-1
- Rebased to 0.14.2 (#845275)

* Fri Feb 03 2012 Angus Salkeld <asalkeld@redhat.com> - 0.9.0-2
- Disable loop and ipc tests as they use features not availble on brew.
- Get the tests to print out (disable parallel-tests).
- Call autogen.sh to get the no parallel-tests
- Disable ppc arch as the "make check" fails.

* Fri Jan 27 2012 Angus Salkeld <asalkeld@redhat.com> - 0.9.0-1
- Rebased to 0.9.0

* Tue Jan 10 2012  Angus Salkeld <asalkeld@redhat.com> - 0.8.1-2
- fix qb_timespec_add_ms()

* Thu Jan 5 2012  Angus Salkeld <asalkeld@redhat.com> - 0.8.1-1
- Rebased to 0.8.1 (#771914)

* Wed Nov 17 2011 Angus Salkeld <asalkeld@redhat.com> - 0.7.0-1
- Rebased to 0.7.0 (#754610)

* Thu Sep 1 2011 Angus Salkeld <asalkeld@redhat.com> - 0.6.0-2
- LOG: fix the default syslog filter

* Tue Aug 30 2011 Angus Salkeld <asalkeld@redhat.com> - 0.6.0-1
- Rebased to 0.6.0 which includes (#734457):
- Add a stop watch
- LOG: serialize the va_list, don't snprintf
- LOG: change active list into array access
- atomic: fix qb_atomic_pointer macros
- LOG: allow the thread priority to be set.
- Fix splint warning on ubuntu 11.04

* Mon Jul 18 2011 Angus Salkeld <asalkeld@redhat.com> - 0.5.1-1
- Rebased to 0.5.1 which includes:
- LOOP: make the return more consistent in qb_loop_timer_expire_time_get()
- LOG: add string.h to qblog.h
- Add a qb_strerror_r wrapper.
- don't let an invalid time stamp provoke a NULL dereference
- LOG: move priority check up to prevent unnecessary format.
- rename README to README.markdown

* Wed Jun 8 2011 Angus Salkeld <asalkeld@redhat.com> - 0.5.0-1
- Rebased to 0.5.0 which includes:
- new logging API
- support for sparc
- coverity fixes

* Tue Feb 8 2011 Angus Salkeld <asalkeld@redhat.com> - 0.4.1-2
- SPEC: improve devel files section
- SPEC: remove global variables

* Mon Jan 31 2011 Angus Salkeld <asalkeld@redhat.com> - 0.4.1-1
- SPEC: add procps to BuildRequire
- SPEC: remove automake and autoconf from BuildRequire
- SPEC: remove call to ./autogen.sh
- SPEC: update to new upstream version 0.4.1
- LOOP: check read() return value
- DOCS: add missing @param on new timeout argument
- BUILD: only set -g and -O options if explicitly requested.
- BUILD: Remove unneccessary check for library "dl"
- BUILD: improve the release build system

* Fri Jan 14 2011 Angus Salkeld <asalkeld@redhat.com> - 0.4.0-2
- remove "." from Summary
- Add "check-devel to BuildRequires
- Add "make check" to check section
- Changed a buildroot to RPM_BUILD_ROOT
- Document alphatag, numcomm and dirty variables.

* Sun Jan 09 2011 Angus Salkeld <asalkeld@redhat.com> - 0.4.0-1
- Initial release
