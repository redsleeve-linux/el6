# note, parametrised macros are order-senisitve (unlike not-parametrized) even with normal macros
# also necessary when passing it as parameter other macros. If not macro, then it is considered as switch
%global debug_suffix_unquoted -debug
# quoted one for shell operations
%global debug_suffix "%{debug_suffix_unquoted}"
%global normal_suffix ""

#if you wont only debug build, but providing java, build only normal build, but  set normalbuild_parameter
%global debugbuild_parameter  slowdebug
%global normalbuild_parameter release
%global debug_warning This package have full debug on. Install only in need, and remove asap.
%global debug_on with full debug on
%global for_debug for packages with debug on

# by default we build normal build always.
%global include_normal_build 1
%if %{include_normal_build}
%global build_loop1 %{normal_suffix}
%else
%global build_loop1 %{nil}
%endif

%global aarch64         aarch64 arm64 armv8
# sometimes we need to distinguish big and little endian PPC64
%global ppc64le         ppc64le
%global ppc64be         ppc64 ppc64p7
%global multilib_arches %{power64} sparc64 x86_64
%global jit_arches      %{ix86} x86_64 sparcv9 sparc64 %{aarch64} %{power64}

# By default, we build a debug build during main build on JIT architectures
%ifarch %{jit_arches}
%global include_debug_build 1
%else
%global include_debug_build 0
%endif

%if %{include_debug_build}
%global build_loop2 %{debug_suffix}
%else
%global build_loop2 %{nil}
%endif

# if you disable both builds, then build fails
%global build_loop  %{build_loop1} %{build_loop2}
# note, that order  normal_suffix debug_suffix, in case of both enabled,
# is expected in one single case at the end of build
%global rev_build_loop  %{build_loop2} %{build_loop1}

%ifarch %{jit_arches}
%global bootstrap_build 1
%else
%global bootstrap_build 0
%endif

%if %{bootstrap_build}
%global targets bootcycle-images docs
%else
%global targets all
%endif

%ifarch %{aarch64}
# Disable hardened build on AArch64 as it didn't bootcycle
%undefine _hardened_build
%global ourcppflags %{nil}
%global ourldflags %{nil}
%else
# Filter out flags from the optflags macro that cause problems with the OpenJDK build
# We filter out -O flags so that the optimisation of HotSpot is not lowered from O3 to O2
# We filter out -Wall which will otherwise cause HotSpot to produce hundreds of thousands of warnings (100+mb logs)
# We replace it with -Wformat (required by -Werror=format-security)
# We filter out -fexceptions as the HotSpot build explicitly does -fno-exceptions and it's otherwise the default for C++
%global ourflags %(echo %optflags | sed -e 's|-Wall|-Wformat|' | sed -r -e 's|-O[0-9]*||')
%global ourcppflags %(echo %ourflags | sed -e 's|-fexceptions||' | sed -e 's|-fasynchronous-unwind-tables||')
# no __global_ldflags in RHEL 6
%global ourldflags %{nil}
%endif

# With diabled nss is NSS deactivated, so in NSS_LIBDIR can be wrong path
# the initialisation must be here. LAter the pkg-connfig have bugy behaviour
#looks liekopenjdk RPM specific bug
# Always set this so the nss.cfg file is not broken
%global NSS_LIBDIR %(pkg-config --variable=libdir nss)
%global NSS_LIBS %(pkg-config --libs nss)
%global NSS_CFLAGS %(pkg-config --cflags nss-softokn)
# see https://bugzilla.redhat.com/show_bug.cgi?id=1332456
%global NSSSOFTOKN_BUILDTIME_NUMBER %(pkg-config --modversion nss-softokn || : )
%global NSS_BUILDTIME_NUMBER %(pkg-config --modversion nss || : )
#this is worakround for processing of requires during srpm creation
%global NSSSOFTOKN_BUILDTIME_VERSION %(if [ "x%{NSSSOFTOKN_BUILDTIME_NUMBER}" == "x" ] ; then echo "" ;else echo ">= %{NSSSOFTOKN_BUILDTIME_NUMBER}" ;fi)
%global NSS_BUILDTIME_VERSION %(if [ "x%{NSS_BUILDTIME_NUMBER}" == "x" ] ; then echo "" ;else echo ">= %{NSS_BUILDTIME_NUMBER}" ;fi)

# fix for https://bugzilla.redhat.com/show_bug.cgi?id=1111349
%global _privatelibs libmawt[.]so.*
%global __provides_exclude ^(%{_privatelibs})$
%global __requires_exclude ^(%{_privatelibs})$

%ifarch x86_64
%global archinstall amd64
%endif
%ifarch ppc
%global archinstall ppc
%endif
%ifarch %{ppc64be}
%global archinstall ppc64
%endif
%ifarch %{ppc64le}
%global archinstall ppc64le
%endif
%ifarch %{ix86}
%global archinstall i386
%endif
%ifarch ia64
%global archinstall ia64
%endif
%ifarch s390
%global archinstall s390
%endif
%ifarch s390x
%global archinstall s390x
%endif
%ifarch %{arm}
%global archinstall arm
%endif
%ifarch %{aarch64}
%global archinstall aarch64
%endif
# 32 bit sparc, optimized for v9
%ifarch sparcv9
%global archinstall sparc
%endif
# 64 bit sparc
%ifarch sparc64
%global archinstall sparcv9
%endif
%ifnarch %{jit_arches}
%global archinstall %{_arch}
%endif



%ifarch %{jit_arches}
%global with_systemtap 1
%else
%global with_systemtap 0
%endif

# Convert an absolute path to a relative path.  Each symbolic link is
# specified relative to the directory in which it is installed so that
# it will resolve properly within chrooted installations.
%global script 'use File::Spec; print File::Spec->abs2rel($ARGV[0], $ARGV[1])'
%global abs2rel %{__perl} -e %{script}


# Standard JPackage naming and versioning defines.
%global origin          openjdk
# note, following three variables are sedded from update_sources if used correctly. Hardcode them rather there.
%global project         aarch64-port
%global repo            jdk8u
%global revision        aarch64-jdk8u121-b13
# eg # jdk8u60-b27 -> jdk8u60 or # aarch64-jdk8u60-b27 -> aarch64-jdk8u60  (dont forget spec escape % by %%)
%global whole_update    %(VERSION=%{revision}; echo ${VERSION%%-*})
# eg  jdk8u60 -> 60 or aarch64-jdk8u60 -> 60
%global updatever       %(VERSION=%{whole_update}; echo ${VERSION##*u})
# eg jdk8u60-b27 -> b27
%global buildver        %(VERSION=%{revision}; echo ${VERSION##*-})
# priority must be 7 digits in total. The expression is workarounding tip
%global priority        %(TIP=1800%{updatever};  echo ${TIP/tip/999})

%global javaver         1.8.0

# parametrized macros are order-sensitive
%global fullversion     %{name}-%{version}-%{release}
#images stub
%global j2sdkimage       j2sdk-image
# output dir stub
%global buildoutputdir() %{expand:openjdk/build/jdk8.build%1}
#we can copy the javadoc to not arched dir, or made it not noarch
%global uniquejavadocdir()    %{expand:%{fullversion}%1}
#main id and dir of this jdk
%global uniquesuffix()        %{expand:%{fullversion}.%{_arch}%1}

# Standard JPackage directories and symbolic links.
%global sdkdir()        %{expand:%{uniquesuffix %%1}}
%global jrelnk()        %{expand:jre-%{javaver}-%{origin}-%{version}-%{release}.%{_arch}%1}

#rhel 6 only fix for https://bugzilla.redhat.com/show_bug.cgi?id=1217177
#this is breakng multipleinstalls
%global sdk_versionless_lnk()        %{expand:%{_jvmdir}/java-%{javaver}-%{origin}.%{_arch}%1}
%global jre_versionless_lnk()        %{expand:%{_jvmdir}/jre-%{javaver}-%{origin}.%{_arch}%1}
#first is link to not-macroed sdkbindir (usage of macro makes alternatives inconsistent again)
#second is link to not-macroed jrebindir
#those are created somewhere during install and used in alternatives later
#end of fix of rhbz#1217177 (but see creation and alternatives)


%global jredir()        %{expand:%{sdkdir %%1}/jre}
%global sdkbindir()     %{expand:%{_jvmdir}/%{sdkdir %%1}/bin}
%global jrebindir()     %{expand:%{_jvmdir}/%{jredir %%1}/bin}
%global jvmjardir()     %{expand:%{_jvmjardir}/%{uniquesuffix %%1}}


#another hunk needed by fix for 1217177
%global jardir_jre() %{expand:
%{_jvmjardir}/jre-%{javaver}-%{origin}.%{_arch}%1
}
%global jardir_sdk() %{expand:
%{_jvmjardir}/java-%{javaver}-%{origin}.%{_arch}%1
}
#end of naother hunk

%if %{with_systemtap}
# Where to install systemtap tapset (links)
# We would like these to be in a package specific subdir,
# but currently systemtap doesn't support that, so we have to
# use the root tapset dir for now. To distinquish between 64
# and 32 bit architectures we place the tapsets under the arch
# specific dir (note that systemtap will only pickup the tapset
# for the primary arch for now). Systemtap uses the machine name
# aka build_cpu as architecture specific directory name.
%global tapsetroot /usr/share/systemtap
%global tapsetdir %{tapsetroot}/tapset/%{_build_cpu}
%endif

# not-duplicated scriplets for normal/debug packages
%global update_desktop_icons /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%global post_script() %{expand:
update-desktop-database %{_datadir}/applications &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
exit 0
}


%global post_headless() %{expand:
# FIXME: identical binaries are copied, not linked. This needs to be
# fixed upstream.
%ifarch %{jit_arches}
# MetaspaceShared::generate_vtable_methods not implemented for PPC JIT
%ifnarch %{power64}
#see https://bugzilla.redhat.com/show_bug.cgi?id=513605
%{jrebindir %%1}/java -Xshare:dump >/dev/null 2>/dev/null
%endif
%endif

PRIORITY=%{priority}
if [ "%1" == %{debug_suffix} ]; then
  let PRIORITY=PRIORITY-1
fi

ext=.gz
alternatives \\
  --install %{_bindir}/java java %{jre_versionless_lnk %%1}/bin/java $PRIORITY \\
  --slave %{_jvmdir}/jre jre %{_jvmdir}/%{jredir %%1} \\
  --slave %{_jvmjardir}/jre jre_exports %{_jvmjardir}/%{jrelnk %%1} \\
  --slave %{_bindir}/jjs jjs %{jrebindir %%1}/jjs \\
  --slave %{_bindir}/keytool keytool %{jrebindir %%1}/keytool \\
  --slave %{_bindir}/orbd orbd %{jrebindir %%1}/orbd \\
  --slave %{_bindir}/pack200 pack200 %{jrebindir %%1}/pack200 \\
  --slave %{_bindir}/rmid rmid %{jrebindir %%1}/rmid \\
  --slave %{_bindir}/rmiregistry rmiregistry %{jrebindir %%1}/rmiregistry \\
  --slave %{_bindir}/servertool servertool %{jrebindir %%1}/servertool \\
  --slave %{_bindir}/tnameserv tnameserv %{jrebindir %%1}/tnameserv \\
  --slave %{_bindir}/policytool policytool %{jrebindir %%1}/policytool \\
  --slave %{_bindir}/unpack200 unpack200 %{jrebindir %%1}/unpack200 \\
  --slave %{_mandir}/man1/java.1$ext java.1$ext \\
  %{_mandir}/man1/java-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jjs.1$ext jjs.1$ext \\
  %{_mandir}/man1/jjs-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/keytool.1$ext keytool.1$ext \\
  %{_mandir}/man1/keytool-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/orbd.1$ext orbd.1$ext \\
  %{_mandir}/man1/orbd-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/pack200.1$ext pack200.1$ext \\
  %{_mandir}/man1/pack200-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/rmid.1$ext rmid.1$ext \\
  %{_mandir}/man1/rmid-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/rmiregistry.1$ext rmiregistry.1$ext \\
  %{_mandir}/man1/rmiregistry-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/servertool.1$ext servertool.1$ext \\
  %{_mandir}/man1/servertool-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/tnameserv.1$ext tnameserv.1$ext \\
  %{_mandir}/man1/tnameserv-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/policytool.1$ext policytool.1$ext \\
  %{_mandir}/man1/policytool-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/unpack200.1$ext unpack200.1$ext \\
  %{_mandir}/man1/unpack200-%{uniquesuffix %%1}.1$ext

for X in %{origin} %{javaver} ; do
  alternatives \\
    --install %{_jvmdir}/jre-"$X" \\
    jre_"$X" %{_jvmdir}/%{jredir %%1} $PRIORITY \\
    --slave %{_jvmjardir}/jre-"$X" \\
    jre_"$X"_exports %{_jvmdir}/%{jredir %%1}
done

#update-alternatives --install %{_jvmdir}/jre-%{javaver}-%{origin} jre_%{javaver}_%{origin} %{_jvmdir}/%{jrelnk %%1} $PRIORITY \\
#--slave %{_jvmjardir}/jre-%{javaver}-%{origin}       jre_%{javaver}_%{origin}_exports      %{jvmjardir %%1}
#removed in favor of hardcoded link rhbnz#1217177

update-desktop-database %{_datadir}/applications &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
exit 0
}

%global postun_script() %{expand:
update-desktop-database %{_datadir}/applications &> /dev/null || :
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{update_desktop_icons}
fi
exit 0
}


%global postun_headless() %{expand:
# now using versionless symlink here, part of rhbnz#1217177
if [ $1 -eq 0 ]
then
  alternatives --remove java %{jre_versionless_lnk %%1}/bin/java
fi
  alternatives --remove jre_%{origin} %{_jvmdir}/%{jredir %%1}
  alternatives --remove jre_%{javaver} %{_jvmdir}/%{jredir %%1}
# removed in favour of rhbnz#1217177
#  alternatives --remove jre_%{javaver}_%{origin} %{_jvmdir}/%{jrelnk %%1}
}

%global posttrans_script() %{expand:
%{update_desktop_icons}
}

%global post_devel() %{expand:

PRIORITY=%{priority}
if [ "%1" == %{debug_suffix} ]; then
  let PRIORITY=PRIORITY-1
fi

ext=.gz
alternatives \\
  --install %{_bindir}/javac javac %{sdk_versionless_lnk %%1}/bin/javac $PRIORITY \\
  --slave %{_jvmdir}/java java_sdk %{_jvmdir}/%{sdkdir %%1} \\
  --slave %{_jvmjardir}/java java_sdk_exports %{_jvmjardir}/%{sdkdir %%1} \\
  --slave %{_bindir}/appletviewer appletviewer %{sdkbindir %%1}/appletviewer \\
  --slave %{_bindir}/extcheck extcheck %{sdkbindir %%1}/extcheck \\
  --slave %{_bindir}/idlj idlj %{sdkbindir %%1}/idlj \\
  --slave %{_bindir}/jar jar %{sdkbindir %%1}/jar \\
  --slave %{_bindir}/jarsigner jarsigner %{sdkbindir %%1}/jarsigner \\
  --slave %{_bindir}/javadoc javadoc %{sdkbindir %%1}/javadoc \\
  --slave %{_bindir}/javah javah %{sdkbindir %%1}/javah \\
  --slave %{_bindir}/javap javap %{sdkbindir %%1}/javap \\
  --slave %{_bindir}/jcmd jcmd %{sdkbindir %%1}/jcmd \\
  --slave %{_bindir}/jconsole jconsole %{sdkbindir %%1}/jconsole \\
  --slave %{_bindir}/jdb jdb %{sdkbindir %%1}/jdb \\
  --slave %{_bindir}/jdeps jdeps %{sdkbindir %%1}/jdeps \\
  --slave %{_bindir}/jhat jhat %{sdkbindir %%1}/jhat \\
  --slave %{_bindir}/jinfo jinfo %{sdkbindir %%1}/jinfo \\
  --slave %{_bindir}/jmap jmap %{sdkbindir %%1}/jmap \\
  --slave %{_bindir}/jps jps %{sdkbindir %%1}/jps \\
  --slave %{_bindir}/jrunscript jrunscript %{sdkbindir %%1}/jrunscript \\
  --slave %{_bindir}/jsadebugd jsadebugd %{sdkbindir %%1}/jsadebugd \\
  --slave %{_bindir}/jstack jstack %{sdkbindir %%1}/jstack \\
  --slave %{_bindir}/jstat jstat %{sdkbindir %%1}/jstat \\
  --slave %{_bindir}/jstatd jstatd %{sdkbindir %%1}/jstatd \\
  --slave %{_bindir}/native2ascii native2ascii %{sdkbindir %%1}/native2ascii \\
  --slave %{_bindir}/rmic rmic %{sdkbindir %%1}/rmic \\
  --slave %{_bindir}/schemagen schemagen %{sdkbindir %%1}/schemagen \\
  --slave %{_bindir}/serialver serialver %{sdkbindir %%1}/serialver \\
  --slave %{_bindir}/wsgen wsgen %{sdkbindir %%1}/wsgen \\
  --slave %{_bindir}/wsimport wsimport %{sdkbindir %%1}/wsimport \\
  --slave %{_bindir}/xjc xjc %{sdkbindir %%1}/xjc \\
  --slave %{_mandir}/man1/appletviewer.1$ext appletviewer.1$ext \\
  %{_mandir}/man1/appletviewer-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/extcheck.1$ext extcheck.1$ext \\
  %{_mandir}/man1/extcheck-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/idlj.1$ext idlj.1$ext \\
  %{_mandir}/man1/idlj-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jar.1$ext jar.1$ext \\
  %{_mandir}/man1/jar-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jarsigner.1$ext jarsigner.1$ext \\
  %{_mandir}/man1/jarsigner-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/javac.1$ext javac.1$ext \\
  %{_mandir}/man1/javac-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/javadoc.1$ext javadoc.1$ext \\
  %{_mandir}/man1/javadoc-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/javah.1$ext javah.1$ext \\
  %{_mandir}/man1/javah-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/javap.1$ext javap.1$ext \\
  %{_mandir}/man1/javap-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jcmd.1$ext jcmd.1$ext \\
  %{_mandir}/man1/jcmd-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jconsole.1$ext jconsole.1$ext \\
  %{_mandir}/man1/jconsole-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jdb.1$ext jdb.1$ext \\
  %{_mandir}/man1/jdb-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jdeps.1$ext jdeps.1$ext \\
  %{_mandir}/man1/jdeps-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jhat.1$ext jhat.1$ext \\
  %{_mandir}/man1/jhat-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jinfo.1$ext jinfo.1$ext \\
  %{_mandir}/man1/jinfo-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jmap.1$ext jmap.1$ext \\
  %{_mandir}/man1/jmap-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jps.1$ext jps.1$ext \\
  %{_mandir}/man1/jps-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jrunscript.1$ext jrunscript.1$ext \\
  %{_mandir}/man1/jrunscript-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jsadebugd.1$ext jsadebugd.1$ext \\
  %{_mandir}/man1/jsadebugd-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jstack.1$ext jstack.1$ext \\
  %{_mandir}/man1/jstack-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jstat.1$ext jstat.1$ext \\
  %{_mandir}/man1/jstat-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/jstatd.1$ext jstatd.1$ext \\
  %{_mandir}/man1/jstatd-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/native2ascii.1$ext native2ascii.1$ext \\
  %{_mandir}/man1/native2ascii-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/rmic.1$ext rmic.1$ext \\
  %{_mandir}/man1/rmic-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/schemagen.1$ext schemagen.1$ext \\
  %{_mandir}/man1/schemagen-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/serialver.1$ext serialver.1$ext \\
  %{_mandir}/man1/serialver-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/wsgen.1$ext wsgen.1$ext \\
  %{_mandir}/man1/wsgen-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/wsimport.1$ext wsimport.1$ext \\
  %{_mandir}/man1/wsimport-%{uniquesuffix %%1}.1$ext \\
  --slave %{_mandir}/man1/xjc.1$ext xjc.1$ext \\
  %{_mandir}/man1/xjc-%{uniquesuffix %%1}.1$ext

for X in %{origin} %{javaver} ; do
  alternatives \\
    --install %{_jvmdir}/java-"$X" \\
    java_sdk_"$X" %{_jvmdir}/%{sdkdir %%1} $PRIORITY  \\
    --slave %{_jvmjardir}/java-"$X" \\
    java_sdk_"$X"_exports %{_jvmjardir}/%{sdkdir %%1}
done

#update-alternatives --install %{_jvmdir}/java-%{javaver}-%{origin} java_sdk_%{javaver}_%{origin} %{_jvmdir}/%{sdkdir %%1} $PRIORITY  \\
#--slave %{_jvmjardir}/java-%{javaver}-%{origin}       java_sdk_%{javaver}_%{origin}_exports      %{_jvmjardir}/%{sdkdir %%1}
#removed in favor of hardcoded link rhbnz#1217177

update-desktop-database %{_datadir}/applications &> /dev/null || :
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

exit 0
}

%global postun_devel() %{expand:
# now using versionless symlink here, part of rhbnz#1217177
if [ $1 -eq 0 ]
then
  alternatives --remove javac %{sdk_versionless_lnk %%1}/bin/javac
fi
  alternatives --remove java_sdk_%{origin} %{_jvmdir}/%{sdkdir %%1}
  alternatives --remove java_sdk_%{javaver} %{_jvmdir}/%{sdkdir %%1}
# removed in favour of rhbnz#1217177
#  alternatives --remove java_sdk_%{javaver}_%{origin} %{_jvmdir}/%{sdkdir %%1}

update-desktop-database %{_datadir}/applications &> /dev/null || :

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    %{update_desktop_icons}
fi
exit 0
}

%global posttrans_devel() %{expand:
%{update_desktop_icons}
}

%global post_javadoc() %{expand:

PRIORITY=%{priority}
if [ "%1" == %{debug_suffix} ]; then
  let PRIORITY=PRIORITY-1
fi

alternatives \\
  --install %{_javadocdir}/java javadocdir %{_javadocdir}/%{uniquejavadocdir %%1}/api \\
  $PRIORITY
exit 0
}

%global postun_javadoc() %{expand:
  alternatives --remove javadocdir %{_javadocdir}/%{uniquejavadocdir %%1}/api
exit 0
}

%global files_jre() %{expand:
%{_datadir}/icons/hicolor/*x*/apps/java-%{javaver}.png
%{_datadir}/applications/*policytool%1.desktop
}


%global files_jre_headless() %{expand:
%defattr(-,root,root,-)
%doc %{buildoutputdir %%1}/images/%{j2sdkimage}/jre/ASSEMBLY_EXCEPTION
%doc %{buildoutputdir %%1}/images/%{j2sdkimage}/jre/LICENSE
%doc %{buildoutputdir %%1}/images/%{j2sdkimage}/jre/THIRD_PARTY_README
%dir %{_jvmdir}/%{sdkdir %%1}
#two rhel 6 only dir rhbz#1217177
%dir %{jre_versionless_lnk %%1}
%dir %{jardir_jre %%1}
%{_jvmdir}/%{jrelnk %%1}
%{_jvmjardir}/%{jrelnk %%1}
%{_jvmprivdir}/*
%{jvmjardir %%1}
%dir %{_jvmdir}/%{jredir %%1}/lib/security
%{_jvmdir}/%{jredir %%1}/lib/security/cacerts
%config(noreplace) %{_jvmdir}/%{jredir %%1}/lib/security/US_export_policy.jar
%config(noreplace) %{_jvmdir}/%{jredir %%1}/lib/security/local_policy.jar
%config(noreplace) %{_jvmdir}/%{jredir %%1}/lib/security/java.policy
%config(noreplace) %{_jvmdir}/%{jredir %%1}/lib/security/java.security
%config(noreplace) %{_jvmdir}/%{jredir %%1}/lib/security/blacklisted.certs
%config(noreplace) %{_jvmdir}/%{jredir %%1}/lib/logging.properties
%{_mandir}/man1/java-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jjs-%{uniquesuffix %%1}.1*
%{_mandir}/man1/keytool-%{uniquesuffix %%1}.1*
%{_mandir}/man1/orbd-%{uniquesuffix %%1}.1*
%{_mandir}/man1/pack200-%{uniquesuffix %%1}.1*
%{_mandir}/man1/rmid-%{uniquesuffix %%1}.1*
%{_mandir}/man1/rmiregistry-%{uniquesuffix %%1}.1*
%{_mandir}/man1/servertool-%{uniquesuffix %%1}.1*
%{_mandir}/man1/tnameserv-%{uniquesuffix %%1}.1*
%{_mandir}/man1/unpack200-%{uniquesuffix %%1}.1*
%{_mandir}/man1/policytool-%{uniquesuffix %%1}.1*
%config(noreplace) %{_jvmdir}/%{jredir %%1}/lib/security/nss.cfg
%ifarch %{jit_arches}
%ifnarch %{power64}
%attr(664, root, root) %ghost %{_jvmdir}/%{jredir %%1}/lib/%{archinstall}/server/classes.jsa
%attr(664, root, root) %ghost %{_jvmdir}/%{jredir %%1}/lib/%{archinstall}/client/classes.jsa
%endif
%endif
%{_jvmdir}/%{jredir %%1}/lib/%{archinstall}/server/
%{_jvmdir}/%{jredir %%1}/lib/%{archinstall}/client/
}

%global files_devel() %{expand:
%defattr(-,root,root,-)
%doc %{buildoutputdir %%1}/images/%{j2sdkimage}/ASSEMBLY_EXCEPTION
%doc %{buildoutputdir %%1}/images/%{j2sdkimage}/LICENSE
%doc %{buildoutputdir %%1}/images/%{j2sdkimage}/THIRD_PARTY_README
%dir %{_jvmdir}/%{sdkdir %%1}/bin
%dir %{_jvmdir}/%{sdkdir %%1}/include
%dir %{_jvmdir}/%{sdkdir %%1}/lib
#two rhel 6 only dir rhbz#1217177
%dir %{sdk_versionless_lnk %%1}
%dir %{jardir_sdk %%1}
%{_jvmdir}/%{sdkdir %%1}/bin/*
%{_jvmdir}/%{sdkdir %%1}/include/*
%{_jvmdir}/%{sdkdir %%1}/lib/*
%{_jvmjardir}/%{sdkdir %%1}
%{_datadir}/applications/*jconsole%1.desktop
%{_mandir}/man1/appletviewer-%{uniquesuffix %%1}.1*
%{_mandir}/man1/extcheck-%{uniquesuffix %%1}.1*
%{_mandir}/man1/idlj-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jar-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jarsigner-%{uniquesuffix %%1}.1*
%{_mandir}/man1/javac-%{uniquesuffix %%1}.1*
%{_mandir}/man1/javadoc-%{uniquesuffix %%1}.1*
%{_mandir}/man1/javah-%{uniquesuffix %%1}.1*
%{_mandir}/man1/javap-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jconsole-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jcmd-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jdb-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jdeps-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jhat-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jinfo-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jmap-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jps-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jrunscript-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jsadebugd-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jstack-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jstat-%{uniquesuffix %%1}.1*
%{_mandir}/man1/jstatd-%{uniquesuffix %%1}.1*
%{_mandir}/man1/native2ascii-%{uniquesuffix %%1}.1*
%{_mandir}/man1/rmic-%{uniquesuffix %%1}.1*
%{_mandir}/man1/schemagen-%{uniquesuffix %%1}.1*
%{_mandir}/man1/serialver-%{uniquesuffix %%1}.1*
%{_mandir}/man1/wsgen-%{uniquesuffix %%1}.1*
%{_mandir}/man1/wsimport-%{uniquesuffix %%1}.1*
%{_mandir}/man1/xjc-%{uniquesuffix %%1}.1*
%if %{with_systemtap}
%dir %{tapsetroot}
%dir %{tapsetdir}
%{tapsetdir}/*%{version}-%{release}.%{_arch}%1.stp
%dir %{_jvmdir}/%{sdkdir %%1}/tapset
%{_jvmdir}/%{sdkdir %%1}/tapset/*.stp
%endif
}

%global files_demo() %{expand:
%defattr(-,root,root,-)
%doc %{buildoutputdir %%1}/images/%{j2sdkimage}/jre/LICENSE
}

%global files_src() %{expand:
%defattr(-,root,root,-)
%doc README.src
%{_jvmdir}/%{sdkdir %%1}/src.zip
}

%global files_javadoc() %{expand:
%defattr(-,root,root,-)
%doc %{_javadocdir}/%{uniquejavadocdir %%1}
%doc %{buildoutputdir %%1}/images/%{j2sdkimage}/jre/LICENSE
}


# not-duplicated requires/provides/obsolate for normal/debug packages
%global java_rpo() %{expand:
Requires: fontconfig
Requires: xorg-x11-fonts-Type1

# RHEL 6 only builds on x86 and x86_64
ExclusiveArch: x86_64 i686

# Requires rest of java
Requires: %{name}-headless%1 = %{epoch}:%{version}-%{release}


# Standard JPackage base provides.
Provides: jre-%{javaver}-%{origin}%1 = %{epoch}:%{version}-%{release}
Provides: jre-%{origin}%1 = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}%1 = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}%1 = %{epoch}:%{version}-%{release}
Provides: jre = %{javaver}%1
Provides: java-%{origin}%1 = %{epoch}:%{version}-%{release}
Provides: java%1 = %{epoch}:%{javaver}
# Standard JPackage extensions provides.
Provides: java-fonts%1 = %{epoch}:%{version}

#Obsoletes: java-1.7.0-openjdk%1
#Obsoletes: java-1.5.0-gcj%1
#Obsoletes: sinjdoc
}

%global java_headless_rpo() %{expand:
# Require /etc/pki/java/cacerts.
Requires: ca-certificates
# Require jpackage-utils for ownership of /usr/lib/jvm/
Requires: jpackage-utils
# Require zoneinfo data provided by tzdata-java subpackage.
Requires: tzdata-java >= 2014f-1
# Part of NSS is statically linked into the libsunec.so library
# so we need at least the version we built against to be available
# on the system. Otherwise, the SunEC provider fails to initialise.
Requires: nss %{NSS_BUILDTIME_VERSION}
Requires: nss-softokn %{NSSSOFTOKN_BUILDTIME_VERSION}
# Post requires alternatives to install tool alternatives.
Requires(post):   %{_sbindir}/alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): %{_sbindir}/alternatives

# Standard JPackage base provides.
Provides: jre-%{javaver}-%{origin}-headless%1 = %{epoch}:%{version}-%{release}
Provides: jre-%{origin}-headless%1 = %{epoch}:%{version}-%{release}
Provides: jre-%{javaver}-headless%1 = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-headless%1 = %{epoch}:%{version}-%{release}
Provides: jre-headless%1 = %{epoch}:%{javaver}
Provides: java-%{origin}-headless%1 = %{epoch}:%{version}-%{release}
Provides: java-headless%1 = %{epoch}:%{javaver}
# Standard JPackage extensions provides.
Provides: jndi%1 = %{epoch}:%{version}
Provides: jndi-ldap%1 = %{epoch}:%{version}
Provides: jndi-cos%1 = %{epoch}:%{version}
Provides: jndi-rmi%1 = %{epoch}:%{version}
Provides: jndi-dns%1 = %{epoch}:%{version}
Provides: jaas%1 = %{epoch}:%{version}
Provides: jsse%1 = %{epoch}:%{version}
Provides: jce%1 = %{epoch}:%{version}
Provides: jdbc-stdext%1 = 4.1
Provides: java-sasl%1 = %{epoch}:%{version}

#Obsoletes: java-1.7.0-openjdk-headless%1
}

%global java_devel_rpo() %{expand:
# Require base package.
Requires:         %{name}%1 = %{epoch}:%{version}-%{release}
# Post requires alternatives to install tool alternatives.
Requires(post):   %{_sbindir}/alternatives
# Postun requires alternatives to uninstall tool alternatives.
Requires(postun): %{_sbindir}/alternatives

# Standard JPackage devel provides.
#Provides: java-sdk-%{javaver}-%{origin}%1 = %{epoch}:%{version}
#Provides: java-sdk-%{javaver}%1 = %{epoch}:%{version}
#Provides: java-sdk-%{origin}%1 = %{epoch}:%{version}
#Provides: java-sdk%1 = %{epoch}:%{javaver}
#Provides: java-%{javaver}-devel%1 = %{epoch}:%{version}
#Provides: java-devel-%{origin}%1 = %{epoch}:%{version}
#Provides: java-devel%1 = %{epoch}:%{javaver}

#Obsoletes: java-1.7.0-openjdk-devel%1
#Obsoletes: java-1.5.0-gcj-devel%1
}


%global java_demo_rpo() %{expand:
Requires: %{name}%1 = %{epoch}:%{version}-%{release}

#Obsoletes: java-1.7.0-openjdk-demo%1
}

%global java_javadoc_rpo() %{expand:
# Post requires alternatives to install javadoc alternative.
Requires(post):   %{_sbindir}/alternatives
# Postun requires alternatives to uninstall javadoc alternative.
Requires(postun): %{_sbindir}/alternatives

# Standard JPackage javadoc provides.
Provides: java-javadoc%1 = %{epoch}:%{version}-%{release}
Provides: java-%{javaver}-javadoc%1 = %{epoch}:%{version}-%{release}

#Obsoletes: java-1.7.0-openjdk-javadoc%1

}

%global java_src_rpo() %{expand:
Requires: %{name}-headless%1 = %{epoch}:%{version}-%{release}

#Obsoletes: java-1.7.0-openjdk-src%1
}

# Prevent brp-java-repack-jars from being run.
%global __jar_repack 0

Name:    java-%{javaver}-%{origin}
Version: %{javaver}.%{updatever}
Release: 0.%{buildver}%{?dist}
# java-1.5.0-ibm from jpackage.org set Epoch to 1 for unknown reasons,
# and this change was brought into RHEL-4.  java-1.5.0-ibm packages
# also included the epoch in their virtual provides.  This created a
# situation where in-the-wild java-1.5.0-ibm packages provided "java =
# 1:1.5.0".  In RPM terms, "1.6.0 < 1:1.5.0" since 1.6.0 is
# interpreted as 0:1.6.0.  So the "java >= 1.6.0" requirement would be
# satisfied by the 1:1.5.0 packages.  Thus we need to set the epoch in
# JDK package >= 1.6.0 to 1, and packages referring to JDK virtual
# provides >= 1.6.0 must specify the epoch, "java >= 1:1.6.0".

Epoch:   1
Summary: OpenJDK Runtime Environment
Group:   Development/Languages

License:  ASL 1.1 and ASL 2.0 and GPL+ and GPLv2 and GPLv2 with exceptions and LGPL+ and LGPLv2 and MPLv1.0 and MPLv1.1 and Public Domain and W3C
URL:      http://openjdk.java.net/

# aarch64-port now contains integration forest of both aarch64 and normal jdk
# Source from upstream OpenJDK8 project. To regenerate, use
# VERSION=aarch64-jdk8u121-b13 FILE_NAME_ROOT=aarch64-port-jdk8u-${VERSION}
# REPO_ROOT=<path to checked-out repository> generate_source_tarball.sh
# where the source is obtained from http://hg.openjdk.java.net/%%{project}/%%{repo}
Source0: %{project}-%{repo}-%{revision}.tar.xz

# Custom README for -src subpackage
Source2:  README.src

# Use 'generate_tarballs.sh' to generate the following tarballs
# They are based on code contained in the IcedTea7 project.

# Systemtap tapsets. Zipped up to keep it small.
Source8: systemtap-tapset-3.1.0.tar.xz

# Desktop files. Adapated from IcedTea.
Source9: jconsole.desktop.in
Source10: policytool.desktop.in

# nss configuration file
Source11: nss.cfg

# Removed libraries that we link instead
Source12: %{name}-remove-intree-libraries.sh

# Ensure we aren't using the limited crypto policy
Source13: TestCryptoLevel.java

# Missing headers not provided by nss-softokn
Source15: lowkeyti.h
Source16: softoknt.h

# Ensure ECDSA is working
Source17: TestECDSA.java

Source20: repackReproduciblePolycies.sh

# New versions of config files with aarch64 support. This is not upstream yet.
Source100: config.guess
Source101: config.sub

# RPM/distribution specific patches

# Accessibility patches
# Ignore AWTError when assistive technologies are loaded 
Patch1:   %{name}-accessible-toolkit.patch

# Upstreamable patches
# PR2737: Allow multiple initialization of PKCS11 libraries
Patch5: multiple-pkcs11-library-init.patch
# PR2095, RH1163501: 2048-bit DH upper bound too small for Fedora infrastructure (sync with IcedTea 2.x)
Patch504: rh1163501.patch
# S4890063, PR2304, RH1214835: HPROF: default text truncated when using doe=n option
Patch511: rh1214835.patch
# Turn off strict overflow on IndicRearrangementProcessor{,2}.cpp following 8140543: Arrange font actions
Patch512: no_strict_overflow.patch
# Support for building the SunEC provider with the system NSS installation
# PR1983: Support using the system installation of NSS with the SunEC provider
# PR2127: SunEC provider crashes when built using system NSS
# PR2815: Race condition in SunEC provider with system NSS
# PR2899: Don't use WithSeed versions of NSS functions as they don't fully process the seed
Patch513: pr1983-jdk.patch
Patch514: pr1983-root.patch
Patch515: pr2127.patch
Patch516: pr2815.patch
Patch517: pr2899.patch

# Arch-specific upstreamable patches
# PR2415: JVM -Xmx requirement is too high on s390
Patch100: %{name}-s390-java-opts.patch
# Type fixing for s390
Patch102: %{name}-size_t.patch
# Use "%z" for size_t on s390 as size_t != intptr_t
Patch103: s390-size_t_format_flags.patch

# Patches which need backporting to 8u
# S8073139, RH1191652; fix name of ppc64le architecture
Patch601: %{name}-rh1191652-root.patch
Patch602: %{name}-rh1191652-jdk.patch
Patch603: %{name}-rh1191652-hotspot-aarch64.patch
# Include all sources in src.zip
Patch7: include-all-srcs.patch
# 8035341: Allow using a system installed libpng
Patch202: system-libpng.patch
# 8042159: Allow using a system-installed lcms2
Patch203: system-lcms.patch
# PR2462: Backport "8074839: Resolve disabled warnings for libunpack and the unpack200 binary"
# This fixes printf warnings that lead to build failure with -Werror=format-security from optflags
Patch502: pr2462.patch
# S6260348, PR3066: GTK+ L&F JTextComponent not respecting desktop caret blink rate
Patch526: 6260348-pr3066.patch

# Patches ineligible for 8u
# 8043805: Allow using a system-installed libjpeg
Patch201: system-libjpeg.patch

# Local fixes
# PR1834, RH1022017: Reduce curves reported by SSL to those in NSS
Patch525: pr1834-rh1022017.patch
# RH1367357: lcms2: Out-of-bounds read in Type_MLU_Read()
Patch533: rh1367357.patch
# Turn on AssumeMP by default on RHEL systems
Patch534: always_assumemp.patch
# RH1393047: Make java.io.ObjectInputStream compatible with pre-Java 8 compilers
Patch535: rh1393047.patch

# Non-OpenJDK fixes

Patch998: rhel6-built.patch


BuildRequires: autoconf
BuildRequires: automake
BuildRequires: alsa-lib-devel
BuildRequires: binutils
BuildRequires: cups-devel
BuildRequires: desktop-file-utils
BuildRequires: fontconfig
BuildRequires: freetype-devel
BuildRequires: giflib-devel
BuildRequires: gcc-c++
BuildRequires: gtk2-devel
#BuildRequires: lcms2-devel # no lcms2 in rhel 6
BuildRequires: libjpeg-devel
BuildRequires: libpng-devel
BuildRequires: libxslt
BuildRequires: libX11-devel
BuildRequires: libXi-devel
BuildRequires: libXinerama-devel
BuildRequires: libXt-devel
BuildRequires: libXtst-devel
# Requirements for setting up the nss.cfg
BuildRequires: nss-devel
BuildRequires: pkgconfig
BuildRequires: xorg-x11-proto-devel
BuildRequires: zip
# Use OpenJDK 7 where available (on RHEL) to avoid
# having to use the rhel-7.x-java-unsafe-candidate hack
%if 0%{?rhel}
BuildRequires: java-1.7.0-openjdk-devel
%else
BuildRequires: java-1.8.0-openjdk-devel
%endif
# Zero-assembler build requirement.
%ifnarch %{jit_arches}
BuildRequires: libffi-devel
%endif
BuildRequires: tzdata-java >= 2015d
# Build requirements for SunEC system NSS support
BuildRequires: nss-softokn-freebl-devel >= 3.14.3-18

# cacerts build requirement.
BuildRequires: openssl
%if %{with_systemtap}
BuildRequires: systemtap-sdt-devel
%endif


# this is built always, also during debug-only build
# when it is built in debug-only, then this package is just placeholder
%{java_rpo %{nil}}

%description
The OpenJDK runtime environment.

%if %{include_debug_build}
%package debug
Summary: OpenJDK Runtime Environment %{debug_on}
Group:   Development/Languages

%{java_rpo %{debug_suffix_unquoted}}
%description debug
The OpenJDK runtime environment.
%{debug_warning}
%endif

%if %{include_normal_build}
%package headless
Summary: OpenJDK Runtime Environment
Group:   Development/Languages

%{java_headless_rpo %{nil}}

%description headless
The OpenJDK runtime environment without audio and video support.
%endif

%if %{include_debug_build}
%package headless-debug
Summary: OpenJDK Runtime Environment %{debug_on}
Group:   Development/Languages

%{java_headless_rpo %{debug_suffix_unquoted}}

%description headless-debug
The OpenJDK runtime environment without audio and video support.
%{debug_warning}
%endif

%if %{include_normal_build}
%package devel
Summary: OpenJDK Development Environment
Group:   Development/Tools

%{java_devel_rpo %{nil}}

%description devel
The OpenJDK development tools.
%endif

%if %{include_debug_build}
%package devel-debug
Summary: OpenJDK Development Environment %{debug_on}
Group:   Development/Tools

%{java_devel_rpo %{debug_suffix_unquoted}}

%description devel-debug
The OpenJDK development tools.
%{debug_warning}
%endif

%if %{include_normal_build}
%package demo
Summary: OpenJDK Demos
Group:   Development/Languages

%{java_demo_rpo %{nil}}

%description demo
The OpenJDK demos.
%endif

%if %{include_debug_build}
%package demo-debug
Summary: OpenJDK Demos %{debug_on}
Group:   Development/Languages

%{java_demo_rpo %{debug_suffix_unquoted}}

%description demo-debug
The OpenJDK demos.
%{debug_warning}
%endif

%if %{include_normal_build}
%package src
Summary: OpenJDK Source Bundle
Group:   Development/Languages

%{java_src_rpo %{nil}}

%description src
The OpenJDK source bundle.
%endif

%if %{include_debug_build}
%package src-debug
Summary: OpenJDK Source Bundle %{for_debug}
Group:   Development/Languages

%{java_src_rpo %{debug_suffix_unquoted}}

%description src-debug
The OpenJDK source bundle %{for_debug}.
%endif

%if %{include_normal_build}
%package javadoc
Summary: OpenJDK API Documentation
Group:   Documentation
Requires: jpackage-utils
BuildArch: noarch

%{java_javadoc_rpo %{nil}}

%description javadoc
The OpenJDK API documentation.
%endif

%if %{include_debug_build}
%package javadoc-debug
Summary: OpenJDK API Documentation %{for_debug}
Group:   Documentation
Requires: jpackage-utils
BuildArch: noarch

%{java_javadoc_rpo %{debug_suffix_unquoted}}

%description javadoc-debug
The OpenJDK API documentation %{for_debug}.
%endif



%prep
if [ %{include_normal_build} -eq 0 -o  %{include_normal_build} -eq 1 ] ; then
  echo "include_normal_build is %{include_normal_build}"
else
  echo "include_normal_build is %{include_normal_build}, thats invalid. Use 1 for yes or 0 for no"
  exit 11
fi
if [ %{include_debug_build} -eq 0 -o  %{include_debug_build} -eq 1 ] ; then
  echo "include_debug_build is %{include_debug_build}"
else
  echo "include_debug_build is %{include_debug_build}, thats invalid. Use 1 for yes or 0 for no"
  exit 12
fi
if [ %{include_debug_build} -eq 0 -a  %{include_normal_build} -eq 0 ] ; then
  echo "you have disabled both include_debug_build and include_debug_build. no go."
  exit 13
fi
%setup -q -c -n %{uniquesuffix ""} -T -a 0
# https://bugzilla.redhat.com/show_bug.cgi?id=1189084
prioritylength=`expr length %{priority}`
if [ $prioritylength -ne 7 ] ; then
 echo "priority must be 7 digits in total, violated"
 exit 14
fi
# For old patches
ln -s openjdk jdk8

cp %{SOURCE2} .

# Add local copies of missing NSS headers
cp -v %{SOURCE15} %{SOURCE16} openjdk/jdk/src/share/native/sun/security/ec

# replace outdated configure guess script
#
# the configure macro will do this too, but it also passes a few flags not
# supported by openjdk configure script
cp %{SOURCE100} openjdk/common/autoconf/build-aux/
cp %{SOURCE101} openjdk/common/autoconf/build-aux/

# OpenJDK patches

# Remove libraries that are linked
sh %{SOURCE12}

%patch201
%patch202
%patch203

%patch1
%patch5
%patch7

# s390 build fixes
%patch100
%patch102
%patch103

# ppc64le fixes

# RHEL 6 fix
%patch998

# Zero fixes.

%patch603
%patch601
%patch602

%patch502
%patch504
%patch511
%patch512
%patch513
%patch514
%patch515
%patch516
%patch517
%patch525
%patch526
%patch533
%patch535

# RHEL-only patches
%if 0%{?rhel}
%patch534
%endif

# Extract systemtap tapsets
%if %{with_systemtap}
tar -x -I xz -f %{SOURCE8}
%if %{include_debug_build}
cp -r tapset tapset%{debug_suffix}
%endif


for suffix in %{build_loop} ; do
  for file in "tapset"$suffix/*.in; do
    OUTPUT_FILE=`echo $file | sed -e s:%{javaver}\.stp\.in$:%{version}-%{release}.%{_arch}.stp:g`
    sed -e s:@ABS_SERVER_LIBJVM_SO@:%{_jvmdir}/%{sdkdir $suffix}/jre/lib/%{archinstall}/server/libjvm.so:g $file > $file.1
# TODO find out which architectures other than i686 have a client vm
%ifarch %{ix86}
    sed -e s:@ABS_CLIENT_LIBJVM_SO@:%{_jvmdir}/%{sdkdir $suffix}/jre/lib/%{archinstall}/client/libjvm.so:g $file.1 > $OUTPUT_FILE
%else
    sed -e '/@ABS_CLIENT_LIBJVM_SO@/d' $file.1 > $OUTPUT_FILE
%endif
    sed -i -e s:@ABS_JAVA_HOME_DIR@:%{_jvmdir}/%{sdkdir $suffix}:g $OUTPUT_FILE
    sed -i -e s:@INSTALL_ARCH_DIR@:%{archinstall}:g $OUTPUT_FILE
    sed -i -e s:@prefix@:%{_jvmdir}/%{sdkdir $suffix}/:g $OUTPUT_FILE
  done
done
# systemtap tapsets ends
%endif

# Prepare desktop files
for suffix in %{build_loop} ; do
for file in %{SOURCE9} %{SOURCE10} ; do
    FILE=`basename $file | sed -e s:\.in$::g`
    EXT="${FILE##*.}"
    NAME="${FILE%.*}"
    OUTPUT_FILE=$NAME$suffix.$EXT
    sed -e s:#JAVA_HOME#:%{sdkbindir $suffix}:g $file > $OUTPUT_FILE
    sed -i -e  s:#JRE_HOME#:%{jrebindir $suffix}:g $OUTPUT_FILE
    sed -i -e  s:#ARCH#:%{version}-%{release}.%{_arch}$suffix:g $OUTPUT_FILE
done
done

%build
# How many cpu's do we have?
export NUM_PROC=%(/usr/bin/getconf _NPROCESSORS_ONLN 2> /dev/null || :)
export NUM_PROC=${NUM_PROC:-1}
%if 0%{?_smp_ncpus_max}
# Honor %%_smp_ncpus_max
[ ${NUM_PROC} -gt %{?_smp_ncpus_max} ] && export NUM_PROC=%{?_smp_ncpus_max}
%endif

# Build IcedTea and OpenJDK.
%ifarch s390x sparc64 alpha %{power64} %{aarch64}
export ARCH_DATA_MODEL=64
%endif
%ifarch alpha
export CFLAGS="$CFLAGS -mieee"
%endif

# We use ourcppflags because the OpenJDK build seems to
# pass these to the HotSpot C++ compiler...
EXTRA_CFLAGS="%ourcppflags"
# Disable various optimizations to fix miscompliation. See:
# - https://bugzilla.redhat.com/show_bug.cgi?id=1120792
EXTRA_CPP_FLAGS="%ourcppflags -fno-tree-vrp"
# PPC/PPC64 needs -fno-tree-vectorize since -O3 would
# otherwise generate wrong code producing segfaults.
%ifarch %{power64} ppc
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-tree-vectorize"
# fix rpmlint warnings
EXTRA_CFLAGS="$EXTRA_CFLAGS -fno-strict-aliasing"
%endif
export EXTRA_CFLAGS

(cd openjdk/common/autoconf
 bash ./autogen.sh
)

for suffix in %{build_loop} ; do
if [ "$suffix" = "%{debug_suffix}" ] ; then
debugbuild=%{debugbuild_parameter}
else
debugbuild=%{normalbuild_parameter}
fi

mkdir -p %{buildoutputdir $suffix}
pushd %{buildoutputdir $suffix}

NSS_LIBS="%{NSS_LIBS} -lfreebl -lsoftokn" \
NSS_CFLAGS="%{NSS_CFLAGS} -DLEGACY_NSS" \
bash ../../configure \
%ifnarch %{jit_arches}
    --with-jvm-variants=zero \
%endif
    --disable-zip-debug-info \
    --with-milestone="fcs" \
    --with-update-version=%{updatever} \
    --with-build-number=%{buildver} \
    --with-boot-jdk=/usr/lib/jvm/java-openjdk \
    --with-debug-level=$debugbuild \
    --enable-unlimited-crypto \
    --enable-system-nss \
    --with-zlib=system \
    --with-libjpeg=system \
    --with-giflib=system \
    --with-libpng=system \
    --with-lcms=bundled \
    --with-stdcpplib=dynamic \
    --with-extra-cxxflags="$EXTRA_CPP_FLAGS" \
    --with-extra-cflags="$EXTRA_CFLAGS" \
    --with-extra-ldflags="%{ourldflags}" \
    --with-num-cores="$NUM_PROC"

cat spec.gmk
cat hotspot-spec.gmk

# The combination of FULL_DEBUG_SYMBOLS=0 and ALT_OBJCOPY=/does_not_exist
# disables FDS for all build configs and reverts to pre-FDS make logic.
# STRIP_POLICY=none says don't do any stripping. DEBUG_BINARIES=true says
# ignore all the other logic about which debug options and just do '-g'.

make \
    DEBUG_BINARIES=true \
    JAVAC_FLAGS=-g \
    STRIP_POLICY=no_strip \
    POST_STRIP_CMD="" \
    LOG=trace \
    %{targets}

# the build (erroneously) removes read permissions from some jars
# this is a regression in OpenJDK 7 (our compiler):
# http://icedtea.classpath.org/bugzilla/show_bug.cgi?id=1437
find images/%{j2sdkimage} -iname '*.jar' -exec chmod ugo+r {} \;
chmod ugo+r images/%{j2sdkimage}/lib/ct.sym

# remove redundant *diz and *debuginfo files
find images/%{j2sdkimage} -iname '*.diz' -exec rm {} \;
find images/%{j2sdkimage} -iname '*.debuginfo' -exec rm {} \;

popd >& /dev/null

# Install nss.cfg right away as we will be using the JRE above
export JAVA_HOME=$(pwd)/%{buildoutputdir $suffix}/images/%{j2sdkimage}

# Install nss.cfg right away as we will be using the JRE above
install -m 644 %{SOURCE11} $JAVA_HOME/jre/lib/security/

# Use system-wide tzdata
rm $JAVA_HOME/jre/lib/tzdb.dat
ln -s %{_datadir}/javazi-1.8/tzdb.dat $JAVA_HOME/jre/lib/tzdb.dat

#build cycles
done

%check

# We test debug first as it will give better diagnostics on a crash
for suffix in %{rev_build_loop} ; do

export JAVA_HOME=$(pwd)/%{buildoutputdir $suffix}/images/%{j2sdkimage}

# Check unlimited policy has been used
$JAVA_HOME/bin/javac -d . %{SOURCE13}
$JAVA_HOME/bin/java TestCryptoLevel

# Check ECC is working
$JAVA_HOME/bin/javac -d . %{SOURCE17}
$JAVA_HOME/bin/java $(echo $(basename %{SOURCE17})|sed "s|\.java||")

# Check debug symbols are present and can identify code
SERVER_JVM="$JAVA_HOME/jre/lib/%{archinstall}/server/libjvm.so"
if [ -f "$SERVER_JVM" ] ; then
  nm -aCl "$SERVER_JVM" | grep javaCalls.cpp
fi
CLIENT_JVM="$JAVA_HOME/jre/lib/%{archinstall}/client/libjvm.so"
if [ -f "$CLIENT_JVM" ] ; then
  nm -aCl "$CLIENT_JVM" | grep javaCalls.cpp
fi
ZERO_JVM="$JAVA_HOME/jre/lib/%{archinstall}/zero/libjvm.so"
if [ -f "$ZERO_JVM" ] ; then
  nm -aCl "$ZERO_JVM" | grep javaCalls.cpp
fi

# Check src.zip has all sources. See RHBZ#1130490
jar -tf $JAVA_HOME/src.zip | grep 'sun.misc.Unsafe'

# Check class files include useful debugging information
$JAVA_HOME/bin/javap -l java.lang.Object | grep "Compiled from"
$JAVA_HOME/bin/javap -l java.lang.Object | grep LineNumberTable
$JAVA_HOME/bin/javap -l java.lang.Object | grep LocalVariableTable

# Check generated class files include useful debugging information
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep "Compiled from"
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep LineNumberTable
$JAVA_HOME/bin/javap -l java.nio.ByteBuffer | grep LocalVariableTable

#build cycles
done

%install
rm -rf $RPM_BUILD_ROOT
STRIP_KEEP_SYMTAB=libjvm*

for suffix in %{build_loop} ; do

pushd %{buildoutputdir  $suffix}/images/%{j2sdkimage}

#install jsa directories so we can owe them
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{jredir $suffix}/lib/%{archinstall}/server/
mkdir -p $RPM_BUILD_ROOT%{_jvmdir}/%{jredir $suffix}/lib/%{archinstall}/client/

  # Install main files.
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}
  cp -a bin include lib src.zip $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmdir}/%{jredir $suffix}
  cp -a jre/bin jre/lib $RPM_BUILD_ROOT%{_jvmdir}/%{jredir $suffix}

%if %{with_systemtap}
  # Install systemtap support files.
  install -dm 755 $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}/tapset
  # note, that uniquesuffix  is in BUILD dir in this case
  cp -a $RPM_BUILD_DIR/%{uniquesuffix ""}/tapset$suffix/*.stp $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}/tapset/
  pushd  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}/tapset/
   tapsetFiles=`ls *.stp`
  popd
  install -d -m 755 $RPM_BUILD_ROOT%{tapsetdir}
  pushd $RPM_BUILD_ROOT%{tapsetdir}
    RELATIVE=$(%{abs2rel} %{_jvmdir}/%{sdkdir $suffix}/tapset %{tapsetdir})
    for name in $tapsetFiles ; do
      targetName=`echo $name | sed "s/.stp/$suffix.stp/"`
      ln -sf $RELATIVE/$name $targetName
    done
  popd
%endif

  # Install cacerts symlink.
  rm -f $RPM_BUILD_ROOT%{_jvmdir}/%{jredir $suffix}/lib/security/cacerts
  pushd $RPM_BUILD_ROOT%{_jvmdir}/%{jredir $suffix}/lib/security
    RELATIVE=$(%{abs2rel} %{_sysconfdir}/pki/java \
      %{_jvmdir}/%{jredir $suffix}/lib/security)
    ln -sf $RELATIVE/cacerts .
  popd

  # Install extension symlinks.
  install -d -m 755 $RPM_BUILD_ROOT%{jvmjardir $suffix}
  pushd $RPM_BUILD_ROOT%{jvmjardir $suffix}
    RELATIVE=$(%{abs2rel} %{_jvmdir}/%{jredir $suffix}/lib %{jvmjardir $suffix})
    ln -sf $RELATIVE/jsse.jar jsse-%{version}.jar
    ln -sf $RELATIVE/jce.jar jce-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-ldap-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-cos-%{version}.jar
    ln -sf $RELATIVE/rt.jar jndi-rmi-%{version}.jar
    ln -sf $RELATIVE/rt.jar jaas-%{version}.jar
    ln -sf $RELATIVE/rt.jar jdbc-stdext-%{version}.jar
    ln -sf jdbc-stdext-%{version}.jar jdbc-stdext-3.0.jar
    ln -sf $RELATIVE/rt.jar sasl-%{version}.jar
    for jar in *-%{version}.jar
    do
      if [ x%{version} != x%{javaver} ]
      then
        ln -sf $jar $(echo $jar | sed "s|-%{version}.jar|-%{javaver}.jar|g")
      fi
      ln -sf $jar $(echo $jar | sed "s|-%{version}.jar|.jar|g")
    done
  popd

  # Install JCE policy symlinks.
  install -d -m 755 $RPM_BUILD_ROOT%{_jvmprivdir}/%{uniquesuffix $suffix}/jce/vanilla

  # Install versioned symlinks.
  pushd $RPM_BUILD_ROOT%{_jvmdir}
    ln -sf %{jredir $suffix} %{jrelnk $suffix}
  popd

  pushd $RPM_BUILD_ROOT%{_jvmjardir}
    ln -sf %{sdkdir $suffix} %{jrelnk $suffix}
  popd

  # Remove javaws man page
  rm -f man/man1/javaws*

  # Install man pages.
  install -d -m 755 $RPM_BUILD_ROOT%{_mandir}/man1
  for manpage in man/man1/*
  do
    # Convert man pages to UTF8 encoding.
    iconv -f ISO_8859-1 -t UTF8 $manpage -o $manpage.tmp
    mv -f $manpage.tmp $manpage
    install -m 644 -p $manpage $RPM_BUILD_ROOT%{_mandir}/man1/$(basename \
      $manpage .1)-%{uniquesuffix $suffix}.1
  done

  # Install demos and samples.
  cp -a demo $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}
  mkdir -p sample/rmi
  if [ ! -e sample/rmi/java-rmi.cgi ] ; then 
    # hack to allow --short-circuit on install
    mv bin/java-rmi.cgi sample/rmi
  fi
  cp -a sample $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}

popd


# Install Javadoc documentation.
install -d -m 755 $RPM_BUILD_ROOT%{_javadocdir}
cp -a %{buildoutputdir $suffix}/docs $RPM_BUILD_ROOT%{_javadocdir}/%{uniquejavadocdir $suffix}

# Install icons and menu entries.
for s in 16 24 32 48 ; do
  install -D -p -m 644 \
    openjdk/jdk/src/solaris/classes/sun/awt/X11/java-icon${s}.png \
    $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/${s}x${s}/apps/java-%{javaver}.png
done

# Install desktop files.
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}/{applications,pixmaps}
for e in jconsole$suffix policytool$suffix ; do
    desktop-file-install --vendor=%{uniquesuffix $suffix} --mode=644 \
        --dir=$RPM_BUILD_ROOT%{_datadir}/applications $e.desktop
done

# Install /etc/.java/.systemPrefs/ directory
# See https://bugzilla.redhat.com/show_bug.cgi?id=741821
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/.java/.systemPrefs

# Find JRE directories.
find $RPM_BUILD_ROOT%{_jvmdir}/%{jredir $suffix} -type d \
  | grep -v jre/lib/security \
  | sed 's|'$RPM_BUILD_ROOT'|%dir |' \
  > %{name}.files-headless"$suffix"
# Find JRE files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{jredir $suffix} -type f -o -type l \
  | grep -v jre/lib/security \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  > %{name}.files.all"$suffix"
#split %%{name}.files to %%{name}.files-headless and %%{name}.files
#see https://bugzilla.redhat.com/show_bug.cgi?id=875408
NOT_HEADLESS=\
"%{_jvmdir}/%{uniquesuffix $suffix}/jre/lib/%{archinstall}/libjsoundalsa.so
%{_jvmdir}/%{uniquesuffix $suffix}/jre/lib/%{archinstall}/libpulse-java.so
%{_jvmdir}/%{uniquesuffix $suffix}/jre/lib/%{archinstall}/libsplashscreen.so
%{_jvmdir}/%{uniquesuffix $suffix}/jre/lib/%{archinstall}/libawt_xawt.so
%{_jvmdir}/%{uniquesuffix $suffix}/jre/lib/%{archinstall}/libjawt.so
%{_jvmdir}/%{uniquesuffix $suffix}/jre/bin/policytool"
#filter  %%{name}.files from  %%{name}.files.all to %%{name}.files-headless
ALL=`cat %{name}.files.all"$suffix"`
for file in $ALL ; do 
  INLCUDE="NO" ; 
  for blacklist in $NOT_HEADLESS ; do
#we can not match normally, because rpmbuild will evaluate !0 result as script failure
    q=`expr match "$file" "$blacklist"` || :
    l=`expr length  "$blacklist"` || :
    if [ $q -eq $l  ]; then 
      INLCUDE="YES" ; 
    fi;
done
if [ "x$INLCUDE" = "xNO"  ]; then 
    echo "$file" >> %{name}.files-headless"$suffix"
else
    echo "$file" >> %{name}.files"$suffix"
fi
done
# Find demo directories.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}/sample -type d \
  | sed 's|'$RPM_BUILD_ROOT'|%dir |' \
  > %{name}-demo.files"$suffix"

# FIXME: remove SONAME entries from demo DSOs.  See
# https://bugzilla.redhat.com/show_bug.cgi?id=436497

# Find non-documentation demo files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}/sample \
  -type f -o -type l | sort \
  | grep -v README \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  >> %{name}-demo.files"$suffix"
# Find documentation demo files.
find $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}/demo \
  $RPM_BUILD_ROOT%{_jvmdir}/%{sdkdir $suffix}/sample \
  -type f -o -type l | sort \
  | grep README \
  | sed 's|'$RPM_BUILD_ROOT'||' \
  | sed 's|^|%doc |' \
  >> %{name}-demo.files"$suffix"

bash %{SOURCE20} $RPM_BUILD_ROOT/%{_jvmdir}/%{jredir $suffix} %{javaver}

#rhel 6 only fix for https://bugzilla.redhat.com/show_bug.cgi?id=1217177
ln -sf %{sdkdir $suffix}  $RPM_BUILD_ROOT/%{sdk_versionless_lnk $suffix}
ln -sf %{sdkdir $suffix}/jre  $RPM_BUILD_ROOT/%{jre_versionless_lnk $suffix}
ln -sf %{_jvmjardir}/%{sdkdir  $suffix}  $RPM_BUILD_ROOT/%{_jvmjardir}/java-%{javaver}-%{origin}.%{_arch}"$suffix"
ln -sf %{_jvmjardir}/%{sdkdir  $suffix}  $RPM_BUILD_ROOT/%{_jvmjardir}/jre-%{javaver}-%{origin}.%{_arch}"$suffix"
#end of fix of rhbz#1217177

# end, dual install
done

%if %{include_normal_build} 
%post 
%{post_script %{nil}}

%post headless
%{post_headless %{nil}}

%postun
%{postun_script %{nil}}

%postun headless
%{postun_headless %{nil}}

%posttrans
%{posttrans_script %{nil}}

%post devel
%{post_devel %{nil}}

%postun devel
%{postun_devel %{nil}}

%posttrans  devel
%{posttrans_devel %{nil}}

%post javadoc
%{post_javadoc %{nil}}

%postun javadoc
%{postun_javadoc %{nil}}
%endif

%if %{include_debug_build} 
%post debug
%{post_script %{debug_suffix_unquoted}}

%post headless-debug
%{post_headless %{debug_suffix_unquoted}}

%postun debug
%{postun_script %{debug_suffix_unquoted}}

%postun headless-debug
%{postun_headless %{debug_suffix_unquoted}}

%posttrans debug
%{posttrans_script %{debug_suffix_unquoted}}

%post devel-debug
%{post_devel %{debug_suffix_unquoted}}

%postun devel-debug
%{postun_devel %{debug_suffix_unquoted}}

%posttrans  devel-debug
%{posttrans_devel %{debug_suffix_unquoted}}

%post javadoc-debug
%{post_javadoc %{debug_suffix_unquoted}}

%postun javadoc-debug
%{postun_javadoc %{debug_suffix_unquoted}}
%endif

%if %{include_normal_build} 
%files -f %{name}.files
# main package builds always
%{files_jre %{nil}}
%else
%files
# placeholder
%endif


%if %{include_normal_build} 
%files headless  -f %{name}.files-headless
# important note, see https://bugzilla.redhat.com/show_bug.cgi?id=1038092 for whole issue 
# all config/norepalce files (and more) have to be declared in pretrans. See pretrans
%{files_jre_headless %{nil}}

%files devel
%{files_devel %{nil}}

%files demo -f %{name}-demo.files
%{files_demo %{nil}}

%files src
%{files_src %{nil}}

%files javadoc
%{files_javadoc %{nil}}
%endif

%if %{include_debug_build} 
%files debug -f %{name}.files-debug
%{files_jre %{debug_suffix_unquoted}}

%files headless-debug  -f %{name}.files-headless-debug
%{files_jre_headless %{debug_suffix_unquoted}}

%files devel-debug
%{files_devel %{debug_suffix_unquoted}}

%files demo-debug -f %{name}-demo.files-debug
%{files_demo %{debug_suffix_unquoted}}

%files src-debug
%{files_src %{debug_suffix_unquoted}}

%files javadoc-debug
%{files_javadoc %{debug_suffix_unquoted}}
%endif

%changelog
* Mon Jan 16 2017 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.121-0.b13
- Update to aarch64-jdk8u121-b13.
- Update PR1834/RH1022017 fix to reduce curves reported by SSL to apply against u121.
- Re-generate RH1393047 ObjectInputStream patch against u121.
- Resolves: rhbz#1410612

* Mon Jan 16 2017 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.112-0.b16
- Update to aarch64-jdk8u112-b16.
- Drop upstreamed patches for 8044762, 8049226, 8154210, 8158260 and 8160122.
- Re-generate size_t and key size (RH1163501) patches against u112.
- Resolves: rhbz#1410612

* Mon Jan 16 2017 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.111-3.b14
- Enable a full bootstrap on JIT archs to ensure stability.
- Resolves: rhbz#1410612

* Thu Jan 12 2017 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.111-2.b18
- Use java-1.7.0-openjdk to bootstrap on RHEL to allow us to use main build target
- Resolves: rhbz#1410612

* Mon Jan 09 2017 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.111-2.b18
- Update to aarch64-jdk8u111-b18, synced with upstream u111, S8170873 and new AArch64 fixes
- Replace our correct version of 8159244 with the amendment to the 8u version from 8160122.
- Resolves: rhbz#1410612

* Tue Nov 08 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.111-1.b15
- Remove method reference from java.io.ObjectInputStream to allow compilation on old ECJ.
- Resolves: rhbz#1393047

* Mon Oct 10 2016 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.111-0.b15
- added nss restricting requires
- Resolves: rhbz#1381990

* Mon Oct 10 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.111-0.b15
- Turn debug builds on for all JIT architectures. Always AssumeMP on RHEL.
- Resolves: rhbz#1381990

* Fri Oct 07 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.111-0.b15
- Update to aarch64-jdk8u111-b15, with AArch64 fix for S8160591.
- Resolves: rhbz#1381990

* Fri Oct 07 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.111-0.b14
- Update to aarch64-jdk8u111-b14.
- Drop the CORBA typo fix, which appears upstream in u111.
- Add LCMS 2 patch to fix Red Hat security issue RH1367357 in the local OpenJDK copy.
- Resolves: rhbz#1381990

* Tue Aug 30 2016 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.102-1.b14
- New variable, @prefix@, needs to be substituted in tapsets (rhbz1371005)
- Resolves: rhbz#1381990

* Tue Aug 23 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.102-0.b14
- Update to aarch64-jdk8u102-b14.
- Drop 8140620, 8148752 and 6961123, all of which appear upstream in u102.
- Move 8159244 to 8u111 section as it only appears to be in unpublished u102 b31.
- Move 8158260 to 8u112 section following its backport to 8u.
- Resolves: rhbz#1381990

* Tue Aug 23 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.101-4.b15
- Update to aarch64-jdk8u101-b15.
- Rebase SystemTap tarball on IcedTea 3.1.0 versions so as to avoid patching.
- Drop additional hunk for 8147771 which is now applied upstream.
- Resolves: rhbz#1381990

* Mon Jul 11 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.101-3.b13
- Replace bad 8159244 patch from upstream 8u with fresh backport from OpenJDK 9.
- Resolves: rhbz#1350034

* Sun Jul 10 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.101-2.b13
- Add missing hunk from 8147771, missed due to inclusion of unneeded 8138811
- Resolves: rhbz#1350034

* Mon Jul 04 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.101-1.b13
- Add workaround for a typo in the CORBA security fix, 8079718
- Resolves: rhbz#1350034

* Fri Jul 01 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.101-0.b13
- Update to u101b13.
- Backport REPOS option in generate_source_tarball.sh
- Drop a leading zero from the priority as the update version is now three digits
- Resolves: rhbz#1350034

* Fri Jul 01 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.92-0.b14
- Add additional fixes (S6260348, S8159244) for u92 update.
- Resolves: rhbz#1350034

* Fri Jul 01 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.92-0.b14
- Update ppc64le fix with upstream version, S8158260.
- Resolves: rhbz#1350034

* Fri Jul 01 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.92-0.b14
- Add fix for ppc64le crash due to illegal instruction.
- Resolves: rhbz#1350034

* Fri Jul 01 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.92-0.b14
- Add backport for S8148752.
- Resolves: rhbz#1350034

* Fri Jul 01 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.92-0.b14
- Update to u92b14.
- Remove upstreamed patches for Zero build failures 8087120 & 8143855.
- Add 8132051 Zero fix upstreamed as 8154210 in 8u112.
- Add upstreamed patch 6961123 from u102 to fix application name in GNOME Shell.
- Add upstreamed patches 8044762 & 8049226 from u112 to fix JDI issues.
- Regenerate java-1.8.0-openjdk-rh1191652-root.patch against u92
- Resolves: rhbz#1350034

* Thu Jun 02 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.91-3.b14
- Forwardport SSL fix to only report curves supported by NSS.
- Resolves: rhbz#1348525

* Sun Apr 10 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.91-1.b14
- Use basename of test file to avoid misinterpretation of full path as a package
- Resolves: rhbz#1325421

* Sun Apr 10 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.91-1.b14
- Update to u91b14.
- Resolves: rhbz#1325421

* Thu Mar 31 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.91-1.b14
- Add ECDSA test to ensure ECC is working.
- Resolves: rhbz#1325421

* Wed Mar 30 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.77-2.b03
- Avoid WithSeed versions of NSS functions as they do not fully process the seed
- Resolves: rhbz#1320662

* Fri Mar 25 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.77-1.b03
- Revert previous change to CFLAGS/LDFLAGS as issue is not us, but rhbz#1320961
- Resolves: rhbz#1320662

* Wed Mar 23 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.77-1.b03
- Disable RPM CFLAGS/LDFLAGS for now due to build issues.
- Resolves: rhbz#1320662

* Wed Mar 23 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.77-1.b03
- RHEL 6 adds -fasynchronous-unwind-tables which leads to libjvm.so being too big on x86
- Resolves: rhbz#1320662

* Wed Mar 23 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.77-1.b03
- Remove patches to generated configure script, which we re-generate anyway.
- Resolves: rhbz#1320662

* Wed Mar 23 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.77-1.b03
- Update to u77b03.
- Drop 8146566 which is applied upstream.
- Replace s390 Java options patch with general version from IcedTea.
- Apply s390 patches unconditionally to avoid arch-specific patch failures.
- Remove fragment of s390 size_t patch that unnecessarily removes a cast, breaking ppc64le.
- Remove aarch64-specific suffix as update/build version are now the same as for other archs.
- Only use z format specifier on s390, not s390x.
- Adjust tarball generation script to allow ecc_impl.h to be included.
- Correct spelling mistakes in tarball generation script.
- Synchronise minor changes from Fedora.
- Use a simple backport for PR2462/8074839.
- Don't backport the crc check for pack.gz. It's not tested well upstream.
- Resolves: rhbz#1320662

* Thu Feb 04 2016 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.71-5.b17
- returned jre_versionless_lnk/bin instead of jrebindir and
-   and    sdk_versionless_lnk/bin isntead of sdkbindir
- Resolves: rhbz#1295752

* Wed Jan 27 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.71-4.b15
- Add patches to allow the SunEC provider to be built with the system NSS install.
- Re-generate source tarball so it includes ecc_impl.h.
- Adjust tarball generation script to allow ecc_impl.h to be included.
- Bring over NSS changes from java-1.7.0-openjdk spec file (NSS_CFLAGS/NSS_LIBS/headers)
- Remove patch which disables the SunEC provider as it is now usable.
- Resolves: rhbz#1208307

* Thu Jan 14 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.71-3.b15
- Add patch to turn off strict overflow on IndicRearrangementProcessor{,2}.cpp
- Resolves: rhbz#1295752

* Wed Jan 13 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.71-2.b15
- RHEL 6 does not have __global_ldflags so set to %%{nil} instead.
- Resolves: rhbz#1295752

* Wed Jan 13 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.71-2.b15
- Remove -Wno-cpp which is not supported on RHEL 6 gcc.
- Resolves: rhbz#1295752

* Wed Jan 13 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.71-2.b15
- Try enabling the RPM CFLAGS and LDFLAGS.
- Resolves: rhbz#1295752

* Wed Jan 13 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.71-1.b15
- January 2016 security update to u71b15.
- Improve verbosity and helpfulness of tarball generation script.
- Update patch documentation using version originally written for Fedora.
- Drop prelink requirement as we no longer use execstack.
- Drop ifdefbugfix patch as this is fixed upstream.
- Provide optional boostrap build and turn it off by default.
- Add patch for size_t formatting on s390 as size_t != intptr_t there.
- Resolves: rhbz#1295752

* Wed Jan 13 2016 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.65-5.b17
- Add flag logic back to spec file but disable for now.
- Restore system-lcms.patch as used in October CPU.
- Resolves: rhbz#1295752

* Tue Jan 12 2016 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.65-4.b17
- moved to integration forest 
- sync with rhel7
- Resolves: rhbz#1295752

* Thu Dec 10 2015 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.65-2.b17
- Add patch to honour %%{_smp_ncpus_max} from Tuomo Soini
- Resolves: rhbz#1152896

* Tue Dec 08 2015 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.65-1.b17
- Bump to distinguish this from the z-stream release.
- Resolves: rhbz#1257655

* Thu Oct 15 2015 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.65-0.b17
- October 2015 security update to u65b17.
- Add script for generating OpenJDK tarballs from a local Mercurial tree.
- Update RH1191652 patch to build against current AArch64 tree.
- Use appropriate source ID to avoid unpacking both tarballs on AArch64.
- Fix library removal script so jpeg, giflib and png sources are removed.
- Update system-lcms.patch to regenerated upstream (8042159) version.
- Drop LCMS update from rhel6-built.patch
- Resolves: rhbz#1257655

* Fri Sep 04 2015 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.60-4.b27
- updated to u60 (1255352)
- Resolves: rhbz#1257655

* Fri Sep 04 2015 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.51-5.b16
- direcotries aligned to rhel6, jdk7 like style ifarch 64 name.arch else naem
- moved to rhel7, jdk8 like style of name.arch. Fixes 1259241
- Resolves: rhbz#1251560

* Fri Aug 21 2015 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.51-4.b16
- Backport S8017773: OpenJDK7 returns incorrect TrueType font metrics
- Resolves: rhbz#1239063

* Thu Aug 13 2015 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.51-3.b16
- priority aligned with other openjdks to 7
- another touching attempt to polycies...
- Resolves: rhbz#1251560

* Thu Aug 13 2015 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.51-2.b16
- main links in alternatives moved to versionless format
- Resolves: rhbz#1217177

* Thu Jul 02 2015 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.51-1.b16
- Bump release number so 6.7 version is greater than 6.6
- Resolves: rhbz#1235161

* Thu Jul 02 2015 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.51-0.b16
- July 2015 security update to u51b16.
- Add script for generating OpenJDK tarballs from a local Mercurial tree.
- Add %%{name} prefix to patches to avoid conflicts with OpenJDK 7 versions.
- Add patches for RH issues fixed in IcedTea 2.x and/or the upcoming u60.
- Use 'openjdk' as directory prefix to allow patch interchange with IcedTea.
- Re-generate EC disablement patch following CPU DH changes.
- Resolves: rhbz#1235161

* Wed Apr 29 2015 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.45-35.b13
- Omit jsa files from power64 file list as well, as they are never generated
- Use the template interpreter on ppc64le
- priority set  gcj < lengthOffFour < otherJdks (RH1175457)
- misusing already fixed bug
- Resolves: rhbz#1189853

* Fri Apr 17 2015 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.45-31.b13
- Make use of system timezone data for OpenJDK 8.
- Resolves: rhbz#1212592

* Fri Apr 10 2015 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.45-30.b13
- repacked sources
- Resolves: RHBZ#1209075

* Thu Apr 09 2015 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.45-29.b13
- do not obsolete openjdk7
- Resolves: rhbz#1209075

* Tue Apr 07 2015 Andrew Hughes <gnu.andrew@redhat.com> - 1:1.8.0.45-27.b13
- Add back ExclusiveArch declaration lost in merge.
- Fix names of PStack patch and removal script to not clash with 7 versions.
- Remove unneeded test case from RHEL 7 ppc64le bug.
- Resolves: rhbz#1209075

* Tue Apr 07 2015 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.45-27.b13
- updated to security u45
- minor sync with 6.7
 - generate_source_tarball.sh
 - adapted java-1.8.0-openjdk-s390-java-opts.patch and java-1.8.0-openjdk-size_t.patch
 - reworked (synced) zero patches (removed 103,11 added 204, 400-403)
 - added upstreamed patch 501 and 505
 - included removeSunEcProvider-RH1154143.patch
- returned java (jre only) provides
- repacked policies (source20)
- removed duplicated NVR provides
- added automated test for priority (length7)
- Resolves: RHBZ#1209075

Fri Jan 09 2015 Severin Gehwolf <sgehwolf@redhat.com> - 1:1.8.0.31-1.b13
- Update to January CPU patch update.
- Resolves: RHBZ#1180300

* Fri Oct 24 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.25-4.b17
- updated aarch64 sources
- epoch synced to 1
- all ppcs excluded from classes dump(1156151)
- removed duplicated provides
- Resolves: rhbz#1146622

* Fri Oct 24 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.25-3.b17
- added patch12,removeSunEcProvider-RH1154143
- xdump excluded from ppc64le (rh1156151)
- Add check for src.zip completeness. See RH1130490 (by sgehwolf@redhat.com)
- Resolves: rhbz#1154143

* Wed Oct 22 2014 Omair Majid <omajid@redhat.com> - 1:1.8.0.25-3.b17
- Do not provide any JPackage-style java* provides.
- Resolves: RHBZ#1155783

* Mon Oct 20 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.25-2.b17
- ec/impl removed from source tarball
- Resolves: RHBZ#1154143

* Mon Oct 06 2014 Severin Gehwolf <sgehwolf@redhat.com> - 1:1.8.0.25-1.b17
- Update to October CPU patch update.
- Resolves: RHBZ#1148896

* Fri Sep 12 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.20-3.b26
- fixed headless (policytool moved to normal)
 - jre/bin/policytool added to not headless exclude list
- updated aarch694 source
- ppc64le synced from fedora
- Resolves: rhbz#1081073

* Mon Sep 08 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.20-2.b26
- forcing build by itself (jdk8 by jdk8)
- Resolves: rhbz#1081073

* Wed Aug 27 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.20-1.b26
- updated to u20-b26
- adapted patch9999 enableArm64.patch
- adapted patch100 s390-java-opts.patch
- adapted patch102 size_t.patch
- removed upstreamed patch  0001-PPC64LE-arch-support-in-openjdk-1.8.patch
- adapted  system-lcms.patch
- removed patch8 set-active-window.patch
- removed patch9 javadoc-error-jdk-8029145.patch
- removed patch10 javadoc-error-jdk-8037484.patch
- removed patch99 applet-hole.patch - itw 1.5.1 is able to ive without it
- Resolves: rhbz#1081073

* Tue Aug 19 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.11-19.b12
- fixed desktop icons
- Icon set to java-1.8.0
- Development removed from policy tool
- Resolves: rhbz#1081073

* Thu Aug 14 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.11-18.b12
- fixed jstack
- Resolves: rhbz#1081073

* Thu Aug 14 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.11-15.b12
- fixed provides/obsolates
- Resolves: rhbz#1081073

* Thu Aug 14 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.11-14.b12
- mayor rework of specfile - sync with f21
 - accessibility kept removed
 - lua script kept unsync
 - priority and epoch kept on 0
 - not included disable-doclint patch
 - kept bundled lcms
 - unused OrderWithRequires
 - used with-stdcpplib instead of with-stdc++lib
- Resolves: rhbz#1081073

* Wed Jul 09 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.11-4.b13
- Added security patches
- Resolves: rhbz#1081073

* Wed Jul 02 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.5-6.b13
- Removed accessibility package
 - removed patch3 java-atk-wrapper-security.patch
 - removed its files and declaration
 - removed creation of libatk-wrapper.so and java-atk-wrapper.jar symlinks
 - removed generation of accessibility.properties
- Resolves: rhbz#1113078

* Fri May 16 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.5-5.b13
- priority lowered to 00000
- Resolves: rhbz#1081073

* Mon Apr 28 2014 Jiri Vanek <jvanek@redhat.com> - 1:1.8.0.5-4.b13
- Initial import from fedora
- Used bundled lcms2
 - added java-1.8.0-openjdk-disable-system-lcms.patch
 - --with-lcms changed to bundled
 - removed build requirement
 - excluded removal of lcms from remove-intree-libraries.sh
- removed --with-extra-cflags="-fno-devirtualize" and --with-extra-cxxflags="-fno-devirtualize"--- 
- added patch998, rhel6-built.patch  to
 - fool autotools
 - replace all ++ chars in autoconfig files by pp
- --with-stdc++lib=dynamic  replaced by --with-stdcpplib=dynamic 
- Bumped release
- Set epoch to 0
- removed patch6, disable-doclint-by-default.patch
- Resolves: rhbz#1081073
