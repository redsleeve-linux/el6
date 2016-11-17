%global _hardened_build 1
# We only compile with gcc, but other people may want other compilers.
# Set the compiler here.
%global opt_cc gcc
# Optional CFLAGS to use with the specific compiler...gcc doesn't need any,
# so uncomment and define to use
#global opt_cflags
%global opt_cxx g++
#global opt_cxxflags
%global opt_f77 gfortran
#global opt_fflags
%global opt_fc gfortran
#global opt_fcflags

%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib(1)")}
# Optional name suffix to use...we leave it off when compiling with gcc, but
# for other compiled versions to install side by side, it will need a
# suffix in order to keep the names from conflicting.
#global _cc_name_suffix -gcc

%global macrosdir %(d=%{_rpmconfigdir}/macros.d; [ -d $d ] || d=%{_sysconfdir}/rpm; echo $d)

Name:			openmpi%{?_cc_name_suffix}
Version:		1.10.2
Release:		2%{?dist}.0
Summary:		Open Message Passing Interface
Group:			Development/Libraries
License:		BSD, MIT and Romio
URL:			http://www.open-mpi.org/

# We can't use %{name} here because of _cc_name_suffix
Source0:		https://www.open-mpi.org/software/ompi/v1.10/downloads/openmpi-%{version}.tar.bz2
Source1:		openmpi.module.in
Source2:		macros.openmpi.in

BuildRequires:		gcc-gfortran
#sparc64 and aarch64 don't have valgrind
%ifnarch %{sparc} aarch64
BuildRequires:		valgrind-devel
%endif
BuildRequires:		libibverbs-devel >= 1.1.3, opensm-devel > 3.3.0
BuildRequires:		librdmacm-devel libibcm-devel
BuildRequires:		papi-devel
BuildRequires:		python libtool-ltdl-devel
BuildRequires:		libesmtp-devel
%ifarch x86_64
BuildRequires:		infinipath-psm-devel
%endif
%if 0%{?rhel} == 6
BuildRequires:          flex
%endif
%ifarch %{arm}
BuildRequires:          java-devel
%endif

# s390 is unlikely to have the hardware we want, and some of the -devel
# packages we require aren't available there.
ExcludeArch: s390 s390x

# Private openmpi libraries
%{?filter_setup:
%filter_from_provides /^libmca_common_sm.so.2/d
%filter_from_provides /^libompi_dbg_msgq.so/d
%filter_from_provides /^libompitrace.so.0/d
%filter_from_provides /^libopen-pal.so.3/d
%filter_from_provides /^libopen-rte.so.3/d
%filter_from_provides /^libotf.so.0/d
%filter_from_provides /^libvt-hyb.so.0/d
%filter_from_provides /^libvt-mpi.so.0/d
%filter_from_provides /^libvt-mt.so.0/d
%filter_from_provides /^libvt.so.0/d
%filter_from_provides /^mca_/d
%filter_from_requires /^libmca_common_sm.so.2/d
%filter_from_requires /^libompitrace.so.0/d
%filter_from_requires /^libopen-pal.so.3/d
%filter_from_requires /^libopen-rte.so.3/d
%filter_from_requires /^libotf.so.0/d
%filter_from_requires /^libvt-hyb.so.0/d
%filter_from_requires /^libvt-mpi.so.0/d
%filter_from_requires /^libvt-mt.so.0/d
%filter_from_requires /^libvt.so.0/d
%filter_setup
}
%global __provides_exclude_from %{_libdir}/openmpi/lib/(lib(mca|ompi|open-(pal|rte|trace)|otf|v)|openmpi/).*.so
%global __requires_exclude lib(mca|ompi|open-(pal|rte|trace)|otf|vt).*

%global common_desc Open MPI is an open source, freely available implementation of both the\
MPI-1 and MPI-2 standards, combining technologies and resources from\
several other projects (FT-MPI, LA-MPI, LAM/MPI, and PACX-MPI) in\
order to build the best MPI library available.  A completely new MPI-2\
compliant implementation, Open MPI offers advantages for system and\
software vendors, application developers, and computer science\
researchers. For more information, see http://www.open-mpi.org/ .

%description
%{common_desc}

%package 1.10
Summary:		Open Message Passing Interface 1.10
Group:			Development/Libraries
# Install both successors of openmpi-1.8.1 on updates from RHEL 6.7:
#  openmpi-1.8-1.8.1 (built from compat-openmpi) and this pkg, openmpi-1.10-1.10.2
# Both have to Obsolete the old openmpi.
Obsoletes:		openmpi < 1.8.1-3
Provides:		mpi
Requires:		environment-modules

%description 1.10
%{common_desc}

%package 1.10-devel
Summary:	Development files for openmpi-1.10
Group:		Development/Libraries
Requires:	%{name}-1.10 = %{version}-%{release}, gcc-gfortran
Provides:	mpi-devel
Obsoletes:	openmpi-devel < 1.8.1-3

%description 1.10-devel
Contains development headers and libraries for openmpi-1.10.

%package 1.10-java
Summary:	Java library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
%if 0%{?fedora} >= 20 || 0%{?rhel} >= 7
Requires:	java-headless
%else
Requires:	java
%endif

%description 1.10-java
Java library.

%package 1.10-java-devel
Summary:	Java development files for openmpi
Group:		Development/Libraries
Requires:	%{name}-java = %{version}-%{release}
Requires:	java-devel

%description 1.10-java-devel
Contains development wrapper for compiling Java with openmpi.

# We set this to for convenience, since this is the unique dir we use for this
# particular package, version, compiler
%global variant openmpi-1.10
%global libname %{variant}%{?_cc_name_suffix}
%global namearch %{variant}-%{_arch}%{?_cc_name_suffix}

%prep
%setup -q -n openmpi-%{version}

# When dealing with multilib installations, aka the ability to run either
# i386 or x86_64 binaries on x86_64 machines, we install the native i386
# openmpi libs/compilers and the native x86_64 libs/compilers.  Obviously,
# on i386 you can only run i386, so you don't really need the -m32 flag
# to gcc in order to force 32 bit mode.  However, since we use the native
# i386 package to support i386 operation on x86_64, and since on x86_64
# the default is x86_64, the i386 package needs to force i386 mode.  This
# is true of all the multilib arches, hence the non-default arch (aka i386
# on x86_64) must force the non-default mode (aka 32 bit compile) in it's
# native-arch package (aka, when built on i386) so that it will work
# properly on the non-native arch as a multilib package (aka i386 installed
# on x86_64).  Just to be safe, we also force the default mode (aka 64 bit)
# in default arch packages (aka, the x86_64 package).  There are, however,
# some arches that don't support forcing *any* mode, those we just leave
# undefined.

%ifarch %{ix86} ppc sparcv9
%global mode 32
%global modeflag -m32
%endif
%ifarch ia64
%global mode 64
%endif
%ifarch x86_64 %{power64} sparc64
%global mode 64
%global modeflag -m64
%endif

%build
# Note that the versions of libevent and hwloc shipped in RHEL-6 are too
# old for openmpi-1.10.2 to use, therefore we have to use the internal version.
./configure --prefix=%{_libdir}/%{libname} \
	--mandir=%{_mandir}/%{namearch} \
	--includedir=%{_includedir}/%{namearch} \
	--sysconfdir=%{_sysconfdir}/%{namearch} \
%ifarch armv5tel
	--host=armv5tel-unknown-linux-gnueabi \
	--enable-shared \
	--enable-mpi-java \
	--enable-mpi-thread-multiple \
%endif
	--disable-silent-rules \
	--with-libevent=internal \
	--with-hwloc=internal \
%ifnarch %{power64}
	--enable-mpi-cxx \
%endif
	--with-verbs=/usr \
	--with-sge \
%ifnarch %{sparc} aarch64
	--with-valgrind \
	--enable-memchecker \
%endif
	--with-libltdl=/usr \
	--with-wrapper-cflags="%{?modeflag}" \
	--with-wrapper-cxxflags="%{?modeflag}" \
	--with-wrapper-fflags="%{?modeflag}" \
	--with-wrapper-fcflags="%{?modeflag}" \
	CC=%{opt_cc} CXX=%{opt_cxx} \
	CFLAGS="%{?opt_cflags} %{!?opt_cflags:$RPM_OPT_FLAGS}" \
	CXXFLAGS="%{?opt_cxxflags} %{!?opt_cxxflags:$RPM_OPT_FLAGS}" \
	FC=%{opt_fc} FCFLAGS="%{?opt_fcflags} %{!?opt_fcflags:$RPM_OPT_FLAGS}" \
	F77=%{opt_f77} FFLAGS="%{?opt_fflags} %{!?opt_fflags:$RPM_OPT_FLAGS}"

make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}
rm -fr %{buildroot}%{_libdir}/%{libname}/lib/pkgconfig
find %{buildroot}%{_libdir}/%{libname}/lib -name \*.la | xargs rm
find %{buildroot}%{_mandir}/%{namearch} -type f | xargs gzip -9
ln -s mpicc.1.gz %{buildroot}%{_mandir}/%{namearch}/man1/mpiCC.1.gz
# Remove dangling symlink
rm -f %{buildroot}%{_mandir}/%{namearch}/man1/mpiCC.1
rm -f %{buildroot}%{_mandir}/%{namearch}/man1/orteCC.1*
rm -f %{buildroot}%{_libdir}/%{libname}/share/vampirtrace/doc/opari/lacsi01.ps.gz
mkdir %{buildroot}%{_mandir}/%{namearch}/man{2,4,5,6,8,9,n}

# Make the environment-modules file
mkdir -p %{buildroot}%{_sysconfdir}/modulefiles
# Since we're doing our own substitution here, use our own definitions.
sed 's#@LIBDIR@#%{_libdir}/%{libname}#g;
     s#@ETCDIR@#%{_sysconfdir}/%{namearch}#g;
     s#@FMODDIR@#%{_fmoddir}/%{namearch}#g;
     s#@INCDIR@#%{_includedir}/%{namearch}#g;
     s#@MANDIR@#%{_mandir}/%{namearch}#g;
     s#@PYSITEARCH@#%{python_sitearch}/%{libname}#g;
     s#@COMPILER@#openmpi-%{_arch}%{?_cc_name_suffix}#g;
     s#@SUFFIX@#%{?_cc_name_suffix}_openmpi#g' \
     < %SOURCE1 \
     > %{buildroot}%{_sysconfdir}/modulefiles/%{namearch}

# make the rpm config file
mkdir -p %{buildroot}/%{_sysconfdir}/rpm
LIBNAME=%{libname}
# do not expand _arch
sed "s#@MACRONAME@#${LIBNAME//[-.]/_}#g;
     s#@MODULENAME@#%{variant}-%%{_arch}%{?_cc_name_suffix}#" \
	< %SOURCE2 \
	> %{buildroot}/%{macrosdir}/macros.%{namearch}

# Link the fortran module to proper location
mkdir -p %{buildroot}/%{_fmoddir}/%{libname}
for mod in %{buildroot}%{_libdir}/%{libname}/lib/*.mod
do
  modname=$(basename $mod)
  ln -s ../../../%{libname}/lib/${modname} %{buildroot}/%{_fmoddir}/%{libname}/
done

mkdir -p %{buildroot}/%{python_sitearch}/%{libname}

%check
make check

%files 1.10
%dir %{_libdir}/%{libname}
%dir %{_sysconfdir}/%{namearch}
%dir %{_libdir}/%{libname}/bin
%dir %{_libdir}/%{libname}/lib
%dir %{_libdir}/%{libname}/lib/openmpi
%dir %{_mandir}/%{namearch}
%dir %{_mandir}/%{namearch}/man*
%dir %{python_sitearch}/%{libname}
%config(noreplace) %{_sysconfdir}/%{namearch}/*
%{_libdir}/%{libname}/bin/mpi[er]*
%{_libdir}/%{libname}/bin/ompi*
%{_libdir}/%{libname}/bin/opari
%{_libdir}/%{libname}/bin/orte*
%{_libdir}/%{libname}/bin/osh*
%{_libdir}/%{libname}/bin/otf*
%{_libdir}/%{libname}/bin/shmem*
%{_libdir}/%{libname}/lib/*.so.*
%{_mandir}/%{namearch}/man1/mpi[er]*
%{_mandir}/%{namearch}/man1/ompi*
#%{_mandir}/%{namearch}/man1/opal-*
%{_mandir}/%{namearch}/man1/orte*
%{_mandir}/%{namearch}/man1/osh*
%{_mandir}/%{namearch}/man1/shmem*
%{_mandir}/%{namearch}/man7/ompi*
%{_mandir}/%{namearch}/man7/orte*
%{_libdir}/%{libname}/lib/openmpi/*
%{_sysconfdir}/modulefiles/
%dir %{_libdir}/%{libname}/share
%dir %{_libdir}/%{libname}/share/openmpi
%{_libdir}/%{libname}/share/openmpi/doc
%{_libdir}/%{libname}/share/openmpi/amca-param-sets
%{_libdir}/%{libname}/share/openmpi/help*.txt
%{_libdir}/%{libname}/share/openmpi/*-wrapper-data.txt
%{_libdir}/%{libname}/share/openmpi/mca-btl-openib-device-params.ini
%{_libdir}/%{libname}/share/openmpi/mca-coll-ml.config

%files 1.10-devel
%dir %{_includedir}/%{namearch}
%dir %{_libdir}/%{libname}/share/vampirtrace
%{_libdir}/%{libname}/bin/mpi[cCf]*
%{_libdir}/%{libname}/bin/vt*
%{_libdir}/%{libname}/bin/opal_*
%{_includedir}/%{namearch}/*
%{_fmoddir}/%{libname}/
%{_libdir}/%{libname}/lib/*.so
%{_libdir}/%{libname}/lib/lib*.a
%{_libdir}/%{libname}/lib/mpi.mod
%{_mandir}/%{namearch}/man1/mpi[cCf]*
%{_mandir}/%{namearch}/man1/opal_*
%{_mandir}/%{namearch}/man3/*
%{_mandir}/%{namearch}/man7/opal*
%{_libdir}/%{libname}/share/openmpi/openmpi-valgrind.supp
%{_libdir}/%{libname}/share/openmpi/mpi*.txt
%{_libdir}/%{libname}/share/openmpi/orte*.txt
%{_libdir}/%{libname}/share/vampirtrace/*
%{macrosdir}/macros.%{namearch}

%files 1.10-java
%{_libdir}/%{libname}/lib/mpi.jar

%files 1.10-java-devel
%{_libdir}/%{libname}/bin/mpijavac
%{_libdir}/%{libname}/bin/mpijavac.pl
# Currently this only contaings openmpi/javadoc
%{_libdir}/%{libname}/share/doc/
%{_mandir}/%{namearch}/man1/mpijavac.1.gz

%changelog
* Wed Sep 14 2016 Bjarne Saltbaek <bjarne@redsleeve.org> - 1.10.2-2.0
- BR: flex for el6
- Patched for building on ARM
- Added java packages from upstream 2.x spec file

* Thu Jan 28 2016 Michal Schmidt <mschmidt@redhat.com> 1.10.2-2
- Name the binary package "openmpi-1.10". The provide name "openmpi"
  remains to openmpi-1.8 for maximum compatibility with RHEL 6.7.
- Related: rhbz1130442

* Wed Jan 27 2016 Michal Schmidt <mschmidt@redhat.com> 1.10.2-1
- Update to 1.10.2.
- Use versioned directory and module names "openmpi-1.10",
  "openmpi-1.10-$arch".
  The unversioned names remain with openmpi-1.8 (built from compat-openmpi).
- Related: rhbz1130442

* Wed Jan 20 2016 Michal Schmidt <mschmidt@redhat.com> 1.10.1-1
- Update to 1.10.1.
- Backport additional fixes from Fedora.
  - Fortran module install (bug #1154982)
  - Add upstream patch to fix zero size message
  Resolves: rhbz1130442, rhbz1142168

* Mon Jun 2 2014 Jay Fenlason <fenlason@redhat.com> 1.8.1-1
- Upgrade to 1.8.1
  Resolves: rhbz1087968

* Mon Mar 4 2013 Jay Fenlason <fenlason@redhat.com> 1.5.4-2
- Fix the build process by getting rid of the -build patch
  and autogen to fix
  Resolves: rhbz749115

* Mon Feb 13 2012 Jay Fenlason <fenlason@redhat.com> 1.5.4-1
- Clean up provides and requires to close
  Resolves: rhbz768457
- Remove and obsolete the -psm variants that have been folded into the main
  packages.
  Resolves: rhbz758618
- New upstream version
  Resolves: rhbz768109
  Related: rhbz739138

* Tue Oct 18 2011 Jay Fenlason <fenlason@redhat.com> 1.5.3-3
- Remove --enable-mpi-threads to close
  Resolves: rhbz741794

* Wed Aug 17 2011 Jay Fenlason <fenlason@redhat.com> - 1.5.3-2
- Fix the rpm macros for the -psm subpackage, so we can build
  a -psm varient of mpitests
  Related: rhbz725016

* Wed Aug 17 2011 Jay Fenlason <fenlason@redhat.com> - 1.5.3-1
- Conditionalize the psm and psm-devel subpackages, to keep rpmbuild
  from trying to build them on ppc
  Related: rhbz725016

* Tue Aug 16 2011 Jay Fenlason <fenlason@redhat.com> 
- Upgrade to new upstream version
  This disables openib-ibcm, which is broken in 1.5.3
  This brings in esmtp and valgrind memchecker support from Fedora
  Related: rhbz725016

* Fri Jan 28 2011 Jay Fenlason <fenlason@redhat.com> - 1.4.3-1.1
- Add BuildRequires: flex
  Resolves: rhbz661292 - flex missing from br

* Thu Jan 13 2011 Jay Fenlason <fenlason@redhat.com> - 1.4.3-1
- Upgrade to new version
  Resolves: rhbz632371 - [6.1 FEAT] Rebase OpenMPI to 1.4.3 (or later)

* Mon Aug 2 2010 Jay Fenlason <fenlason@redhat.com> - 1.4.1-4.3
- Split the psm support packages into their own rpms to close
  Resolves: rhbz616575 openmpi does not work with non-infinipath hardware

* Fri Jun 4 2010 Jay Fenlason <fenlason@redhat.com> - 1.4.1-4.2
- BuildRequire the infinipath-psm package to pull in support
  for it on x86_64.
  Related: rhbz570274

* Wed Mar 31 2010 Jay Fenlason <fenlason@redhat.com> - 1.4.1-4.1
- Add the -autogen patch so this builds on RHEL-6
  Related: rhbz555835

* Mon Mar 29 2010 Jay Fenlason <fenlason@redhat.com> - 1.4.1-4
- Update to fix licencing and packaging issues:
  Use the system plpa and ltdl librarires rather than the ones in the tarball
  Remove licence incompatible files from the tarball.
- update module.in to prepend-path		PYTHONPATH

* Tue Mar 9 2010 Jay Fenlason <fenlason@redhat.com> - 1.4.1-3
- remove the pkgconfig file completely like we did in RHEL.

* Tue Jan 26 2010 Jay Fenlason <fenlason@redhat.com> - 1.4.1-2
- BuildRequires: python

* Tue Jan 26 2010 Jay Fenlason <fenlason@redhat.com> - 1.4.1-1
- New upstream version, which includes the changeset_r22324 patch.
- Correct a typo in the Source0 line in this spec file.

* Fri Jan 15 2010 Doug Ledford <dledford@redhat.com> - 1.4-4
- Fix an issue with usage of _cc_name_suffix that cause a broken define in
  our module file

* Fri Jan 15 2010 Doug Ledford <dledford@redhat.com> - 1.4-3
- Fix pkgconfig file substitution
- Bump version so we are later than the equivalent version from Red Hat
  Enterprise Linux

* Wed Jan 13 2010 Doug Ledford <dledford@redhat.com> - 1.4-1
- Update to latest upstream stable version
- Add support for libibcm usage
- Enable sge support via configure options since it's no longer on by default
- Add patch to resolve allreduce issue (bz538199)
- Remove no longer needed patch for Chelsio cards

* Tue Sep 22 2009 Jay Fenlason <fenlason@redhat.com> - 1.3.3-6
- Create and own man* directories for use by dependent packages.

* Wed Sep 16 2009 Jay Fenlason <fenlason@redhat.com> - 1.3.3-5
- Move the module file from %%{_datadir}/Modules/modulefiles/%%{namearch} to
  %%{_sysconfdir}/modulefiles/%%{namearch} where it belongs.
- Have the -devel subpackage own the man1 and man7 directories for completeness.
- Add a blank line before the clean section.
- Remove --enable-mpirun-prefix-by-default from configure.

* Wed Sep 9 2009 Jay Fenlason <fenlason@redhat.com> - 1.3.3-4
- Modify packaging to conform to
  https://fedoraproject.org/wiki/PackagingDrafts/MPI (bz521334).
- remove --with-ft=cr from configure, as it was apparently causing problems
  for some people.
- Add librdmacm-devel and librdmacm to BuildRequires (related bz515565).
- Add openmpi-bz515567.patch to add support for the latest Chelsio device IDs
  (related bz515567).
- Add exclude-arch (s390 s390x) because we don't have required -devel packages
  there.

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Doug Ledford <dledford@redhat.com> - 1.3.3-2
- Add MPI_BIN and MPI_LIB to the modules file (related bz511099)

* Tue Jul 21 2009 Doug Ledford <dledford@redhat.com> - 1.3.3-1
- Make sure all created dirs are owned (bz474677)
- Fix loading of pkgconfig file (bz476844)
- Resolve file conflict between us and libotf (bz496131)
- Resolve dangling symlinks issue (bz496909)
- Resolve unexpanded %%{mode} issues (bz496911)
- Restore -devel subpackage (bz499851)
- Make getting the default openmpi devel environment easier (bz504357)
- Make the -devel package pull in the base package (bz459458)
- Make it easier to use alternative compilers to build package (bz246484)

* Sat Jul 18 2009 Jussi Lehtola <jussilehtola@fedoraproject.org> - 1.3.1-4
- Add Provides: openmpi-devel to fix other package builds in rawhide.

* Fri May 08 2009 Lubomir Rintel <lkundrak@v3.sk> - 1.3.1-3
- Treat i586 the same way as i386

* Wed Apr 22 2009 Doug Ledford <dledford@redhat.com> - 1.3.1-2
- fixed broken update
- Resolves: bz496909, bz496131, bz496911

* Tue Apr 14 2009 Tom "spot" Callaway <tcallawa@redhat.com> - 1.3.1-1
- update to 1.3.1, cleanup alternatives, spec, make new vt subpackage

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2.4-2
- Autorebuild for GCC 4.3

* Wed Oct 17 2007 Doug Ledford <dledford@redhat.com> - 1.2.4-1
- Update to 1.2.4 upstream version
- Build against libtorque
- Pass a valid mode to open
- Resolves: bz189441, bz265141

* Tue Aug 28 2007 Fedora Release Engineering <rel-eng at fedoraproject dot org> - 1.2.3-5
- Rebuild for selinux ppc32 issue.

* Mon Jul 16 2007 Doug Ledford <dledford@redhat.com> - 1.2.3-4
- Fix a directory permission problem on the base openmpi directories

* Thu Jul 12 2007 Florian La Roche <laroche@redhat.com> - 1.2.3-3
- requires alternatives for various sub-rpms

* Mon Jul 02 2007 Doug Ledford <dledford@redhat.com> - 1.2.3-2
- Fix dangling symlink issue caused by a bad macro usage
- Resolves: bz246450

* Wed Jun 27 2007 Doug Ledford <dledford@redhat.com> - 1.2.3-1
- Update to latest upstream version
- Fix file ownership on -libs package
- Take a swing at solving the multi-install compatibility issues

* Mon Feb 19 2007 Doug Ledford <dledford@redhat.com> - 1.1.1-7
- Bump version to be at least as high as the RHEL4U5 openmpi
- Integrate fixes made in RHEL4 openmpi into RHEL5 (fix a multilib conflict
  for the openmpi.module file by moving from _datadir to _libdir, make sure
  all sed replacements have the g flag so they replace all instances of
  the marker per line, not just the first, and add a %%defattr tag to the
  files section of the -libs package to avoid install errors about
  brewbuilder not being a user or group)
- Resolves: bz229298

* Wed Jan 17 2007 Doug Ledford <dledford@redhat.com> - 1.1.1-5
- Remove the FORTIFY_SOURCE and stack protect options
- Related: bz213075

* Fri Oct 20 2006 Doug Ledford <dledford@redhat.com> - 1.1.1-4
- Bump and build against the final openib-1.1 package

* Wed Oct 18 2006 Doug Ledford <dledford@redhat.com> - 1.1.1-3
- Fix an snprintf length bug in opal/util/cmd_line.c
- RESOLVES: rhbz#210714

* Wed Oct 18 2006 Doug Ledford <dledford@redhat.com> - 1.1.1-2
- Bump and build against openib-1.1-0.pre1.1 instead of 1.0

* Tue Oct 17 2006 Doug Ledford <dledford@redhat.com> - 1.1.1-1
- Update to upstream 1.1.1 version

* Fri Oct 13 2006 Doug Ledford <dledford@redhat.com> - 1.1-7
- ia64 can't take -m64 on the gcc command line, so don't set it there

* Wed Oct 11 2006 Doug Ledford <dledford@redhat.com> - 1.1-6
- Bump rev to match fc6 rev
- Fixup some issue with alternatives support
- Split the 32bit and 64bit libs ld.so.conf.d files into two files so
  multilib or single lib installs both work properly
- Put libs into their own package
- Add symlinks to /usr/share/openmpi/bin%%{mode} so that opal_wrapper-%%{mode}
  can be called even if it isn't the currently selected default method in
  the alternatives setup (opal_wrapper needs to be called by mpicc, mpic++,
  etc. in order to determine compile mode from argv[0]).

* Sun Aug 27 2006 Doug Ledford <dledford@redhat.com> - 1.1-4
- Make sure the post/preun scripts only add/remove alternatives on initial
  install and final removal, otherwise don't touch.

* Fri Aug 25 2006 Doug Ledford <dledford@redhat.com> - 1.1-3
- Don't ghost the mpi.conf file as that means it will get removed when
  you remove 1 out of a number of alternatives based packages
- Put the .mod file in -devel

* Mon Aug  7 2006 Doug Ledford <dledford@redhat.com> - 1.1-2
- Various lint cleanups
- Switch to using the standard alternatives mechanism instead of a home
  grown one

* Wed Aug  2 2006 Doug Ledford <dledford@redhat.com> - 1.1-1
- Upgrade to 1.1
- Build with Infiniband support via openib

* Mon Jun 12 2006 Jason Vas Dias <jvdias@redhat.com> - 1.0.2-1
- Upgrade to 1.0.2

* Wed Feb 15 2006 Jason Vas Dias <jvdias@redhat.com> - 1.0.1-1
- Import into Fedora Core
- Resolve LAM clashes 

* Wed Jan 25 2006 Orion Poplawski <orion@cora.nwra.com> - 1.0.1-2
- Use configure options to install includes and libraries
- Add ld.so.conf.d file to find libraries
- Add -fPIC for x86_64

* Tue Jan 24 2006 Orion Poplawski <orion@cora.nwra.com> - 1.0.1-1
- 1.0.1
- Use alternatives

* Sat Nov 19 2005 Ed Hill <ed@eh3.com> - 1.0-2
- fix lam conflicts

* Fri Nov 18 2005 Ed Hill <ed@eh3.com> - 1.0-1
- initial specfile created

