# If you're used to Fedora (21ish), here's what's different:
# no nouveau
# no llvmpipe (but m-p-l used for r300/r600/radeonsi)
# bundled glu, manpages, mesa-demos, glx-utils
# three builds of osmesa with pinned soname
# no vdpau drivers
# egl (for glamor), but not gles or wayland
# no dri3

# set this to 1 temporarily when doing llvm rebases, to avoid build loops
%define llvm_rebase 0
%define use_bundled_gcc         1
%define gcc_version             4.8.5-4
#4.8.5-4
# S390 doesn't have video cards, but we need swrast for xserver's GLX
%ifarch s390 s390x
%define with_hardware 0
%define dri_drivers --with-dri-drivers=swrast
%else
%define with_hardware 1
%define base_drivers swrast,radeon,r200
%ifarch %{ix86}
%define platform_drivers ,i915,i965
%define with_vmware 1
%endif
%ifarch x86_64
%define platform_drivers ,i915,i965
%define with_vmware 1
%endif
%ifarch ia64
%define platform_drivers ,i915
%endif
%define dri_drivers --with-dri-drivers=%{base_drivers}%{?platform_drivers}
%endif

%define manpages gl-manpages-1.0.1
%define xdriinfo xdriinfo-1.0.2
%define gitdate 20130625
%define demosgitdate 20101028

%define demopkg %{name}-demos-%{demosgitdate}
%define demodir %{_libdir}/mesa

Summary: Mesa graphics libraries
Name: mesa
Version: 11.0.7
Release: 4%{?dist}
License: MIT
Group: System Environment/Libraries
URL: http://www.mesa3d.org
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

# Source0 is none of these, because sanitize
#Source0: ftp://ftp.freedesktop.org/pub/mesa/%{version}%{?snapshot}/MesaLib-%{version}%{?snapshot}.tar.bz2
#Source0: http://www.mesa3d.org/beta/MesaLib-%{version}%{?snapshot}.tar.bz2
#Source1: http://www.mesa3d.org/beta/MesaDemos-%{version}%{?snapshot}.tar.bz2
#Source0: %{name}-%{gitdate}.tar.xz

Source0: mesa-11.0.7.tar.xz
Source1: %{name}-demos-%{demosgitdate}.tar.bz2
Source2: %{manpages}.tar.bz2
Source3: make-git-snapshot.sh
Source4: ftp://ftp.freedesktop.org/pub/mesa/glu/glu-9.0.0.tar.bz2
Source5: http://www.x.org/pub/individual/app/%{xdriinfo}.tar.bz2
Source300:      gcc-%{gcc_version}.el7.src.rpm

Patch1: mesa-8.1-osmesa-version.patch
Patch10: mesa-demos-glew-hack.patch
Patch15: mesa-9.2-hardware-float.patch
Patch31: mesa-7.6-glx13-app-warning.patch

# kwin doesn't work with msaa enabled
Patch57: intel-disable-msaa.patch

# Just useless header with painfull license
Patch59: drop-chromium.patch

# skl updates
Patch70: 0001-i965-gen9-Switch-thread-scratch-space-to-non-coheren.patch


# GCC 4.8 BuildRequires
# ==================================================================================
%if %{use_bundled_gcc}

%ifarch %{arm}
BuildRequires: libmpc-devel >= 0.8
BuildRequires: gcc-java
%endif
%ifarch s390x
%global multilib_32_arch s390
%endif
%ifarch sparc64
%global multilib_32_arch sparcv9
%endif
%ifarch ppc64
%global multilib_32_arch ppc
%endif
%ifarch x86_64
%if 0%{?rhel} >= 6
%global multilib_32_arch i686
%else
%global multilib_32_arch i386
%endif
%endif

%global multilib_64_archs sparc64 ppc64 s390x x86_64

%if 0%{?rhel} >= 6
# Need binutils which support --build-id >= 2.17.50.0.17-3
# Need binutils which support %gnu_unique_object >= 2.19.51.0.14
# Need binutils which support .cfi_sections >= 2.19.51.0.14-33
BuildRequires: binutils >= 2.19.51.0.14-33
# While gcc doesn't include statically linked binaries, during testing
# -static is used several times.
BuildRequires: glibc-static
%else
# Don't have binutils which support --build-id >= 2.17.50.0.17-3
# Don't have binutils which support %gnu_unique_object >= 2.19.51.0.14
# Don't have binutils which  support .cfi_sections >= 2.19.51.0.14-33
BuildRequires: binutils >= 2.17.50.0.2-8
%endif
BuildRequires: zlib-devel, gettext, dejagnu, bison, flex, texinfo, sharutils
BuildRequires: /usr/bin/pod2man
%if 0%{?rhel} >= 7
BuildRequires: texinfo-tex
%endif
#BuildRequires: systemtap-sdt-devel >= 1.3
# For VTA guality testing
BuildRequires: gdb
# Make sure pthread.h doesn't contain __thread tokens
# Make sure glibc supports stack protector
# Make sure glibc supports DT_GNU_HASH
BuildRequires: glibc-devel >= 2.4.90-13
%if 0%{?rhel} >= 6
BuildRequires: elfutils-devel >= 0.147
BuildRequires: elfutils-libelf-devel >= 0.147
%else
BuildRequires: elfutils-devel >= 0.72
%endif
%ifarch ppc ppc64 s390 s390x sparc sparcv9 alpha
# Make sure glibc supports TFmode long double
BuildRequires: glibc >= 2.3.90-35
%endif
%ifarch %{multilib_64_archs} sparcv9 ppc
# Ensure glibc{,-devel} is installed for both multilib arches
BuildRequires: /lib/libc.so.6 /usr/lib/libc.so /lib64/libc.so.6 /usr/lib64/libc.so
%endif
%ifarch ia64
BuildRequires: libunwind >= 0.98
%endif
# Need .eh_frame ld optimizations
# Need proper visibility support
# Need -pie support
# Need --as-needed/--no-as-needed support
# On ppc64, need omit dot symbols support and --non-overlapping-opd
# Need binutils that owns /usr/bin/c++filt
# Need binutils that support .weakref
# Need binutils that supports --hash-style=gnu
# Need binutils that support mffgpr/mftgpr
#%if 0%{?rhel} >= 6
## Need binutils which support --build-id >= 2.17.50.0.17-3
## Need binutils which support %gnu_unique_object >= 2.19.51.0.14
## Need binutils which support .cfi_sections >= 2.19.51.0.14-33
#Requires: binutils >= 2.19.51.0.14-33
#%else
## Don't have binutils which support --build-id >= 2.17.50.0.17-3
## Don't have binutils which support %gnu_unique_object >= 2.19.51.0.14
## Don't have binutils which  support .cfi_sections >= 2.19.51.0.14-33
#Requires: binutils >= 2.17.50.0.2-8
#%endif
## Make sure gdb will understand DW_FORM_strp
#Conflicts: gdb < 5.1-2
#Requires: glibc-devel >= 2.2.90-12
#%ifarch ppc ppc64 s390 s390x sparc sparcv9 alpha
## Make sure glibc supports TFmode long double
#Requires: glibc >= 2.3.90-35
#%endif
#Requires: libgcc >= 4.1.2-43
#Requires: libgomp >= 4.4.4-13
#%if 0%{?rhel} == 6
#Requires: libstdc++ >= 4.4.4-13
#%else
#Requires: libstdc++ = 4.1.2
#%endif
##FIXME gcc version
#Requires: libstdc++-devel = %{version}-%{release}
BuildRequires: gmp-devel >= 4.1.2-8
%if 0%{?rhel} >= 6
BuildRequires: mpfr-devel >= 2.2.1
%endif
%if 0%{?rhel} >= 7
BuildRequires: libmpc-devel >= 0.8.1
%endif

%endif # bundled gcc BuildRequires

BuildRequires: pkgconfig autoconf automake libtool
%if %{with_hardware}
BuildRequires: kernel-headers >= 2.6.27-0.305.rc5.git6
%endif
BuildRequires: libdrm-devel >= 2.4.37
BuildRequires: libXxf86vm-devel
BuildRequires: expat-devel >= 2.0
BuildRequires: xorg-x11-proto-devel >= 7.1-10
BuildRequires: makedepend
BuildRequires: libselinux-devel
BuildRequires: libXext-devel
%if !0%{?llvm_rebase}
BuildRequires: freeglut-devel
%endif
BuildRequires: mesa-libGL-devel
# aieee, but, needed for GLU bootstrap
BuildRequires: libXfixes-devel
BuildRequires: libXdamage-devel
BuildRequires: libXi-devel
BuildRequires: libXmu-devel
BuildRequires: elfutils
BuildRequires: python
BuildRequires: python-mako
BuildRequires: libxml2-python
BuildRequires: bison flex
BuildRequires: chrpath
BuildRequires: gettext
BuildRequires: libudev-devel
%ifnarch s390 s390x ppc
BuildRequires: mesa-private-llvm-devel
BuildRequires: elfutils-libelf-devel
%endif

%description
Mesa

%package libGL
Summary: Mesa libGL runtime libraries and DRI drivers
Group: System Environment/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libGL
Requires: mesa-dri-drivers%{?_isa} = %{version}-%{release}
Requires: libX11 > 1.6
%if %{with_hardware}
Requires: libdrm >= 2.4.24-1
Conflicts: xorg-x11-server-Xorg < 1.4.99.901-14
%endif

%description libGL
Mesa libGL runtime library.

%package libEGL
Summary: Mesa libEGL runtime libraries
Group: System Environment/Libraries

%description libEGL
Mesa libEGL runtime libraries

%package dri-filesystem
Summary: Mesa DRI driver filesystem
Group: User Interface/X Hardware Support
%description dri-filesystem
Mesa DRI driver filesystem

%package dri-drivers
Summary: Mesa-based DRI drivers
Group: User Interface/X Hardware Support
Requires: mesa-dri-filesystem%{?_isa}
Provides: mesa-dri-drivers-experimental = %{version}-%{release}
Obsoletes: mesa-dri-drivers-experimental < %{version}-%{release}
%ifnarch s390 s390x
Requires: mesa-dri1-drivers >= 7.11-6
%endif
%description dri-drivers
Mesa-based DRI drivers.


%package libGL-devel
Summary: Mesa libGL development package
Group: Development/Libraries
Requires: mesa-libGL = %{version}-%{release}
Requires: libX11-devel
Provides: libGL-devel
Conflicts: xorg-x11-proto-devel <= 7.2-12

%description libGL-devel
Mesa libGL development package


%package libEGL-devel
Summary: Mesa libEGL development package
Group: Development/Libraries
Requires: mesa-libEGL = %{version}-%{release}
Provides: khrplatform-devel = %{version}-%{release}
Obsoletes: khrplatform-devel < %{version}-%{release}

%description libEGL-devel
Mesa libEGL development package


%package libGLU
Summary: Mesa libGLU runtime library
Group: System Environment/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libGLU

%description libGLU
Mesa libGLU runtime library


%package libGLU-devel
Summary: Mesa libGLU development package
Group: Development/Libraries
Requires: mesa-libGLU = %{version}-%{release}
Requires: libGL-devel
Provides: libGLU-devel

%description libGLU-devel
Mesa libGLU development package

%package libOSMesa
Summary: Mesa offscreen rendering libraries
Group: System Environment/Libraries
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Provides: libOSMesa

%description libOSMesa
Mesa offscreen rendering libraries


%package libOSMesa-devel
Summary: Mesa offscreen rendering development package
Group: Development/Libraries
Requires: mesa-libOSMesa = %{version}-%{release}

%description libOSMesa-devel
Mesa offscreen rendering development package


%if !0%{?llvm_rebase}
%package -n glx-utils
Summary: GLX utilities
Group: Development/Libraries

%description -n glx-utils
The glx-utils package provides the glxinfo and glxgears utilities.


%package demos
Summary: Mesa demos
Group: Development/Libraries

%description demos
This package provides some demo applications for testing Mesa.
%endif


%package libgbm
Summary: Mesa gbm library
Group: System Environment/Libraries
Provides: libgbm

%description libgbm
Mesa gbm runtime library.


%package libgbm-devel
Summary: Mesa libgbm development package
Group: Development/Libraries
Requires: mesa-libgbm%{?_isa} = %{version}-%{release}
Provides: libgbm-devel

%description libgbm-devel
Mesa libgbm development package

%if 0%{?with_vmware}
%package libxatracker
Summary: Mesa XA state tracker for vmware
Group: System Environment/Libraries
Provides: libxatracker

%description libxatracker
Mesa XA state tracker for vmware

%package libxatracker-devel
Summary: Mesa XA state tracker development package
Group: Development/Libraries
Requires: mesa-libxatracker%{?_isa} = %{version}-%{release}
Provides: libxatracker-devel

%description libxatracker-devel
Mesa XA state tracker development package
%endif

%prep
%setup -q -n mesa-%{version}%{?snapshot} -b1 -b2 -b4 -b5
#setup -q -n mesa-%{gitdate} -b1 -b2 -b4 -b5
grep -q ^/ src/gallium/auxiliary/vl/vl_decoder.c && exit 1
%patch1 -p1 -b .osmesa
%patch15 -p1 -b .hwfloat
%patch31 -p1 -b .glx13-warning
%patch57 -p1 -b .nomsaa
%patch59 -p1 -b .drop-chromium
%patch70 -p1 -b .skl0

sed -i 's/\[llvm-config\]/\[mesa-private-llvm-config-%{__isa_bits}\]/g' configure.ac
sed -i 's/`$LLVM_CONFIG --version`/$LLVM_VERSION_MAJOR.$LLVM_VERSION_MINOR-mesa/' configure.ac
# 147 is fine if you're not building dri3
sed -i 's/LIBUDEV_REQUIRED=151/LIBUDEV_REQUIRED=147/' configure.ac

pushd ../%{demopkg}
# make idempotent
rm -f src/glew/Makefile.am
%patch10 -p1 -b .glew-hack
# Hack the demos to use installed data files
sed -i 's,../images,%{_libdir}/mesa,' src/demos/*.c
sed -i 's,geartrain.dat,%{_libdir}/mesa/&,' src/demos/geartrain.c
sed -i 's,isosurf.dat,%{_libdir}/mesa/&,' src/demos/isosurf.c
sed -i 's,terrain.dat,%{_libdir}/mesa/&,' src/demos/terrain.c
popd

%build
%if %{use_bundled_gcc}
GCC_FILE="gcc48-%{gcc_version}*.rpm"
GCC_PATH="%{_rpmdir}"

rpmbuild --nodeps --rebuild %{SOURCE300}
cd %{_rpmdir}
if [ ! -f $GCC_PATH/$GCC_FILE ]; then
    GCC_PATH="$GCC_PATH/%{_arch}"
fi
rpm2cpio $GCC_PATH/$GCC_FILE | cpio -iduv
# Clean gcc48 rpms to avoid including them to package
rm -f gcc48-*.rpm
cd -
PATH=%{_rpmdir}/usr/bin:$PATH
export PATH
export CXX=g++
%endif  # bundled gcc

# default to dri (not xlib) for libGL on all arches
# XXX please fix upstream
sed -i 's/^default_driver.*$/default_driver="dri"/' configure.ac

autoreconf --install -f -v

export CFLAGS="$RPM_OPT_FLAGS -fvisibility=hidden"
export CXXFLAGS="$RPM_OPT_FLAGS -fvisibility=hidden"
%ifarch %{ix86}
# i do not have words for how much the assembly dispatch code infuriates me
%define common_flags --enable-selinux --enable-pic --disable-asm
%else
%define common_flags --enable-selinux --enable-pic
%endif 
%define osmesa_flags --enable-osmesa --disable-gallium-osmesa %{common_flags} --with-gallium-drivers="" --with-dri-drivers="" --disable-egl --disable-dri

# pick up the 8 bpc from mesa build
%configure %{osmesa_flags} --with-osmesa-bits=16
make SRC_DIRS="mapi/glapi/gen mapi/glapi glsl mesa"
mv %{_lib} osmesa16
make clean

%configure %{osmesa_flags} --with-osmesa-bits=32
make SRC_DIRS="mapi/glapi/gen mapi/glapi glsl mesa"
mv %{_lib} osmesa32
make clean

# just to be sure...
[ `find . -name \*.o | wc -l` -eq 0 ] || exit 1

# XXX should get visibility working again post-dricore.
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"

# now build the rest of mesa
%configure %{common_flags} \
    --enable-osmesa \
    --enable-egl \
    --disable-gles1 \
    --disable-gles2 \
    --enable-gbm \
    --enable-glx-tls \
    --disable-opencl \
    --disable-xvmc \
    --disable-dri3 \
    --with-dri-driverdir=%{_libdir}/dri \
    --enable-texture-float=yes \
%if %{with_hardware}
    %{?with_vmware:--enable-xa} \
    --with-egl-platforms=x11,drm \
%ifnarch ppc
    --enable-gallium-llvm \
    --with-gallium-drivers=%{?with_vmware:svga,swrast,}"r300,r600,radeonsi" \
%else
    --disable-gallium-llvm \
    --with-gallium-drivers="r300,r600" \
%endif
%else
    --with-egl-platforms=x11 \
    --with-gallium-drivers="" \
    --disable-driglx-direct \
%endif
    %{?dri_drivers}

make V=1 %{?_smp_mflags}

pushd ../glu-9.0.0
%configure --disable-static
make %{?_smp_mflags}
popd

%if !0%{?llvm_rebase}
pushd ../%{demopkg}
autoreconf -v --install
%configure --bindir=%{demodir}
make %{?_smp_mflags}
popd

pushd ../%{xdriinfo}
%configure
make %{?_smp_mflags}
popd
%endif

pushd ../%{manpages}
autoreconf -v --install
%configure
make %{?_smp_mflags}
popd

%install
rm -rf $RPM_BUILD_ROOT

# core libs and headers, but not drivers.
make install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/dri/kms_swrast_dri.so

# strip out stupid rpath
chrpath -d $RPM_BUILD_ROOT%{_libdir}/dri/*_dri.so

# strip out undesirable headers
pushd $RPM_BUILD_ROOT%{_includedir}/GL 
rm -f [a-fh-np-wyz]*.h gg*.h glf*.h glew.h glut*.h glxew.h
popd

pushd ../glu-9.0.0
make %{?_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT
popd

# remove .la files
find $RPM_BUILD_ROOT -name \*.la | xargs rm -f

%if !0%{?llvm_rebase}
pushd ../%{demopkg}
# XXX demos, since they don't install automatically.  should fix that.
install -d $RPM_BUILD_ROOT%{_bindir}
install -m 0755 src/xdemos/glxgears $RPM_BUILD_ROOT%{_bindir}
install -m 0755 src/xdemos/glxinfo $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{demodir}
find src/demos/ -type f -perm /0111 |
    xargs install -m 0755 -t $RPM_BUILD_ROOT/%{demodir}
install -m 0644 src/images/*.rgb $RPM_BUILD_ROOT/%{demodir}
install -m 0644 src/demos/*.dat $RPM_BUILD_ROOT/%{demodir}
popd
pushd ../%{xdriinfo}
make %{?_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT
popd
%endif

# and osmesa
mv osmesa*/*OSMesa* $RPM_BUILD_ROOT%{_libdir}
chrpath -d $RPM_BUILD_ROOT%{_libdir}/libOSMesa*.so*

# man pages
pushd ../%{manpages}
make %{?_smp_mflags} install DESTDIR=$RPM_BUILD_ROOT
popd

# this keeps breaking, check it early.  note that the exit from eu-ftr is odd.
pushd $RPM_BUILD_ROOT%{_libdir}
for i in libOSMesa*.so libGL.so ; do
    eu-findtextrel $i && exit 1
done

%clean
rm -rf $RPM_BUILD_ROOT

%check

%post libGL -p /sbin/ldconfig
%postun libGL -p /sbin/ldconfig
%post libGLU -p /sbin/ldconfig
%postun libGLU -p /sbin/ldconfig
%post libOSMesa -p /sbin/ldconfig
%postun libOSMesa -p /sbin/ldconfig
%post libEGL -p /sbin/ldconfig
%postun libEGL -p /sbin/ldconfig
%post libgbm -p /sbin/ldconfig
%postun libgbm -p /sbin/ldconfig
%if 0%{?with_vmware}
%post libxatracker -p /sbin/ldconfig
%postun libxatracker -p /sbin/ldconfig
%endif

%files libGL
%defattr(-,root,root,-)
%{_libdir}/libGL.so.1
%{_libdir}/libGL.so.1.*

%files libEGL
%defattr(-,root,root,-)
%{_libdir}/libEGL.so.1
%{_libdir}/libEGL.so.1.*

%files dri-filesystem
%defattr(-,root,root,-)
%doc docs/COPYING
%dir %{_libdir}/dri

%files dri-drivers
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/drirc
%if %{with_hardware}
%{_libdir}/dri/radeon_dri.so
%{_libdir}/dri/r200_dri.so
%{_libdir}/dri/r300_dri.so
%{_libdir}/dri/r600_dri.so
%ifnarch ppc
%{_libdir}/dri/radeonsi_dri.so
%endif
%ifarch %{ix86} x86_64 ia64
%{_libdir}/dri/i915_dri.so
%ifnarch ia64
%{_libdir}/dri/i965_dri.so
%endif
%if 0%{?with_vmware}
%{_libdir}/dri/vmwgfx_dri.so
%endif
%endif
%endif
%{_libdir}/dri/swrast_dri.so
%{_libdir}/libglapi*.so*

%files libGL-devel
%defattr(-,root,root,-)
%{_includedir}/GL/gl.h
%{_includedir}/GL/glcorearb.h
%{_includedir}/GL/gl_mangle.h
%{_includedir}/GL/glext.h
%{_includedir}/GL/glx.h
%{_includedir}/GL/glx_mangle.h
%{_includedir}/GL/glxext.h
%dir %{_includedir}/GL/internal
%{_includedir}/GL/internal/dri_interface.h
%{_libdir}/pkgconfig/dri.pc
%{_libdir}/libGL.so
%{_libdir}/pkgconfig/gl.pc
%{_datadir}/man/man3/gl[^uX]*.3gl*
%{_datadir}/man/man3/glX*.3gl*

%files libEGL-devel
%defattr(-,root,root,-)
%dir %{_includedir}/EGL
%{_includedir}/EGL/eglext.h
%{_includedir}/EGL/egl.h
%{_includedir}/EGL/eglmesaext.h
%{_includedir}/EGL/eglplatform.h
%dir %{_includedir}/KHR
%{_includedir}/KHR/khrplatform.h
%{_libdir}/pkgconfig/egl.pc
%{_libdir}/libEGL.so

%files libGLU
%defattr(-,root,root,-)
%{_libdir}/libGLU.so.1
%{_libdir}/libGLU.so.1.3.*

%files libGLU-devel
%defattr(-,root,root,-)
%{_libdir}/libGLU.so
%{_libdir}/pkgconfig/glu.pc
%{_includedir}/GL/glu.h
%{_includedir}/GL/glu_mangle.h
%{_datadir}/man/man3/glu*.3gl*

%files libOSMesa
%defattr(-,root,root,-)
%{_libdir}/libOSMesa.so.6*
%{_libdir}/libOSMesa16.so.6*
%{_libdir}/libOSMesa32.so.6*

%files libOSMesa-devel
%defattr(-,root,root,-)
%{_includedir}/GL/osmesa.h
%{_libdir}/libOSMesa.so
%{_libdir}/libOSMesa16.so
%{_libdir}/libOSMesa32.so
%{_libdir}/pkgconfig/osmesa.pc

%if !0%{?llvm_rebase}
%files -n glx-utils
%defattr(-,root,root,-)
%{_bindir}/glxgears
%{_bindir}/glxinfo
%{_bindir}/xdriinfo
%{_datadir}/man/man1/xdriinfo.1*

%files demos
%defattr(-,root,root,-)
%{demodir}
%endif

%files libgbm
%defattr(-,root,root,-)
%doc docs/COPYING
%{_libdir}/libgbm.so.1
%{_libdir}/libgbm.so.1.*

%files libgbm-devel
%defattr(-,root,root,-)
%{_libdir}/libgbm.so
%{_includedir}/gbm.h
%{_libdir}/pkgconfig/gbm.pc

%if 0%{?with_vmware}
%files libxatracker
%defattr(-,root,root,-)
%doc docs/COPYING
%if %{with_hardware}
%{_libdir}/libxatracker.so.2
%{_libdir}/libxatracker.so.2.*
%endif

%files libxatracker-devel
%defattr(-,root,root,-)
%if %{with_hardware}
%{_libdir}/libxatracker.so
%{_includedir}/xa_tracker.h
%{_includedir}/xa_composite.h
%{_includedir}/xa_context.h
%{_libdir}/pkgconfig/xatracker.pc
%endif
%endif

%changelog
* Tue Mar 08 2016 Adam Jackson <ajax@redhat.com> - 11.0.7-4
- Updates for new skylake parts

* Wed Dec 09 2015 Dave Airlie <airlied@redhat.com> 11.0.7-1
- 11.0.7 rebase + enable llvmpipe on x86

* Sun Dec 06 2015 Dave Airlie <airlied@redhat.com> 10.6.9-6
- final stage - reenable everything, 10.6.9

* Sun Dec 06 2015 Dave Airlie <airlied@redhat.com> 10.6.9-5
- reenable GLU - rebase step two.

* Sun Dec 06 2015 Dave Airlie <airlied@redhat.com> 10.6.9-4
- use gcc that built mesa-private-llvm.

* Fri Dec 04 2015 Dave Airlie <airlied@redhat.com> 10.6.9-3
- rebuild for mesa-private-llvm 3.6.2

* Mon Nov 16 2015 Dave Airlie <airlied@redhat.com> 10.6.9-2
- enable vmwgfx and llvmpipe

* Mon Nov 16 2015 Dave Airlie <airlied@redhat.com> 10.6.9-1
- rebase to 10.6.9

* Tue Jun 03 2014 Adam Jackson <ajax@redhat.com> 10.1.2-2
- Fix fallback to software on unknown Intel, Broadwell in particular

* Wed May 07 2014 Jérôme Glisse <jglisse@redhat.com> 10.1.2-1
- Update to 10.1.2 to fix various gpu lockup on r6xx, r7xx.

* Thu Apr 24 2014 Adam Jackson <ajax@redhat.com> 10.1.1-2
- Make libGL Require: sufficiently new libX11 for internal API

* Tue Apr 22 2014 Adam Jackson <ajax@redhat.com> 10.1.1-1
- Bootstrap stage three, re-enable demos

* Tue Apr 22 2014 Adam Jackson <ajax@redhat.com> 10.1.1-0.2
- Bootstrap stage two, enable GLU

* Tue Apr 22 2014 Adam Jackson <ajax@redhat.com> 10.1.1-0.1
- Rebase to Mesa 10.1.1
- Initial rebuild against llvm 3.4
- Add llvm_rebase macro for future convenience

* Thu Dec 05 2013 Dave Airlie <airlied@redhat.com> 9.2-0.7
- further fix to the inversion fix (#987701)

* Tue Dec 03 2013 Dave Airlie <airlied@redhat.com> 9.2-0.6
- fix glxinfo on Citrix and inverted swrast rendering (#1025714, #987701)

* Thu Sep 12 2013 Dave Airlie <airlied@redhat.com> 9.2-0.5
- fix packaging tps test (#1000467)

* Wed Jul 10 2013 Jerome Glisse <ajax@redhat.com> 9.2-0.4
- Fix egl backend flags for glamor

* Wed Jul 10 2013 Jerome Glisse <ajax@redhat.com> 9.2-0.3
- Add libgbm subpackages for glamor

* Wed Jun 26 2013 Adam Jackson <ajax@redhat.com> 9.2-0.2
- Add libEGL subpackages for glamor

* Tue Jun 25 2013 Adam Jackson <ajax@redhat.com> 9.2-0.1
- Rebase to 9.2-pre

* Thu May 30 2013 Dave Airlie <airlied@redhat.com> 9.0-0.9
- CVE-2013-1872: Updated patch from upstream (#963063)

* Wed May 22 2013 Dave Airlie <airlied@redhat.com< 9.0-0.8.1
- CVE-2013-1872: Updated patch (#963063)

* Mon May 20 2013 Dave Airlie <airlied@redhat.com> 9.0-0.8
- CVE-2013-1872: memory corruption oob read/write on intel (#963063)
- CVE-2013-1993: interger overflows in protocol handling (#961613)

* Fri Jan 25 2013 Dave Airlie <airlied@redhat.com> 9.0-0.7
- CVE-2012-5129: heap buffer overflow in glGetUniform* (#903933)

* Thu Jan 24 2013 Adam Jackson <ajax@redhat.com> 9.0-0.6
- Quieten driver load failure messages when the display is possibly non-
  local (#901627)

* Wed Dec 19 2012 Dave Airlie <airlied@redhat.com> 9.0-0.3
- block intel msaa so kwin doesn't regress (#885882)

* Tue Oct 02 2012 Dave Airlie <airlied@redhat.com> 9.0-0.2
- fix mesa-dri-filesystem requires.

* Mon Sep 24 2012 Dave Airlie <airlied@redhat.com> 9.0-0.1
- realign with upstream version for rebase + glu

* Sat Sep 22 2012 Dave Airlie <airlied@redhat.com> 8.1-0.20
- fix osmesa harder, noticed by rpmdiff

* Fri Sep 21 2012 Adam Jackson <ajax@redhat.com> 8.1-0.19
- Fix pthread linkage of glapi and osmesa
- Drop llvmpipe-related patches
- Don't require mesa-dri1-drivers on s390{,x}

* Fri Sep 21 2012 Dave Airlie <airlied@redhat.com> 8.1-0.18
- add mesa-dri1-drivers requires

* Wed Aug 22 2012 Dave Airlie <airlied@redhat.com> 8.1-0.17
- bump for osmesa fixes

* Wed Aug 01 2012 Dave Airlie <airlied@redhat.com> 8.1-0.16
- initial import of 8.1 snapshot from Fedora

* Wed May 16 2012 Dave Airlie <airlied@redhat.com> 7.11-5
- Add missing Ivybridge server PCI ID. (#821873)

* Wed Feb 29 2012 Jerome Glisse <jglisse@redhat.com> 7.11-4
- Resolves: rhbz#788168 (r600g add new pci ids)

* Mon Oct 17 2011 Adam Jackson <ajax@redhat.com> 7.11-3
- Drop nouveau (#745686)

* Thu Oct 06 2011 Adam Jackson <ajax@redhat.com> 7.11-2
- mesa-7.11-b9c7773e.patch: Sync with 7.11 branch
- mesa-7.11-gen6-depth-stalls.patch: Fix GPU hangs on gen6+ in openarena
  and others (#741806)
- Drop tdfx_dri.so, as there's no glide3 package or drm support in el6.

* Tue Aug 09 2011 Adam Jackson <ajax@redhat.com> 7.11-1
- Mesa 7.11 final plus stable backports

* Fri Jul 22 2011 Ben Skeggs <bskeggs@redhat.com> 7.11-0.6
- fix mesa-libGL requires

* Wed Jul 20 2011 Adam Jackson <ajax@redhat.com> 7.11-0.5
- Prov/Obs for -experimental

* Wed Jul 20 2011 Adam Jackson <ajax@redhat.com> 7.11-0.4
- Today's 7.11 branch snapshot, 7.11-rc2 plus one
- Drop (empty) -experimental subpackage

* Mon Jul 18 2011 Adam Jackson <ajax@redhat.com> 7.11-0.3
- Today's 7.11 branch snapshot.

* Wed Jul 13 2011 Adam Jackson <ajax@redhat.com> 7.11-0.2
- Mesa rebase: 7.11-rc1 plus updates through a20a9508 (#713772)

* Fri Jan 14 2011 Dave Airlie <airlied@redhat.com> 7.10-1
- enable Intel Sandybridge support (#667563)

* Mon Apr 12 2010 Dave Airlie <airlied@redhat.com> 7.7-2
- update to mesa 7.7.1 release
