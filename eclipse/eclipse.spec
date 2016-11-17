# TODO:
# - see why about.html isn't being copied on ppc
# - fix ant libs
Epoch:  1

%global eclipse_major   3
%global eclipse_minor   6
%global eclipse_majmin  %{eclipse_major}.%{eclipse_minor}
%global eclipse_micro   1
%global initialize      1
%global download_url    http://download.eclipse.org/technology/linuxtools/eclipse-build/3.6.x_Helios/
%global bootstrap 1

# All arches line up between Eclipse and Linux kernel names except i386 -> x86
%ifarch %{ix86}
%global eclipse_arch    x86
%endif
%ifarch %{arm}
    %global eclipse_arch arm
%endif
%ifarch ppc64 ppc64p7
    %global eclipse_arch ppc64
%endif
%ifarch s390 s390x ppc x86_64 aarch64 ppc64le
    %global eclipse_arch %{_arch}
%endif

# FIXME:  update java packaging guidelines for this.  See
# fedora-devel-java-list discussion in September 2008.
#
# Prevent brp-java-repack-jars from being run.
%define __jar_repack 0

Summary:        An open, extensible IDE
Name:           eclipse
Version:        %{eclipse_majmin}.%{eclipse_micro}
Release:        6.13%{?dist}.0
License:        EPL
Group:          Text Editors/Integrated Development Environments (IDE)
URL:            http://www.eclipse.org/
Source0:        %{download_url}eclipse-build-0.6.2RC0.tar.bz2
Source1:        %{download_url}eclipse-%{version}-src.tar.bz2
Source2:        eclipse.sh.in
Source17:       efj.sh.in
# This script copies the platform sub-set of the SDK for generating metadata
Source28:       %{name}-mv-Platform.sh
# Shell script portability patch: prepare-build-dir.sh
Patch2:         prepare-build-dir.sh.patch
# Eclipse help XSS vulnerability fix
Patch3:        eclipse-help-webapps-xss-BZ661901.patch
# RHEL deps are slightly different
Patch4:        %{name}-rhel-deps.patch
# Upstream fixes for test runs
# http://bugs.eclipse.org/334716
Patch5:        provisiontestsseparately.patch
# Fix patch to JUNIT.XSL for overall test report
# http://dev.eclipse.org/viewcvs/viewvc.cgi?view=revision&root=Technology_LINUXTOOLS&revision=27145
Patch6:        correctJUNITXSLpath.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  ant ant-nodeps
BuildRequires:  jpackage-utils >= 0:1.5, make, gcc
BuildRequires:  gnome-vfs2-devel
BuildRequires:  gtk2-devel
BuildRequires:  glib2-devel
BuildRequires:  libgnome-devel
BuildRequires:  libgnomeui-devel
BuildRequires:  gcc-c++
BuildRequires:  nspr-devel
BuildRequires:  libXtst-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  cairo >= 1.0
BuildRequires:  unzip
BuildRequires:  desktop-file-utils
BuildRequires:  java-devel >= 1.6.0
BuildRequires:  java-javadoc
BuildRequires:  libXt-devel
BuildRequires:  xulrunner-devel

%if !%{bootstrap}
BuildRequires: icu4j-eclipse >= 1:4.2.1
BuildRequires: apache-jasper >= 5.5.28
BuildRequires: apache-tomcat-apis
BuildRequires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging ant-apache-bsf ant-commons-net
BuildRequires: ant-javamail ant-jdepend ant-junit ant-swing ant-trax ant-jsch
BuildRequires: jsch >= 0:0.1.41
BuildRequires: jakarta-commons-el >= 1.0-9
BuildRequires: jakarta-commons-logging >= 1.0.4-6jpp.3
BuildRequires: jakarta-commons-codec
BuildRequires: jakarta-commons-httpclient
BuildRequires: jetty-eclipse >= 6.1.24-1
BuildRequires: lucene >= 2.3.1-3.4
BuildRequires: lucene-contrib >= 2.3.1-3.4
BuildRequires: junit >= 3.8.1-3jpp
BuildRequires: junit4
BuildRequires: hamcrest >= 0:1.1-9.2
BuildRequires: sat4j >= 2.2.0-1
BuildRequires: objectweb-asm >= 3.2-2.1
%else
BuildRequires: icu4j-javadoc
%endif

%if 0%{?rhel} >= 6
ExclusiveArch: i686 x86_64 %{arm}
%endif

%description
The Eclipse platform is designed for building integrated development
environments (IDEs), server-side applications, desktop applications, and
everything in between.

%package     swt
Summary:        SWT Library for GTK+-2.0
Group:          Text Editors/Integrated Development Environments (IDE)
# %{_libdir}/java directory owned by jpackage-utils
Requires:       jpackage-utils
Requires:       gtk2
Requires:       xulrunner >= 1.9
Conflicts:      mozilla
Provides:       libswt3-gtk2 = 1:%{version}-%{release}
# The 20 is more than the currently (2008-06-25) latest 3.3.2 package
# but I want to leave some room in case we need to do an F9 update.
Obsoletes:       libswt3-gtk2 < 1:3.3.2-20

%description swt
SWT Library for GTK+-2.0.

%package        rcp
Summary:        Eclipse Rich Client Platform
Group:          Development/Languages
Requires:       %{name}-swt = %{epoch}:%{version}-%{release}
%if ! %{bootstrap}
Requires:       icu4j-eclipse >= 1:4.2.1
%endif
Requires:       java >= 1.6.0

%description    rcp
Eclipse Rich Client Platform

%package        platform
Summary:        Eclipse platform common files
Group:          Text Editors/Integrated Development Environments (IDE)
Requires:   %{name}-rcp = %{epoch}:%{version}-%{release}
%if ! %{bootstrap}
Requires: ant-antlr ant-apache-bcel ant-apache-log4j ant-apache-oro ant-apache-regexp ant-apache-resolver ant-commons-logging ant-apache-bsf ant-commons-net
Requires: ant-javamail ant-jdepend ant-junit ant-nodeps ant-swing ant-trax ant-jsch
Requires: jakarta-commons-el >= 1.0-9
Requires: jakarta-commons-logging >= 1.0.4-6jpp.3
Requires: jakarta-commons-codec
Requires: apache-jasper >= 5.5.28
Requires: apache-tomcat-apis
Requires: jetty-eclipse >= 6.1.24-1
Requires: jsch >= 0.1.41
Requires: lucene >= 2.3.1-3.4
Requires: lucene-contrib >= 2.3.1-3.4
Requires: sat4j >= 2.2.0-1
%endif
Provides: eclipse-cvs-client = 1:%{version}-%{release}
Obsoletes: eclipse-cvs-client < 1:3.3.2-20

%description    platform
The Eclipse Platform is the base of all IDE plugins.  This does not include the
Java Development Tools or the Plugin Development Environment.

%package        jdt
Summary:        Eclipse Java Development Tools
Group:          Text Editors/Integrated Development Environments (IDE)
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires:       %{name}-cvs-client = %{epoch}:%{version}-%{release}
%if ! %{bootstrap}
Requires:       junit >= 3.8.1-3jpp
Requires:       junit4
Requires:       jakarta-commons-httpclient
%endif
Requires:       java-javadoc
Requires:       java-devel

%description    jdt
Eclipse Java Development Tools.  This package is required to use Eclipse for
developing software written in the Java programming language.

%package        pde
Summary:        Eclipse Plugin Development Environment
Group:          Text Editors/Integrated Development Environments (IDE)
Provides:       eclipse = %{epoch}:%{version}-%{release}
Provides:       eclipse-sdk = %{epoch}:%{version}-%{release}
Requires:       %{name}-platform = %{epoch}:%{version}-%{release}
Requires:       %{name}-jdt = %{epoch}:%{version}-%{release}
%if ! %{bootstrap}
Requires:       objectweb-asm >= 3.2-2.1
Requires:       hamcrest >= 0:1.1-9.2
%endif
# For PDE Build wrapper script + creating jars
Requires:       zip
Requires:       bash
Provides:       %{name}-pde-runtime = 1:%{version}-%{release}
Obsoletes:      %{name}-pde-runtime < 1:3.3.2-20

%description    pde
Eclipse Plugin Development Environment.  This package is required for
developing Eclipse plugins.

%prep
%setup -q -n eclipse-build-0.6.2
cp %{SOURCE1} .
ant -DbuildArch=%{eclipse_arch} applyPatches
pushd build/eclipse-%{version}-src

# Apply shell script portability 
# patch to upstream prepare-build-dir.sh
%patch2
# Eclipse help XSS vulnerability fix
%patch3

# Use our system-installed javadocs, reference only what we built, and
# don't like to osgi.org docs (FIXME:  maybe we should package them?)
sed -i -e "s|http://java.sun.com/j2se/1.4.2/docs/api|%{_datadir}/javadoc/java|" \
   -e "/osgi\.org/d" \
   -e "s|-breakiterator|;../org.eclipse.equinox.util/@dot\n;../org.eclipse.ecf.filetransfer_3.0.0.v20090302-0803.jar\n;../org.eclipse.ecf_3.0.0.v20090302-0803.jar\n-breakiterator|" \
    plugins/org.eclipse.platform.doc.isv/platformOptions.txt
sed -i -e "s|http://java.sun.com/j2se/1.5/docs/api|%{_datadir}/javadoc/java|" \
   -e "s/win32.win32.x86/gtk.linux.%{eclipse_arch}/" \
   plugins/org.eclipse.jdt.doc.isv/jdtaptOptions.txt \
   plugins/org.eclipse.jdt.doc.isv/jdtOptions.txt
sed -i -e "s|http://java.sun.com/j2se/1.4/docs/api|%{_datadir}/javadoc/java|" \
   -e "s/motif.linux.x86/gtk.linux.%{eclipse_arch}/" \
   plugins/org.eclipse.pde.doc.user/pdeOptions.txt \
   plugins/org.eclipse.pde.doc.user/pdeOptions.txt


# FIXME:  do this as part of eclipse-build
#
# the swt version is set to HEAD on s390x but shouldn't be
# get swt version
SWT_MAJ_VER=$(grep maj_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_MIN_VER=$(grep min_ver plugins/org.eclipse.swt/Eclipse\ SWT/common/library/make_common.mak | cut -f 2 -d =)
SWT_VERSION=$SWT_MAJ_VER$SWT_MIN_VER
swt_frag_ver=$(grep v$SWT_VERSION plugins/org.eclipse.swt.gtk.linux.x86/build.xml | sed "s:.*<.*\"\(.*\)\" />:\1:")
swt_frag_ver_s390x=$(grep "version\.suffix\" value=" plugins/org.eclipse.swt.gtk.linux.s390x/build.xml | sed "s:.*<.*\"\(.*\)\" />:\1:")
#sed --in-place "s|$swt_frag_ver_s390x|$swt_frag_ver|g" plugins/org.eclipse.swt.gtk.linux.s390x/build.xml \
#                                                      plugins/org.eclipse.swt.gtk.linux.s390x/META-INF/MANIFEST.MF

%if ! %{bootstrap}
# make sure there are no jars left
JARS=""
for j in $(find -name \*.jar); do
  if [ ! -L $j ]; then
    JARS="$JARS `echo $j`"
  fi
done
if [ ! -z "$JARS" ]; then
    echo "These jars should be deleted and symlinked to system jars: $JARS"
   #FIXME: enable  exit 1
fi
%endif

popd

%patch4 -b .cvs
%patch5 -b .testprovisioning
%patch6 -b .testaggregation

%if %{bootstrap}
sed -i -e "s_.*icu.*_&:/usr/share/java/com.ibm.icu-4.2.jar_" dependencies.properties
sed -i -e "/codec/d" dependencies.properties
sed -i -e "/ant-junit/d" nonosgidependencies.properties
sed -i -e "/ant-apache-bcel/d" nonosgidependencies.properties
sed -i -e "/ant-javamail/d" nonosgidependencies.properties
sed -i -e "/ant-apache-resolver/d" nonosgidependencies.properties
sed -i -e "/ant-jdepend/d" nonosgidependencies.properties
sed -i -e "/ant-trax/d" nonosgidependencies.properties
sed -i -e "/ant-swing/d" nonosgidependencies.properties
sed -i -e "/ant-antlr/d" nonosgidependencies.properties
sed -i -e "/ant-apache-regexp/d" nonosgidependencies.properties
sed -i -e "/ant-commons-logging/d" nonosgidependencies.properties
sed -i -e "/ant-commons-net/d" nonosgidependencies.properties
sed -i -e "/ant-apache-bsf/d" nonosgidependencies.properties
sed -i -e "/ant-apache-oro/d" nonosgidependencies.properties
sed -i -e "/ant-jsch/d" nonosgidependencies.properties
sed -i -e "/ant-apache-log4j/d" nonosgidependencies.properties
sed -i -e "/hamcrest/d" jdtdependencies.properties
sed -i -e "/junit/d" jdtnonosgidependencies.properties
%endif

%build
export JAVA_HOME=%{java_home}
ant provision.cvs

%install
rm -rf $RPM_BUILD_ROOT
ant -DdestDir=$RPM_BUILD_ROOT -Dprefix=/usr -Dmultilib=true installSDKinDropins

# We don't need icon.xpm
# https://bugs.eclipse.org/292472
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/icon.xpm

# Set GDK_NATIVE_WINDOWS=true
# https://bugzilla.redhat.com/531675 (https://bugs.eclipse.org/290395)
rm $RPM_BUILD_ROOT/%{_bindir}/%{name}
install -p -D -m0755 %{SOURCE2} $RPM_BUILD_ROOT%{_bindir}/%{name}
sed --in-place "s:/usr/lib:%{_libdir}:" \
  $RPM_BUILD_ROOT%{_bindir}/%{name}

# Some directories we need
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/java

pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
# Create file listings for the extracted shared libraries
echo -n "" > %{_builddir}/%{buildsubdir}/%{name}-platform.install;
for id in `ls configuration/org.eclipse.osgi/bundles`; do
  if [ "Xconfiguration" = $(echo X`find configuration/org.eclipse.osgi/bundles/$id -name libswt\*.so` | sed "s:/.*::") ]; then
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" > %{_builddir}/%{buildsubdir}/%{name}-swt.install;
  else
    echo "%{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles/$id" >> %{_builddir}/%{buildsubdir}/%{name}-platform.install;
  fi
done
popd

# Symlinks to the SWT JNI shared libraries in %%{_libdir}/eclipse
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
for lib in $(find configuration -name libswt\*.so); do
  ln -s $lib `basename $lib`
done
popd

# Temporary fix until https://bugs.eclipse.org/294877 is resolved
sed -i "s|-Xms40m|-Xms128m|g" $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
sed -i "s|-Xmx384m|-Xmx512m|g" $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/core/internal/dtree/DataTreeNode,forwardDeltaWith" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/jdt/internal/compiler/lookup/ParameterizedMethodBinding,<init>" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/cdt/internal/core/dom/parser/cpp/semantics/CPPTemplates,instantiateTemplate" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/eclipse/cdt/internal/core/pdom/dom/cpp/PDOMCPPLinkage,addBinding" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/python/pydev/editor/codecompletion/revisited/PythonPathHelper,isValidSourceFile" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini
echo "-XX:CompileCommand=exclude,org/python/pydev/ui/filetypes/FileTypesPreferencesPage,getDottedValidSourceFiles" >> $RPM_BUILD_ROOT/%{_sysconfdir}/eclipse.ini

# SWT JAR symlink in libdir
pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
ln -s ../%{name}/swt-gtk-%{eclipse_majmin}.%{eclipse_micro}.jar ../java/swt.jar
popd

# Install the efj wrapper script
install -p -D -m0755 %{SOURCE17} $RPM_BUILD_ROOT%{_bindir}/efj
sed --in-place "s:startup.jar:%{_libdir}/%{name}/startup.jar:" \
  $RPM_BUILD_ROOT%{_bindir}/efj

# A sanity check.
desktop-file-validate %{buildroot}/%{_datadir}/applications/%{name}.desktop

# Create a script that can be used to make a symlink tree of the
# eclipse platform.
cp -p pdebuild/eclipse-copy-platform.sh copy-platform
(
  cd $RPM_BUILD_ROOT%{_libdir}/%{name}
  ls -d * | grep -E -v '^(plugins|features|about_files|dropins)$'
  ls -d plugins/* features/*
) |
sed -e's,^\(.*\),[ ! -e \1 ] \&\& ln -s $eclipse/\1 \1,' >> copy-platform
mkdir -p $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts
mv copy-platform $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts
copyPlatform=$RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts/copy-platform

# This symlink is actually provided by the icu4j-eclipse package
# We need to remove this *after* copy-platform creation otherwise
# copy-platform gets generated wrong.
rm $RPM_BUILD_ROOT/%{_libdir}/%{name}/plugins/com.ibm.icu_*.jar

pushd $RPM_BUILD_ROOT%{_libdir}/%{name}
for p in $(ls -d dropins/jdt/plugins/*); do
    plugin=$(basename $p)
    echo $p | sed -e"s,^\(.*\),[ ! -e plugins/$plugin ] \&\& ln -s \$eclipse/\1 plugins/$plugin," >> $copyPlatform
done
for p in $(ls -d dropins/sdk/plugins/*); do
    plugin=$(basename $p)
    echo $p | sed -e"s,^\(.*\),[ ! -e plugins/$plugin ] \&\& ln -s \$eclipse/\1 plugins/$plugin," >> $copyPlatform
done
popd

# Install the PDE Build wrapper script.
install -p -D -m0755 pdebuild/eclipse-pdebuild.sh \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts/pdebuild
PDEBUILDVERSION=$(ls $RPM_BUILD_ROOT%{_libdir}/%{name}/dropins/sdk/plugins \
  | grep org.eclipse.pde.build_ | \
  sed 's/org.eclipse.pde.build_//')
sed -i "s/@PDEBUILDVERSION@/$PDEBUILDVERSION/g" \
  $RPM_BUILD_ROOT%{_libdir}/%{name}/buildscripts/pdebuild

%clean
rm -rf $RPM_BUILD_ROOT

%post platform
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%postun platform
touch --no-create %{_datadir}/icons/hicolor
if [ -x /usr/bin/gtk-update-icon-cache ]; then
  gtk-update-icon-cache -q %{_datadir}/icons/hicolor
fi

%if %{initialize}
%files swt -f %{name}-swt.install
%else
%files swt
%endif
%defattr(-,root,root)
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%if %{initialize}
%dir %{_libdir}/%{name}/libswt-*.so
%dir %{_libdir}/%{name}/configuration
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi
%dir %{_libdir}/%{name}/configuration/org.eclipse.osgi/bundles
%endif
%{_libdir}/%{name}/notice.html
%{_libdir}/%{name}/epl-v10.html
%{_libdir}/%{name}/plugins/org.eclipse.swt_*
%{_libdir}/%{name}/plugins/org.eclipse.swt.gtk.linux.%{eclipse_arch}_*
%{_libdir}/%{name}/swt-gtk*.jar
%{_libdir}/%{name}/swt.jar
%{_libdir}/java/swt.jar

%files rcp
%defattr(-,root,root)
%dir %{_libdir}/%{name}/features
%dir %{_datadir}/%{name}
%if %{initialize}
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.bundledata*
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.lazy*
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.manager
%{_libdir}/%{name}/configuration/org.eclipse.osgi/.state*
%endif
%if %{bootstrap}
%{_libdir}/%{name}/plugins/com.ibm.icu_*
%endif
%dir %{_libdir}/%{name}/configuration
%config %{_libdir}/%{name}/configuration/config.ini
%config %{_libdir}/%{name}/configuration/org.eclipse.equinox.simpleconfigurator/bundles.info
%dir %{_libdir}/%{name}/configuration/org.eclipse.equinox.simpleconfigurator
%ifnarch ppc ppc64
%{_libdir}/%{name}/about.html
%endif
%ifarch x86_64
%{_libdir}/%{name}/about_files
%endif
%{_libdir}/%{name}/readme
%{_libdir}/%{name}/startup.jar
%{_libdir}/%{name}/features/org.eclipse.rcp_*
%{_libdir}/%{name}/plugins/org.eclipse.core.commands_*
%{_libdir}/%{name}/plugins/org.eclipse.core.contenttype_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding.beans_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding.observable_*
%{_libdir}/%{name}/plugins/org.eclipse.core.databinding.property_*
%{_libdir}/%{name}/plugins/org.eclipse.core.expressions_*
%{_libdir}/%{name}/plugins/org.eclipse.core.jobs_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime.compatibility.auth_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.app_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.common_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.ds_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.launcher.gtk.linux.%{eclipse_arch}_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.preferences_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.util_*
%{_libdir}/%{name}/plugins/org.eclipse.help_*
%{_libdir}/%{name}/plugins/org.eclipse.jface_*
%{_libdir}/%{name}/plugins/org.eclipse.jface.databinding_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi_*
%{_libdir}/%{name}/plugins/org.eclipse.rcp_*
%{_libdir}/%{name}/plugins/org.eclipse.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.workbench_*
%{_libdir}/%{name}/plugins/org.eclipse.update.configurator_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.simpleconfigurator_*

%if %{initialize}
%files platform -f %{name}-platform.install
%else
%files platform
%endif
%defattr(-,root,root)
%attr(0755,root,root) %{_bindir}/%{name}
%{_libdir}/%{name}/.eclipseproduct
%config %{_libdir}/%{name}/eclipse.ini
%config %{_sysconfdir}/eclipse.ini
%ifnarch ppc ppc64
%{_libdir}/%{name}/about_files
%endif
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_datadir}/icons/*/*/apps/*
%{_libdir}/%{name}/eclipse
%dir %{_libdir}/%{name}/dropins
%dir %{_datadir}/%{name}/dropins
%{_libdir}/%{name}/features/org.eclipse.platform_*
%{_libdir}/%{name}/plugins/com.jcraft.jsch_*
%{_libdir}/%{name}/plugins/javax.servlet_*
%{_libdir}/%{name}/plugins/javax.servlet.jsp_*
%{_libdir}/%{name}/plugins/org.apache.ant_*
%{_libdir}/%{name}/plugins/org.apache.commons.el_*
%{_libdir}/%{name}/plugins/org.apache.commons.logging_*
%{_libdir}/%{name}/plugins/org.apache.lucene_*
%{_libdir}/%{name}/plugins/org.apache.lucene.analysis_*
%{_libdir}/%{name}/plugins/org.eclipse.ant.core_*
%{_libdir}/%{name}/plugins/org.eclipse.compare_*
%{_libdir}/%{name}/plugins/org.eclipse.compare.core_*
%{_libdir}/%{name}/plugins/org.eclipse.core.boot_*
%{_libdir}/%{name}/plugins/org.eclipse.core.externaltools_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filebuffers_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filesystem_*
%{_libdir}/%{name}/plugins/org.eclipse.core.filesystem.linux.%{eclipse_arch}_*
%{_libdir}/%{name}/plugins/org.eclipse.core.net_*
%{_libdir}/%{name}/plugins/org.eclipse.core.net.linux.*
%ifarch %{ix86}
%{_libdir}/%{name}/plugins/org.eclipse.update.core.linux_*
%endif
%{_libdir}/%{name}/plugins/org.eclipse.core.resources_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime.compatibility_*
%{_libdir}/%{name}/plugins/org.eclipse.core.runtime.compatibility.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.core.variables_*
%{_libdir}/%{name}/plugins/org.eclipse.debug.core_*
%{_libdir}/%{name}/plugins/org.eclipse.debug.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.event_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.jetty_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.http.servlet_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.jsp.jasper_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.jsp.jasper.registry_*
%{_libdir}/%{name}/plugins/org.eclipse.help.appserver_*
%{_libdir}/%{name}/plugins/org.eclipse.help.base_*
%{_libdir}/%{name}/plugins/org.eclipse.help.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.help.webapp_*
%{_libdir}/%{name}/plugins/org.eclipse.jface.text_*
%{_libdir}/%{name}/plugins/org.eclipse.jsch.core_*
%{_libdir}/%{name}/plugins/org.eclipse.jsch.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.ltk.core.refactoring_*
%{_libdir}/%{name}/plugins/org.eclipse.ltk.ui.refactoring_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi.services_*
%{_libdir}/%{name}/plugins/org.eclipse.osgi.util_*
%{_libdir}/%{name}/plugins/org.eclipse.platform_*
%{_libdir}/%{name}/plugins/org.eclipse.platform.doc.user_*
%{_libdir}/%{name}/plugins/org.eclipse.search_*
%{_libdir}/%{name}/plugins/org.eclipse.team.core_*
%{_libdir}/%{name}/plugins/org.eclipse.team.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.text_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.browser_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.cheatsheets_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.console_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.editors_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.externaltools_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.forms_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.ide_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.ide.application_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.intro_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.intro.universal_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.navigator_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.navigator.resources_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.net_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.presentations.r21_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.views_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.views.properties.tabbed_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.workbench.compatibility_*
%{_libdir}/%{name}/plugins/org.eclipse.ui.workbench.texteditor_*
%{_libdir}/%{name}/plugins/org.eclipse.update.core_*
%{_libdir}/%{name}/plugins/org.eclipse.update.scheduler_*
%{_libdir}/%{name}/plugins/org.eclipse.update.ui_*
%{_libdir}/%{name}/plugins/org.mortbay.jetty.util_*
%{_libdir}/%{name}/plugins/org.mortbay.jetty.server_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.initializer_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.core_*
%{_libdir}/%{name}/plugins/org.eclipse.cvs_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.ssh2_*
%{_libdir}/%{name}/plugins/org.eclipse.team.cvs.ui_*
%{_libdir}/%{name}/features/org.eclipse.cvs_*
%{_libdir}/%{name}/features/org.eclipse.help_*
%{_libdir}/%{name}/plugins/org.apache.jasper_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.frameworkadmin_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.frameworkadmin.equinox_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.simpleconfigurator.manipulator_*
%{_libdir}/%{name}/features/org.eclipse.equinox.p2.user.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.director_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.core_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.engine_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.jarprocessor_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.metadata_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.metadata.repository_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.artifact.repository_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.touchpoint.eclipse_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.touchpoint.natives_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.console_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ql_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.operations_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui.sdk_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.ui.sdk.scheduler_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.updatechecker_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.garbagecollector_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.directorywatcher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.publisher_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.repository_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.repository.tools_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.reconciler.dropins_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.metadata.generator_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.updatesite_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.security_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.security.ui_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.extensionlocation_*
%{_libdir}/%{name}/plugins/org.eclipse.equinox.p2.director.app_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer.httpclient_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer.httpclient.ssl_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.provider.filetransfer.ssl_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.ssl_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.filetransfer_*
%{_libdir}/%{name}/plugins/org.eclipse.ecf.identity_*
%{_libdir}/%{name}/plugins/org.apache.commons.codec_*
%{_libdir}/%{name}/plugins/org.apache.commons.httpclient_*
%{_libdir}/%{name}/plugins/org.sat4j.core_*
%{_libdir}/%{name}/plugins/org.sat4j.pb_*
# Put this in -platform since we're putting the p2 stuff here
%{_libdir}/%{name}/artifacts.xml
# FIXME: should we ship content.xml for the platform?
#%{_libdir}/%{name}/metadata
%{_libdir}/%{name}/p2

%files jdt
%defattr(-,root,root)
%{_bindir}/efj
%{_libdir}/%{name}/dropins/jdt

%files pde
%defattr(-,root,root)
%{_libdir}/%{name}/buildscripts
%{_libdir}/%{name}/dropins/sdk
%{_libdir}/%{name}/configuration/org.eclipse.equinox.source

%changelog
* Fri Oct 28 2016 Bjarne Saltbaek <bjarne@redsleeve.org> 1:3.6.1-6.13.0
- Fix arm-build

* Wed Jan 19 2011 Andrew Overholt <overholt@redhat.com> 1:3.6.1-6.13
- Drop patch to remove ant-trax (needed by test runs).

* Wed Jan 19 2011 Andrew Overholt <overholt@redhat.com> 1:3.6.1-6.12
- Add two upstream patches to allow for running SDK JUnit tests.

* Wed Jan 12 2011 Andrew Overholt <overholt@redhat.com> 1:3.6.1-6.11
- Bring in line with Fedora.
- Remove some stuff that is now done in eclipse-build.
- Fix sources URL.
- Add PDE dependency on zip for pdebuild script.
- Use new eclipse-build targets.
- Increase minimum required memory in eclipse.ini.

* Tue Jan 11 2011 Andrew Overholt <overholt@redhat.com> 1:3.6.1-6.10
- Put ant.launching into JDT's dropins directory.

* Tue Jan 11 2011 Andrew Overholt <overholt@redhat.com> 1:3.6.1-6.9
- Use apache-tomcat-apis JARs.
- Version objectweb-asm BR/R.

* Mon Jan 10 2011 Chris Aniszczyk <overholt@redhat.com> 1:3.6.1-6.8
- Fix JSP API symlinks.

* Wed Dec 15 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.1-6.7
- Install o.e.jdt.junit.core in jdt (rhbz#663207).

* Mon Dec 13 2010 Severin Gehwolf <sgehwolf@redhat.com> 1:3.6.1-6
- Add Eclipse help XSS vulnerability fix (RH Bz #661901).

* Wed Dec 01 2010 Jeff Johnston <jjohnstn@redhat.com> 1:3.6.1-5
- Remove work around for openjdk bug#647737 as openjdk has
  posted its own work around and will shortly be fixing problem 
  correctly.

* Wed Nov 10 2010 Jeff Johnston <jjohnstn@redhat.com> 1:3.6.1-4
- Work around for openjdk bug#647737.

* Mon Nov 8 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.1-3
- Add missing Requires on tomcat5-jsp-api (bug#650145).

* Thu Oct 14 2010 Severin Gehwolf <sgehwolf@redhat.com> 1:3.6.1-2
- Add prepare-build-dir.sh patch.

* Tue Oct 5 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.1-1
- Update to 3.6.1.

* Thu Jul 15 2010 Elliott Baron <ebaron@fedoraproject.org> 1:3.6.0-3
- Increasing min versions for jetty, icu4j-eclipse and sat4j.

* Fri Jul 9 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.0-2
- o.e.core.net.linux is no longer x86 only.

* Fri Jul 9 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.6.0-1
- Update to 3.6.0.
- Based on eclipse-build 0.6.1 RC0.

* Thu Jul 08 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.2-10
- Rebuild for new jetty.

* Thu Jun 17 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.2-9
- Fix typo in symlinking.

* Thu Jun 17 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.2-8
- No need to link jasper.

* Thu Jun 17 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.2-7
- Fix servlet and jsp apis symlinks.

* Thu Jun 17 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.2-6
- Fix jetty symlinks.

* Thu Jun 10 2010 Andrew Overholt <overholt@redhat.com> 1:3.5.2-5
- Move hamcrest to dropins/jdt (rhbz#601059).
- Re-symlink after provisioning (rhbz#602865).

* Mon Apr 12 2010 Andrew Overholt <overholt@redhat.com> 1:3.5.2-4
- Rebuild to pick up new xulrunner.

* Fri Mar 19 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.2-3
- Use eclipse-build 0.5.0 release.

* Mon Mar 8 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.2-2
- Fix multilib install.

* Sun Mar 7 2010 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.2-1
- Update to 3.5.2.

* Thu Jan 07 2010 Andrew Overholt <overholt@redhat.com> 1:3.5.1-28
- Version Provides for "eclipse" and "eclipse-sdk" (-pde).

* Tue Dec 22 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.1-27
- Fix patch application.

* Tue Dec 22 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.1-26
- Backport eclipse-build patch for e.o#291128.

* Tue Dec 15 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-25
- Fix o.e.jdt.junit dropins issue. RHBZ#538803 (Thanks to Patrick Higgins).

* Fri Dec 4 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-24
- Replace gecko BR/Rs with xulrunner.
- Drop xulrunner-devel-unstable now that it's merged in xulrunner-devel.

* Thu Dec 3 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-23
- Remove old manipulations to bundles.info.
- Update to eclipse-build 0.4 release.

* Mon Nov 30 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.1-22
- Move ant-nodeps out of bootstrap.

* Tue Nov 17 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.1-21
- Fix typo in memory settings.

* Tue Nov 17 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-20
- Fix ppc64 swt jar version.

* Mon Nov 16 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.1-19
- Temporarily patch for e.o#294877.
- Fix some whitespace.

* Fri Nov 13 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-18
- No about files on ppc64 too.

* Wed Nov 11 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-17
- Update to eclipse-build 0.4 RC4 (fixes pdebuild escaping).

* Tue Nov 10 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-16
- Specify -DbuildArch when running ant applyPatches.

* Tue Nov 10 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-15
- Update to eclipse-build 0.4 RC3.

* Fri Nov 10 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-14
- Fix build with commons-codec 1.4.

* Fri Oct 30 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.1-13
- Make /usr/bin/eclipse a wrapper script due to rhbz#531675 (e.o#290395).

* Mon Oct 26 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.1-12
- Remove old TODO items.

* Fri Oct 23 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-12
- No need to invoke desktop-file-install, it's handled by e-b install now. 

* Thu Oct 22 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-11
- Remove ppc64 files copying and sedding. Supported by eclipse-build now.

* Tue Oct 20 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-10
- Remove old/not needed BR/Rs.

* Mon Oct 19 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-9
- New e-b snapshot that contains fragments for ppc64.

* Thu Oct 15 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-8
- Add bootstrap flag.

* Mon Oct 12 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-7
- Put back JAVA_HOME.

* Mon Oct 12 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-6
- New eclipse-build snapshot. Pdebuild and ecf compilation are part of it.

* Thu Oct 8 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-5
- Fix install call.

* Thu Oct 8 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-4
- New eclipse-build snapshot. Remove parts included in it.

* Wed Oct 07 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.1-3
- Add patch for bugs.eclipse.org/287307

* Mon Oct 5 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-2
- Add /usr/share/eclipse/dropins to dropins locations.

* Fri Oct 2 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.1-1
- Update to 3.5.1.

* Tue Sep 29 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-4
- Symlink to unversioned jetty jars.

* Tue Sep 29 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-3
- Build with eclipse-build 0.4.0 RC0.

* Wed Sep 23 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.0-2
- Move jakarta-commons-codec requirement from jdt to platform.

* Tue Sep 22 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-1
- Fix help toolbar jsp problem.

* Fri Sep 18 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.13
- Update ecf-filetransfer and build it.

* Tue Sep 15 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.12
- Build with system jetty.

* Mon Sep 14 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.0-0.11
- Add /usr/share/eclipse/dropins to list of dropins locations
  (rhbz#522117).

* Wed Sep 09 2009 Mat Booth <fedora@matbooth.co.uk> 1:3.5.0-0.10
- Patch the target platform templates so they find all the required
  source bundles (see RHBZ # 521969).

* Mon Aug 31 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.9
- Remove all testframework sources, patches, build and etc.

* Tue Aug 18 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.8
- Use system hamcrest.

* Mon Aug 17 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.7
- Use o.e.equinox.initializer from SOURCE1 instead of separate one.

* Fri Aug 14 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.6
- Do not use the provided eclipse.ini but the one from build.

* Thu Aug 13 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.5
- Add epoch to icu4j Requires/BuildRequires.

* Tue Aug 11 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.4.0
- Fix sources url.
- Make it use system icu4j and sat4j.

* Fri Aug 7 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.3.35
- Another missing ppc64 fragment.

* Fri Aug 7 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.3.34
- Fix missing fragment on ppc64.

* Thu Aug 6 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.3.33
- Fix missing launcher for ppc64.

* Wed Aug 5 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.3.32
- Manually enable o.e.core.runtime and o.e.equinox.ds because it's not enabled on ppc64.

* Wed Aug 5 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.3.31
- Revert initialize call path changes.

* Wed Aug 5 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.3.30
- Additional output to debug ppc64 build failures.

* Wed Aug 5 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.3.29
- Reenable initialize.
- Fix paths in initializer call.

* Wed Aug 5 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.3.28
- Disable initialize.

* Tue Aug 4 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.3.27
- No need to copy eclipse.ini for secondary archs.

* Tue Aug 4 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.3.26
- eclipse/about_files are not installed on ppc for some reason.

* Mon Aug 3 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.3.25
- Swith to eclipse-build for building.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:3.5.0-0.3.9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jun 17 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.2.9
- Fix package-build template to add target for -Dconfigs.

* Tue May 19 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.0-0.2.8
- Remove Fedora branding.

* Thu May 7 2009 Andrew Overholt <overholt@redhat.com> 1:3.5.0-0.2.7
- Update patch to tests' library.xml to allow for easy debugging of tests.

* Wed Apr 29 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.2.6
- Fix initializer run (sed again).

* Wed Apr 29 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.2.5
- Bump tomcat6 BR.
- Fix director run to not require sed on bundles.info.

* Wed Apr 22 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.2.4
- Update to newer I-build.
- Update fedora customization.
- Bump dependencies minimal versions.
- Fix update site functionality.
- Simplify jdt %%files section.

* Tue Apr 14 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.2.3
- Rediff patch30.

* Tue Apr 14 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.2.2
- Fix version of source bundles.

* Mon Apr 13 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.2.1
- Create org.eclipse.swt.gtk.linux.* based on the ppc version.

* Mon Apr 13 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.2
- Remove patches for the ecj package and others already applied upstream.
- Rediff some ppc64 patches.

* Mon Apr 13 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.1.12
- o.e.update.core.linux is x86 only.

* Mon Apr 13 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.1.11
- Remove more p2 generated files.

* Mon Apr 13 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.1.10
- Do not install p2 generatad file.

* Fri Apr 10 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.1.9
- BR/R jakarta-commons-codec and jakarta-commons-httpclient.

* Thu Apr 9 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.1.8
- Add patch for xulrunner compilation.

* Tue Apr 7 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.1.7
- Fix patch name.

* Thu Apr 2 2009 Alexander Kurtakov <akurtako@redhat.com> 1:3.5.0-0.1.6
- First try for 3.5 build.
