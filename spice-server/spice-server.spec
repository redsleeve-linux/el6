
%global tarname spice

Name:           spice-server
Version:        0.12.4
Release:        13%{?dist}.2
Summary:        Implements the server side of the SPICE protocol
Group:          System Environment/Libraries
License:        LGPLv2+
URL:            http://www.spice-space.org/
Source0:        http://spice-space.org/download/releases/%{tarname}-%{version}.tar.bz2
Patch1: 0001-red_channel-prevent-adding-and-pushing-pipe-items-af.patch
Patch2: 0002-red_channel-add-ref-count-to-RedClient.patch
Patch3: 0003-main_dispatcher-add-ref-count-protection-to-RedClien.patch
Patch4: 0004-decouple-disconnection-of-the-main-channel-from-clie.patch
Patch5: 0005-reds-s-red_client_disconnect-red_channel_client_shut.patch
Patch6: 0006-snd_worker-fix-memory-leak-of-PlaybackChannel.patch
Patch7: 0007-snd_worker-snd_disconnect_channel-don-t-call-snd_cha.patch
Patch8: 0008-log-improve-debug-information-related-to-client-disc.patch
Patch9: 0009-red_worker-decrease-the-timeout-when-flushing-comman.patch
Patch10: 0010-Fix-buffer-overflow-when-decrypting-client-SPICE-tic.patch
Patch11: 0011-spice_timer_queue-don-t-call-timers-repeatedly.patch
Patch12: 0012-red_channel-add-on_input-callback-for-tracing-incomi.patch
Patch13: 0013-red_channel-add-option-to-monitor-whether-a-channel-.patch
Patch14: 0014-main_channel-monitoring-client-connection-status.patch
Patch15: 0015-Use-TLS-version-1.0-or-better.patch
Patch16: 0016-server-move-three-functions-to-red_channel.patch
Patch17: 0017-server-s-red_wait_all_sent-red_channel_wait_all_sent.patch
Patch18: 0018-red_worker-cleanup-red_clear_surface_drawables_from_.patch
Patch19: 0019-red_channel-cleanup-of-red_channel_client-blocking-m.patch
Patch20: 0020-red_worker-disconnect-the-channel-instead-of-shutdow.patch
Patch21: 0021-Don-t-truncate-large-now-values-in-_spice_timer_set.patch
Patch22: 0022-Fix-assert-in-mjpeg_encoder_adjust_params_to_bit_rat.patch
Patch23: 0023-server-don-t-assert-on-invalid-client-message.patch
Patch24: 0024-Fix-crash-when-clearing-surface-memory.patch
Patch25: 0025-server-fix-crash-when-restarting-VM-with-old-client.patch
Patch26: 0026-Validate-surface-bounding-box-before-using-it.patch
Patch27: 0027-Avoid-race-conditions-reading-monitor-configs-from-g.patch
Patch28: 0028-worker-validate-correctly-surfaces.patch
Patch29: 0029-worker-avoid-double-free-or-double-create-of-surface.patch
Patch30: 0030-Define-a-constant-to-limit-data-from-guest.patch
Patch31: 0031-Fix-some-integer-overflow-causing-large-memory-alloc.patch
Patch32: 0032-Check-properly-surface-to-be-created.patch
Patch33: 0033-Fix-buffer-reading-overflow.patch
Patch34: 0034-Prevent-32-bit-integer-overflow-in-bitmap_consistent.patch
Patch35: 0035-Fix-race-condition-on-red_get_clip_rects.patch
Patch36: 0036-Fix-race-in-red_get_image.patch
Patch37: 0037-Fix-race-condition-in-red_get_string.patch
Patch38: 0038-Fix-integer-overflow-computing-glyph_size-in-red_get.patch
Patch39: 0039-Fix-race-condition-in-red_get_data_chunks_ptr.patch
Patch40: 0040-Prevent-memory-leak-if-red_get_data_chunks_ptr-fails.patch
Patch41: 0041-Prevent-DoS-from-guest-trying-to-allocate-too-much-d.patch
Patch42: 0042-Fix-some-possible-overflows-in-red_get_string-for-32.patch
Patch43: 0043-Make-sure-we-can-read-QXLPathSeg-structures.patch
Patch44: 0044-Avoid-race-condition-copying-segments-in-red_get_pat.patch
Patch45: 0045-Prevent-data_size-to-be-set-independently-from-data.patch
Patch46: 0046-Prevent-leak-if-size-from-red_get_data_chunks-don-t-.patch
Patch47: 0047-Initial-test.patch
Patch48: 0048-Check-red_get_data_chunks_ptr-returns-success-in-red.patch
Patch49: 0049-Fix-integer-overflows-in-red_get_path.patch
Patch50: 0050-Avoid-integer-underflow-under-32-bit-architectures.patch
Patch51: 0051-Prevent-integer-overflow-in-red_get_clip_rects.patch
Patch52: 0052-Add-some-tests-for-cursors.patch
Patch53: 0053-Check-properly-if-red_get_data_chunks-fails-or-not.patch
Patch54: 0054-spicevmc-Drop-unsent-data-on-client-disconnection.patch
Patch55: 0055-smartcard-add-a-ref-to-item-before-adding-to-pipe.patch
Patch56: 0056-smartcard-allocate-msg-with-the-expected-size.patch
Patch57: 0057-create-a-function-to-validate-surface-parameters.patch
Patch58: 0058-improve-primary-surface-parameter-checks.patch
Patch59: 0059-Prevent-possible-DoS-attempts-during-protocol-handsh.patch
Patch60: 0060-Prevent-integer-overflows-in-capability-checks.patch
Patch61: 0061-main-channel-Prevent-overflow-reading-messages-from-.patch


Source100:      pyparsing.py


BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

ExclusiveArch:  x86_64

BuildRequires:  pkgconfig
BuildRequires:  gcc-c++
BuildRequires:  alsa-lib-devel
BuildRequires:  pixman-devel >= 0.18
BuildRequires:  libjpeg-turbo-devel
BuildRequires:  libXrandr-devel
BuildRequires:  libXext-devel
BuildRequires:  libXfixes-devel
BuildRequires:  openssl-devel
BuildRequires:  celt051-devel
BuildRequires:  libcacard-devel >= 0.1.2
BuildRequires:  glib2-devel >= 2.22
# BuildRequires:  spice-protocol >= 0.10.1 -- not needed since spice-0.11.3
BuildRequires:  cyrus-sasl-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool

Requires:       pixman >= 0.18
Requires:       pkgconfig

%package devel
Summary:        Header files, libraries and development documentation for %{name}
Group:          Development/Libraries

Requires:       %{name} = %{version}-%{release}
Requires:       alsa-lib-devel
Requires:       pixman-devel >= 0.18
Requires:       libjpeg-turbo-devel
Requires:       openssl-devel
Requires:       celt051-devel
Requires:       spice-protocol >= 0.12.2
Requires:       glib2-devel >= 2.22


%description
The Simple Protocol for Independent Computing Environments (SPICE) is
a remote display system built for virtual environments which allows
you to view a computing 'desktop' environment not only on the machine
where it is running, but from anywhere on the Internet and from a wide
variety of machine architectures.

This package contains the runtime libraries for any application that wishes
to be a SPICE server.

%description devel
This package contains the header files, static libraries and development
documentation for %{name}. If you like to develop programs
using %{name}, you will need to install %{name}-devel.


%prep
%setup -q -n %{tarname}-%{version}
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


# no point of calling git-version-gen for spice-common and also
# git-version-gen is missing in spice-common
sed -i 's,\[m4_esyscmd.build-aux/git-version-gen.*\],[%{version}],' spice-common/configure.ac

%build
pythonpath=$(dirname %{SOURCE100})
export PYTHONPATH=$pythonpath
autoreconf -fi
%configure --enable-smartcard --with-sasl
#sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
#sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make -C spice-common/common %{?_smp_mflags} V=1 LDFLAGS="-Wl,-z,relro"
make -C server %{?_smp_mflags} V=1 LDFLAGS="-Wl,-z,relro"


%install
rm -rf $RPM_BUILD_ROOT
make -C server install DESTDIR=$RPM_BUILD_ROOT V=1 LDFLAGS="-Wl,-z,relro"
mkdir -p $RPM_BUILD_ROOT/%{_libdir}/pkgconfig
install -m 00644 %{name}.pc $RPM_BUILD_ROOT/%{_libdir}/pkgconfig


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-, root, root, 0755)
%doc COPYING README
%{_libdir}/libspice-server.so.*

%files devel
%defattr(-, root, root, 0755)
%doc COPYING README
%{_includedir}/spice-server/
%{_libdir}/libspice-server.so
%{_libdir}/pkgconfig/spice-server.pc
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la


%changelog
* Fri Dec 09 2016 Frediano Ziglio <fziglio@redhat.com> - 0.12.4-13.2
- Fix buffer overflow in main_channel_alloc_msg_rcv_buf when reading large
  messages.
  Resolves: CVE-2016-9577
- Fix remote DoS via crafted message.
  Resolves: CVE-2016-9578

* Tue Apr 26 2016 Christophe Fergeau <cfergeau@redhat.com> - 0.12.4-13.1
- Fix heap-based memory corruption within smartcard handling
  Resolves: CVE-2016-0749
- Fix host memory access from guest with invalid primary surface parameters
  Resolves: CVE-2016-2150

* Fri Jan 22 2016 Christophe Fergeau <cfergeau@redhat.com> 0.12.4-13
- Fix " qemu-kvm: spicevmc.c:324: spicevmc_red_channel_alloc_msg_rcv_buf:
  Assertion `!state->recv_from_client_buf' failed." assertion during migration
  Resolves: rhbz#1264113

* Wed Sep 23 2015 Frediano Ziglio <fziglio@redhat.com> 0.12.4-12.3
- CVE-2015-5260 CVE-2015-5261 fixed various security flaws
  Resolves: rhbz#1262770

* Wed Sep 23 2015 Frediano Ziglio <fziglio@redhat.com> 0.12.4-12.2
- Validate surface_id
  Resolves: rhbz#1262770

* Tue Jul 21 2015 Christophe Fergeau <cfergeau@redhat.com> 0.12.4-12.1
- Avoid race conditions reading monitor configs from guest. This race could
  trigger memory corruption host-side
  Resolves: rhbz#1239124

* Mon Mar 02 2015 Christophe Fergeau <cfergeau@redhat.com> 0.12.4-12
- Fix spicevmc-related crash which could be triggered with older clients
  Resolves: rhbz#1163480
- Fix crash when using VNC + QXL + rhel-6.0.0 machine type
  Resolves: rhbz#1135372

* Thu Aug 07 2014 Marc-Andre Lureau <marcandre.lureau@redhat.com> 0.12.4-11
- Fix invalid surface clearing
  Resolves: rhbz#1127342

* Tue Aug 05 2014 Marc-Andre Lureau <marcandre.lureau@redhat.com> 0.12.4-10
- Fix crash on invalid client message.
  Resolves: rhbz#962187

* Tue Jun 03 2014 Christophe Fergeau <cfergeau@redhat.com> 0.12.4-9
- Fix potential infinite loop on long running VMs (> 46 days)
  Resolves: rhbz#1072700
- Fix assertion in video streaming code
  Resolves: rhbz#1086820

* Fri Apr 25 2014 Christophe Fergeau <cfergeau@redhat.com> 0.12.4-8
- Fix bad dates in changelog
  Resolves: rhbz#1038670
- Fix crash on migration during reboot
  Resolves: rhbz#1004443
- Use TLS 1.0 or better
  Resolves: rhbz#1035695

* Mon Dec 02 2013 Uri Lublin <uril@redhat.com> 0.12.4-7
- Monitor whether the client is alive
  Resolves: rhbz#994175

* Mon Oct 14 2013 Christophe Fergeau <cfergeau@redhat.com> 0.12.4-6
- Fix bad error handling in the patch for CVE-2013-4282
  Related: rhbz#999839 (CVE-2013-4282)

* Thu Oct 10 2013 Christophe Fergeau <cfergeau@redhat.com> 0.12.4-5
- Make sure we build with -Wl,-z,relro. We used to be getting that flag
  from openssl, but this is no longer the case, and rpmdiff gave a huge
  warning about it being gone
  Related: rhbz#999839 (CVE-2013-4282)

* Mon Sep 02 2013 Christophe Fergeau <cfergeau@redhat.com> 0.12.4-4
- Fix spice-server crash when client sends a password which is too long
  Resolves: rhbz#999839 (CVE-2013-4282)

* Tue Aug 27 2013 Uri Lublin <uril@redhat.com> - 0.12.4-3
- decrease the timeout for flushing commands and waiting for client.
  Resolves: rhbz#995041

* Mon Jul 29 2013 Yonit Halperin <yhalperi@redhat.com> - 0.12.4-2
- Fix crashes when client is disconnected
  Resolves: rhbz#918169

* Thu Jul 18 2013 Uri Lublin <uril@redhat.com> - 0.12.4-1
- Rebase to upstream 0.12.4
  Resolves: rhbz#952671
  Resolves: rhbz#859027
  Resolves: rhbz#823472
  Resolves: rhbz#961848
  Resolves: rhbz#977998
  Resolves: rhbz#887775


* Thu Jun 27 2013 Uri Lublin <uril@redhat.com> - 0.12.3-1
- Rebase to upstream 0.12.3 + some additional patches
  Resolves: rhbz#952671
  Resolves: rhbz#884812
  Resolves: rhbz#918472
  Resolves: rhbz#958276
  Resolves: rhbz#978403

* Sun May 19 2013 Uri Lublin <uril@redhat.com> - 0.12.0-14
- Fix a crash running a F19 guest -- do not abort on stride > 0
  Resolves: rhbz#952666

* Sun May 19 2013 Uri Lublin <uril@redhat.com> - 0.12.0-13
- Migration related fixes
  * Destroy video streams before sending MSG_MIGRATE
  * Fix wrong is_low_bandwidth setting after 2 migrations of a session
    that was originally a low bandwidth one.
  Resolves: rhbz#950029
  Resolves: rhbz#956345

* Wed Jan 16 2013 Hans de Goede <hdegoede@redhat.com> - 0.12.0-12
- Fix a crash when rapidly changing monitor configuration
  Resolves: rhbz#868807

* Wed Jan 09 2013 Uri Lublin <uril@redhat.com> 0.12.0-11
- Fix a crash when setting screen-saver properties.
- Fix a leak.
  Resolves: rhbz#891326

* Thu Dec 20 2012 Yonit Halperin <yhalperi@redhat.com> 0.12.0-10
- Fix throwing away drawables that have masks
  Resolves: rhbz#864982

* Mon Dec 17 2012 Uri Lublin <uril@redhat.com> 0.12.0-9
- Fix calling set_client_capabilities when it is unsupported by qemu
  (fixes a crash when qemu-kvm is started with spice but without qxl)
  Resolves: rhbz#880276

* Fri Dec 7 2012 Yonit Halperin <yhalperi@redhat.com> 0.12.0-8
- Fix crash when reconnecting while a video is played
  Resolves: rhbz#883564

* Mon Dec 3 2012 Yonit Halperin <yhalperi@redhat.com> 0.12.0-7
- Fix mishandling of agent data received from the client after agent disconnection
  Resolves: rhbz#881980

* Thu Nov 29 2012 Yonit Halperin <yhalperi@redhat.com> 0.12.0-6
- Fix sending internal images with stride > bpp*width to lz compression
  Resolves: rhbz#876685

* Mon Nov 26 2012 Yonit Halperin <yhalperi@redhat.com> 0.12.0-5
- Fix various migration related bugs
  * don't process both cmd ring and dispatcher queue till migration data is received
  * fix assigning bad memory references to marshaller
  * fix memory corruption when receiving display migration data that exceeds 1024 bytes
  Resolves: rhbz#866929
  Resolves: rhbz#862352
  Resolves: rhbz#878700

* Wed Nov 21 2012 Uri Lublin <uril@redhat.com> 0.12.0-4
- Build/Requires libjpeg-turbo-devel instead of libjpeg-devel
- Related: rhbz#788687

* Thu Nov 15 2012 Alon Levy <alevy@redhat.com> 0.12.0-3
- don't call set_client_capabilities if vm is stopped.
- Resolves: rhbz#867405

* Mon Oct 29 2012 Uri Lublin <uril@redhat.com> 0.12.0-2
- Make spice-server-devel package Require spice-protocol >= 0.12.2
- Related: rhbz#842353

* Thu Sep 20 2012 Uri Lublin <uril@redhat.com> 0.12.0-1
- Rebase to upstream spice-server 0.12.0, which adds:
  * support setting client monitor configuration via device
    QXLInterface::client_monitors_config
  * support notifying guest of client capabilities
    QXLInterface::set_client_capabilities
  * new capability for A8 Surface support
  Resolves: rhbz#836123
  Resolves: rhbz#842353
  Resolves: rhbz#842310

* Mon Sep 03 2012 Uri Lublin <uril@redhat.com> 0.11.3-1
- Rebase to upstream spice-server 0.11.3, which adds:
  * Support for seamless migration
  * Support for Render
  * spice-protocol is in the tarball now (a submodule in git)
  Resolves: rhbz#836123
  Resolves: rhbz#842353

* Sun May 20 2012 Yonit Halperin <yhalperi@redhat.com> 0.10.1-10
- Fix crash in video streaming
  Resolves: rhbz#822686

* Wed May 16 2012 Yonit Halperin <yhalperi@redhat.com> 0.10.1-9
- Fix memory leak during video streaming
  Resolves rhbz#821334
- Fix segfault introduced when fixing rhbz#813826
  Related: rhbz#813826

* Tue May 15 2012 Alon Levy <alevy@redhat.com> - 0.10.1-8
- Fix self_bitmap lifetime to that of RedDrawable
  Resolves rhbz#821235

* Tue May 8 2012 Alon Levy <alevy@redhat.com> - 0.10.1-7
- Add usbredir to list of channels for security purposes
  Resolves rhbz#819484

* Mon May 07 2012 Yonit Halperin <yhalperi@redhat.com> - 0.10.1-6
  - Fix glitches in youtube movies
    + support video streams with frames of different sizes
  Resolves: rhbz#813826

* Thu Apr 05 2012 Hans de Goede <hdegoede@redhat.com> - 0.10.1-5
- Don't free the rcc twice when unregistering an usbredir chardev
  Resolves: rhbz#806169

* Mon Mar 05 2012 Christophe Fergeau <cfergeau@redhat.com> - 0.10.1-4
- add more logging for expired/invalid tickets
  Resolves: rhbz#787669
- add more logging about use of certificates
  Resolves: rhbz#787678

* Thu Feb 23 2012 alon <alevy@redhat.com> - 0.10.1-3
- fix race that can lead to accessing freed memory
Resolves: rhbz#790749

* Wed Feb 22 2012 Yonit Halperin <yhalperi@redhat.com> - 0.10.1-2
- support IPV6 addresses in channel events sent to qemu
Resolves: rhbz#788444

* Mon Jan 23 2012 Hans de Goede <hdegoede@redhat.com> - 0.10.1-1
- Rebase to upstream 0.10.1
Resolves: rhbz#758089
- This release adds support for usbredirection
Resolves: rhbz#758091
- This release fixes a bug in smartcard error handling
Resolves: rhbz#741259

* Wed Oct 26 2011 Alon Levy <alevy@redhat.com> - 0.8.2-5
- main dispatcher added
Resolves: rhbz#746950

* Wed Sep 28 2011 Uri Lublin <uril@redhat.com> - 0.8.2-4
- semi-seamless migration support
- added pyparsing.py as source, and using it to build the package.
- client patches are not applied.
- requires spice-protocol-0.8.1-2 (equivalent to upstream 0.8.2)
- advertise itself as version 0.8.3, to notify the new feature.
Resolves: rhbz#738266

* Mon Aug 01 2011 Uri Lublin <uril@redhat.com> - 0.8.2-3
- Drop unnecessary X11 and alsa requires from spice-server.pc
  + Fix a rpmdiff warning
Related: rhbz#723676
- server/red_dispatcher: fix wrong resolution set for tablet
Resolves: rhbz#726973

* Wed Jul 27 2011 Uri Lublin <uril@redhat.com> - 0.8.2-2
- On migration, do not read command rings before RED_WORKER_MESSAGE_START
Resolves: rhbz#718713

* Fri Jul 22 2011 Uri Lublin <uril@redhat.com> - 0.8.2-1
- Rebase to upstream 0.8.2, including
 + sasl support (fdo bz 34795)
 + support guest async io
 + support guest suspend and hibernate
 + add symbol versioning to libspice-server.so
 + prevent running an old spice-server with a newer qemu
 + Bug fixes (RHBZ): 714801, 713474, 674532, 653545
 + BuildRequires spice-protocol >= 0.8.1 and cyrus-sasl-devel
Resolves: #723676

* Mon Jun 27 2011 Uri Lublin <uril@redhat.com> - 0.8.1-2
- Remove Obsolete lines (added in 0.7.2-3)
Resolves: #707119

* Sun Jun 05 2011 Uri Lublin <uril@redhat.com> - 0.8.1-1
- Rebase to upstream 0.8.1, including
 + Make copy/paste support configurable
 + Some server/vdagent bugs fixed
Resolves: #710200

* Mon Mar 07 2011 Uri Lublin <uril@redhat.com> - 0.8.0-1
- Rebase to upstream 0.8.0
  + Includes "Fix segfault on migration" patch
  + Some spice-client bug fixes.
Resolves: #672035

* Mon Feb 21 2011 Uri Lublin <uril@redhat.com> - 0.7.3-2
- Fix segfault on migration
Resolves: #674451

* Thu Feb 17 2011 Uri Lublin <uril@redhat.com> - 0.7.3-1
- Rebase to upstream 0.7.3:
  + Mostly smart-card updates:
    - including all the changes in 0.7.2.4
  + Some gcc warning cleanups.
- Fix permissions of spice-server.pc
Resolves: #672035

* Fri Feb 04 2011 Uri Lublin <uril@redhat.com> - 0.7.2-4
- smartcard -- libcacard 0.1.2 updates:
 - server
  - use network byte order when talking to device.
 - both
  - no more reader_id_t, uint32_t instead
  - no more ReaderAddResponse, use VSC_Error with
    code==VSC_SUCCESS instead.
  - change an assert to a red_printf("error:..")
    if got an unexpectedly undefined reader id.
 - client (not part of this package)
  - track number of expected reader insertions
Resolves: #674937

* Fri Feb 04 2011 Uri Lublin <uril@redhat.com> - 0.7.2-3
- Obsolete old packages that are not needed now
Resolves: #674171

* Mon Jan 24 2011 Uri Lublin <uril@redhat.com> - 0.7.2-2
- Rebase to spice upstream release 0.7.2
- Drop all patches (all upstreamed)
- Enable smartcard (CAC) support
Resolves: #672035

* Fri Jul 30 2010 Uri Lublin <uril@redhat.com> - 0.4.2-15
 - Fix unsafe accesses
  + fix unsafe guest data accessing.
  + fix unsafe free() call.
  + fix unsafe cursor items handling.
  + add missing overflow check.
Resolves: #568811

* Wed Jun 30 2010 Uri Lublin <uril@redhat.com> - 0.4.2-14
- make opengl optional - add a missing patch
  ifdef out some opengl calls.
Resolves: #482556

* Wed Jun 30 2010 Uri Lublin <uril@redhat.com> - 0.4.2-13
- remove Requires and BuildRequires mesa-libGLU-devel
  + open-gl is now disabled.
- bumped release to -13 due to tag issue
Related: #482556

* Wed Jun 30 2010 Uri Lublin <uril@redhat.com> - 0.4.2-11
- make opengl optional, disabled by default (2 patches)
Resolves: #482556

* Thu Apr 22 2010 Uri Lublin <uril@redhat.com> - 0.4.2-10
- spice: server: new-api (4 more patches)
     + streaming-video, agent-mouse, playback-compression.
Related: #571286

* Sun Apr  4 2010 Uri Lublin <uril@redhat.com> - 0.4.2-9
 - generate auto* generated files (e.g. Makefile.in)
Resolves: #579329

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-8
 - spice server: renaming library and includedir
Resolves: #573349

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-7
 - fix wrong access to ring item
Resolves: #575556

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-6
 - more permissive video identification
Resolves: #575576

* Tue Mar 23 2010 Uri Lublin <uril@redhat.com> - 0.4.2-5
 - new migration process
Resolves: #576029

* Wed Mar 17 2010 Uri Lublin <uril@redhat.com> - 0.4.2-4
- spice: server: new-api (2 more patches)
Related: #571286

* Mon Mar  8 2010 Uri Lublin <uril@redhat.com> - 0.4.2-3
 - Use default configure macro (remove _prefix and _libdir)
Related: #543948

* Sun Mar 07 2010 Uri Lublin <uril@redhat.com> - 0.4.2-2
- spice: server: new-api (10 patches)
Related: #571286

* Sun Mar 07 2010 Uri Lublin <uril@redhat.com> - 0.4.2-1
- spice: server: avoid video streaming of small images
Resolves: #571283

* Sun Jan 11 2009 Uri Lublin <uril@redhat.com> - 0.4.2-0
 - first spec for 0.4.2
Related: #549807
