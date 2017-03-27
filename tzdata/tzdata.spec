
%bcond_without java7

%if %{with java7}
%define bin_java %{_prefix}/lib/jvm/java-1.7.0/bin/java
%define bin_javac %{_prefix}/lib/jvm/java-1.7.0/bin/javac
%else
%define bin_java java
%define bin_javac javac
%endif

Summary: Timezone data
Name: tzdata
Version: 2017a
%define tzdata_version 2017a
%define tzcode_version 2017a
Release: 1%{?dist}
License: Public Domain
Group: System Environment/Base
URL: https://www.iana.org/time-zones
Source0: ftp://ftp.iana.org/tz/releases/tzdata%{tzdata_version}.tar.gz
Source1: ftp://ftp.iana.org/tz/releases/tzcode%{tzcode_version}.tar.gz

Patch0: 0001-Fix-Liberia-1972-transition-and-pre-1972-abbr.patch

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: gawk, glibc, perl
BuildRequires: glibc-common >= 2.5.90-7
%if %{with java7}
BuildRequires: java-1.7.0-openjdk-devel
%else
BuildRequires: java-devel
%endif

Conflicts: glibc-common <= 2.3.2-63
BuildArchitectures: noarch

%description
This package contains data files with rules for various timezones around
the world.

%post -p <lua>
-- Update /etc/localtime with the zone configured in /etc/sysconfig/clock.

-- This needs to be kept in sync with /usr/sbin/tzdata-update.

local default = "US/Eastern"
local localtime = "/etc/localtime"
local sysconfig = "/etc/sysconfig/clock"
local zoneinfo = "/usr/share/zoneinfo/"

-- Extract the ZONE setting from /etc/sysconfig/clock.
-- Return nil on error or if the ZONE setting is missing from the file.
local function findzone(sysconfig)
  local f = io.open(sysconfig)
  local zone
  if f ~= nil then
    while true do
      local line = f:read()
      if line == nil then
        break
      end
      zone = string.match(line, '^[ \t]*ZONE[ \t]*=[ \t]*"?([^ \t\n"]*)')
      if zone ~= nil then
        break
      end
    end
    f:close()
  end
  return zone
end

-- Read the entire file PATH.  Returns nil on error.
local function readall(path)
  local f = io.open(path)
  if f == nil then
    return nil
  end
  local result = f:read("*a")
  f:close()
  return result
end

-- Replace the file at PATH with zoneinfo data ZONEDATA.
-- Do nothing if PATH refers to a symbolic link.
local function update(path, zonedata)
  if zonedata == nil then
    return
  end

  -- Do not replace symbolic links.
  local st = posix.stat(path)
  if st ~= nil and st.type == "link" then
    return
  end

  -- Avoid replacing an existing file with identical contents.
  local old = readall(path)
  if old ~= zonedata then
    -- Write temporary .tzupdate file and rename it into place.
    local tmp = path .. ".tzupdate"
    local f = io.open(tmp, "w+")
    if f == nil then
      return
    end
    f:write(zonedata)
    f:close()
    if not os.rename(tmp, path) then
      os.remove(tmp)
    end
  end
end

zone = findzone(sysconfig)
if zone ~= nil then
  local zonedata = readall(zoneinfo .. zone)
  if zonedata ~= nil then
    update(localtime, zonedata)
    update("/var/spool/postfix/etc/localtime", zonedata)
    return
  end
end

-- No valid zone configuration found.  Install the default zone
-- if /etc/localtime does not exist.
if posix.stat(localtime) == nil then
  local zonedata = readall(zoneinfo .. default)
  update(localtime, zonedata)
end

%package java
Summary: Timezone data for Java
Group: System Environment/Base
Source3: javazic.tar.gz
Source4: http://omajid.fedorapeople.org/javazic-1.8-37392f2f5d59.tar.xz

Patch100: javazic-fixup.patch
Patch101: rebase-01.patch
Patch102: rebase-02.patch
Patch103: 7090844.patch
Patch104: 7133138.patch
Patch105: 8051641.patch

%description java
This package contains timezone information for use by Java runtimes.

%prep
%setup -q -c -a 1

%patch0 -p1

mkdir javazic
tar zxf %{SOURCE3} -C javazic
pushd javazic
%patch100
%patch101
%patch102
%patch103
%patch104

# Hack alert! sun.tools may be defined and installed in the
# VM. In order to guarantee that we are using IcedTea/OpenJDK
# for creating the zoneinfo files, rebase all the packages
# from "sun." to "rht.". Unfortunately, gcj does not support
# any of the -Xclasspath options, so we must go this route
# to ensure the greatest compatibility.
mv sun rht
find . -type f -name '*.java' -print0 \
    | xargs -0 -- sed -i -e 's:sun\.tools\.:rht.tools.:g' \
                         -e 's:sun\.util\.:rht.util.:g'
popd

tar xf %{SOURCE4}
%patch105

echo "%{name}%{tzdata_version}" >> VERSION

%build
FILES="africa antarctica asia australasia europe northamerica southamerica
      pacificnew etcetera backward"

mkdir zoneinfo/{,posix,right}
zic -y ./yearistype -d zoneinfo -L /dev/null -p America/New_York $FILES
zic -y ./yearistype -d zoneinfo/posix -L /dev/null $FILES
zic -y ./yearistype -d zoneinfo/right -L leapseconds $FILES

grep -v tz-art.htm tz-link.htm > tz-link.html

# Java 6/7 tzdata
pushd javazic
%{bin_javac} -source 1.5 -target 1.5 -classpath . `find . -name \*.java`
popd

%{bin_java} -classpath javazic/ rht.tools.javazic.Main -V %{version} \
  -d javazi \
  $FILES javazic/tzdata_jdk/gmt javazic/tzdata_jdk/jdk11_backward

# Java 8 tzdata
%if %{with java7}
pushd javazic-1.8
%{bin_javac} -source 1.7 -target 1.7 -classpath . `find . -name \*.java`
popd

%{bin_java} -classpath javazic-1.8 build.tools.tzdb.TzdbZoneRulesCompiler \
    -srcdir . -dstfile tzdb.dat \
    -verbose \
    $FILES javazic-1.8/tzdata_jdk/gmt javazic-1.8/tzdata_jdk/jdk11_backward
%endif

%install
rm -fr $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}
cp -prd zoneinfo $RPM_BUILD_ROOT%{_datadir}
install -p -m 644 zone.tab zone1970.tab iso3166.tab $RPM_BUILD_ROOT%{_datadir}/zoneinfo
cp -prd javazi $RPM_BUILD_ROOT%{_datadir}/javazi

%if %{with java7}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/javazi-1.8
install -p -m 644 tzdb.dat $RPM_BUILD_ROOT%{_datadir}/javazi-1.8/
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_datadir}/zoneinfo
%doc README
%doc Theory
%doc tz-link.html

%files java
%defattr(-,root,root)
%{_datadir}/javazi
%if %{with java7}
%{_datadir}/javazi-1.8
%endif

%changelog
* Thu Mar 02 2017 Patsy Franklin <pfrankli@redhat.com> - 2017a-1
- Rebase to tzdata-2017a
  - Mongolia no longer observes DST. (BZ #1425222)
  - Add upstream patch to fix over-runing of POSIX limit on zone abbreviations.
- Add zone1970.tab file to the install list. (BZ #1427694)

* Wed Nov 23 2016 Patsy Franklin <pfrankli@redhat.com> - 2016j-1
- Rebase to tzdata-2016ij
  - Saratov region of Russia is moving from +03 offset to +04 offset
    on 2016-12-04.

* Wed Nov 02 2016 Patsy Franklin <pfrankli@redhat.com> - 2016i-1
- Rebase to tzdata-2016i:
  - Cyprus is now split into two time zones as of 2016-10-30
  - Tonga will reintroduce DST on 2016-11-06

* Thu Oct 20 2016 Patsy Franklin <pfrankli@redhat.com> - 2016h-1
- Rebase to tzdata-2016h:
  - Palestine will end DST on 2016-10-29 not 2016-10-21.

* Wed Sep 28 2016 Patsy Franklin <pfrankli@redhat.com> - 2016g-2
- Rebase to tzdata-2016g.
  - Turkey changed from EET/EEST (+02/+03) to permanent +03,
    on 2016-09-07.
  - A new leap second will be added on 2016-12-31 23:59:60 UTC.

* Tue Sep 27 2016 Patsy Franklin <pfrankli@redhat.com> - 2016g-1.20160927.prerelease
- Change the Release to 1.20160927_prerelease.dist.

* Mon Sep 26 2016 Patsy Franklin <pfrankli@redhat.com> - 2016g-1.prerelease
- Rebase to prerelease version of tzdata-2016g.
  - Turkey changed from EET/EEST (+02/+03) to permanent +03,
    on 2016-09-07. 
  - A new leap second will be added on 2016-12-31 23:59:60 UTC.

* Tue Sep 20 2016 Patsy Franklin <pfrankli@redhat.com> - 2016f-2
- Interim builds to add support for leap second.

* Tue Jul 05 2016 Patsy Franklin <pfrankli@redhat.com> - 2016f-1
- Rebase to 2016f
  - Egypt cancelled DST.
  - Asia/Novosibirsk transitions from +06 to +07 on 2016-07-24 at 02:00.

* Tue Jun 14 2016 Patsy Franklin <pfrankli@redhat.com> - 2016e-1
- Rebase to 2016e
  - Egypt reinstates DST.

* Tue Apr 19 2016 Patsy Franklin <pfrankli@redhat.com> - 2016d-1
- Rebase to 2016d
  - America/Caracas switches from -0430 to -04 on 2016-05-01 at 02:30.
  - Asia/Magadan switches from +10 to +11 on 2016-04-24 at 02:00.
  - New zone Asia/Tomsk, split off from Asia/Novosibirsk.  It covers
    Tomsk Oblast, Russia, which switches from +06 to +07 on 2016-05-29
    at 02:00.

* Wed Mar 23 2016 Patsy Franklin <pfrankli@redhat.com> - 2016c-1
- Rebase to 2016c
  - Azerbaijan no longer observes DST.
  - Chile reverts from permanent to seasonal DST.

* Mon Mar 14 2016 Patsy Franklin <pfrankli@redhat.com> - 2016b-1
- Rebase to 2016b
  - New zones Europe/Astrakhan and Europe/Ulyanovsk for Astrakhan and
    Ulyanovsk Oblasts, Russia, both of which will switch from +03 to +04 on
    2016-03-27 at 02:00 local time.  They need distinct zones since their
    post-1970 histories disagree.  New zone Asia/Barnaul for Altai Krai and
    Altai Republic, Russia, which will switch from +06 to +07 on the same date
    and local time.  The Astrakhan change is already official; the others have
    passed the first reading in the State Duma and are extremely likely.
    Also, Asia/Sakhalin moves from +10 to +11 on 2016-03-27 at 02:00.
  - As a trial of a new system that needs less information to be made up,
    the new zones use numeric time zone abbreviations like "+04"
    instead of invented abbreviations like "ASTT".
  - Haiti will not observe DST in 2016.
  - Palestine's spring-forward transition on 2016-03-26 is at 01:00, not 00:00.
    Guess future transitions will be March's last
    Saturday at 01:00, not March's last Friday at 24:00.

* Thu Jan 28 2016 Patsy Franklin <pfrankli@redhat.com> - 2016a-2
- Rebuild with --target rhel-6.8-noarch-candidate.

* Thu Jan 28 2016 Patsy Franklin <pfrankli@redhat.com> - 2016a-1
- Rebase to 2016a
  - America/Cayman will not observe daylight saving this year after all.
    Revert our guess that it would.
  - Asia/Chita switches from +0800 to +0900 on 2016-03-27 at 02:00.
  - Asia/Tehran now has DST predictions for the year 2038 and later,
    to be March 21 00:00 to September 21 00:00.  This is likely better
    than predicting no DST, albeit off by a day every now and then.

* Mon Dec 21 2015 Patsy Franklin <pfrankli@redhat.com> - 2015g-4
- tzdata now performs /etc/localtime updates (#1289696)

* Mon Dec 21 2015 Patsy Franklin <pfrankli@redhat.com> - 2015g-3
- Synchronize javazic tool for OpenJDK 6 & 7 with upstream. (#1212549)
- Fix Africa/Casablanca transitions from 2027 forward. (#1217109)

* Thu Oct  1 2015 Patsy Franklin <pfrankli@redhat.com> - 2015g-2
- Rebuild with --target rhel-6.7-noarch-candidate.

* Thu Oct  1 2015 Patsy Franklin <pfrankli@redhat.com> - 2015g-1
- Rebase to 2015g
  - Turkey's 2015 fall-back transition is scheduled for Nov. 8, not Oct. 25.
  - Norfolk moves from +1130 to +1100 on 2015-10-04 at 02:00 local time.
  - Fiji's 2016 fall-back transition is scheduled for January 17, not 24.
  - Fort Nelson, British Columbia will not fall back on 2015-11-01.  It has
    effectively been on MST (-0700) since it advanced its clocks on 2015-03-08.
    New zone America/Fort_Nelson.

* Mon Aug 10 2015 Patsy Franklin <pfrankli@redhat.com> - 2015f-1
- Rebase to 2015f
  - North Korea switches to +0830 on 2015-08-15.
    The abbreviation remains "KST".
  - Uruguay no longer observes DST.

* Sun Jun 14 2015 Patsy Franklin <pfrankli@redhat.com> - 2015e-1
- Rebase to 2015e:
  - Morocco will suspend DST from 2015-06-14 03:00 through 2015-07-19 02:00,
    not 06-13 and 07-18 as we had guessed.  (Thanks to Milamber.)
  - Assume Cayman Islands will observe DST starting next year, using US rules.
    Although it isn't guaranteed, it is the most likely.

* Tue Jun  9 2015 Patsy Franklin <pfrankli@redhat.com> - 2015d-3
-  Morocco will suspend DST from 2015-06-14 03:00 through 2015-07-19 02:00,
   not 06-13 and 07-18 as we had guessed.

* Sat Apr 25 2015 Patsy Franklin <pfrankli@redhat.com> - 2015d-1
- Rebase to 2015d:
  - The Egyptian Cabinet announced that DST will be cancelled for 2015.
  - The abbreviations for Hawaii-Aleutian standard and daylight times
    have been changed from HAST/HADT to HST/HDT, as per US Government
    Printing Office style. This affects only America/Adak since 1983,
    as America/Honolulu was already using the new style. 

* Tue Apr 21 2015 Patsy Franklin <pfrankli@redhat.com> - 2015c-3
- The Egyptian Cabinet announced that DST will be cancelled for 2015.

* Tue Apr 14 2015 Patsy Franklin <pfrankli@redhat.com> - 2015c-2
- Rebuild. Forgot to use --target rhel-6.6-noarch-candidate on the
  final build.

* Tue Apr 14 2015 Patsy Franklin <pfrankli@redhat.com> - 2015c-1
- Rebase to 2015c
  - Egypt's spring-forward transition is at 24:00 on April's last Thursday,
    not 00:00 on April's last Friday.  2015's transition will therefore be on
    Thursday, April 30 at 24:00, not Friday, April 24 at 00:00.  Similar fixes
    apply to 2026, 2037, 2043, etc.

* Sat Mar 21 2015 Patsy Franklin <pfrankli@redhat.com> - 2015b-1
- Rebase to 2015b
  - Mongolia will start observing DST again this year, from the last
    Saturday in March at 02:00 to the last Saturday in September at 00:00.
  - Palestine will start DST on March 28, not March 27.  Also,
    correct the fall 2014 transition from September 26 to October 24.
    Adjust future predictions accordingly.

* Fri Jan 30 2015 Patsy Franklin <pfrankli@redhat.com> - 2015a-1
- Rebase to 2015a
  - New leap second 2015-06-30 23:59:60 UTC as per IERS Bulletin C 49.
  - The Mexican state of Quintana Roo, represented by America/Cancun,
    will shift from Central Time with DST to Eastern Time without DST
    on 2015-02-01 at 02:00.
  - Chile will not change clocks in April or thereafter; its new
    standard time will be its old daylight saving time.  This affects
    America/Santiago, Pacific/Easter, and Antarctica/Palmer.

* Tue Nov 11 2014 Patsy Franklin <pfrankli@redhat.com> - 2014j-1
- Rebase to 2014j
  - Turks & Caicos' switch from US eastern time to UTC-4 year-round
    did not occur on 2014-11-02 at 02:00.  It's currently scheduled
    for 2015-11-01 at 02:00.

* Wed Oct 22 2014 Patsy Franklin <pfrankli@redhat.com> - 2014i-1
- Rebase to 2014i
  - Pacific/Fiji will observe DST from 2014-11-02 02:00 to 2015-01-18 03:00.
  - A new Zone Pacific/Bougainville, for the part of Papua New Guinea
    that plans to switch from UTC+10 to UTC+11 on 2014-12-28 at 02:00.

* Fri Sep 26 2014 Petr Machata <pmachata@redhat.com> - 2014h-1
- Rebase to 2014h
  - Changes to historical transitions in America/Jamaica and
    Asia/Novokuznetsk.
  - Africa/{Blantyre, Bujumbura, Gaborone, Harare, Kigali, Lubumbashi,
    Lusaka} now alias Africa/Maputo, because they don't differ in
    post-1970 stamps.
  - Africa/Maseru and Africa/Mbabane now alias Africa/Johannesburg for
    the same reason.

* Tue Sep  2 2014 Patsy Franklin <pfrankli@redhat.com> - 2014g-1
- Rebase to 2014g
  - Turks & Caicos is switching from US eastern time to UTC-4
    year-round, modeled as a switch from EST/EDT to AST 
    on 2014-11-02 at 02:00.

* Sun Aug 10 2014 Patsy Franklin <pfrankli@redhat.com> - 2014f-1
- Rebase to 2014f
  - Several Russian time zone changes effective on 2014-10-26
    at 02:00 local time.  See NEWS file for additional details.

* Wed Jul 16 2014 Patsy Franklin <pfrankli@redhat.com> - 2014e-3
- More changes for OpenJDK8. Only require one version of 
  java-devel.

* Thu Jun 19 2014 Patsy Franklin <pfrankli@redhat.com> - 2014e-2
- Add support for OpenJDK8.

* Sat Jun 14 2014 Patsy Franklin <pfrankli@redhat.com> - 2014e-1
- Rebase to 2014e
  - Morrocco suspends DTS for Ramadan 
       June 28 at 03:00 and August 2 at 02:00
  - Egypt suspends DTS for Ramadan
       June 26 and July 31 at 24:00

* Thu May 29 2014 Patsy Franklin <pfrankli@redhat.com> - 2014d-1
- Rebase to 2014d
  - zic no longer generates files containing time stamps before
    the Big Bang.  This works around GNOME bug 730332

* Wed May 21 2014 Patsy Franklin <pfrankli@redhat.com> - 2014c-1
- Rebase to 2014c
  - Egypt's government to re-apply daylight saving time.
  - zic now generates transitions for minimum time values
  - Port to Cygwin sans glibc.
  - Remove now-confusing comment about Jordan.

* Tue May 13 2014 Petr Machata <pmachata@redhat.com> - 2014b-3.24.el5
- The transition time will be 24:00, not 0:00.

* Mon May 12 2014 Patsy Franklin <pfrankli@redhat.com> - 2014b-2
- Egypt's government to re-apply daylight saving time
  effective May 15, 2014.

* Tue Mar 25 2014 Patsy Franklin <pfrankli@redhat.com> - 2014b-1
- Rebase to 2014b
  - Crimea switches to Moscow time on 2014-03-30 at 02:00 local time.
  - New entry for Troll station, Antarctica.

* Mon Mar 10 2014 Patsy Franklin <pfrankli@redhat.com> - 2014a-1
- Turkey begins DST on 2014-03-31, not 03-30.

* Mon Jan 20 2014 Patsy Franklin <pfrankli@redhat.com> - 2013i-2
- Fiji ends DST on 2014-01-19 at 02:00, not the previously-scheduled 03:00.

* Tue Dec 17 2013 Patsy Franklin <pfrankli@redhat.com> 2013i-1
- Rebase with early release of 2013i from Paul Eggert github.
  - Jordan switches back to standard time at 00:00 on December 20,2013.
  - The 2006-2011 transition schedule is planned to resume in 2014.
  - The compile-time flag NOSOLAR has been removed.
  - The files solar87, solar88, and solar89 are no longer distributed.
  - tz-link.htm now mentions Noda Time.

* Wed Oct  2 2013 Patsy Franklin <pfrankli@redhat.com> 2013g-1
- Morocco moved end of DST from September to October (#1003875).
 
* Thu Jul  4 2013 Petr Machata <pmachata@redhat.com> - 2013c-2
- Update descriptions in iso3166.tab; make Jerusalem coordinates in
  zone.tab more precise
  (0001-Adjust-commentary-to-try-to-defuse-recent-issues-som.patch)
- Update local mean time for Jerusalem to match more-precise longitude
  (0002-asia-Asia-Jerusalem-Fix-LMT-to-match-more-precise-lo.patch)
- Move Morocco's midsummer 2013 transitions
  (0003-Move-Morocco-s-midsummer-2013-transitions.patch)
  Fixes 980805 980807 981019 981020
- Israel now falls back on the last Sunday of October
  (0004-Israel-now-falls-back-on-the-last-Sunday-of-October.patch)

* Fri May 17 2013 Petr Machata <pmachata@redhat.com> - 2013c-1
- Upstream 2013c
  - Sync past stamps for Palestine and West Bank with timeanddate.com
  - Assume that the recent change to Paraguay's DST rules is permanent
  - Macquarie was uninhabited between 1919 and 1948.  It's also part
    of Australia (update in zone.tab).

* Wed Mar 27 2013 Petr Machata <pmachata@redhat.com> - 2013b-2
- Palestine starts Daylight Saving Time on March 29, 2013
  (tzdata-2013b-gaza.patch)

* Wed Mar 13 2013 Petr Machata <pmachata@redhat.com> - 2013b-1
- Upstream 2013b
  - Paraguay will end DST on March 24 this year
  - Haiti uses US daylight-saving rules this year
  - Morocco does not observe DST during Ramadan
- Upstream 2013a
  - Retire Chile patch, 2013a has the data
  - New Zones Asia/Khandyga, Asia/Ust-Nera, Europe/Busingen
  - Many changes in historical timestamps

* Wed Feb 27 2013 Petr Machata <pmachata@redhat.com> - 2012j-2
- DTS in Chile will end on 2013-04-28
  (0016-Chile-is-changing-its-DST-rules.patch)

* Fri Nov 30 2012 Petr Machata <pmachata@redhat.com> - 2012j-1
- Upstream 2012j
  - Libya moved to CET

* Tue Nov  6 2012 Petr Machata <pmachata@redhat.com> - 2012i-2
- Preserve hardlinks that zic leaves behind, install with cp -d

* Mon Nov  5 2012 Petr Machata <pmachata@redhat.com> - 2012i-1
- Upstream 2012i
  - Cuba switched to DST

* Mon Nov  5 2012 Petr Machata <pmachata@redhat.com> - 2012h-2
- Switch back to using system zic, ignore upstream Makefile at all.
  We do so for java anyway.
- Drop Factory from distribution

* Wed Oct 31 2012 Petr Machata <pmachata@redhat.com> - 2012h-1
- Upstream 2012h
  - Brazilian state Bahia no longer has DST.
  - Brazilian state Tocantins now has DST.
  - Israel has new DST rules next year.
  - Jordan stays on DST this winter.

* Mon Oct 22 2012 Petr Machata <pmachata@redhat.com> - 2012g-1
- Upstream 2012g
  - Adjust the packaging for new Makefile
  - Palestine: Fall transition was Sep 21, not Sep 28
  - Samoa: Daylight Saving Time commences on Sunday 30th September
    2012 and ends on Sunday 7th of April 2013.
- Resolves: #868173

* Mon Sep 17 2012 Petr Machata <pmachata@redhat.com> - 2012f-1
- Upstream 2012f
  - Fiji will start daylight savings at 2 am on Sunday 21st October 2012
    and end at 3 am on Sunday 20th January 2013.  Guess it will be like
    that in following years as well.
- Upstream 2012e
  - Tokelau is in time zone UTC+13, not UTC+14 (and always was)
- Upstream 2012d
  - Morocco will not observe DST during the month of Ramadan.
    DST cessation end date was corrected.
  - Drop tzdata-2012c-morocco.patch

* Fri Jul 13 2012 Petr Machata <pmachata@redhat.com> - 2012c-3
- Morocco will not observe DST during the month of Ramadan
  (tzdata-2012c-morocco.patch)

* Mon May 14 2012 Petr Machata <pmachata@redhat.com> - 2012c-1
- Upstream 2012c
  - Haiti observes DST from 2012 on
  - Gaza Strip and Hebron observe DST in 2012
  - Change start of DST in Syria to last Friday in March
- Resolves: #820732

* Fri Mar 16 2012 Petr Machata <pmachata@redhat.com> - 2012b-3
- Morocco moved DST entry to last Sunday of April
- Resolves: #802460

* Thu Mar 15 2012 Petr Machata <pmachata@redhat.com> - 2012b-2
- Morocco DST starts on the last Sunday of March (March 25, 2012) and
  ends on last Sunday of September, except the month of Ramadan.  It
  is currently unclear what that Ramadan bit means, so this is not
  covered by the patch as of now.
- Resolves: #802460

* Tue Mar 13 2012 Petr Machata <pmachata@redhat.com> - 2012b-1
- Rebase to 2012b; changes vs. 2011n-2:
  - Changes to zones for Antarctica stations
  - Armenia abolished DST in 2012 and forward
  - Cuba enters DST on 31st March
  - Falkland Islands will stay on permanent Summer Time
  - New zone for Creston Valley, Canada, which differs from Dawson
    Creek in past stamps.  Changes to historical stamps in Canada.
  - Last year, Tokelau skipped over the date line together with Samoa
- Resolves: #802460

* Fri Feb 24 2012 Petr Machata <pmachata@redhat.com> - 2011n-2
- The Chilean Government has decided to postpone the entrance into
  winter time (to leave DST) from March 11 2012 to April 28th 2012
- Resolves: #796569

* Tue Feb 21 2012 Petr Machata <pmachata@redhat.com> - 2011n-1
- Rebase to 2011n
  - Cuba postponed DST by two weeks to Nov 13
  - Fiji will enter DST on Jan 21
- Add a patch for the leap second that will occur this summer
- Resolves: #773755

* Wed Oct 19 2011 Petr Machata <pmachata@redhat.com> - 2011l-4
- Ukraine will enter Winter Time after all
- Resolves: #740000

* Fri Oct 14 2011 Petr Machata <pmachata@redhat.com> - 2011l-3
- State of Bahia, Brazil, to resume Summer Time on Oct 16
- The project moved, reflect this in URL
- Resolves: #740000

* Tue Oct 11 2011 Petr Machata <pmachata@redhat.com> - 2011l-2
- Upstream 2011l:
  - Fix ancient stamps for America/Sitka
  - Asia/Hebron transitioned to standard time already on Sep 30, not Oct 3
  - Fiji will introduce DST on Oct 22
- Resolves: #740000

* Wed Sep 21 2011 Petr Machata <pmachata@redhat.com> - 2011k-0.1.20110921
- Upstream 2011i:
  - Add Africa/Juba (South Sudan) zone
  - Samoa skips over the date line on 2011-12-30
  - Use KALT as abbreviation for Europe/Kalinigrad
  - Canonical version of the Newfoundland patch
  - Change America/Resolute use of EST to 2006-2007 only
  - Assume Metlakatla abandoned use of daylight saving in 1983
  - Sync iso3166.tab and zone.tab with above
- Upstream 2011j:
  - Fix the Samoa date line skip
  - Changes in past timestamp typos several Africa zones
- Proposed upstream 2011k:
  - Belarus and Ukraine adopt permanent DST in 2011
  - Palestine suspends DST during Ramadan in 2011
  - Gaza and West Bank split in 2011.  West Bank is tracked in the
    timezone Asia/Hebron.  zone.tab update accordingly.
- Resolves: #740000

* Wed Aug 10 2011 Petr Machata <pmachata@redhat.com> - 2011h-3
- Patch for upcoming change in Newfoundland.  The transition time
  changes from 12:01 AM to 2:00 AM.
- Resolves: #729693

* Mon Jun 27 2011 Petr Machata <pmachata@redhat.com> - 2011h-2
- Upstream 2011h:
  - Russia abandons DST in 2011.
  - *.tab: change AN (Netherlands Antilles) to CW (Curacao)
- Resolves: #716936

* Tue Apr 26 2011 Petr Machata <pmachata@redhat.com> - 2011g-1
- Upstream 2011e:
  - Morocco introduced DST for 2011 from April 2 to July 31.
  - Delay end of DST in Chile in 2011 until May 7.
- Resolves: #694521
- Upstream 2011f:
  - The Falkland Islands will not turn back clocks this winter, but
    stay on daylight saving time.
- Upstream 2011g:
  - Egypt abandons DST in 2011 (and forward)
- Resolves: #698613
- Dropped tzdata-2011d-chile.patch
- Dropped tzdata-2011d-morocco.patch

* Wed Mar 30 2011 Petr Machata <pmachata@redhat.com> - 2011d-3
- Morocco introduced DST for 2011 from April 2 to July 31. (tzdata-2011d-morocco.patch)
- Resolves: #692031

* Tue Mar 29 2011 Petr Machata <pmachata@redhat.com> - 2011d-2
- Delay end of DST in Chile in 2011 until May 7. (tzdata-2011d-chile.patch)
- Resolves: #691439

* Tue Mar 15 2011 Petr Machata <pmachata@redhat.com> - 2011d-1
- Upstream 2011d:
  - Change end of DST in Samoa in 2011.
  - Change start of DST in Cuba in 2011.
  - Move start of DST in Turkey by one day in 2011.
- Dropped tzdata-2011b-c.patch
- Resolves: #684213

* Fri Mar 04 2011 Petr Machata <pmachata@redhat.com> - 2011b-1
- Upstream 2011a:
  - Updates of historical stamps for Hawaii
- Upstream 2011b:
  - America/North_Dakota/Beulah: Mercer County, North Dakota, changed
    from the mountain time zone to the central time zone
- Kemerovo oblast should use OMST/OMSST abbreviation (tzdata-2011b-kemerovo.patch)
- Resolves: #596800
- tzdata-2011b-c.patch
  - Update of historical stamps for Juneau, Sitka, and histcurrent
    stamps for Metlakatla.  Sitka and Metlakatla are new zones.
  - Delay end of DST in Chile in 2011 until first Sunday in April.
- Resolves: #681907

* Mon Dec 13 2010 Petr Machata <pmachata@redhat.com> - 2010o-1
- Upstream 2010m:
  - Hong Kong didn't observe DST in 1977
  - In zone.tab, remove obsolete association of Vostok Station with
    South Magnetic Pole; add association with Lake Vostok
- Upstream 2010n:
  - Change end of DST in Samoa in 2011 from 2011-04-03 0:00 to
    2011-04-03 1:00
- Upstream 2010o:
  - Fiji will end DST on March 6, 2011, not March 27, 2011
- Resolves: #662781

* Mon Aug 30 2010 Petr Machata <pmachata@redhat.com> - 2010l-1
- Upstream 2010l:
  - Change Cairo's 2010 reversion to DST from the midnight between
    September 8 and 9 to the midnight between September 9 and 10.
  - Change Gaza's 2010 return to standard time to the midnight between
    August 10 and 11.
  - Bahia de Banderas (Mexican state of Nayarit) changed time zone
    UTC-7 to new time zone UTC-6 on April 4, 2010
- Resolves: #628645

* Tue Jul 27 2010 Andreas Schwab <schwab@redhat.com> - 2010k-1
- Upadate to 2010k (#618600)
  - No DST in Egypt during Ramadan in 2010
  - Bahía de Banderas moved to UTC-6 on April 4, 2010, new time zone
    America/Bahia_Banderas
  - Rename Pacific/Truk to Pacific/Chuuk and Pacific/Ponape to Pacific/Pohnpei
  - Update historical data of Europe/Helsinki
  - Update tz-links page

* Fri Apr 23 2010 Petr Machata <pmachata@redhat.com> - 2010i-1
- Upstream 2010i:
  - Morocco will have DST from 2010-05-02 to 2010-08-08
  - San Luis, Argentina will keep permanent DST after April 11, 2010
  - Updates of historical stamps for Taiwan
- Resolves: #585134 (Morocco starts DST on May 2, 2010)

* Tue Apr 06 2010 Petr Machata <pmachata@redhat.com> - 2010h-1
- Upstream 2009p
  - Argentina does not enter DST on October 18
  - San Luis switched from UTC-4 to UTC-3 on October 11th
- Upstream 2009q
  - Change DST end in Syria from November 1 to last Friday in October
  - Changes to past Hong Kong transitions
  - Kemerovo oblast' in Russia will change current time zone on March 28, 2010.
    Asia/Novokuznetsk is the new time zone name
- Upstream 2009r
  - Changes to local times of three Australian research stations in Antarctica
- Upstream 2009s
  - Fiji plans to re-introduce DST from November 29th 2009 to April 25th 2010
- Upstream 2009u
  - Bangladesh changed their clock back to Standard Time on December 31, 2009
- Upstream 2010a
  - Source code cleanups
- Upstream 2010b
  - Northern Mexico's border cities share the DST schedule with the
    United States
- Upstream 2010c
  - Paraguay DST now in effect from 2nd Sunday of April to 1st Sunday
    of October
- Upstream 2010d
  - The DST change in Bangladesh takes place a minute earlier
  - Fiji to end DST on 2010-03-28 at 03:00, about a month earlier
  - Samoa to observe DST this year; they didn't observe DST last year
  - DST in Chile extended to 3 April
- Upstream 2010e:
  - Fix a typo in Bangladesh DST rule
- Upstream 2010f:
  - Changes to Australian stations in Antarctica
  - Correct 2010 Samoa DST start date
  - New zone Antarctica/Macquarie
  - Change Syria DST start from last Friday in March to first Friday
    in April in 2010 and forward
- Upstream 2010g:
  - No Bangladesh DST in 2010 and forward.
  - Gaza DST starts last Saturday in March at 12:01 a.m. in 2010 and forward
  - Kamchatka and Anadyr change to Moscow+8 on 2010-03-28
  - Samara changes to Moscow+0 on 2010-03-28
  - Related zone.tab updates
- Upstream 2010h:
  - No DST in Tunisia in 2010 and forward
  - No DST in Pakistan in 2010 and forward
- Dropped tzdata-2009o-argentinas.patch
- Resolves: #568668 (DST time change in Paraguay [Asuncion])

* Wed Oct 21 2009 Petr Machata <pmachata@redhat.com> - 2009o-2
- San Luis (Argentina) entered DST on October 11 (tzdata-2009o-argentinas.patch)

* Mon Oct 19 2009 Petr Machata <pmachata@redhat.com> - 2009o-1
- Upstream 2009o
  - Bangladesh won't go back to Standard Time from October 1, 2009
  - Pakistan leaves DST on October 1, 2009
- Dropped tzdata-2009m-karachi.patch
- Argentina does not enter DST on October 18 (tzdata-2009o-argentinas.patch)

* Tue Sep 22 2009 Petr Machata <pmachata@redhat.com> - 2009m-2
- Add markers for autoupdate of spec file
- Pakistan leaves the period of DST on October 1 (tzdata-2009m-karachi.patch)

* Wed Sep 16 2009 Petr Machata <pmachata@redhat.com> - 2009m-1
- Upstream 2009m
  - Palestine will will revert back to winter time on Friday, 2009-09-04
  - Samoa passed the DST Bill that fixes DST dates for 2009 and 2010
- Drop Egypt patch

* Thu Aug 13 2009 Petr Machata <pmachata@redhat.com> - 2009k-3
- Egypt starts winter time on August 21.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009k-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jul 20 2009 Petr Machata <pmachata@redhat.com> - 2009k-1
- Upstream 2009k
  - Mauritius will not continue to observe DST the coming summer
  - Arbitrarily end DST at the end of 2009 so that a POSIX-style time
    zone string can appear in the Dhaka binary file

* Thu Jun 18 2009 Petr Machata <pmachata@redhat.com> - 2009j-1
- Upstream 2009j
  - DST switch for Bangladesh will occur an hour earlier than was
    thought.

* Mon Jun  8 2009 Petr Machata <pmachata@redhat.com> - 2009i-1
- Upstream 2009i
  - Bangladesh introduces DST 2009-06-20

* Tue May 26 2009 Petr Machata <pmachata@redhat.com> - 2009h-2
- Upstream 2009h
  - Convert use of 00:00 stamps to 24:00 of the previous day
  - Clarify that the data is Public Domain
- Drop Cairo patch

* Mon Apr 13 2009 Petr Machata <pmachata@redhat.com> - 2009f-1
- Upstream 2009f
  - Pakistan will observe DST between 2009-04-15 and (probably) 2009-11-01
- Drop Pakistan patch

* Mon Apr 13 2009 Petr Machata <pmachata@redhat.com> - 2009e-3
- Bump up for rebuild

* Mon Apr 13 2009 Petr Machata <pmachata@redhat.com> - 2009e-2
- Pakistan will observe DST between 2009-04-15 and (probably) 2009-11-01

* Mon Apr  6 2009 Petr Machata <pmachata@redhat.com> - 2009e-1
- Upstream 2009e
  - Historical changes for Jordan
  - Palestine will start DST on 2009-03-26 and end 2009-09-27
- Egypt ends DST on 2009-09-24

* Mon Mar 23 2009 Petr Machata <pmachata@redhat.com> - 2009d-1
- Upstream 2009d
  - Morocco will observe DST from 2009-06-01 00:00 to 2009-08-21 00:00
  - Tunisia will not observe DST this year.
  - Syria will start DST on 2009-03-27 00:00 this year
  - Cuba will start DST on midnight between 2009-03-07 and 2009-03-08
  - Province of San Luis, Argentina, went to UTC-04:00 on 2009-03-15

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2009a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Jan 23 2009 Petr Machata <pmachata@redhat.com> - 2009a-1
- Upstream 2009a
  - Fix Asia/Kathmandu spelling
  - Historical timestamps for Switzerland and Cuba
  - DST update for America/Resolute

* Thu Oct 30 2008 Petr Machata <pmachata@redhat.com> - 2008i-1
- Upstream 2008i
  - Updates for Argentina: Drop DST in zones America/Argentina/Jujuy,
    La_Rioja, San_Juan, Catamarca, Mendoza, Rio_Gallegos, Ushuaia; new
    zone America/Argentina/Salta (for provinces SA, LP, NQ, RN).

* Mon Oct 13 2008 Petr Machata <pmachata@redhat.com> - 2008h-1
- Upstream 2008h
  - Fix exact DST transition hour for Mauritius
  - Syria will leave the period of DST on Nov 1
  - Fix coordinates of Pacific/Niue

* Tue Oct  7 2008 Petr Machata <pmachata@redhat.com> - 2008g-1
- Upstream 2008g
  - Fixed future DST transitions for Brazil

* Tue Sep 16 2008 Petr Machata <pmachata@redhat.com> - 2008f-1
- Upstream 2008f
  - Changes for Mauritius (extends DST to years to come)
  - Palestine changes clocks for the duration of Ramadan
  - Argentina will start DST on Sunday October 19, 2008
  - Brazil will start DST on 2008-10-19
- Drop Pakistan and Morocco patches

* Thu Aug 28 2008 Petr Machata <pmachata@redhat.com> - 2008e-2
- Pakistan DST is scheduled until Oct/31
- Morocco DST is scheduled until Aug/31

* Tue Aug 12 2008 Petr Machata <pmachata@redhat.com> - 2008e-1
- Upstream 2008e
  - Changes for Mauritius
  - Leap second coverage for 31/Dec 2008
  - Corrections of historical dates

* Tue Jul  8 2008 Petr Machata <pmachata@redhat.com> - 2008d-1
- Upstream 2008d
  - Changes for Brazil and Mauritius

* Fri May 30 2008 Petr Machata <pmachata@redhat.com> - 2008c-1
- Upstream 2008c
  - Mongolia changes zone
  - Pakistan DST is scheduled until Sep/1, instead of Aug/31
- Drop Morocco and Pakistan patches that are superseded by upstream
- Fix a typo in Java subpackage name

* Tue May 27 2008 Petr Machata <pmachata@redhat.com> - 2008b-3
- Morocco introduces DST

* Fri May 23 2008 Petr Machata <pmachata@redhat.com> - 2008b-2
- Pakistan introduces DST

* Wed Mar 26 2008 Petr Machata <pmachata@redhat.com> - 2008b-1
- Upstream 2008b
  - DST changes for Syria, Cuba; Iraq abandons DST
  - Saigon zone renamed Ho_Chi_Minh; backward link provided
  - Add America/Argentina/San_Luis information

* Tue Mar  4 2008 Petr Machata <pmachata@redhat.com> - 2007k-2
- Chile moves DST to 29/Mar
- Related: #435959

* Thu Jan  3 2008 Petr Machata <pmachata@redhat.com> - 2007k-1
- Upstream 2007k
  - Argentina readopted the daylight saving time

* Tue Dec  4 2007 Petr Machata <pmachata@redhat.com> - 2007j-1
- Upstream 2007j
  - New links America/St_Barthelemy and America/Marigot
  - Venezuela is changing their clocks on December 9 at 03:00

* Mon Nov  5 2007 Petr Machata <pmachata@redhat.com> - 2007i-1
- Upstream 2007i
  - Syria DST will take place at Midnight between Thursday and Friday.
  - Cuba will end DST on the last Sunday of October.
- Update tst-timezone.c from glibc CVS

* Mon Oct  1 2007 Petr Machata <pmachata@redhat.com> - 2007h-1
- Upstream 2007h
  - Brazil will observe DST from 2007-10-14 to 2008-02-17
  - Egypt and Gaza switched earlier than we expected
  - Iran will resume DST next year
  - Venezuela is scheduled to change TZ to -4:30 on January 1

* Tue Sep 25 2007 Keith Seitz <keiths@redhat.com> - 2007g-2
- Add support for building java's zoneinfo files in new
  tzdata-java RPM.

* Wed Aug 22 2007 Petr Machata <pmachata@redhat.com> - 2007g-1
- Fix licensing tag.
- Upstream 2007g
  - Egypt switches the September 7, not September 28
  - Daviess, Dubous, Knox, Martin, and Pike Counties, Indiana, switch
    from central to eastern time in November
  - South Australia, Tasmania, Victoria, New South Wales and Lord Howe
    Island are changing their DST rules effective next year
  - Sync several Antarctic station's rules with the New Zealand
  - leapseconds contain changes from the most recent IERS bulletin

* Wed May  9 2007 Petr Machata <pmachata@redhat.com> - 2007f-1
- Upstream 2007f
  - New Zealand is extending DST, starting later this year.
  - Haiti no longer observes DST.
  - The Turks and Caicos switch at 02:00, not at 00:00, and have
    adopted US DST rules.

* Tue Apr  3 2007 Petr Machata <pmachata@redhat.com> - 2007e-1
- Upstream 2007e
  - Syria switched to summer time at Mar/29.
  - Honduras will not enter DST this year.

* Wed Mar 21 2007 Petr Machata <pmachata@redhat.com> - 2007d-1
- Upstream 2007d
  - Mongolia has abolished DST.
  - Turkey will use EU rules this year, changing at 01:00 UTC rather
    than 01:00 standard time.
  - Cuba observed DST starting Sunday.
  - Resolute, Nunavut switched from Central to Eastern time last
    November.

* Mon Feb 26 2007 Petr Machata <pmachata@redhat.com> - 2007c-1
- Upstream 2007c
  - Pulaski County, Indiana, switched back to eastern time.
  - Turkey switches at 01:00 standard time, not at 01:00 UTC.
- Upstream 2007b
  - Changes to the commentary in "leapseconds".

* Wed Feb  7 2007 Petr Machata <pmachata@redhat.com> - 2007a-2
- tidy up the specfile per rpmlint comments

* Thu Jan 18 2007 Petr Machata <pmachata@redhat.com> - 2007a-1
- Upstream 2007a
  - Updates to Bahamas, they will be in sync with 2007 US DST change
  - New zone Australia/Eucla
  - Africa/Asmera renamed to Africa/Asmara, link created
  - Atlantic/Faeroe renamed to Atlantic/Faroe, link created
- Packaging
  - Adding BuildRequires: glibc-common >= 2.5.90-7 to build tzdata
    with extended 64-bit format necessary for dates beyond 2037

* Wed Nov 29 2006 Petr Machata <pmachata@redhat.com> - 2006p-1
- Upstream 2006p
  - Official version of Western Australia DST trial changes
  - Latitude/longitude changes for Europe/Jersey and Europe/Podgorica

* Wed Nov 22 2006 Petr Machata <pmachata@redhat.com> - 2006o-2
- Patch for Western Australia DST trial

* Thu Nov  9 2006 Petr Machata <pmachata@redhat.com> - 2006o-1
- Cuba has ended its three years of permanent DST.
- Updates in historical timestamps for Chile.

* Tue Oct 10 2006 Petr Machata <pmachata@redhat.com> - 2006m-2
- Proposed upstream patch (#210058)
  - Jordan will switch to winter time on October 27, not September 29
  - Brazil's DST this year is the first Sunday in November to the last
    Sunday in February.  (Thanks to Frederico A. C. Neves.)
  - ISO 3166 codes for Serbia and Montenegro, zone Europe/Podgorica
  - Commentary and past timestamps changes

* Tue Oct  3 2006 Petr Machata <pmachata@redhat.com> - 2006m-1
- Upstream 2006m:
  - Adjustments for Egypt, Palestine, Uruguay
  - Better description of `until' field in zic (8) manpage

* Thu Sep 21 2006 Petr Machata <pmachata@redhat.com> - 2006l-1
- Upstream 2006k, 2006l:
  - Adjustments for Egypt, Palestine, Cuba, Honduras
  - Documentation changes

* Tue Aug 22 2006 Petr Machata <pmachata@redhat.com> - 2006j-1
- Upstream 2006j
  - Honduras stopped observing DST on Monday at 00:00
  - America/Bermuda will follow the US's lead next year
  - America/Moncton will use US-style rules next year
  - New Zone America/Blanc-Sablon, for Canadians who observe AST all
    year
  - New zone: America/Atikokan instead of America/Coral_Harbour
  - New zones: Europe/Jersey, Europe/Guernsey, Europe/Isle_of_Man
  - Historical changes
  - Commentary updates
- Upstream 2006i
  - localtime.c fixes
- Upstream 2006h
  - zic leapsecond fix

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2006g-1.1
- rebuild

* Thu May 11 2006 Petr Machata <pmachata@redhat.com> - 2006g-1
- Honduras chose to follow Guatemala and will observe DST May/6 to Sep/2
- Nicaragua updates

* Tue May  2 2006 Petr Machata <pmachata@redhat.com> - 2006f-1
- Upstream 2006f
  - America/Guatemala observes DST between Apr/30 and Oct/1
  - Historical changes for Nicaragua
  - Update of America/Indiana/Vincennes in zone table

* Thu Apr 20 2006 Petr Machata <pmachata@redhat.com> - 2006d-1
- Upstream 2006d
  - Haiti observes DST
  - Sri Lanka change actually took effect Apr/15
  - All Canada is now scheduled for 2007 US DST rules
  - Some historical fixes

* Thu Apr  6 2006 Petr Machata <pmachata@redhat.com> - 2006c-1
- Upstream 2006c
  - Time-related changes:
    - dozens of historical and commentary changes
    - Iran stopped observing DST
    - Sri Lanka switches from UTC+6 to UTC+5:30
    - America/Thule and America/Edmonton will adopt new US rules,
      starting 2007
    - Tunisia is adopting regular DST
  - Code:
    - asctime.c: Chages in format strings to silent gcc warnings
    - removing K&R notation from function signatures
    - few fixes across the code

* Thu Mar 16 2006 Petr Machata <pmachata@redhat.com> - 2006b-2
- Patch for Sri Lanka time zone change (#184514)

* Wed Feb 22 2006 Petr Machata <pmachata@redhat.com> 2006b-1
- Upstream 2006b:
  - using tz64code version, as 32 is legacy according to tzdata ML
  - new manual pages for ctime, strftime, tzset
  - some source code reorganizations
  - no timezone/dst rule updates

* Thu Feb 02 2006 Petr Machata <pmachata@redhat.com> 2006a-2
- Small changes in tst-timezone.c

* Thu Feb 02 2006 Petr Machata <pmachata@redhat.com> 2006a-1
- Upstream 2006a:
  - private.h(scheck): changing char* to char const*
  - Rule changes for Palestine, zone changes for Indiana/US, both
    changes for Canada.
  - Many related doc changes.
- Naming scheme in spec file doesn't use %%{name}, but tzdata.

* Thu Jan 12 2006 Petr Machata <pmachata@redhat.com> 2005r-3
- 2005r-3
  - Meta changes.  Renaming tzdata.tar.bz2 file to tzdata$ver-base,
    so that it won't clash across updates.

* Thu Jan  5 2006 Petr Machata <pmachata@redhat.com> 2005r-2
- 2005r
  - Zones EST, MST, HST, EST5EDT, CST6CDT, MST7MDT, PST8PDT moved to
    northamerica to guard against old files with obsolete information
    being left in the time zone binary directory.
  - Changes for countries that are supposed to join 2007 US DST
    change.  This includes most of Canada, however entries already in
    the database (Alberta, British Columbia, Newfoundland, Northwest
    Territories, and Yukon) were left alone for the time being.
  - Fixes in zdump.c (abbrok): conditions are chained, and the string
    is checked for emptiness.

* Sat Dec 17 2005 Jakub Jelinek <jakub@redhat.com> 2005q-2
- 2005q
  - changes for Georgia, Azerbaijan, Jordan, Palestine, Cuba, Nicaragua
  - SystemV timezone changes

* Wed Nov  2 2005 Jakub Jelinek <jakub@redhat.com> 2005n-2
- 2005n
  - changes for Kyrgyzstan and Uruguay
- fix a typo in the Makefile (used TZDATA env var instead of TZDIR during
  make check), update tst-timezone.c from glibc CVS (#172102)

* Tue Sep  6 2005 Jakub Jelinek <jakub@redhat.com> 2005m-2
- 2005m
  - changes for USA (extending DST by 4 weeks since 2007), Tunisia,
    Australia, Kazakhstan
  - historical timezone data changes for Japan, Poland, Northern Ireland and
    Mali
  - timezone name change for East Timor

* Fri Jul 15 2005 Jakub Jelinek <jakub@redhat.com> 2005k-2
- 2005k
  - leap seconds update

* Sat Apr 30 2005 Jakub Jelinek <jakub@redhat.com> 2005i-2
- 2005i
  - updates for Iran, Haiti and Nicaragua

* Mon Apr  4 2005 Jakub Jelinek <jakub@redhat.com> 2005h-2
- 2005h
  - fixes for Kazakhstan

* Thu Mar 17 2005 Jakub Jelinek <jakub@redhat.com> 2005g-2
- 2005g
  - fixes for Uruguay
- include README and Theory from tzcode tarball in %%{_docdir};
  Theory includes a good summary of how the timezone data files
  are supposed to be named

* Tue Mar  1 2005 Jakub Jelinek <jakub@redhat.com> 2005f-2
- 2005f
  - more updates for Israel, updates for Azerbaijan

* Wed Jan 26 2005 Jakub Jelinek <jakub@redhat.com> 2005c-3
- 2005c
  - updates for Israel and Paraguay

* Mon Nov 29 2004 Jakub Jelinek <jakub@redhat.com> 2004g-1
- 2004g (#141107)
  - updates for Cuba

* Mon Oct 11 2004 Jakub Jelinek <jakub@redhat.com> 2004e-2
- 2004e (#135194)
  - updates for Brazil, Uruguay and Argentina

* Wed Aug  4 2004 Jakub Jelinek <jakub@redhat.com> 2004b-2
- 2004b

* Mon Oct  6 2003 Jakub Jelinek <jakub@redhat.com> 2003d-1
- 2003d

* Thu Sep 25 2003 Jakub Jelinek <jakub@redhat.com> 2003c-1
- 2003c
- updates for Brazil (#104840)

* Mon Jul 28 2003 Jakub Jelinek <jakub@redhat.com> 2003a-2
- rebuilt

* Mon Jul 28 2003 Jakub Jelinek <jakub@redhat.com> 2003a-1
- initial package
