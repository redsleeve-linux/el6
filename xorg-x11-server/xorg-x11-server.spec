# This package is an experiment in active integration of upstream SCM with
# Fedora packaging.  It works something like this:
#
# The "pristine" source is actually a git repo (with no working checkout).
# The first step of %%prep is to check it out and switch to a "fedora" branch.
# If you need to add a patch to the server, just do it like a normal git
# operation, dump it with git-format-patch to a file in the standard naming
# format, and add a PatchN: line.  If you want to push something upstream,
# check out the master branch, pull, cherry-pick, and push.

#global gitdate 20131118
%global stable_abi 1

%if !0%{?gitdate} || %{stable_abi}
# Released ABI versions.  Have to keep these manually in sync with the
# source because rpm is a terrible language.
%global ansic_major 0
%global ansic_minor 4
%global videodrv_major 19
%global videodrv_minor 0
%global xinput_major 21
%global xinput_minor 0
%global extension_major 9
%global extension_minor 0
%endif

%if 0%{?gitdate}
# For git snapshots, use date for major and a serial number for minor
%global minor_serial 0
%global git_ansic_major %{gitdate}
%global git_ansic_minor %{minor_serial}
%global git_videodrv_major %{gitdate}
%global git_videodrv_minor %{minor_serial}
%global git_xinput_major %{gitdate}
%global git_xinput_minor %{minor_serial}
%global git_extension_major %{gitdate}
%global git_extension_minor %{minor_serial}
%endif

%global pkgname xorg-server

Summary:   X.Org X11 X server
Name:      xorg-x11-server
Version:   1.17.4
Release:   9.5%{?gitdate:.%{gitdate}}%{?dist}.0
URL:       http://www.x.org
License:   MIT
Group:     User Interface/X

#VCS:      git:git://git.freedesktop.org/git/xorg/xserver
%if 0%{?gitdate}
# git snapshot.  to recreate, run:
# ./make-git-snapshot.sh `cat commitid`
#Source0:   xorg-server-%{gitdate}.tar.xz
Source0:   http://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.bz2
Source1:   make-git-snapshot.sh
Source2:   commitid
%else
Source0:   http://www.x.org/pub/individual/xserver/%{pkgname}-%{version}.tar.bz2
Source1:   gitignore
%endif

Source4:   10-quirks.conf

Source10:   xserver.pamd

# "useful" xvfb-run script
Source20:  http://svn.exactcode.de/t2/trunk/package/xorg/xorg-server/xvfb-run.sh

# for requires generation in drivers
Source30: xserver-sdk-abi-requires.release
Source31: xserver-sdk-abi-requires.git

# maintainer convenience script
Source40: driver-abi-rebuild.sh

# pam and other mustard
Patch0001: 0005-Enable-PAM-support.patch
#Patch0002: 0006-modes-Combine-xf86DefaultModes-and-DMTModes.patch
Patch0003: 0009-Re-add-nr-command-line-option-for-gdm-compatibility.patch
Patch0004: 0011-xfree86-Lid-status-hack.patch
Patch0005: 0014-vbe-Only-interpret-complete-failure-as-DDC-unsupport.patch

# need to rebase these two!
Patch0010: 0001-ephyr-Add-notresizeable-option-to-make-windows-non-r.patch
# RHEL6 - different default, do not remove
Patch0011: 0001-RHEL6-make-ephyr-resizable-by-default.patch

# Trivial things to never merge upstream ever:
# This really could be done prettier.
Patch5002: xserver-1.4.99-ssh-isnt-local.patch

Patch6030: 0001-right-of.patch
#Patch6044: xserver-1.6.99-hush-prerelease-warning.patch

Patch7025: 0001-Always-install-vbe-and-int10-sdk-headers.patch

# do not upstream - do not even use here yet
Patch7027: xserver-autobind-hotplug.patch

# extra magic to be upstreamed
Patch9003: 0001-link-with-z-now.patch

# submitted: http://lists.x.org/archives/xorg-devel/2013-October/037996.html
Patch9100: exa-only-draw-valid-trapezoids.patch

Patch9205: 0001-xfree86-Allow-mixed-fbdev-and-pci-setups.patch

# Bug 1122652 - XGrabPointer() returned unexpected code: 0
Patch9207: 0001-dix-Fix-GrabPointer-to-not-wrongly-succeed-on-redire.patch

# Bug 1138353 - Backing store does not work with application in RHEL 6.5
Patch9312: 0001-composite-Implement-backing-store-Always.patch

Patch9300: 0001-rpath-hack.patch

# Bug 1179840 - [RFE] Enable "maxclients" option in x server
Patch9400: 0001-configurable-maximum-number-of-clients.patch
Patch9401: 0001-dix-Enable-indirect-GLX-by-default-add-xorg.conf-opt.patch

%global moduledir	%{_libdir}/xorg/modules
%global drimoduledir	%{_libdir}/dri
%global sdkdir		%{_includedir}/xorg

%ifarch s390 s390x
%global with_hw_servers 0
%else
%global with_hw_servers 1
%endif

%if %{with_hw_servers}
%global enable_xorg --enable-xorg
%else
%global enable_xorg --disable-xorg
%endif

%global kdrive --enable-kdrive --enable-xephyr --disable-xfake --disable-xfbdev
%global xservers --enable-xvfb --enable-xnest %{kdrive} %{enable_xorg}

BuildRequires: systemtap-sdt-devel
BuildRequires: git-core
BuildRequires: automake autoconf libtool pkgconfig
BuildRequires: xorg-x11-util-macros >= 1.17

BuildRequires: xorg-x11-proto-devel >= 7.7-13
BuildRequires: xorg-x11-font-utils >= 7.2-11

BuildRequires: xorg-x11-xtrans-devel >= 1.3.2
BuildRequires: libXfont-devel libXau-devel libxkbfile-devel libXres-devel
BuildRequires: libfontenc-devel libXtst-devel libXdmcp-devel
BuildRequires: libX11-devel libXext-devel
BuildRequires: libXinerama-devel libXi-devel
BuildRequires: pam-devel
BuildRequires: libepoxy-devel
BuildRequires: pkgconfig(gbm)
BuildRequires: mesa-libEGL-devel
BuildRequires: libxshmfence-devel

# DMX config utils buildreqs.
BuildRequires: libXt-devel libdmx-devel libXmu-devel libXrender-devel
BuildRequires: libXi-devel libXpm-devel libXaw-devel libXfixes-devel

%if !0%{?rhel}
BuildRequires: wayland-devel pkgconfig(wayland-client)
BuildRequires: pkgconfig(xshmfence) >= 1.1
%endif
BuildRequires: libXv-devel
BuildRequires: pixman-devel >= 0.30.0
BuildRequires: libpciaccess-devel >= 0.13.1 openssl-devel byacc flex
BuildRequires: mesa-libGL-devel >= 9.2
# XXX silly...
BuildRequires: libdrm-devel >= 2.4.0 kernel-headers

BuildRequires: audit-libs-devel libselinux-devel >= 2.0.86-1
BuildRequires: hal-devel
%if !0%{?rhel}
# libunwind is Exclusive for the following arches
%ifarch aarch64 %{arm} hppa ia64 mips ppc ppc64 %{ix86} x86_64
BuildRequires: libunwind-devel
%endif
%endif

BuildRequires: pkgconfig(xcb-aux)
BuildRequires: pkgconfig(xcb-image)
BuildRequires: pkgconfig(xcb-icccm)
BuildRequires: pkgconfig(xcb-keysyms)
BuildRequires: pkgconfig(xcb-renderutil)

# All server subpackages have a virtual provide for the name of the server
# they deliver.  The Xorg one is versioned, the others are intentionally
# unversioned.

%description
X.Org X11 X server

%package common
Summary: Xorg server common files
Group: User Interface/X
Requires: pixman >= 0.30.0
Requires: xkeyboard-config xkbcomp

%description common
Common files shared among all X servers.

%if %{with_hw_servers}
%package Xorg
Summary: Xorg X server
Group: User Interface/X
Provides: Xorg = %{version}-%{release}
Provides: Xserver
%if !0%{?gitdate} || %{stable_abi}
Provides: xserver-abi(ansic-%{ansic_major}) = %{ansic_minor}
Provides: xserver-abi(videodrv-%{videodrv_major}) = %{videodrv_minor}
Provides: xserver-abi(xinput-%{xinput_major}) = %{xinput_minor}
Provides: xserver-abi(extension-%{extension_major}) = %{extension_minor}
%endif
%if 0%{?gitdate}
Provides: xserver-abi(ansic-%{git_ansic_major}) = %{git_ansic_minor}
Provides: xserver-abi(videodrv-%{git_videodrv_major}) = %{git_videodrv_minor}
Provides: xserver-abi(xinput-%{git_xinput_major}) = %{git_xinput_minor}
Provides: xserver-abi(extension-%{git_extension_major}) = %{git_extension_minor}
%endif
Requires: libpciaccess >= 0.13.1
Obsoletes: xorg-x11-glamor < %{version}-%{release}
Provides: xorg-x11-glamor = %{version}-%{release}
Obsoletes: xorg-x11-drv-modesetting < %{version}-%{release}
Provides: xorg-x11-drv-modesetting = %{version}-%{release}

%ifarch %{ix86} x86_64
Requires: xorg-x11-drv-vesa
%else
Requires: xorg-x11-drv-fbdev
%endif
Requires: xorg-x11-drv-void xorg-x11-drv-evdev >= 2.1.0-3
Requires: mesa-libEGL

%if 0%{?fedora} > 17
# Dropped from F18, use a video card instead
# in F17 updates-testing: 0.7.4-1.fc17
Obsoletes: xorg-x11-drv-ark <= 0.7.3-15.fc17
Obsoletes: xorg-x11-drv-chips <= 1.2.4-8.fc18
Obsoletes: xorg-x11-drv-s3 <= 0.6.3-14.fc17
Obsoletes: xorg-x11-drv-tseng <= 1.2.4-12.fc17
%endif


Requires: xorg-x11-server-common >= %{version}-%{release}
Requires: system-setup-keyboard

%description Xorg
X.org X11 is an open source implementation of the X Window System.  It
provides the basic low level functionality which full fledged
graphical user interfaces (GUIs) such as GNOME and KDE are designed
upon.
%endif


%package Xnest
Summary: A nested server.
Group: User Interface/X
Requires: xorg-x11-server-common >= %{version}-%{release}
Provides: Xnest

%description Xnest
Xnest is an X server which has been implemented as an ordinary
X application.  It runs in a window just like other X applications,
but it is an X server itself in which you can run other software.  It
is a very useful tool for developers who wish to test their
applications without running them on their real X server.

%package Xdmx
Summary: Distributed Multihead X Server and utilities
Group: User Interface/X
Requires: xorg-x11-server-common >= %{version}-%{release}
Requires: libX11 >= 1.6.0
Provides: Xdmx

%description Xdmx
Xdmx is proxy X server that provides multi-head support for multiple displays
attached to different machines (each of which is running a typical X server).
When Xinerama is used with Xdmx, the multiple displays on multiple machines
are presented to the user as a single unified screen.  A simple application
for Xdmx would be to provide multi-head support using two desktop machines,
each of which has a single display device attached to it.  A complex
application for Xdmx would be to unify a 4 by 4 grid of 1280x1024 displays
(each attached to one of 16 computers) into a unified 5120x4096 display.

%package Xvfb
Summary: A X Windows System virtual framebuffer X server.
Group: User Interface/X
# xvfb-run is GPLv2, rest is MIT
License: MIT and GPLv2
Requires: xorg-x11-server-common >= %{version}-%{release}
# required for xvfb-run
Requires: xorg-x11-xauth
Provides: Xvfb

%description Xvfb
Xvfb (X Virtual Frame Buffer) is an X server that is able to run on
machines with no display hardware and no physical input devices.
Xvfb simulates a dumb framebuffer using virtual memory.  Xvfb does
not open any devices, but behaves otherwise as an X display.  Xvfb
is normally used for testing servers.


%package Xephyr
Summary: A nested server.
Group: User Interface/X
Requires: xorg-x11-server-common >= %{version}-%{release}
Provides: Xephyr

%description Xephyr
Xephyr is an X server which has been implemented as an ordinary
X application.  It runs in a window just like other X applications,
but it is an X server itself in which you can run other software.  It
is a very useful tool for developers who wish to test their
applications without running them on their real X server.  Unlike
Xnest, Xephyr renders to an X image rather than relaying the
X protocol, and therefore supports the newer X extensions like
Render and Composite.


%if %{with_hw_servers}
%package devel
Summary: SDK for X server driver module development
Group: User Interface/X
Requires: xorg-x11-util-macros
Requires: xorg-x11-proto-devel
Requires: pkgconfig pixman-devel libpciaccess-devel
Provides: xorg-x11-server-static
Provides: xorg-x11-server-sdk = %{version}-%{release}
Obsoletes: xorg-x11-glamor-devel < %{version}-%{release}
Provides: xorg-x11-glamor-devel = %{version}-%{release}
Provides: libxf86config-devel = %{version}-%{release} 
Obsoletes: libxf86config-devel < 1.6.99-29 

%description devel
The SDK package provides the developmental files which are necessary for
developing X server driver modules, and for compiling driver modules
outside of the standard X11 source code tree.  Developers writing video
drivers, input drivers, or other X modules should install this package.
%endif

%package source
Summary: Xserver source code required to build VNC server (Xvnc)
Group: Development/Libraries
BuildArch: noarch

%description source
Xserver source code needed to build VNC server (Xvnc)

%prep
#setup -q -n %{pkgname}-%{?gitdate:%{gitdate}}%{!?gitdate:%{version}}
%setup -q -n %{pkgname}-%{version}

#if 0%{?gitdate}
%if 0
git checkout -b fedora
sed -i 's/git/&+ssh/' .git/config
if [ -z "$GIT_COMMITTER_NAME" ]; then
    git config user.email "x@fedoraproject.org"
    git config user.name "Fedora X Ninjas"
fi
%else
git init
if [ -z "$GIT_COMMITTER_NAME" ]; then
    git config user.email "x@fedoraproject.org"
    git config user.name "Fedora X Ninjas"
fi
cp %{SOURCE1} .gitignore
git add .
git commit -a -q -m "%{version} baseline."
%endif

# Apply all the patches.
git am -p1 %{patches} < /dev/null

%if %{with_hw_servers} && 0%{?stable_abi}
# check the ABI in the source against what we expect.
getmajor() {
    grep -i ^#define.ABI.$1_VERSION hw/xfree86/common/xf86Module.h |
    tr '(),' '   ' | awk '{ print $4 }'
}

getminor() {
    grep -i ^#define.ABI.$1_VERSION hw/xfree86/common/xf86Module.h |
    tr '(),' '   ' | awk '{ print $5 }'
}

test `getmajor ansic` == %{ansic_major}
test `getminor ansic` == %{ansic_minor}
test `getmajor videodrv` == %{videodrv_major}
test `getminor videodrv` == %{videodrv_minor}
test `getmajor xinput` == %{xinput_major}
test `getminor xinput` == %{xinput_minor}
test `getmajor extension` == %{extension_major}
test `getminor extension` == %{extension_minor}

%endif

%build

%global default_font_path "catalogue:/etc/X11/fontpath.d,built-ins"

%if %{with_hw_servers}
%global dri_flags --with-dri-driver-path=%{drimoduledir} --enable-dri2 %{?!rhel:--enable-dri3}
%else
%global dri_flags --disable-dri
%endif

%if 0%{?fedora}
%global bodhi_flags --with-vendor-name="Fedora Project"
%global wayland --with-wayland
%endif

# ick
%if 0%{?rhel}
sed -i 's/WAYLAND_SCANNER_RULES.*//g' configure.ac
%global bodhi_flags --with-vendor-web="http://wiki.centos.org/Documentation" --with-vendor-name="CentOS"
%endif

# --with-pie ?
autoreconf -f -v --install || exit 1
# export CFLAGS="${RPM_OPT_FLAGS}"
# XXX without dtrace
export CFLAGS="${RPM_OPT_FLAGS} -Wl,-z,relro -fno-strict-aliasing"

%configure --enable-maintainer-mode %{xservers} \
	--enable-listen-tcp \
	--disable-static \
	--with-pic \
	--enable-dmx \
	--with-int10=x86emu \
	--with-default-font-path=%{default_font_path} \
	--with-module-dir=%{moduledir} \
	--with-builderstring="Build ID: %{name} %{version}-%{release}" \
	--with-os-name="$(hostname -s) $(uname -r)" \
	--with-xkb-output=%{_localstatedir}/lib/xkb \
        --without-dtrace \
	--disable-linux-acpi --disable-linux-apm \
	--enable-xselinux --enable-xcsecurity --enable-record \
	--enable-config-hal \
	--enable-glamor \
	--disable-config-udev \
	--disable-unit-tests \
        --enable-install-libxf86config \
	%{?wayland} \
	%{dri_flags} %{?bodhi_flags} \
	${CONFIGURE}
        
make V=1 %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT moduledir=%{moduledir}

%if %{with_hw_servers}
rm -rf $RPM_BUILD_ROOT%{_libdir}/xorg/modules/multimedia/
mkdir -p $RPM_BUILD_ROOT%{_libdir}/xorg/modules/{drivers,input}

# yay pam
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/pam.d
install -m 0644 %{SOURCE10} $RPM_BUILD_ROOT%{_sysconfdir}/pam.d/xserver
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps
touch $RPM_BUILD_ROOT%{_sysconfdir}/security/console.apps/xserver

mkdir -p $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{_datadir}/X11/xorg.conf.d

# make sure the (empty) /etc/X11/xorg.conf.d is there, system-setup-keyboard
# relies on it more or less.
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/X11/xorg.conf.d

mkdir -p $RPM_BUILD_ROOT%{_bindir}

%if %{stable_abi}
install -m 755 %{SOURCE30} $RPM_BUILD_ROOT%{_bindir}/xserver-sdk-abi-requires
%else
sed -e s/@MAJOR@/%{gitdate}/g -e s/@MINOR@/%{minor_serial}/g %{SOURCE31} > \
    $RPM_BUILD_ROOT%{_bindir}/xserver-sdk-abi-requires
chmod 755 $RPM_BUILD_ROOT%{_bindir}/xserver-sdk-abi-requires
%endif

%endif

# xdmx (note case) was renamed because hfs+ is case-insentive, lame
ln -s %{_bindir}/dmxinfo $RPM_BUILD_ROOT%{_bindir}/xdmx

# Make the source package
%global xserver_source_dir %{_datadir}/xorg-x11-server-source
%global inst_srcdir %{buildroot}/%{xserver_source_dir}
mkdir -p %{inst_srcdir}/{Xext,xkb,GL,hw/{xquartz/bundle,xfree86/common}}
mkdir -p %{inst_srcdir}/{hw/dmx/doc,man,doc,hw/dmx/doxygen}
cp {,%{inst_srcdir}/}hw/xquartz/bundle/cpprules.in
cp {,%{inst_srcdir}/}man/Xserver.man
cp {,%{inst_srcdir}/}doc/smartsched
cp {,%{inst_srcdir}/}hw/dmx/doxygen/doxygen.conf.in
cp {,%{inst_srcdir}/}xserver.ent.in
cp {,%{inst_srcdir}/}hw/xfree86/Xorg.sh.in
cp xkb/README.compiled %{inst_srcdir}/xkb
cp hw/xfree86/xorgconf.cpp %{inst_srcdir}/hw/xfree86

install -m 0755 %{SOURCE20} $RPM_BUILD_ROOT%{_bindir}/xvfb-run

find . -type f | egrep '.*\.(c|h|am|ac|inc|m4|h.in|pc.in|man.pre|pl|txt)$' |
xargs tar cf - | (cd %{inst_srcdir} && tar xf -)
# SLEDGEHAMMER
find %{inst_srcdir}/hw/xfree86 -name \*.c -delete

# Remove unwanted files/dirs
{
    rm -f $RPM_BUILD_ROOT%{_libdir}/X11/Options
    rm -f $RPM_BUILD_ROOT%{_bindir}/in?
    rm -f $RPM_BUILD_ROOT%{_bindir}/ioport
    rm -f $RPM_BUILD_ROOT%{_bindir}/out?
    rm -f $RPM_BUILD_ROOT%{_bindir}/pcitweak
    rm -f $RPM_BUILD_ROOT%{_mandir}/man1/pcitweak.1*
    find $RPM_BUILD_ROOT -type f -name '*.la' | xargs rm -f -- || :
%if !%{with_hw_servers}
    rm -f $RPM_BUILD_ROOT%{_libdir}/pkgconfig/xorg-server.pc
    rm -f $RPM_BUILD_ROOT%{_datadir}/aclocal/xorg-server.m4
    rm -rf $RPM_BUILD_ROOT%{_defaultdocdir}/xorg-server
%endif
}

%clean
rm -rf $RPM_BUILD_ROOT


%files common
%defattr(-,root,root,-)
%doc COPYING
%{_mandir}/man1/Xserver.1*
%{_libdir}/xorg/protocol.txt
%dir %{_localstatedir}/lib/xkb
%{_localstatedir}/lib/xkb/README.compiled

%if 1
%global Xorgperms %attr(4755, root, root)
%else
# disable until module loading is audited
%global Xorgperms %attr(0711,root,root) %caps(cap_sys_admin,cap_sys_rawio,cap_dac_override=pe)
%endif

%if %{with_hw_servers}
%files Xorg
%defattr(-,root,root,-)
%config %attr(0644,root,root) %{_sysconfdir}/pam.d/xserver
%config(missingok) /etc/security/console.apps/xserver
%{_bindir}/X
%{Xorgperms} %{_bindir}/Xorg
%{_bindir}/cvt
%{_bindir}/gtf
%dir %{_libdir}/xorg
%dir %{_libdir}/xorg/modules
%dir %{_libdir}/xorg/modules/drivers
%{_libdir}/xorg/modules/drivers/modesetting_drv.so
%dir %{_libdir}/xorg/modules/extensions
%{_libdir}/xorg/modules/extensions/libglx.so
%if !0%{?rhel}
%{_libdir}/xorg/modules/extensions/libxwayland.so
%endif
%dir %{_libdir}/xorg/modules/input
%{_libdir}/xorg/modules/libfbdevhw.so
%{_libdir}/xorg/modules/libexa.so
%{_libdir}/xorg/modules/libfb.so
%{_libdir}/xorg/modules/libglamoregl.so
%{_libdir}/xorg/modules/libshadow.so
%{_libdir}/xorg/modules/libshadowfb.so
%{_libdir}/xorg/modules/libvgahw.so
%{_libdir}/xorg/modules/libwfb.so
%{_libdir}/xorg/modules/libint10.so
%{_libdir}/xorg/modules/libvbe.so
%{_mandir}/man1/gtf.1*
%{_mandir}/man1/Xorg.1*
%{_mandir}/man1/cvt.1*
%{_mandir}/man4/fbdevhw.4*
%{_mandir}/man4/exa.4*
%{_mandir}/man4/modesetting.4*
%{_mandir}/man5/xorg.conf.5*
%{_mandir}/man5/xorg.conf.d.5*
%dir %{_sysconfdir}/X11/xorg.conf.d
%dir %{_datadir}/X11/xorg.conf.d
%{_datadir}/X11/xorg.conf.d/10-quirks.conf
%endif


%files Xnest
%defattr(-,root,root,-)
%{_bindir}/Xnest
%{_mandir}/man1/Xnest.1*

%files Xdmx
%defattr(-,root,root,-)
%{_bindir}/Xdmx
%{_bindir}/dmxaddinput
%{_bindir}/dmxaddscreen
%{_bindir}/dmxreconfig
%{_bindir}/dmxresize
%{_bindir}/dmxrminput
%{_bindir}/dmxrmscreen
%{_bindir}/dmxtodmx
%{_bindir}/dmxwininfo
%{_bindir}/vdltodmx
%{_bindir}/dmxinfo
%{_bindir}/xdmx
%{_bindir}/xdmxconfig
%{_mandir}/man1/Xdmx.1*
%{_mandir}/man1/dmxtodmx.1*
%{_mandir}/man1/vdltodmx.1*
%{_mandir}/man1/xdmxconfig.1*

%files Xvfb
%defattr(-,root,root,-)
%{_bindir}/Xvfb
%{_bindir}/xvfb-run
%{_mandir}/man1/Xvfb.1*


%files Xephyr
%defattr(-,root,root,-)
%{_bindir}/Xephyr
%{_mandir}/man1/Xephyr.1*


%if %{with_hw_servers}
%files devel
%doc COPYING
%defattr(-,root,root,-)
#{_docdir}/xorg-server
%{_bindir}/xserver-sdk-abi-requires
%{_libdir}/pkgconfig/xorg-server.pc
%dir %{_includedir}/xorg
%{sdkdir}/*.h
%{_datadir}/aclocal/xorg-server.m4
%{_libdir}/libxf86config.a
%endif


%files source
%defattr(-, root, root, -)
%{xserver_source_dir}

%changelog
* Sat Nov 19 2016 Bjarne Saltbaek <bjarne@redsleeve.org> 1.17.4-9.4.0
- Re-added libxf86config since pyxf86config needs it

* Tue Jul 12 2016 Johnny Hughes <johnny@centos.org> - 1.17.4-9.4
- Removed upstream Branding in the SPEC file

* Wed Jun 01 2016 Adam Jackson <ajax@redhat.com> - 1.17.4-9.4
- Restore listen-on-TCP behaviour

* Mon May 23 2016 Adam Jackson <ajax@redhat.com> - 1.17.4-9.1
- Restore indirect GLX by default, and add xorg.conf option for it

* Fri Apr 01 2016 Adam Jackson <ajax@redhat.com> 1.17.4-9
- Require mesa-libEGL from Xorg subpackage

* Wed Jan 20 2016 Olivier Fourdan <ofourdan@redhat.com> 1.17.4-8
- Configurable number of clients (#1179840)

* Wed Dec 09 2015 Adam Jackson <ajax@redhat.com> 1.17.4-7
- Add bug-compatibility for exposure event generation for backing store's
  Always mode, and re-enable the feature

* Wed Nov 18 2015 Adam Jackson <ajax@redhat.com> 1.17.4-5
- Set rpath in the GLX link flags so we always pick up Mesa's libGL

* Wed Nov 18 2015 Adam Jackson <ajax@redhat.com> 1.17.4-4
- Enable DRI3

* Thu Nov 12 2015 Olivier Fourdan <ofourdan@redhat.com> 1.17.4-3
- Add missing hw/xfree86/Xorg.sh.in to xorg-x11-server-source package.
  This is needed to build packages depending on xorg-x11-server-source
  (e.g. tigervnc), otherwise the build will fail.

* Wed Nov 11 2015 Adam Jackson <ajax@redhat.com> 1.17.4-2
- Enable glamor

* Wed Nov 11 2015 Adam Jackson <ajax@redhat.com> 1.17.4-1
- xserver 1.17.4

* Mon Nov 02 2015 Adam Jackson <ajax@redhat.com> 1.15.0-37
- Explicitly Require libpciaccess >= 0.13.1

* Wed May 13 2015 Adam Jackson <ajax@redhat.com> 1.15.0-36
- Fix crash on zero-sized PutImage (#1208094)

* Mon May 04 2015 Adam Jackson <ajax@redhat.com> 1.15.0-35
- Fix XACE labeling of shm pixmaps with Xinerama active (#1199591)

* Mon May 04 2015 Adam Jackson <ajax@redhat.com> 1.15.0-34
- Backport printf '*' support (#1184365)

* Mon Apr 27 2015 Olivier Fourdan <ofourdan@redhat.com> 1.15.0-33
- Fix xvfb-run option "--auto-display" (#1049297)

* Wed Feb 25 2015 Adam Jackson <ajax@redhat.com> 1.15.0-32
- Fix backing store's Always mode

* Thu Feb 12 2015 Olivier Fourdan <ofourdan@redhat.com> 1.15.0-31
- Synchronize CAPS-Lock state in nested X servers such as Xnest
  and Xephyr (#1161061)
- Add a new command line option "--auto-display" to xvfb-run to take
  advantage of the XServer's "-displayfd" option to get the display
  number directly from Xfvb (#1049297)

* Fri Feb 06 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.15.0-30
- CVE fixes for: CVE-2015-0255

* Thu Jan 08 2015 Peter Hutterer <peter.hutterer@redhat.com> 1.15.0-29
- Fix numlock/caps lock on hotplugged keyboards (#963829)

* Wed Jan 07 2015 Adam Jackson <ajax@redhat.com> 1.15.0-28
- Restore basic driver Requires: for Xorg
- Fix CVE-2014-8092-3 patch to be valid C++, fixes tigervnc build

* Wed Dec 10 2014 Adam Jackson <ajax@redhat.com> 1.15.0-26
- Fix Xephyr's 8bpp emulation with multiple screens to use per-screen colormap

* Wed Dec 10 2014 Adam Jackson <ajax@redhat.com> 1.15.0-25
- CVE fixes for: CVE-2014-8099, CVE-2014-8098, CVE-2014-8097, CVE-2014-8096,
  CVE-2014-8095, CVE-2014-8094, CVE-2014-8093, CVE-2014-8092, CVE-2014-8091,
  CVE-2014-8101, CVE-2014-8100, CVE-2014-8103, CVE-2014-8102

* Wed Sep 03 2014 Adam Jackson <ajax@redhat.com> 1.15.0-22
- Remove a broken interlock from the mixed-fbdev-and-pci path

* Wed Aug 20 2014 Adam Jackson <ajax@redhat.com> 1.15.0-21
- Fix hardware cursor support in Xephyr

* Wed Aug 13 2014 Adam Jackson <ajax@redhat.com> 1.15.0-20
- Add modesetting to the fallback driver list
- Repair X -configure

* Tue Aug 12 2014 Adam Jackson <ajax@redhat.com> 1.15.0-19
- Fix GrabPointer to not wrongly succed on redirected windows

* Tue Aug 12 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.15.0-18
- Remove erroneous bug checks preventing the Xen Virtual Pointer from
  initializing (#1124637)

* Tue Aug 05 2014 Adam Jackson <ajax@redhat.com> 1.15.0-17
- Allow mixed binding of fbdev and pci devices when it appears to be safe

* Wed Jul 16 2014 Adam Jackson <ajax@redhat.com> 1.15.0-16
- Fix initial Xephyr size setup

* Sun May 25 2014 Peter Hutterer <peter.hutterer@redhat.com> - 1.15.0-15
- Restore Xephyr default resizability (and the -notresizable option)

* Tue May 20 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.15.0-14
- Don't process events from disabled devices, it can cause a crash
  (#1084244)

* Fri May 16 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.15.0-13
- Fix crasher when pressing a Wacom I4 or I5 ring button while moving the
  touchpad

* Thu May 01 2014 Adam Jackson <ajax@redhat.com> 1.15.0-12
- Rebase some 6.5 mustard patches

* Wed Apr 30 2014 Adam Jackson <ajax@redhat.com> 1.15.0-11
- Fix color update on 8bpp Xephyr (#1057667)

* Tue Apr 29 2014 Adam Jackson <ajax@redhat.com> 1.15.0-10
- Re-align spec with 6.5 (hal, xdmx, xcsecurity, etc.)

* Mon Apr 28 2014 Adam Jackson <ajax@redhat.com> 1.15.0-9
- Re-enable pam support

* Wed Apr 23 2014 Adam Jackson <ajax@redhat.com> 1.15.0-8
- Make -devel provide -sdk for specfile compat

* Thu Feb 27 2014 Jérôme Glisse <jglisse@redhat.com> 1.15.0-7
- Do not open tty on non seat0 (#1053063)

* Tue Feb 25 2014 Adam Jackson <ajax@redhat.com> 1.15.0-6
- Fix dist tag
- Link Xorg with -z now

* Sat Feb 22 2014 Dave Airlie <airlied@redhat.com> 1.15.0-5
- fix slave outputs being set as primary (#1067786)

* Thu Feb 13 2014 Peter Hutterer <peter.hutterer@redhat.com> 1.15.0-4
- Fix button state check (#1061541)

* Wed Feb 12 2014 Adam Jackson <ajax@redhat.com> 1.15.0-3.1
- Mass rebuild

* Wed Feb 05 2014 Adam Jackson <ajax@redhat.com> 1.15.0-3
- Be sure to not link Xorg against libGL, just libglx.

* Tue Jan 14 2014 Adam Jackson <ajax@redhat.com> 1.15.0-2
- exa-only-draw-valid-trapezoids.patch: Fix crash in exa.

* Mon Jan 13 2014 Adam Jackson <ajax@redhat.com> 1.15.0-1
- xserver 1.15.0

* Tue Dec 17 2013 Adam Jackson <ajax@redhat.com> 1.14.99.904-1
- 1.15RC4
- Re-disable int10 on arm

* Mon Dec  2 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.14.99.902-2
- Add aarch64 to platforms that have libunwind

* Wed Nov 20 2013 Adam Jackson <ajax@redhat.com> 1.14.99.902-1
- 1.15RC2

* Mon Nov 18 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-6
- Prefer fbdev to vesa, fixes fallback path on UEFI

* Fri Nov 08 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-5
- Restore XkbCopyDeviceKeymap for (older) tigervnc

* Fri Nov 08 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-4
- Explicitly enable DRI2

* Thu Nov 07 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-3
- Merge Xinerama+{Damage,Render,Composite} fix series

* Thu Nov 07 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-2
- Fix build with --disable-present

* Thu Nov 07 2013 Adam Jackson <ajax@redhat.com
- Don't bother trying to build the unit tests for now

* Wed Nov 06 2013 Adam Jackson <ajax@redhat.com> 1.14.99.901-1
- 1.15RC1

* Mon Oct 28 2013 Adam Jackson <ajax@redhat.com> 1.14.99.3-2
- Don't build xwayland in RHEL

* Fri Oct 25 2013 Adam Jackson <ajax@redhat.com> 1.14.99.3-1
- xserver 1.14.99.3
- xwayland branch refresh
- Drop some F17-era Obsoletes
- Update BuildReqs to match reality

* Wed Oct 23 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.3-6
- Fix Xdmx cursor jumps (#1019821)

* Tue Oct 08 2013 Adam Jackson <ajax@redhat.com> 1.14.3-5
- Snap wayland damage reports to the bounding box

* Thu Oct 03 2013 Adam Jackson <ajax@redhat.com> 1.14.3-4
- Fix up fixing up the driver list after filtering out non-wayland

* Wed Oct 02 2013 Adam Jackson <ajax@redhat.com> 1.14.3-3
- Only look at wayland-capable drivers when run with -wayland

* Mon Sep 23 2013 Adam Jackson <ajax@redhat.com> 1.14.3-2
- xwayland support

* Mon Sep 16 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.3-1
- xserver 1.14.3

* Tue Jul 30 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-9
- Fix active touch grabs, second touchpoint didn't get sent to client
- Fix version mismatch for XI 2.2+ clients (where a library supports > 2.2
  but another version than the originally requested one).

* Tue Jul 30 2013 Dave Airlie <airlied@redhat.com> 1.14.2-8
- fixes for multi-monitor reverse optimus

* Mon Jul 22 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-7
- Fix erroneous valuator 1 coordinate when an absolute device in relative
  mode doesn't send y coordinates.

* Fri Jul 19 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-6
- Add new version of the resolution-based scaling patch - scale y down
  instead of x up. That gives almost the same behaviour as current
  synaptics. Drop the synaptics quirk, this needs to be now removed from the
  driver.

* Mon Jul 15 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-5
- Fix logspam when trying to free a non-existant grab.
- Update touch patch to upstream version (from fdo #66720)
- re-add xephyr resizable patch, got lost in rebase (#976995)

* Fri Jul 12 2013 Dave Airlie <airlied@redhat.com> 1.14.2-4
- reapply dropped patch to fix regression (#981953)

* Tue Jul 09 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-3
- Fix crash on 32-bit with virtual box guest additions (#972095)

* Tue Jul 09 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-2
- Fix crash in gnome-shell when tapping a menu twice (fdo #66720)

* Thu Jul 04 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.2-1
- xorg-server 1.4.2
- drop merged patches
- Add a quirk to set the synaptics resolution to 0 by default. The pre-scale
  patch in the server clashes with synaptics inaccurate resolution numbers,
  causing the touchpad movement to be stunted.

* Thu Jun 06 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.1.901-2
- Backport the touch grab race condition patches from fdo #56578

* Thu Jun 06 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.1.901-1
- xserver 1.14.2RC1

* Tue Jun 04 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.1-4
- Update quirks for trackballs and the La-VIEW Technology Naos 5000 mouse

* Sun Jun 02 2013 Adam Jackson <ajax@redhat.com> 1.14.1-3
- Backport an arm/ppc crash fix from master (#965749)

* Tue May 14 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.1-2
- Add -resizeable option to Xephyr, enable by default (#962572)
- Fix crash on 24bpp host server (#518960)

* Mon May 06 2013 Dave Airlie <airlied@redhat.com> 1.14.1-1
- upstream rebase
- reorganise the randr/gpu screen patches + backports

* Wed Apr 17 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.0-6
- CVE-2013-1940: Fix xf86FlushInput() to drain evdev events
  (#950438, #952949)

* Fri Apr 12 2013 Dave Airlie <airlied@redhat.com> 1.14.0-5
- reenable reverse optimus and some missing patch from F18

* Fri Apr 12 2013 Dave Airlie <airlied@redhat.com> 1.14.0-4
- fix bug with GPU hotplugging while VT switched
- reenable reverse optimus and some missing patch from F18

* Fri Mar 22 2013 Dan Horák <dan@danny.cz> 1.14.0-3
- libunwind exists only on selected arches

* Thu Mar 14 2013 Adam Jackson <ajax@redhat.com> 1.14.0-2
- Different RHEL customization

* Thu Mar 07 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.14.0-1
- xserver 1.14

* Wed Mar 06 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.13.99.902-2
- Use libunwind for backtraces

* Fri Feb 15 2013 Adam Jackson <ajax@redhat.com>
- Drop -sdk Prov/Obs, changed to -devel in F9
- Drop xorg-x11-X* Obsoletes, leftover from the modular transition in FC5

* Fri Feb 15 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.13.99.902-1
- xserver 1.14RC2 from git

* Thu Feb 14 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.13.99.901-5
- Fix scrolling for Evoluent Vertical Mouse 3 (#612140#c20)

* Fri Jan 25 2013 Peter Hutterer <peter.hutterer@redhat.com> 1.13.99.901-4
- Add quirk for Evoluent Vertical Mouse 3, button mapping is quirky
  (#612140)

* Wed Jan 23 2013 Adam Jackson <ajax@redhat.com> 1.13.99.901-3
- Bump XI minor for barriers

* Wed Jan 09 2013 Adam Jackson <ajax@redhat.com> 1.13.99.901-2
- Pick up fixes from git

* Wed Jan 09 2013 Adam Jackson <ajax@redhat.com> 1.13.99.901-1
- xserver 1.14RC1

* Tue Dec 18 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.13.1-1
- server 1.13.1

* Fri Dec 14 2012 Adam Jackson <ajax@redhat.com> 1.13.0-15
- Cherry-pick a fix for selection for TouchBegin from multiple clients

* Wed Dec 12 2012 Dave Airlie <airlied@redhat.com> 1.13.0-14
- add events for autoconfig of gpus devices, allow usb devices to notify gnome

* Wed Dec 12 2012 Dave Airlie <airlied@redhat.com> 1.13.0-13
- fix hotplug issue with usb devices and large screens

* Wed Dec 12 2012 Dave Airlie <airlied@redhat.com< 1.13.0-12
- backout non-pci configuration less patch, its breaks multi-GPU

* Fri Nov 30 2012 Adam Jackson <ajax@redhat.com> 1.13.0-11
- Bump default EQ length to reduce the number of unhelpful abrt reports

* Wed Nov 28 2012 Adam Jackson <ajax@redhat.com> 1.13.0-10
- Fix VT switch key handling

* Wed Nov 28 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.13.0-9
- Fix server crash when a XI 1.x device grab is activated on a disabled
  synaptics touchpad is disabled

* Tue Nov 27 2012 Jiri Kastner <jkastner@redhat.com> 1.13.0-8
- Fix for non-PCI configuration-less setups

* Wed Oct 31 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.13.0-7
- Fix build issues on new kernels caused by removal of _INPUT_H

* Tue Oct 30 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.13.0-6
- Add touchscreen fixes (including pointer emulation) #871064

* Tue Sep 25 2012 Dave Airlie <airlied@redhat.com> 1.13.0-6
- update server autobind patch to fix crash reported on irc

* Thu Sep 20 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.13.0-5
- Set the transformation matrix to the unity matrix to avoid spurious cursor
  jumps (#852841)

* Fri Sep 14 2012 Dave Airlie <airlied@redhat.com> 1.13.0-4
- fix bug when hotplugging a monitor causes oops

* Mon Sep 10 2012 Dave Airlie <airlied@redhat.com> 1.13.0-3
- fix race across GPU power down and server startup

* Mon Sep 10 2012 Dave Airlie <airlied@redhat.com> 1.13.0-2
- fix compat output segfault on output less gpus.

* Fri Sep 07 2012 Dave Airlie <airlied@redhat.com> 1.13.0-1
- rebase to upstream 1.13.0 release tarball

* Fri Sep 07 2012 Dave Airlie <airlied@redhat.com> 1.12.99.905-5
- fix prime offload with DRI2 compositors

* Mon Sep 03 2012 Dave Airlie <airlied@redhat.com> 1.12.99.905-4
- fix multi-gpu after VT switch

* Mon Aug 27 2012 Dave Airlie <airlied@redhat.com> 1.12.99.905-3
- port multi-seat video fixes from upstream

* Fri Aug 24 2012 Dave Airlie <airlied@redhat.com> 1.12.99.905-2
- reintroduce auto config but working this time
- fix two recycle/exit crashes

* Wed Aug 22 2012 Dave Airlie <airlied@redhat.com> 1.12.99.905-1
- rebase to 1.12.99.905 snapshot

* Fri Aug 17 2012 Dave Airlie <airlied@redhat.com> 1.12.99.904-4
- autobind was horribly broken on unplug - drop it like its hotplug.

* Fri Aug 17 2012 Dave Airlie <airlied@redhat.com> 1.12.99.904-3
- add git fixes + autobind to gpu devices.

* Wed Aug 15 2012 Adam Jackson <ajax@redhat.com> 1.12.99.904-2
- Always install int10 and vbe sdk headers

* Wed Aug 08 2012 Dave Airlie <airlied@redhat.com> 1.12.99.904-1
- rebase to 1.12.99.904 snapshot

* Fri Aug 03 2012 Adam Jackson <ajax@redhat.com> 1.12.99.903-6
- Make failure to iopl non-fatal

* Mon Jul 30 2012 Adam Jackson <ajax@redhat.com> 1.12.99.903-5
- No need to --disable-xaa explicitly anymore.

* Thu Jul 26 2012 Adam Jackson <ajax@redhat.com> 1.12.99.903-4
- Install xserver-sdk-abi-requires.release based on stable_abi not gitdate,
  so drivers built against a server that Provides multiple ABI versions will
  Require the stable version.

* Thu Jul 26 2012 Adam Jackson <ajax@redhat.com> 1.12.99.903-3
- Make it possible to Provide: both stable and gitdate-style ABI versions.

* Thu Jul 26 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.12.99.903-2
- xserver-1.12-os-print-newline-after-printing-display-name.patch: drop,
  014ad46f1b353a95e2c4289443ee857cfbabb3ae

* Thu Jul 26 2012 Dave Airlie <airlied@redhat.com> 1.12.99.903-1
- rebase to 1.12.99.903 snapshot

* Wed Jul 25 2012 Dave Airlie <airlied@redhat.com> 1.12.99.902-3
- fix crash due to GLX being linked twice

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.12.99.902-2.20120717
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 18 2012 Dave Airlie <airlied@redhat.com> 1.12.99.902-1
- server 1.12.99.902

* Mon Jul 09 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.12.3-1
- server 1.12.3

* Tue Jun 26 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.12.2-4
- send keycode/event type down the wire when SlowKeys enable, otherwise
  GNOME won't warn about it (#816764)

* Thu Jun 21 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.12.2-3
- print newline after printing $DISPLAY to -displayfd (#824594)

* Fri Jun 15 2012 Dan Horák <dan[at]danny.cz> 1.12.2-2
- fix build without xorg (aka s390x)

* Wed May 30 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.12.2-1
- xserver 1.12.2

* Fri May 25 2012 Dave Airlie <airlied@redhat.com> 1.12.1-2
- xserver-fix-pci-slot-claims.patch: backport slot claiming fix from master
- xserver-1.12-modesetting-fallback.patch: add modesetting to fallback list

* Mon May 14 2012 Peter Hutterer <peter.hutterer@redhat.com>
- Drop xserver-1.10.99.1-test.patch:
  cd89482088f71ed517c2e88ed437e4752070c3f4 fixed it

* Mon May 14 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.12.1-1
- server 1.12.1
- force autoreconf to avoid libtool errors
- update patches for new indentation style.

* Mon May 14 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.12.0-6
- Make timers signal-safe (#814869)

* Sun May 13 2012 Dennis Gilmore <dennis@ausil.us> 1.12.0-5
- enable vbe on arm arches

* Thu Apr 26 2012 Adam Jackson <ajax@redhat.com> 1.12.0-4
- Obsolete some old video drivers in F18+

* Wed Mar 21 2012 Adam Jackson <ajax@redhat.com> 1.12.0-3
- Tweak arches for RHEL

* Wed Mar 14 2012 Adam Jackson <ajax@redhat.com> 1.12.0-2
- Install Xorg mode 4755, there's no security benefit to 4711. (#712432)

* Mon Mar 05 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.12.0-1
- xserver 1.12
- xserver-1.12-dix-reset-last.scroll-when-resetting-the-valuator-45.patch:
  drop, 6f2838818

* Thu Feb 16 2012 Adam Jackson <ajax@redhat.com> 1.11.99.903-2.20120215
- Don't pretend int10 is a thing on non-PC arches

* Thu Feb 16 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.11.99.903-1.20120215
- Server version is 1.11.99.903 now, use that.

* Wed Feb 15 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.11.99.901-7.20120215
- Today's git snapshot

* Sun Feb 12 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.11.99.901-6.20120124
- Fix installation of xserver-sdk-abi-requires script, if stable_abi is set
  always install the relese one, not the git one

* Sat Feb 11 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.11.99.901-5.20120124
- ABI is considered stable now:
  video 12.0, input 16.0, extension 6.0, font 0.6, ansic 0.4

* Sat Feb 11 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.11.99.901-4.20120124
- xserver-1.12-dix-reset-last.scroll-when-resetting-the-valuator-45.patch:
  reset last.scroll on the device whenever the slave device switched to
  avoid jumps during scrolling (#788632).

* Tue Jan 24 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.11.99.901-3.20120124
- Today's git snapshot
- xserver-1.12-xaa-sdk-headers.patch: drop, a55214d11916b

* Wed Jan 04 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.11.99.901-2.20120103
- xserver-1.12-Xext-fix-selinux-build-failure.patch: fix build error
  triggered by Red Hat-specific patch to libselinux

* Tue Jan 03 2012 Peter Hutterer <peter.hutterer@redhat.com> 1.11.99.901-1.20120103
- Git snapshot 98cde254acb9b98337ddecf64c138d38c14ec2bf
- xserver-1.11.99-optionstr.patch: drop
- 0001-Xext-don-t-swap-CARD8-in-SProcSELinuxQueryVersion.patch: drop

* Fri Dec 16 2011 Adam Jackson <ajax@redhat.com> 1.11.99.1-11
- Always install XAA SDK headers so drivers still build

* Thu Dec 15 2011 Adam Jackson <ajax@redhat.com> 1.11.99.1-10
- --disable-xaa

* Thu Dec 01 2011 Adam Jackson <ajax@redhat.com> 1.11.99.1-9
- xserver-1.8-disable-vboxvideo.patch: Drop, should be fixed now
- Drop vesamodes and extramodes, rhpxl is no more
- Stop building libxf86config, pyxf86config will be gone soon

* Tue Nov 29 2011 Dave Airlie <airlied@redhat.com> 1.11.99.1-8
- put optionstr.h into devel package

* Mon Nov 21 2011 Adam Jackson <ajax@redhat.com> 1.11.99.1-7
- Restore DRI1 until drivers are properly prepared for it

* Thu Nov 17 2011 Adam Jackson <ajax@redhat.com> 1.11.99.1-6
- Disable DRI1

* Wed Nov 16 2011 Adam Jackson <ajax@redhat.com> 1.11.99.1-5
- Obsolete some dead input drivers.

* Mon Nov 14 2011 Adam Jackson <ajax@redhat.com> 1.11.99.1-3
- Fix permissions on abi script when doing git snapshots

* Wed Nov 09 2011 Peter Hutterer <peter.hutterer@redhat.com>  1.11.99.1-1.20111109
- Update to today's git snapshot
- xserver-1.6.1-nouveau.patch: drop, upstream
- xserver-1.10.99-config-add-udev-systemd-multi-seat-support.patch: drop,
  upstream
- 0001-dix-block-signals-when-closing-all-devices.patch: drop, upstream

* Wed Nov 09 2011 Adam Jackson <ajax@redhat.com>
- Change the ABI magic for snapshots

* Mon Oct 24 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.11.1-2
- Block signals when removing all input devices #737031

* Thu Oct 13 2011 Adam Jackson <ajax@redhat.com>
- Drop some Requires >= on things where we had newer versions in F14.

* Mon Sep 26 2011 Adam Jackson <ajax@redhat.com> 1.11.1-1
- xserver 1.11.1

* Mon Sep 12 2011 Adam Tkac <atkac redhat com> 1.11.0-2
- ship more files in the -source subpkg

* Tue Sep 06 2011 Adam Jackson <ajax@redhat.com> 1.11.0-1
- xserver 1.11.0

* Thu Aug 18 2011 Adam Jackson <ajax@redhat.com> 1.10.99.902-1.20110818
- xserver 1.11rc2

* Fri Jul 29 2011 Dave Airlie <airlied@redhat.com> 1.10.99.1-10.2011051
- xvfb-run requires xauth installed, fix requires (from jlaska on irc)

* Wed Jul 27 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.10.99.1-9.20110511
- Add support for multi-seat support from the config/udev backend.

* Wed Jun 29 2011 Dan Horák <dan[at]danny.cz> 1.10.99.1-8.20110511
- don't build tests when --disable-xorg is used like on s390(x)

* Tue Jun 21 2011 Adam Jackson <ajax@redhat.com> 1.10.99.1-7.20110511
- BuildRequires: systemtap-sdt-devel, configure --with-dtrace

* Wed May 11 2011 Adam Tkac <atkac redhat com> 1.10.99.1-6.20110511
- include hw/dmx/doc/doxygen.conf.in in the -source subpkg

* Mon May 09 2011  1.10.99.1-5.20110511
- Today's server from git
- xserver-1.10-fix-trapezoids.patch: drop, c6cb70be1ed7cf7
- xserver-1.10-glx-pixmap-crash.patch: drop, 6a433b67ca15fd1
- xserver-1.10-bg-none-revert.patch: drop, dc0cf7596782087

* Thu Apr 21 2011 Hans de Goede <hdegoede@redhat.com> 1.10.99.1-4.20110418
- Drop xserver-1.9.0-qxl-fallback.patch, since the latest qxl driver
  supports both revision 1 and 2 qxl devices (#642153)

* Wed Apr 20 2011 Soren Sandmann <ssp@redhat.com> 1.10.99.1-3.20110418
- xserver-1.10-fix-trapezoids.patch: this patch is necessary to prevent
  trap corruption with pixman 0.21.8.

* Tue Apr 19 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.10.99.1-2.20110418
- rebase all patches
- xserver-1.10-vbe-malloc.patch: drop, d8caa782009abf4d
- "git rm" all unused patches

* Mon Apr 18 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.10.99.1-1.20110418
- Today's server from git

* Wed Mar 30 2011 Adam Jackson <ajax@redhat.com> 1.10.0-7
- xserver-1.10-glx-pixmap-crash.patch, xserver-1.10-bg-none-revert.patch:
  bugfixes from xserver-next

* Tue Mar 22 2011 Adam Jackson <ajax@redhat.com> 1.10.0-6
- Fix thinko in pointer barrier patch

* Tue Mar 22 2011 Adam Tkac <atkac redhat com> 1.10.0-5
- add more files into -source subpkg

* Thu Mar 17 2011 Adam Jackson <ajax@redhat.com> 1.10.0-4
- xserver-1.10-pointer-barriers.patch: Backport CRTC confinement from master
  and pointer barriers from the development tree for same.
- xserver-1.10-vbe-malloc.patch: Fix a buffer overrun in the VBE code.

* Fri Mar 11 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.10.0-3
- Add Xen virtual pointer quirk to 10-quirks.conf (#523914, #679699)

* Wed Mar 09 2011 Adam Jackson <ajax@redhat.com> 1.10.0-2
- Merge from F16:

    * Wed Mar 09 2011 Adam Jackson <ajax@redhat.com> 1.10.0-2
    - Disable filesystem caps in paranoia until module loading is audited

    * Fri Feb 25 2011 Peter Hutterer <peter.hutterer@redhat.com> 1.9.99.902-1
    - xserver 1.10.0
    - server-1.9-99.901-xkb-repeat-issues.patch: drop, merged
    - xserver-1.4.99-pic-libxf86config.patch: drop, see 60801ff8
    - xserver-1.6.99-default-modes.patch: drop, see dc498b4
    - xserver-1.7.1-multilib.patch: drop, see a16e282
    - ABI bumps: xinput to 12.2, extension to 5.0, video to 10.0
