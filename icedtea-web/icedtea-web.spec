# Version of java
%define javaver 1.8.0

# Alternatives priority
%define priority 18000

%define javadir     %{_jvmdir}/java-%{javaver}-openjdk.%{_arch}
%define jredir      %{_jvmdir}/jre-%{javaver}-openjdk.%{_arch}
%ifarch x86_64
%define javaplugin  libjavaplugin.so.%{_arch}
%else
%define javaplugin  libjavaplugin.so
%endif

%define binsuffix      .itweb

Name:		icedtea-web
Version:	1.6.2
Release:	2%{?dist}
Summary:	Additional Java components for OpenJDK - Java browser plug-in and Web Start implementation

Group:      Applications/Internet
License:    LGPLv2+ and GPLv2 with exceptions
URL:        http://icedtea.classpath.org/wiki/IcedTea-Web
Source0:    http://icedtea.classpath.org/download/source/%{name}-%{version}.tar.gz

BuildRequires:  java-%{javaver}-openjdk-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gecko-devel
BuildRequires:  glib2-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  xulrunner-devel
BuildRequires:  junit4
# new in 1.5 to have  clean up for malformed XMLs
BuildRequires:  tagsoup
# rhino is used as JS evaluator in testtime
BuildRequires:      rhino

# For functionality and the OpenJDK dirs
Requires:      java-%{javaver}-openjdk

# For the mozilla plugin dir
Requires:       mozilla-filesystem%{?_isa}

# When itw builds against it, it have to be also in runtime
Requires:      tagsoup

# rhino is used as JS evaluator in runtime
Requires:      rhino

# Post requires alternatives to install plugin alternative.
Requires(post):   %{_sbindir}/alternatives

# Postun requires alternatives to uninstall plugin alternative.
Requires(postun): %{_sbindir}/alternatives

# Standard JPackage plugin provides.
Provides: java-plugin = 1:%{javaver}
Provides: javaws      = 1:%{javaver}

Provides:   java-%{javaver}-openjdk-plugin =  1:%{version}
Obsoletes:  java-1.6.0-openjdk-plugin

ExclusiveArch: x86_64 i686 %{arm}

%description
The IcedTea-Web project provides a Java web browser plugin, an implementation
of Java Web Start (originally based on the Netx project) and a settings tool to
manage deployment settings for the aforementioned plugin and Web Start
implementations. 

%package javadoc
Summary:    API documentation for IcedTea-Web
Group:      Documentation
Requires:   %{name} = %{version}-%{release}
Requires:   jpackage-utils
BuildArch:  noarch

%description javadoc
This package contains Javadocs for the IcedTea-Web project.

%prep
%setup -q

%build
autoreconf -vfi
CXXFLAGS="$RPM_OPT_FLAGS $RPM_LD_FLAGS" \
%configure \
    --with-pkgversion=rhel-%{release}-%{_arch} \
    --docdir=%{_datadir}/javadoc/%{name} \
    --with-jdk-home=%{javadir} \
    --with-jre-home=%{jredir} \
    --libdir=%{_libdir} \
    --program-suffix=%{binsuffix} \
    --prefix=%{_prefix}
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

# icedteaweb-completion is currently not handled by make nor make install
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/
cp icedteaweb-completion $RPM_BUILD_ROOT%{_sysconfdir}/bash_completion.d/

# Move javaws man page to a more specific name
mv $RPM_BUILD_ROOT/%{_mandir}/man1/javaws.1 $RPM_BUILD_ROOT/%{_mandir}/man1/javaws-itweb.1

# Install desktop files.
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
desktop-file-install --vendor ''\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications javaws.desktop
desktop-file-install --vendor ''\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications itweb-settings.desktop
desktop-file-install --vendor ''\
  --dir $RPM_BUILD_ROOT%{_datadir}/applications policyeditor.desktop


%check
#make check

%post
alternatives \
  --install %{_libdir}/mozilla/plugins/libjavaplugin.so %{javaplugin} \
  %{_libdir}/IcedTeaPlugin.so %{priority} \
  --slave %{_bindir}/javaws javaws %{_prefix}/bin/javaws%{binsuffix} \
  --slave %{_mandir}/man1/javaws.1.gz javaws.1.gz \
  %{_mandir}/man1/javaws-itweb.1.gz

%posttrans
update-desktop-database &> /dev/null || :
exit 0

%postun
update-desktop-database &> /dev/null || :
if [ $1 -eq 0 ]
then
  alternatives --remove %{javaplugin} \
    %{_libdir}/IcedTeaPlugin.so
fi
exit 0

%files
%defattr(-,root,root,-)
%{_sysconfdir}/bash_completion.d/icedteaweb-completion
%{_prefix}/bin/*
%{_libdir}/IcedTeaPlugin.so
%{_datadir}/applications/*
%{_datadir}/%{name}
%{_datadir}/man/man1/*
%{_datadir}/man/cs/man1/*
%{_datadir}/man/de/man1/*
%{_datadir}/man/pl/man1/*
%{_datadir}/pixmaps/*
%doc NEWS README COPYING

%files javadoc
%defattr(-,root,root,-)
%{_datadir}/javadoc/%{name}
%doc COPYING

%changelog
* Thu Sep 08 2016 Bjarne Saltbaek <bjarne@redsleeve.org> - 1.6.2-2
- added %{arm} to ExclusiveArch

* Wed Feb 03 2016 Jiri Vanek <jvanek@redhat.com> 1.6.2-1
- updated to 1.6.2
- fixed also rhbz#1303437 - package owns /etc/bash_completion.d but it should not own it 
- Resolves: rhbz#1275523

* Thu Nov 19 2015 Jiri Vanek <jvanek@redhat.com> 1.6.1-4
- updated to 1.6.1
- Resolves: rhbz#1275523

* Mon Aug 18 2014 Jiri Vanek <jvanek@redhat.com> 1.5.1-1
- fixed obsolates to any jdk6 plugin
- Resolves: rhbz#1075790

* Fri Aug 15 2014 Jiri Vanek <jvanek@redhat.com> 1.5.1-0
- update to upstream 1.5.1
- removed all patches (all upstreamed)
- Resolves: rhbz#1075790

* Thu Apr 24 2014 Jiri Vanek <jvanek@redhat.com> 1.5-3
- rebuild with tagsoup dependency
- Resolves: rhbz#1075790

* Mon Apr 07 2014 Jiri Vanek <jvanek@redhat.com> 1.5-2
- temporally removed tagsoup dependency - needs to be negotiated
- Resolves: rhbz#1075790

* Mon Apr 07 2014 Jiri Vanek <jvanek@redhat.com> 1.5-1
- sync with f21
- removed rhel5 specific clean and buildroot
- Resolves: rhbz#1075790

* Wed Jul 10 2013 Jiri Vanek <jvanek@redhat.com> 1.4.1-0
- updated to 1.4.1
- add icedtea-web man page
- removed upstreamed  patch1 b25-appContextFix.patch
- Resolves: rhbz#916161

* Wed Jul 10 2013 Jiri Vanek <jvanek@redhat.com> 1.4.0-2
- cleaned specfile
- Resolves: rhbz#916161

* Wed Jul 10 2013 Jiri Vanek <jvanek@redhat.com> 1.4.0-1
- added patch1 b25-appContextFix.patch to make it run with future openjdk
- Resolves: rhbz#975098

* Fri Jun 07 2013 Jiri Vanek <jvanek@redhat.com> 1.4-0
- Updated to 1.4
- See announcement for detail
 - http://mail.openjdk.java.net/pipermail/distro-pkg-dev/2013-May/023195.html
- Resolves: rhbz#916161

* Wed Apr 17 2013 Jiri Vanek <jvanek@redhat.com> 1.3.2-0
- Updated to icedtea-web 1.3.2 - see RHBZ 916161 for details
- this update contains security fixes:
  - CVE-2013-1927, RH884705: fixed gifar vulnerability
  - CVE-2013-1926, RH916774: Class-loader incorrectly shared for applets with same relative-path.
-Common
  - Added new option in itw-settings which allows users to set JVM arguments when plugin is initialized.
- NetX
  - PR580: http://www.horaoficial.cl/ loads improperly
- Plugin
   PR1260: IcedTea-Web should not rely on GTK
   PR1157: Applets can hang browser after fatal exceptio
- and much more since 1.3, over 1.3.1
- Resolves: rhbz#949095

* Fri Dec 07 2012 Jiri Vanek <jvanek@redhat.com> 1.2.2-3
- Fixed provides and obsolates
- Resolves: rhbz#838084.

* Mon Dec 03 2012 Deepak Bhole <dbhole@redhat.com> 1.2.2-2
- Build with OpenJDK7
- Import fix for PR1161 (needed for proper functionality with OpenJDK7)

* Thu Nov 01 2012 Deepak Bhole <dbhole@redhat.com> 1.2.2-1
- Updated to 1.2.2
- Resolves: CVE-2012-4540

* Wed Jul 25 2012 Deepak Bhole <dbhole@redhat.com> 1.2.1-1
- Updated to 1.2.1
- Resolves: CVE-2012-3422
- Resolves: CVE-2012-3423

* Mon Mar 05 2012 Deepak Bhole <dbhole@redhat.com> 1.2-1
- Updated to 1.2 proper

* Wed Feb 15 2012 Deepak Bhole <dbhole@redhat.com> 1.2-0.1.2pre
- Updated to 1.2pre snapshot

* Fri Oct 28 2011 Deepak Bhole <dbhole@redhat.com> 1.1.4-1
- Updated to 1.1.4
- Resolves: rhbz#744739

* Tue Oct 11 2011 Deepak Bhole <dbhole@redhat.com> 1.1.3-1
- Bumped to 1.1.3
- Fixed alternative removal command
- Resolves: rhbz#741796

* Tue Sep 20 2011 Deepak Bhole <dbhole@redhat.com> 1.1.2-2
- Resolves: rhbz#737899. Do not own directories not created by the package.

* Wed Aug 31 2011 Deepak Bhole <dbhole@redhat.com> 1.1.2-1
- Updated to 1.1.2
- Resolves: rhbz#683479
- Resolves: rhbz#725794
- Resolves: rhbz#718181 
- Resolves: rhbz#731358
- Resolves: rhbz#725718
- Use the new --with-jre-home switch (#731358)

* Mon Jul 25 2011 Deepak Bhole <dbhole@redhat.com> 1.1.1-1
- Bump to 1.1.1
- Removed icedtea-web-shared-classloader.patch (now upstream)
- Updated alternative removal commands to reflect the situation in RHEL6
- Resolves: rhbz#713514

* Tue Apr 05 2011 Deepak Bhole <dbhole@redhat.com> 1.0.2-3
- Added update-desktop-database directives in post and postun 

* Tue Apr 05 2011 Deepak Bhole <dbhole@redhat.com> 1.0.2-2
- Resolves rhbz#693601
- Added epochs to java plugin and javaws provides to match those of Oracle

* Tue Apr 05 2011 Deepak Bhole <dbhole@redhat.com> 1.0.2-1
- Resolves rhbz#693601 
- Update to IcedTea-Web 1.0.2
- Dropped patch0 (instance validity check). Now part of 1.0.2
- Also resolves #682674 by adding a javaws Provides

* Mon Mar 28 2011 Deepak Bhole <dbhole@redhat.com> 1.0.1-4
- Removed icedtea-web-desktop-encoding.patch which now causes rpmlint warnings 

* Mon Mar 28 2011 Deepak Bhole <dbhole@redhat.com> - 1.0.1-3
- Resolves rhbz#645781 (desktop sharing now works)
- Updated the classloader sharing patch to fix loader sharing rules
- Added version and release string in plugin display

* Fri Mar 04 2011 Deepak Bhole <dbhole@redhat.com> - 1.0.1-2
- Resolved rhbz#645781: MS Live Meeting Applet Not Working With OpenJDK Plugin

* Tue Feb 22 2011 Deepak Bhole <dbhole@redhat.com> - 1.0.1-1
- Bumped to 1.0.1
- Removed icedtea-web-pkg-access.patch (now upstream)
- Resolves CVE-2011-0706 and CVE-2010-4450

* Wed Feb 09 2011 Deepak Bhole <dbhole@redhat.com> - 1.0-5
- Minor comment/group/etc. updates from omajid@redhat.com
- Added base package requirement for javadoc subpackage

* Fri Feb 04 2011 Deepak Bhole <dbhole@redhat.com> - 1.0-4
- Added encoding to desktop files

* Wed Feb 02 2011 Deepak Bhole <dbhole@redhat.com> - 1.0-3
- Bump to 1.0 proper
- Install to jre dir only
- Restrict access to net.sourceforge.jnlp.*
- Resolves bugs 674519, 674517, 674524, 671470

* Fri Jan 14 2011 Deepak Bhole <dbhole@redhat.com> - 1.0-2
- Made exclusive arch
- Fixed archinstall macro value
- Fixed min required OpenJDK version to match what is in RHEL6
- Added BR for desktop-file-utils

* Fri Jan 14 2011 Deepak Bhole <dbhole@redhat.com> - 1.0-1
- Initial build with 1.0pre
