Name:           nfs4-acl-tools
Version:        0.3.3
Release:        8%{?dist}.0
Summary:        The nfs4 ACL tools
Group:          Applications/System
License:        BSD
URL:            http://www.citi.umich.edu/projects/nfsv4/linux/

BuildRoot:      %{_tmppath}/%{name}-%{version}-root-%(%{__id_u} -n)
Source0:        http://www.citi.umich.edu/projects/nfsv4/linux/nfs4-acl-tools/%{name}-%{version}.tar.gz

BuildRequires: libtool
BuildRequires: libattr-devel

Patch001: nfs4acl-0.3.3-ace.patch

Patch100: nfs4acl-0.2.0-compile.patch
Patch002: nfs4-acl-tools-0.3.3-bz769862.patch
Patch003: nfs4acl-0.3.3-ignore-deny-ace.patch
#
# RHEL6.8
#
Patch004: nfs4-acl-tools-0.3.3-allowspaces.patch
Patch005: nfs4-acl-tools-0.3.3-fdleak.patch

Patch10001: nfs4acl-0.3.3-libtool.patch

%description
This package contains commandline and GUI ACL utilities for the Linux
NFSv4 client.

%prep
%setup -q

%patch001 -p1
%patch002 -p1
# 1161164 - nfs4_setfacl, nfs4_getfacl ignores DENY ace for...
%patch003 -p1
# 1252265 - nfs4_setfacl command fails when NFSv4 group...
%patch004 -p1
# 662726 - nfs4-acl-tools: FD leak in edit_ACL()
%patch005 -p1

%patch100 -p1

%patch10001 -p1

%build
%ifarch s390 s390x sparc
PIE="-fPIE"
%else
PIE="-fpie"
%endif
CFLAGS="`echo $RPM_OPT_FLAGS $PIE`"
export LDFLAGS="-pie"
%configure
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc COPYING INSTALL README TODO VERSION
%{_bindir}/nfs4_editfacl
%{_bindir}/nfs4_getfacl
%{_bindir}/nfs4_setfacl
%{_mandir}/man1/*
%{_mandir}/man5/*

%changelog
* Tue Sep 06 2016 Bjarne Saltbaek <bjarne@redsleeve.org> - 0.3.3-8.0
- Added patch from Jacco
- added "--tag=CC" to the make command due to libtool errors

* Mon Nov 23 2015 Steve Dickson <steved@redhat.com> - 0.3.3-8
- Allow spaces in principal names (bz 1252265)
- nfs4_setfacl.c: Fix fd leak in edit_ACL() (bz 662726)

* Thu Feb 19 2015 Steve Dickson <steved@redhat.com> - 0.3.3-7
- Ignore DENY aces for DELETE, WRITE_OWNER, NAMED_ATTRS (bz 1161164)

* Tue Jan 31 2012 Steve Dickson <steved@redhat.com> - 0.3.3-6
- Fixed a glibc detection of a double free (bz 769862)

* Mon Nov 16 2009 Steve Dickson <steved@redhat.com> - 0.3.3-5
- Fixes segfaulting issues with ACEs that have empty mask fields

* Thu Jul 30 2009 Steve Dickson <steved@redhat.com> - 0.3.3-4
- Change Group in spec file (bz 512580)

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.3.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Feb 18 2009 Steve Dickson <steved@redhat.com> - 0.3.3-1
- Updated to latest upstream version: 0.3.3

* Wed Oct 29 2008 Steve Dickson <steved@redhat.com> - 0.3.2-3
- Removed fuzzness from the compile.patch (bz 321745)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 0.3.2-2
- Autorebuild for GCC 4.3

* Fri Oct 26 2007 Steve Dickson <steved@redhat.com> - 0.3.2-1
- Updated to latest upstream version 0.3.2

* Tue Mar 27 2007 Steve Dickson <steved@redhat.com> - 0.3.1-1.2
- Checked in to Fedora CVS 

* Thu Mar  8 2007  Steve Dickson <steved@redhat.com> - 0.3.1-1.1
- Updated to latest upstream version 0.3.1 which eliminated the 
  need for the patches introduced in the previous commit.

* Tue Mar  6 2007  Tom "spot" Callaway <tcallawa@redhat.com> 0.3.0-1.1
- lose the BR for autotools
- Patch in support for destdir
- use %%configure macro, make DESTDIR= install
- add sparc to -fPIE (trivial, but correct)
- destdir revealed missing/poorly created symlink, patch fixes it, add nfs4_editfacl to files
- LDFLAGS passed to configure/exported were being blindly overwritten, patch fixes

* Fri Mar  2 2007  Steve Dickson <steved@redhat.com> - 0.3.0-1
- Updated to latest upstream version 0.3.0
- Fixed minor issues in spec file from the package review

* Fri Feb 16 2007 Steve Dickson <steved@redhat.com> - 0.2.0-1
- Initial commit
