Name:           pulseaudio
Summary:        Improved Linux Sound Server
Version:        0.9.21
Release:        24%{?dist}.0
License:        LGPLv2+
Group:          System Environment/Daemons
Source0:        http://0pointer.de/lennart/projects/pulseaudio/pulseaudio-%{version}.tar.gz
Source1:        default.pa-for-gdm
Patch0: 0001-dbus-remove-filter-functions-only-if-they-were-actua.patch
Patch1: 0002-native-fix-request-counter-miscalculations.patch
Patch2: 0003-core-make-sure-we-always-return-a-valid-memblock-in-.patch
Patch3: 0004-bluetooth-destruct-stream-only-if-it-is-not-already-.patch
Patch4: 0005-bluetooth-don-t-hit-an-assert-if-latency-is-queried-.patch
Patch5: 0006-client-detect-forking-in-sample-cache-API-too.patch
Patch6: 0007-client-verify-connection-state-in-pa_stream_connect_.patch
Patch7: 0008-udev-don-t-forget-to-unref-devices-we-are-not-intere.patch
Patch8: 0009-once-make-once-related-variables-volatile.patch
Patch9: 0010-bluetooth-fix-invalid-memory-access.patch
Patch10: 0011-log-add-an-easy-way-to-disable-log-rate-limiting.patch
Patch11: 0012-udev-make-sure-we-get-events-only-for-sound-devices.patch
Patch12: 0013-alsa-ignore-volume-changes-from-the-hw-if-we-are-not.patch
Patch13: 0014-cpu-check-for-CMOV-flag-before-using-this-intsructio.patch
Patch14: 0015-alsa-cover-Input-Source-Int-Mic.patch
Patch15: 0016-alsa-Cover-the-Int-Mic-Boost-element.patch
Patch16: 0017-udev-handle-sound-cards-with-both-modem-and-audio-pr.patch
Patch17: 0018-udev-rework-modem-detection-a-bit.patch
Patch18: 0019-daemon-first-take-name-on-the-bus-then-return-in-sta.patch
Patch19: 0020-alsa-cover-bass-boost-mixer-element.patch
Patch20: 0021-Mark-shared-variables-as-volatile.patch
Patch21: 0022-udev-use-ID_MODEL_ENC-instead-of-ID_MODEL-if-it-is-s.patch
Patch22: 0023-pacat-allow-configuration-of-latency-in-msec.patch
Patch23: 0024-client-implement-PULSE_LATENCY_MSEC.patch
Patch24: 0025-client-include-dolby-channel-names-in-comments.patch
Patch25: 0026-alsa-add-profile-set-for-M-Audio-FastTrack-Pro-USB.patch
Patch26: 0027-threaded-mainloop-Properly-initialise-m-n_waiting_fo.patch
Patch27: 0028-udev-Use-SOUND_CLASS-instead-of-SOUND_FORM_FACTOR-wh.patch
Patch28: 0029-More-src-pulsecore-cpu-arm.c-FTBFS-fixes.patch
Patch29: 0030-Fix-the-following-warnings-which-now-cause-buildd-fa.patch
Patch30: 0031-libpulse-Store-pa_stream-pointers-to-hashmaps-instea.patch
Patch31: 0032-native-rework-handling-of-seeks-that-depend-on-varia.patch
Patch32: 0033-core-Fix-macro-typo-PA_SINK_IS_LINKED-PA_SINK_INPUT_.patch
Patch33: 0034-alsa-cover-Desktop-Speaker-mixer-elements.patch
Patch34: 0035-alsa-cover-Shared-Mic-Line-in-Analog-Source.patch
Patch35: 0036-alsa-cover-Internal-Mic-elements.patch
Patch36: 0037-alsa-use-default-output-port-names.patch
Patch37: 0038-build-sys-add-gobject-to-build-dependencies.patch
Patch38: 0039-padsp-emulate-dev-audio-too.patch
Patch39: 0040-dbus-first-restart-timer-then-dispatch-it.patch
Patch40: 0041-fdsem-be-more-verbose-when-reading-from-eventfd-fail.patch
Patch41: 0042-pacat-always-fully-fulfill-write-requests.patch
Patch42: 0043-pacmd-store-away-fd-type.patch
Patch43: 0044-pacmd-don-t-enter-busy-loop-when-reading-from-stdin-.patch
Patch44: 0045-shm-don-t-complain-about-missing-SHM-segments.patch
Patch45: 0046-vala-fix-definition-of-INVALID_INDEX.patch
Patch46: 0047-vala-fix-definition-of-the-GLib-mainloop-adapter.patch
Patch47: 0048-Add-missing-profile-and-alsa-mixer-paths-to-src-Make.patch
Patch48: 0049-channelmap-Use-Subwoofer-as-pretty-name-for-LFE.patch
Patch49: 0050-vala-fix-wrapping-of-port-setting-calls.patch
Patch50: 0051-proplist-explicitly-mention-a-role-test.patch
Patch51: 0052-stream-restore-be-a-little-bit-more-verbose-why-we-d.patch
Patch52: 0053-sample-cache-use-the-sample-name-as-unmodified-fallb.patch
Patch53: 0054-scache-when-playing-a-sample-from-the-cache-make-sur.patch
Patch54: 0055-pacat-pass-buffer_attr-to-recording-streams-too.patch
Patch55: 0056-suspend-on-idle-resume-audio-device-even-for-initial.patch
Patch56: 0057-native-improve-logging-for-buffer_attrs.patch
Patch57: 0058-alsa-util-strip-spaces-from-ALSA-card-pcm-names.patch
Patch58: 0059-alsa-reset-max_rewind-max_request-while-suspending.patch
Patch59: 0060-core-util-introduce-generic-function-pa_strip.patch
Patch60: 0061-esd-simple-use-pa_memblockq_pop_missing.patch
Patch61: 0062-core-rework-how-stream-volumes-affect-sink-volumes.patch
Patch62: 0063-core-util-ensure-that-we-chmod-only-the-dir-we-ourse.patch
Patch63: 0064-Handle-Digital-Mic-as-an-Input-Source.patch
Patch65: 0066-intended-roles-Do-not-pick-monitor-sources-when-doin.patch
Patch66: 0067-socket-client-properly-handle-asyncns-failures.patch
Patch67: translation-bz575687.patch
Patch68: translation-bz575687-2.patch
Patch69: rhbz647797.patch
Patch70: fix-hdmi.patch
Patch71: 0001-rules-remove-stray-goto.patch
Patch72: 0001-man-improve-manpage.patch
Patch73: 0001-combine-sink-rework-output-add-remove.patch
Patch74: 0002-combine-sink-add-support-for-DYNAMIC_LATENCY.patch
Patch75: 0003-combine-sink-Make-the-latency-range-calculation-easi.patch
Patch76: 0004-combine-sink-Add-a-convenience-variable.patch
Patch77: 0005-combine-sink-Fix-the-initial-requested-latency-of-ne.patch
Patch78: 0006-combine-sink-Rearrange-block_usec-initialization.patch
Patch79: 0001-profile-sets-remove-missing-paths.patch
Patch80: 0001-Fix-input-device-for-M-audio-fasttrack-pro.patch

Patch10001: pulseaudio-0.9.21-svolume-arm.patch

URL:            http://pulseaudio.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  m4
# Libtool is dragging in rpaths.  Fedora's libtool should get rid of the
# unneccessary ones.
BuildRequires:  libtool
BuildRequires:  libtool-ltdl-devel
BuildRequires:  intltool
BuildRequires:  pkgconfig
BuildRequires:  doxygen
BuildRequires:  xmltoman
BuildRequires:  tcp_wrappers-devel
BuildRequires:  libsamplerate-devel
BuildRequires:  libsndfile-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  glib2-devel
BuildRequires:  gtk2-devel
BuildRequires:  GConf2-devel
BuildRequires:  avahi-devel
%if 0%{?rhel} == 0
BuildRequires:  lirc-devel
BuildRequires:  jack-audio-connection-kit-devel
%endif
BuildRequires:  libatomic_ops-devel
%ifnarch s390 s390x
BuildRequires:  bluez-libs-devel
%endif
BuildRequires:  libXt-devel
BuildRequires:  xorg-x11-proto-devel
BuildRequires:  libXtst-devel
BuildRequires:  libXi-devel
BuildRequires:  libSM-devel
BuildRequires:  libX11-devel
BuildRequires:  libICE-devel
BuildRequires:  openssl-devel
BuildRequires:  libtdb-devel
BuildRequires:  speex-devel >= 1.2
BuildRequires:  libasyncns-devel
BuildRequires:  libudev-devel >= 143
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Obsoletes:      pulseaudio-devel
Obsoletes:      pulseaudio-core-libs
Provides:       pulseaudio-core-libs
Requires:       udev >= 145-3
Requires:       rtkit
Requires:       kernel >= 2.6.30

%description
PulseAudio is a sound server for Linux and other Unix like operating
systems. It is intended to be an improved drop-in replacement for the
Enlightened Sound Daemon (ESOUND).

%package esound-compat
Summary:        PulseAudio EsounD daemon compatibility script
Group:          System Environment/Daemons
Requires:       %{name} = %{version}-%{release}
Provides:       esound
Obsoletes:      esound

%description esound-compat
A compatibility script that allows applications to call /usr/bin/esd
and start PulseAudio with EsounD protocol modules.

%if 0%{?rhel} == 0
%package module-lirc
Summary:        LIRC support for the PulseAudio sound server
Group:          System Environment/Daemons
Requires:       %{name} = %{version}-%{release}

%description module-lirc
LIRC volume control module for the PulseAudio sound server.
%endif

%package module-x11
Summary:        X11 support for the PulseAudio sound server
Group:          System Environment/Daemons
Requires:       %{name} = %{version}-%{release}
Requires:       %{name}-utils = %{version}-%{release}

%description module-x11
X11 bell and security modules for the PulseAudio sound server.

%package module-zeroconf
Summary:        Zeroconf support for the PulseAudio sound server
Group:          System Environment/Daemons
Requires:       %{name} = %{version}-%{release}
Requires:       pulseaudio-utils

%description module-zeroconf
Zeroconf publishing module for the PulseAudio sound server.

%ifnarch s390 s390x
%package module-bluetooth
Summary:        Bluetooth support for the PulseAudio sound server
Group:          System Environment/Daemons
Requires:       %{name} = %{version}-%{release}
Requires:       bluez >= 4.34

%description module-bluetooth
Contains Bluetooth audio (A2DP/HSP/HFP) support for the PulseAudio sound server.

Also contains a module that can be used to automatically turn down the volume if
a bluetooth mobile phone leaves the proximity or turn it up again if it enters the
proximity again
%endif

%if 0%{?rhel} == 0
%package module-jack
Summary:        JACK support for the PulseAudio sound server
Group:          System Environment/Daemons
Requires:       %{name} = %{version}-%{release}

%description module-jack
JACK sink and source modules for the PulseAudio sound server.
%endif

%package module-gconf
Summary:        GConf support for the PulseAudio sound server
Group:          System Environment/Daemons
Requires:       %{name} = %{version}-%{release}

%description module-gconf
GConf configuration backend for the PulseAudio sound server.

%package libs
Summary:        Libraries for PulseAudio clients
License:        LGPLv2+
Group:          System Environment/Libraries
Provides:       pulseaudio-lib
Obsoletes:      pulseaudio-lib

%description libs
This package contains the runtime libraries for any application that wishes
to interface with a PulseAudio sound server.

%package core-libs
Summary:        Core libraries for the PulseAudio sound server.
License:        LGPLv2+
Group:          System Environment/Libraries

%description core-libs
This package contains runtime libraries that are used internally in the
PulseAudio sound server.

%package libs-glib2
Summary:        GLIB 2.x bindings for PulseAudio clients
License:        LGPLv2+
Group:          System Environment/Libraries
Provides:       pulseaudio-lib-glib2
Obsoletes:      pulseaudio-lib-glib2

%description libs-glib2
This package contains bindings to integrate the PulseAudio client library with
a GLIB 2.x based application.

%package libs-zeroconf
Summary:    Zeroconf support for PulseAudio clients
License:        LGPLv2+
Group:      System Environment/Libraries
Provides:       pulseaudio-lib-zeroconf
Obsoletes:      pulseaudio-lib-zeroconf

%description libs-zeroconf
This package contains the runtime libraries and tools that allow PulseAudio
clients to automatically detect PulseAudio servers using Zeroconf.

%package libs-devel
Summary:        Headers and libraries for PulseAudio client development
License:        LGPLv2+
Group:          Development/Libraries
Requires:       %{name}-libs = %{version}-%{release}
Requires:       %{name}-libs-glib2 = %{version}-%{release}
Requires:       %{name}-libs-zeroconf = %{version}-%{release}
Requires:       pkgconfig
Requires:       glib2-devel
%if 0%{?rhel} == 0
Requires:       vala
%endif
Provides:       pulseaudio-lib-devel
Obsoletes:      pulseaudio-lib-devel

%description libs-devel
Headers and libraries for developing applications that can communicate with
a PulseAudio sound server.

%package utils
Summary:        PulseAudio sound server utilities
License:        LGPLv2+
Group:          Applications/Multimedia
Requires:       %{name}-libs = %{version}-%{release}

%description utils
This package contains command line utilities for the PulseAudio sound server.

%package gdm-hooks
Summary:        PulseAudio GDM integration
License:        LGPLv2+
Group:          Applications/Multimedia
Requires:       gdm >= 1:2.22.0
# for the gdm user
Requires(pre):  gdm

%description gdm-hooks
This package contains GDM integration hooks for the PulseAudio sound server.

%prep
%setup -q -T -b0
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1
%patch31 -p1
%patch32 -p1
%patch33 -p1
%patch34 -p1
%patch35 -p1
%patch36 -p1
%patch37 -p1
%patch38 -p1
%patch39 -p1
%patch40 -p1
%patch41 -p1
%patch42 -p1
%patch43 -p1
%patch44 -p1
%patch45 -p1
%patch46 -p1
%patch47 -p1
%patch48 -p1
%patch49 -p1
%patch50 -p1
%patch51 -p1
%patch52 -p1
%patch53 -p1
%patch54 -p1
%patch55 -p1
%patch56 -p1
%patch57 -p1
%patch58 -p1
%patch59 -p1
%patch60 -p1
%patch61 -p1
%patch62 -p1
%patch63 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p2
%patch69 -p1
%patch70 -p1
%patch71 -p1
%patch72 -p1
%patch73 -p1
%patch74 -p1
%patch75 -p1
%patch76 -p1
%patch77 -p1
%patch78 -p1
%patch79 -p1
%patch80 -p1

%patch10001 -p1

%build
autoreconf
%configure --disable-static --disable-rpath --with-system-user=pulse --with-system-group=pulse --with-access-group=pulse-access --disable-hal
# we really should preopen here --preopen-mods=module-udev-detect.la, --force-preopen
make LIBTOOL=/usr/bin/libtool %{?_smp_mflags}
make doxygen

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.la $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/*.la
# configure --disable-static had no effect; delete manually.
rm -rf $RPM_BUILD_ROOT%{_libdir}/*.a $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/*.a
rm $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/liboss-util.so
rm $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/module-oss.so
rm $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/module-detect.so
rm $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/module-pipe-sink.so
rm $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/module-pipe-source.so
rm $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/module-device-manager.so
rm -f $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/module-jack-sink.so
rm -f $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/module-jack-source.so
rm -f $RPM_BUILD_ROOT%{_libdir}/pulse-%{version}/modules/module-lirc.so
rm $RPM_BUILD_ROOT%{_bindir}/start-pulseaudio-kde
rm $RPM_BUILD_ROOT%{_sysconfdir}/xdg/autostart/pulseaudio-kde.desktop
# preserve time stamps, for multilib's sake
touch -r src/daemon/daemon.conf.in $RPM_BUILD_ROOT%{_sysconfdir}/pulse/daemon.conf
touch -r src/daemon/default.pa.in $RPM_BUILD_ROOT%{_sysconfdir}/pulse/default.pa
touch -r man/pulseaudio.1.xml.in $RPM_BUILD_ROOT%{_mandir}/man1/pulseaudio.1
touch -r man/default.pa.5.xml.in $RPM_BUILD_ROOT%{_mandir}/man5/default.pa.5
touch -r man/pulse-client.conf.5.xml.in $RPM_BUILD_ROOT%{_mandir}/man5/pulse-client.conf.5
touch -r man/pulse-daemon.conf.5.xml.in $RPM_BUILD_ROOT%{_mandir}/man5/pulse-daemon.conf.5
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/pulse
mkdir -p $RPM_BUILD_ROOT%{_localstatedir}/lib/gdm/.pulse
cp $RPM_SOURCE_DIR/default.pa-for-gdm $RPM_BUILD_ROOT%{_localstatedir}/lib/gdm/.pulse/default.pa

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/groupadd -f -r pulse || :
/usr/bin/id pulse >/dev/null 2>&1 || \
            /usr/sbin/useradd -r -c 'PulseAudio System Daemon' -s /sbin/nologin -d /var/run/pulse -g pulse pulse || :
/usr/sbin/groupadd -f -r pulse-access || :
exit 0

%post -p /sbin/ldconfig

%postun
/sbin/ldconfig

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%post libs-glib2 -p /sbin/ldconfig
%postun libs-glib2 -p /sbin/ldconfig

%post libs-zeroconf -p /sbin/ldconfig
%postun libs-zeroconf -p /sbin/ldconfig

%files
%defattr(-,root,root)
%doc README LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%config(noreplace) %{_sysconfdir}/pulse/daemon.conf
%config(noreplace) %{_sysconfdir}/pulse/default.pa
%config(noreplace) %{_sysconfdir}/pulse/system.pa
%config(noreplace) %{_sysconfdir}/dbus-1/system.d/pulseaudio-system.conf
%{_bindir}/pulseaudio
%{_libdir}/libpulsecore-%{version}.so
%dir %{_libdir}/pulse-%{version}/
%dir %{_libdir}/pulse-%{version}/modules/
%{_libdir}/pulse-%{version}/modules/libalsa-util.so
%{_libdir}/pulse-%{version}/modules/libcli.so
%{_libdir}/pulse-%{version}/modules/libprotocol-cli.so
%{_libdir}/pulse-%{version}/modules/libprotocol-esound.so
%{_libdir}/pulse-%{version}/modules/libprotocol-http.so
%{_libdir}/pulse-%{version}/modules/libprotocol-native.so
%{_libdir}/pulse-%{version}/modules/libprotocol-simple.so
%{_libdir}/pulse-%{version}/modules/librtp.so
%{_libdir}/pulse-%{version}/modules/module-alsa-sink.so
%{_libdir}/pulse-%{version}/modules/module-alsa-source.so
%{_libdir}/pulse-%{version}/modules/module-alsa-card.so
%{_libdir}/pulse-%{version}/modules/module-cli-protocol-tcp.so
%{_libdir}/pulse-%{version}/modules/module-cli-protocol-unix.so
%{_libdir}/pulse-%{version}/modules/module-cli.so
%{_libdir}/pulse-%{version}/modules/module-combine.so
%{_libdir}/pulse-%{version}/modules/module-loopback.so
%{_libdir}/pulse-%{version}/modules/module-esound-compat-spawnfd.so
%{_libdir}/pulse-%{version}/modules/module-esound-compat-spawnpid.so
%{_libdir}/pulse-%{version}/modules/module-esound-protocol-tcp.so
%{_libdir}/pulse-%{version}/modules/module-esound-protocol-unix.so
%{_libdir}/pulse-%{version}/modules/module-esound-sink.so
%{_libdir}/pulse-%{version}/modules/module-udev-detect.so
%{_libdir}/pulse-%{version}/modules/module-hal-detect.so
%{_libdir}/pulse-%{version}/modules/module-http-protocol-tcp.so
%{_libdir}/pulse-%{version}/modules/module-http-protocol-unix.so
%{_libdir}/pulse-%{version}/modules/module-match.so
%{_libdir}/pulse-%{version}/modules/module-mmkbd-evdev.so
%{_libdir}/pulse-%{version}/modules/module-native-protocol-fd.so
%{_libdir}/pulse-%{version}/modules/module-native-protocol-tcp.so
%{_libdir}/pulse-%{version}/modules/module-native-protocol-unix.so
%{_libdir}/pulse-%{version}/modules/module-null-sink.so
%{_libdir}/pulse-%{version}/modules/module-rescue-streams.so
%{_libdir}/pulse-%{version}/modules/module-rtp-recv.so
%{_libdir}/pulse-%{version}/modules/module-rtp-send.so
%{_libdir}/pulse-%{version}/modules/module-simple-protocol-tcp.so
%{_libdir}/pulse-%{version}/modules/module-simple-protocol-unix.so
%{_libdir}/pulse-%{version}/modules/module-sine.so
%{_libdir}/pulse-%{version}/modules/module-tunnel-sink.so
%{_libdir}/pulse-%{version}/modules/module-tunnel-source.so
%{_libdir}/pulse-%{version}/modules/module-volume-restore.so
%{_libdir}/pulse-%{version}/modules/module-suspend-on-idle.so
%{_libdir}/pulse-%{version}/modules/module-default-device-restore.so
%{_libdir}/pulse-%{version}/modules/module-device-restore.so
%{_libdir}/pulse-%{version}/modules/module-stream-restore.so
%{_libdir}/pulse-%{version}/modules/module-card-restore.so
%{_libdir}/pulse-%{version}/modules/module-ladspa-sink.so
%{_libdir}/pulse-%{version}/modules/module-remap-sink.so
%{_libdir}/pulse-%{version}/modules/module-always-sink.so
%{_libdir}/pulse-%{version}/modules/module-console-kit.so
%{_libdir}/pulse-%{version}/modules/module-position-event-sounds.so
%{_libdir}/pulse-%{version}/modules/module-augment-properties.so
%{_libdir}/pulse-%{version}/modules/module-cork-music-on-phone.so
%{_libdir}/pulse-%{version}/modules/module-sine-source.so
%{_libdir}/pulse-%{version}/modules/module-intended-roles.so
%{_libdir}/pulse-%{version}/modules/module-rygel-media-server.so
%{_datadir}/pulseaudio/alsa-mixer/paths/*
%{_datadir}/pulseaudio/alsa-mixer/profile-sets/*
%{_mandir}/man1/pulseaudio.1.gz
%{_mandir}/man5/default.pa.5.gz
%{_mandir}/man5/pulse-client.conf.5.gz
%{_mandir}/man5/pulse-daemon.conf.5.gz
/lib/udev/rules.d/90-pulseaudio.rules
%dir %{_libexecdir}/pulse
%attr(0700, pulse, pulse) %dir %{_localstatedir}/lib/pulse

%files esound-compat
%defattr(-,root,root)
%{_bindir}/esdcompat
%{_mandir}/man1/esdcompat.1.gz

%if 0%{?rhel} == 0
%files module-lirc
%defattr(-,root,root)
%{_libdir}/pulse-%{version}/modules/module-lirc.so
%endif

%files module-x11
%defattr(-,root,root)
%config %{_sysconfdir}/xdg/autostart/pulseaudio.desktop
%{_bindir}/start-pulseaudio-x11
%{_libdir}/pulse-%{version}/modules/module-x11-bell.so
%{_libdir}/pulse-%{version}/modules/module-x11-publish.so
%{_libdir}/pulse-%{version}/modules/module-x11-xsmp.so
%{_libdir}/pulse-%{version}/modules/module-x11-cork-request.so

%files module-zeroconf
%defattr(-,root,root)
%{_libdir}/pulse-%{version}/modules/libavahi-wrap.so
%{_libdir}/pulse-%{version}/modules/module-zeroconf-publish.so
%{_libdir}/pulse-%{version}/modules/module-zeroconf-discover.so
%{_libdir}/pulse-%{version}/modules/libraop.so
%{_libdir}/pulse-%{version}/modules/module-raop-discover.so
%{_libdir}/pulse-%{version}/modules/module-raop-sink.so

%if 0%{?rhel} == 0
%files module-jack
%defattr(-,root,root)
%{_libdir}/pulse-%{version}/modules/module-jack-sink.so
%{_libdir}/pulse-%{version}/modules/module-jack-source.so
%endif

%ifnarch s390 s390x
%files module-bluetooth
%defattr(-,root,root)
%{_libdir}/pulse-%{version}/modules/module-bluetooth-proximity.so
%{_libdir}/pulse-%{version}/modules/module-bluetooth-device.so
%{_libdir}/pulse-%{version}/modules/module-bluetooth-discover.so
%{_libdir}/pulse-%{version}/modules/libbluetooth-ipc.so
%{_libdir}/pulse-%{version}/modules/libbluetooth-sbc.so
%{_libdir}/pulse-%{version}/modules/libbluetooth-util.so
%{_libexecdir}/pulse/proximity-helper
%endif

%files module-gconf
%defattr(-,root,root)
%{_libdir}/pulse-%{version}/modules/module-gconf.so
%{_libexecdir}/pulse/gconf-helper

%files libs -f %{name}.lang
%defattr(-,root,root)
%doc README LICENSE GPL LGPL
%dir %{_sysconfdir}/pulse/
%config(noreplace) %{_sysconfdir}/pulse/client.conf
%{_libdir}/libpulse.so.*
%{_libdir}/libpulsecommon-%{version}.so
%{_libdir}/libpulse-simple.so.*

%files libs-glib2
%defattr(-,root,root)
%{_libdir}/libpulse-mainloop-glib.so.*

%files libs-zeroconf
%defattr(-,root,root)
%{_bindir}/pabrowse
%{_libdir}/libpulse-browse.so.*
%{_mandir}/man1/pabrowse.1.gz

%files libs-devel
%defattr(-,root,root)
%doc doxygen/html
%{_includedir}/pulse/
%{_libdir}/libpulse.so
%{_libdir}/libpulse-mainloop-glib.so
%{_libdir}/libpulse-simple.so
%{_libdir}/libpulse-browse.so
%{_libdir}/pkgconfig/libpulse*.pc
%{_datadir}/vala/vapi/libpulse.vapi

%files utils
%defattr(-,root,root)
%{_bindir}/pacat
%{_bindir}/pacmd
%{_bindir}/pactl
%{_bindir}/paplay
%{_bindir}/parec
%{_bindir}/pamon
%{_bindir}/parecord
%{_bindir}/pax11publish
%{_bindir}/padsp
%{_bindir}/pasuspender
%{_libdir}/libpulsedsp.so
%{_mandir}/man1/pacat.1.gz
%{_mandir}/man1/pacmd.1.gz
%{_mandir}/man1/pactl.1.gz
%{_mandir}/man1/paplay.1.gz
%{_mandir}/man1/pasuspender.1.gz
%{_mandir}/man1/padsp.1.gz
%{_mandir}/man1/pax11publish.1.gz

%files gdm-hooks
%defattr(-,root,root)
%attr(0700, gdm, gdm) %dir %{_localstatedir}/lib/gdm/.pulse
%attr(0600, gdm, gdm) %{_localstatedir}/lib/gdm/.pulse/default.pa

%changelog
* Thu Feb 04 2016 Jacco Ligthart <jacco@redsleeve.org> 0.9.21-24.0
- Fix building on ARM

* Thu Nov 26 2015 Wim Taymans <wtaymans@redhat.com> 0.9.21-24
- Rebuild for fast
- Resolves: rhbz#656998

* Thu Nov 26 2015 Wim Taymans <wtaymans@redhat.com> 0.9.21-23
- Fix input device for M-audio fasttrack pro
- Fixes rhbz#656998

* Thu Feb 12 2015 Wim Taymans <wtaymans@redhat.com> 0.9.21-22
- remove missing paths from extra hdmi profile
- Resolves: rhbz#1191623

* Tue Feb 03 2015 Wim Taymans <wtaymans@redhat.com> 0.9.21-21
- Add DYNAMIC latency for module-combine
- Resolves: rhbz#1111375

* Tue Feb 03 2015 Wim Taymans <wtaymans@redhat.com> 0.9.21-20
- improve manpage
  Resolves: rhbz#812444

* Tue Jan 20 2015 Wim Taymans <wtaymans@redhat.com> 0.9.21-19
- bump version for fastrack build

* Mon Jun 23 2014 Wim Taymans <wtaymans@redhat.com> 0.9.21-18
- Remove leftover goto from merge
  Related: rhbz#1110950

* Tue Jun 03 2014 Ray Strode <rstrode@redhat.com> 0.9.21-17
- Fix file list in Makefile
  Related: rhbz#1095750

* Mon Jun 02 2014 Ray Strode <rstrode@redhat.com> - 0.9.21-16
- Fix HDMI audio for cards with multiple devices
  Resolves: rhbz#1095750

* Tue Jul  3 2012 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-15
- Use the right patch
- Resolves: rhbz#647797

* Tue Jun 26 2012 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-14
- Resolves: rhbz#647797

* Wed Aug 11 2010 Lennart Poettering <lennart@poettering.net> - 0.9.21-13
- add missing patch to CVS
- Resolves: rhbz#575687

* Wed Aug 11 2010 Lennart Poettering <lennart@poettering.net> - 0.9.21-12
- Add Gujarati translation from 575687
- Resolves: rhbz#575687

* Mon May 24 2010 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-11
- Fix version screwup
- Resolves: rhbz#575687
- Resolves: rhbz#561772

* Mon May 24 2010 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-10
- Forgot patch
- Resolves: rhbz#575687
- Resolves: rhbz#561772

* Fri May 14 2010 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-9
- Add translations
- Resolves: rhbz#575687
- Resolves: rhbz#561772

* Mon Mar 22 2010 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-8
- Port over fixes from F-12
- Related: rhbz#566327
- Related: rhbz#571815

* Sun Jan 17 2010 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-7
- backport another fix from upstream
- Related: rhbz#543948

* Fri Jan 15 2010 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-6
- backport 31 fixes from upstream git
- sync spec file with f12
- Related: rhbz#543948

* Fri Jan 15 2010 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-5
- Don't build bluetooth stuff on s390 (#529866)

* Tue Jan 12 2010 Matthias Clasen <mclasen@redhat.com> - 0.9.21-4
- Don't require vala (#554749)

* Fri Jan 8 2010 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-3
- Fix date of changelog entry
- Related: rhbz#543948

* Fri Jan 8 2010 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-2
- Do not build against lirc on RHEL
- Related: rhbz#543948

* Fri Dec  4 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.9.21-1.1
- Do not build against jack on RHEL

* Mon Nov 23 2009 Lennart Poettering <lpoetter@redhat.com> - 0.9.21-1
- New release

* Wed Nov 11 2009 Lennart Poettering <lpoetter@redhat.com> - 0.9.20-1
- New release

* Wed Nov 04 2009 Warren Togami <wtogami@redhat.com> - 0.9.19-2
- Bug #532583 gdm should not require pulseaudio

* Wed Sep 30 2009 Lennart Poettering <lpoetter@redhat.com> - 0.9.19-1
- New release

* Sat Sep 19 2009 Lennart Poettering <lpoetter@redhat.com> - 0.9.18-1
- New release

* Fri Sep 11 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.17-1
- Final release

* Thu Sep 10 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.16-14
- Final release

* Thu Sep 3 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.16-13.test7
- Fix build for ppc

* Thu Sep 3 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.16-12.test7
- New test release

* Thu Aug 27 2009 Tomas Mraz <tmraz@redhat.com> - 0.9.16-11.test6
- rebuilt with new openssl

* Mon Aug 24 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.16-10.test6
- Fix build for ppc

* Mon Aug 24 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.16-9.test6
- New test release

* Thu Aug 20 2009 Matthias Clasen <mclasen@redhat.com> - 0.9.16-7.test5
- Fix install ordering between gdm and pulseaudio-gdm-hooks

* Wed Aug 19 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.16-6.test5
- New test release

* Wed Aug 5 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.16-5.test4
- New test release

* Tue Jul 28 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.16-4.test3
- New test release

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.16-3.test2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Jul 2 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.16-2.test2
- New test release

* Tue Jun 23 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.16-1.test1
- Fix endianess build

* Tue Jun 23 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.16-0.test1
- First 0.9.16 test release

* Wed Apr 22 2009 Warren Togami <wtogami@redhat.com> 0.9.15-11
- Bug #497214
  Do not start pulseaudio daemon if PULSE_SERVER directs pulse elsewhere.

* Mon Apr 13 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-10
- Final 0.9.15 release

* Thu Apr 9 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-9.test8
- New test release

* Wed Apr 1 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-8.test7
- Only load bt modules when installed

* Wed Apr 1 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-7.test7
- New test release

* Wed Apr 1 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-6.test6
- Fix mistag

* Wed Apr 1 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-5.test6
- Fix tarball name

* Wed Apr 1 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-4.test6
- New test release

* Thu Mar 5 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-3.test5
- New test release

* Thu Mar 5 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-3.test4
- New test release

* Fri Feb 27 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-3.test3
- Steal patch from git master to fix .so dependencies

* Wed Feb 25 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-2.test3
- Add more missing X11 dependencies

* Wed Feb 25 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-1.test3
- Add missing dependency on XTEST

* Tue Feb 24 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-0.test3
- New test release

* Thu Feb 12 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.15-0.test2
- New test release

* Tue Jan 13 2009 Adel Gadllah <adel.gadllah@gmail.com> 0.9.14-2
- Prefer mixer controls with volumes over switches

* Tue Jan 13 2009 Lennart Poettering <lpoetter@redhat.com> 0.9.14-1
- New release

* Thu Nov 13 2008 Matthias Clasen <mclasen@redhat.com> 0.9.13-7
- Rebuild

* Sat Nov 1 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.13-6
- Backport another two fixes from current git master

* Tue Oct 28 2008 Matthias Clasen <mclasen@redhat.com> 0.9.13-5
- Require new enough speex-devel

* Fri Oct 24 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.13-4
- Backport another fix from current git master

* Thu Oct 23 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.13-3
- Backport a couple of fixes from current git master

* Thu Oct 9 2008 Matthhias Clasen <mclasen@redhat.com> 0.9.13-2
- Handle locales properly

* Mon Oct 6 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.13-1
- New release

* Mon Sep 15 2008 Matthias Clasen <mclasen@redhat.com> 0.9.12-6
- Survive a missing ~/.pulse (#462407)

* Thu Sep 11 2008 - Bastien Nocera <bnocera@redhat.com> 0.9.12-5
- Rebuild

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.12-4
- Ship /var/lib/pulse in the RPM

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.12-3
- Don't remove pulse users/groups on package removal

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.12-2
- Add intltool to deps

* Tue Sep 9 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.12-1
- Release 0.9.12

* Thu Jul 24 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-1
- Final release 0.9.11

* Tue Jul 22 2008 Jon McCann <jmccann@redhat.com> 0.9.11-0.7.git20080626
- Fix for CK API changes

* Thu Jun 26 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-0.6.git20080626
- New GIT snapshot

* Sun Jun 22 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-0.5.svn20080622
- New GIT snapshot

* Wed Jun 18 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-0.4.svn20080618
- New SVN snapshot

* Thu May 30 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-0.3.svn20080529
- Fix snapshot versioning

* Thu May 29 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.11-0.0.svn20080529
- New SVN snapshot

* Tue May 20 2008 Matthias Clasen <mclasen@redhat.com> 0.9.11-0.2.svn20080516
- Actually apply the patch

* Sat May 17 2008 Matthias Clasen <mclasen@redhat.com> 0.9.11-0.1.svn20080516
- Fix a wrong assertion in module-default-device-restore

* Fri May 16 2008 Matthias Clasen <mclasen@redhat.com> 0.9.11-0.0.svn20080516
- Update to an svn snapshot of the 'glitch-free' rewrite of pulseaudio

* Sun Mar 30 2008 Lennart Poettering <lpoetter@redhat.com> 0.9.10-1
- Update to PulseAudio 0.9.10
- drop all patches, since they have been integrated upstream

* Thu Mar 27 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-13
- Abort on CPU time comsumption, so we can get core

* Thu Mar 13 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-12
- Own /usr/libexec/pulse (#437228)

* Wed Mar 12 2008 Adam Jackson <ajax@redhat.com> 0.9.8-11
- pulseaudio-0.9.8-disable-realtime.patch: Don't ask PolicyKit for increased
  scheduling mojo for now.  It's not clear that it's a win; and if it is,
  the policy should just be fixed to always allow it.

* Wed Mar 12 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-10
- Build the manual pages with xmltoman

* Fri Feb 29 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-9
- Fix the fix.

* Fri Feb 29 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-8
- Fix multilib issue (#228383)
- Prevent dumping core if exiting sooner that ltdl initializaion (#427962)

* Thu Feb 21 2008 Adam Tkac <atkac redhat com> 0.9.8-7
- really rebuild against new libcap

* Sun Feb 17 2008 Adam Tkac <atkac redhat com> 0.9.8-6
- rebuild against new libcap

* Wed Jan 23 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-5
- Fix CVE-2008-0008 security issue (#425481)

* Sun Jan 13 2008 Lubomir Kundrak <lkundrak@redhat.com> 0.9.8-4.1
- Actually add content to pulseaudio-0.9.8-create-dot-pulse.patch
- Make the Source0 tag point to URL instead of a local file
- Drop the nochown patch; it's not applied at all and no longer needed

* Thu Nov 29 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.8-4
- add missing dependency on pulseaudio-utils for pulseaudio-module-x11

* Thu Nov 29 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.8-3
- Create ~/.pulse/ if not existant

* Thu Nov 29 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.8-2
- Add missing dependency on jack-audio-connection-kit-devel

* Wed Nov 28 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.8-1
- Upgrade to current upstream

* Wed Oct 17 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.16.svn20071017
- Another SVN snapshot, fixing another round of bugs (#330541)
- Split libpulscore into a seperate package to work around multilib limitation (#335011)

* Mon Oct 1 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.15.svn20071001
- Another SVN snapshot, fixing another round of bugs

* Sat Sep 29 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.14.svn20070929
- Another SVN snapshot, fixing a couple of subtle bugs

* Tue Sep 25 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.13.svn20070925
- Remove libpulsecore.so symlink from pulseaudio-libs-devel to avoid multilib issues

* Tue Sep 25 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.12.svn20070925
- New SVN snapshot
- Split off libflashsupport again
- Rename "-lib" packages to "-libs", like all other packages do it.
- Provide esound

* Fri Sep 7 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.11.svn20070907
- Update SVN snapshot, don't link libpulsecore.so statically anymore

* Wed Sep 5 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.10.svn20070905
- Update SVN snapshot

* Tue Sep 4 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.9.svn20070904
- Update SVN snapshot
- ship libflashsupport in our package
- drop pulseaudio-devel since libpulsecore is not linked statically

* Thu Aug 23 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.8.svn20070823
- Update SVN snapshot

* Thu Aug 16 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.7.svn20070816
- Update SVN snapshot

* Thu Aug 16 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.6.svn20070816
- Update SVN snapshot

* Tue Aug 14 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.5.svn20070814
- Forgot to upload tarball

* Tue Aug 14 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.4.svn20070814
- Update snapshot. Install file into /etc/xdg/autostart/ to load module-x11-smp
  only after login

* Sun Aug 12 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.3.svn20070812
- Depend on tcp_wrappers-devel instead of tcp_wrappers, to make sure we
  actually get the headers installed.

* Sun Aug 12 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.2.svn20070812
- Update snapshot, contains 64 bit build fixes, and disables module-x11-xsmp by
  default to avoid deadlock when PA is started from gnome-session

* Sun Aug 12 2007 Lennart Poettering <lpoetter@redhat.com> 0.9.7-0.1.svn20070812
- Take snapshot from SVN

* Tue May 29 2007 Pierre Ossman <drzeus@drzeus.cx> 0.9.6-2
- Add libatomic_ops-devel as a build requirement.

* Tue May 29 2007 Pierre Ossman <drzeus@drzeus.cx> 0.9.6-1
- Upgrade to 0.9.6.

* Sat Mar  2 2007 Pierre Ossman <drzeus@drzeus.cx> 0.9.5-5
- Fix merge problems with patch.

* Fri Mar  2 2007 Pierre Ossman <drzeus@drzeus.cx> 0.9.5-4
- Add patch to handle ALSA changing the frame size (bug 230211).
- Add patch for suspended ALSA devices (bug 228205).

* Mon Feb  5 2007 Pierre Ossman <drzeus@drzeus.cx> 0.9.5-3
- Add esound-compat subpackage that allows PulseAudio to be a drop-in
  replacement for esd (based on patch by Matthias Clasen).
- Backport patch allows startup to continue even when the users'
  config cannot be read.

* Wed Oct 23 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.5-2
- Create user and groups for daemon.

* Mon Aug 28 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.5-1
- Upgrade to 0.9.5.

* Wed Aug 23 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.4-3
- Make sure JACK modules are built and packaged.

* Tue Aug 22 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.4-2
- Merge the ALSA modules into the main package as ALSA is the
  standard API.

* Sun Aug 20 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.4-1
- Update to 0.9.4.
- Remove fix for rpath as it is merged upstream.

* Fri Jul 21 2006 Toshio Kuratomi <toshio@tiki-lounge.com> 0.9.3-2
- Remove static libraries.
- Fix for rpath issues.

* Fri Jul 21 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.3-1
- Update to 0.9.3
- GLib 1.2 bindings dropped.
- Howl compat dropped as Avahi is supported natively.
- Added fix for pc files on x86_64.

* Sat Jul  8 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.2-1
- Update to 0.9.2.
- Added Avahi HOWL compat dependencies.

* Thu Jun  8 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.1-1
- Update to 0.9.1.

* Mon May 29 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.0-2
- Build and package doxygen docs
- Call ldconfig for relevant subpackages.

* Mon May 29 2006 Pierre Ossman <drzeus@drzeus.cx> 0.9.0-1
- Update to 0.9.0

* Tue May  9 2006 Pierre Ossman <drzeus@drzeus.cx> 0.8.1-1
- Update to 0.8.1
- Split into more packages
- Remove the modules' static libs as those shouldn't be used (they shouldn't
  even be installed)

* Fri Feb 24 2006 Tom "spot" Callaway <tcallawa@redhat.com> 0.7-2
- dance around with perms so we don't strip the binary
- add missing BR

* Mon Nov 28 2005 Tom "spot" Callaway <tcallawa@redhat.com> 0.7-1
- Initial package for Fedora Extras
