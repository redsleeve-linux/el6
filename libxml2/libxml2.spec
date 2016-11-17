Summary: Library providing XML and HTML support
Name: libxml2
Version: 2.7.6
Release: 21%{?dist}%{?extra_release}.1
License: MIT
Group: Development/Libraries
Source: ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
BuildRequires: python python-devel zlib-devel pkgconfig
URL: http://xmlsoft.org/
Patch0: libxml2-multilib.patch
Patch1: libxml2-2.7.6-xpath-leak.patch
Patch2: libxml2-2.7.7-xpath-bug.patch
Patch3: libxml2-2.7.7-xpath-leak.patch
Patch4: libxml2-2.7.7-xpath-axis-semantic.patch
Patch5: libxml2-2.7.7-xpath-axis-semantic2.patch
Patch6: libxml2-2.7.7-xpath-rounding.patch
Patch7: libxml2-2.7.8-xpath-freeing.patch
Patch8: libxml2-2.7.8-xpath-freeing2.patch
Patch9: CVE-2011-1944.patch
Patch10: libxml2-2.7.8-xpath-hardening.patch
Patch11: CVE-2011-0216.patch
Patch12: CVE-2011-2834.patch
Patch13: CVE-2011-3905.patch
Patch14: CVE-2011-3919.patch
Patch15: CVE-2012-0841.patch
Patch16: force_randomization.patch
Patch17: libxml2-Fix-a-failure-to-report-xmlreader-parsing-failures.patch
Patch18: libxml2-Fix-parser-local-buffers-size-problems.patch
Patch19: libxml2-Fix-entities-local-buffers-size-problems.patch
Patch20: libxml2-Fix-an-error-in-previous-commit.patch
Patch21: libxml2-Do-not-fetch-external-parsed-entities.patch
Patch22: libxml2-Impose-a-reasonable-limit-on-attribute-size.patch
Patch23: libxml2-Impose-a-reasonable-limit-on-comment-size.patch
Patch24: libxml2-Impose-a-reasonable-limit-on-PI-size.patch
Patch25: libxml2-Cleanups-and-new-limit-APIs-for-dictionaries.patch
Patch26: libxml2-Introduce-some-default-parser-limits.patch
Patch27: libxml2-Implement-some-default-limits-in-the-XPath-module.patch
Patch28: libxml2-Fixup-limits-parser.patch
Patch29: libxml2-Enforce-XML_PARSER_EOF-state-handling-through-the-parser.patch
Patch30: libxml2-Avoid-quadratic-behaviour-in-some-push-parsing-cases.patch
Patch31: libxml2-More-avoid-quadratic-behaviour.patch
Patch32: libxml2-Strengthen-behaviour-of-the-push-parser-in-problematic-situations.patch
Patch33: libxml2-More-fixups-on-the-push-parser-behaviour.patch
Patch34: libxml2-Fix-a-segfault-on-XSD-validation-on-pattern-error.patch
Patch35: libxml2-Fix-an-unimplemented-part-in-RNG-value-validation.patch
Patch36: libxml2-Fix-an-off-by-one-pointer-access.patch
Patch37: libxml2-Change-the-XPath-code-to-percolate-allocation-errors.patch
Patch38: libxml2-Fix-potential-out-of-bound-access.patch
Patch39: libxml2-Detect-excessive-entities-expansion-upon-replacement.patch
Patch40: libxml2-Fix-a-regression-in-2.9.0-breaking-validation-while-streaming.patch
Patch41: libxml2-Do-not-fetch-external-parameter-entities.patch
Patch42: libxml2-Improve-handling-of-xmlStopParser.patch
Patch43: libxml2-Fix-regression-introduced-by-CVE-2014-0191.patch
Patch44: CVE-2014-3660-rhel6.patch
Patch45: libxml2-Fix-html-serialization-error-and-htmlSetMetaEncoding.patch
Patch46: libxml2-Fix-missing-entities-after-CVE-2014-3660-fix.patch
Patch47: libxml2-Stop-parsing-on-entities-boundaries-errors.patch
Patch48: CVE-2015-1819.RHEL-6.patch
Patch49: libxml2-Cleanup-conditional-section-error-handling.patch
Patch50: libxml2-Fail-parsing-early-on-if-encoding-conversion-failed.patch
Patch51: libxml2-Another-variation-of-overflow-in-Conditional-sections.patch
Patch52: libxml2-Fix-an-error-in-previous-Conditional-section-patch.patch
Patch53: libxml2-Fix-parsing-short-unclosed-comment-uninitialized-access.patch
Patch54: libxml2-Avoid-extra-processing-of-MarkupDecl-when-EOF.patch
Patch55: libxml2-Avoid-processing-entities-after-encoding-conversion-failures.patch
Patch56: libxml2-xmlStopParser-reset-errNo.patch
Patch57: libxml2-CVE-2015-7497-Avoid-an-heap-buffer-overflow-in-xmlDictComputeFastQKey.patch
Patch58: libxml2-CVE-2015-5312-Another-entity-expansion-issue.patch
Patch59: libxml2-Add-xmlHaltParser-to-stop-the-parser.patch
Patch60: libxml2-Reuse-xmlHaltParser-where-it-makes-sense.patch
Patch61: libxml2-Do-not-print-error-context-when-there-is-none.patch
Patch62: libxml2-Detect-incoherency-on-GROW.patch
Patch63: libxml2-Fix-some-loop-issues-embedding-NEXT.patch
Patch64: libxml2-Bug-on-creating-new-stream-from-entity.patch
Patch65: libxml2-CVE-2015-7500-Fix-memory-access-error-due-to-incorrect-entities-boundaries.patch
Patch66: libxml2-CVE-2015-8242-Buffer-overead-with-HTML-parser-in-push-mode.patch
Patch67: libxml2-libxml-violates-the-zlib-interface-and-crashes.patch
Patch68: libxml2-Fix-large-parse-of-file-from-memory.patch

Patch69: libxml2-Heap-based-buffer-overread-in-xmlNextChar.patch
Patch70: libxml2-Bug-763071-heap-buffer-overflow-in-xmlStrncat-https-bugzilla.gnome.org-show_bug.cgi-id-763071.patch
Patch71: libxml2-Bug-757711-heap-buffer-overflow-in-xmlFAParsePosCharGroup-https-bugzilla.gnome.org-show_bug.cgi-id-757711.patch
Patch72: libxml2-Bug-758588-Heap-based-buffer-overread-in-xmlParserPrintFileContextInternal-https-bugzilla.gnome.org-show_bug.cgi-id-758588.patch
Patch73: libxml2-Bug-758605-Heap-based-buffer-overread-in-xmlDictAddString-https-bugzilla.gnome.org-show_bug.cgi-id-758605.patch
Patch74: libxml2-Bug-759398-Heap-use-after-free-in-xmlDictComputeFastKey-https-bugzilla.gnome.org-show_bug.cgi-id-759398.patch
Patch75: libxml2-Fix-inappropriate-fetch-of-entities-content.patch
Patch76: libxml2-Heap-use-after-free-in-htmlParsePubidLiteral-and-htmlParseSystemiteral.patch
Patch77: libxml2-Heap-use-after-free-in-xmlSAX2AttributeNs.patch
Patch78: libxml2-Heap-based-buffer-underreads-due-to-xmlParseName.patch
Patch79: libxml2-Heap-based-buffer-overread-in-htmlCurrentChar.patch
Patch80: libxml2-Add-missing-increments-of-recursion-depth-counter-to-XML-parser.patch
Patch81: libxml2-Avoid-building-recursive-entities.patch
Patch82: libxml2-Fix-some-format-string-warnings-with-possible-format-string-vulnerability.patch
Patch83: libxml2-More-format-string-warnings-with-possible-format-string-vulnerability.patch

%description
This library allows to manipulate XML files. It includes support
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select subnodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package devel
Summary: Libraries, includes, etc. to develop XML and HTML applications
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}
Requires: zlib-devel
Requires: pkgconfig

%description devel
Libraries, include files, etc you can use to develop XML applications.
This library allows to manipulate XML files. It includes support 
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select subnodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package static
Summary: Static library for libxml2
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}

%description static
Static library for libxml2 provided for specific uses or shaving a few
microseconds when parsing, do not link to them for generic purpose packages.

%package python
Summary: Python bindings for the libxml2 library
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}

%description python
The libxml2-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxml2 library to manipulate XML files.

This library allows to manipulate XML files. It includes support 
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DTDs, either
at parse time or later once the document has been modified.

%prep
%setup -q
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
%patch64 -p1
%patch65 -p1
%patch66 -p1
%patch67 -p1
%patch68 -p1

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
%patch81 -p1
%patch82 -p1
%patch83 -p1

%build
%configure
make %{_smp_mflags}
gzip -9 ChangeLog

%install
rm -fr %{buildroot}

%makeinstall
gzip -9 doc/libxml2-api.xml
rm -f $RPM_BUILD_ROOT%{_libdir}/*.la

# multiarch crazyness on timestamp differences or Makefile/binaries for examples
touch -m --reference=$RPM_BUILD_ROOT/%{_includedir}/libxml2/libxml/parser.h $RPM_BUILD_ROOT/%{_bindir}/xml2-config
(cd doc/examples ; make clean ; rm -rf .deps Makefile)

%clean
rm -fr %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS ChangeLog.gz NEWS README Copyright TODO
%doc %{_mandir}/man1/xmllint.1*
%doc %{_mandir}/man1/xmlcatalog.1*
%doc %{_mandir}/man3/libxml.3*

%{_libdir}/lib*.so.*
%{_bindir}/xmllint
%{_bindir}/xmlcatalog

%files devel
%defattr(-, root, root)

%doc %{_mandir}/man1/xml2-config.1*
%doc doc/*.html doc/html doc/*.gif doc/*.png
%doc doc/tutorial doc/libxml2-api.xml.gz
%doc doc/examples
%doc %dir %{_datadir}/gtk-doc/html/libxml2
%doc %{_datadir}/gtk-doc/html/libxml2/*.devhelp
%doc %{_datadir}/gtk-doc/html/libxml2/*.html
%doc %{_datadir}/gtk-doc/html/libxml2/*.png
%doc %{_datadir}/gtk-doc/html/libxml2/*.css

%{_libdir}/lib*.so
%{_libdir}/*.sh
%{_includedir}/*
%{_bindir}/xml2-config
%{_datadir}/aclocal/libxml.m4
%{_libdir}/pkgconfig/libxml-2.0.pc

%files static
%defattr(-, root, root)

%{_libdir}/*a

%files python
%defattr(-, root, root)

%{_libdir}/python*/site-packages/libxml2.py*
%{_libdir}/python*/site-packages/drv_libxml2.py*
%{_libdir}/python*/site-packages/libxml2mod*
%doc python/TODO
%doc python/libxml2class.txt
%doc python/tests/*.py
%doc doc/*.py
%doc doc/python.html

%changelog
* Tue Jun  7 2016 Daniel Veillard <veillard@redhat.com> - 2.7.6-21.el6.8.1
- Heap-based buffer overread in xmlNextChar (CVE-2016-1762)
- Bug 763071: Heap-buffer-overflow in xmlStrncat <https://bugzilla.gnome.org/show_bug.cgi?id=763071> (CVE-2016-1834)
- Bug 757711: Heap-buffer-overflow in xmlFAParsePosCharGroup <https://bugzilla.gnome.org/show_bug.cgi?id=757711> (CVE-2016-1840)
- Bug 758588: Heap-based buffer overread in xmlParserPrintFileContextInternal <https://bugzilla.gnome.org/show_bug.cgi?id=758588> (CVE-2016-1838)
- Bug 758605: Heap-based buffer overread in xmlDictAddString <https://bugzilla.gnome.org/show_bug.cgi?id=758605> (CVE-2016-1839)
- Bug 759398: Heap use-after-free in xmlDictComputeFastKey <https://bugzilla.gnome.org/show_bug.cgi?id=759398> (CVE-2016-1836)
- Fix inappropriate fetch of entities content (CVE-2016-4449)
- Heap use-after-free in htmlParsePubidLiteral and htmlParseSystemiteral (CVE-2016-1837)
- Heap use-after-free in xmlSAX2AttributeNs (CVE-2016-1835)
- Heap-based buffer-underreads due to xmlParseName (CVE-2016-4447)
- Heap-based buffer overread in htmlCurrentChar (CVE-2016-1833)
- Add missing increments of recursion depth counter to XML parser. (CVE-2016-3705)
- Avoid building recursive entities (CVE-2016-3627)
- Fix some format string warnings with possible format string vulnerability (CVE-2016-4448)
- More format string warnings with possible format string vulnerability (CVE-2016-4448)

* Sun Jan 24 2016 Daniel Veillard <veillard@redhat.com> - libxml2-2.7.6-21.el6.8
- Fix large parse of file from memory (rhbz#862969)

* Mon Nov 30 2015 Daniel Veillard <veillard@redhat.com> - 2.7.6-20.1
- Fix a series of CVEs (rhbz#1286495)
- CVE-2015-7941 Cleanup conditional section error handling
- CVE-2015-8317 Fail parsing early on if encoding conversion failed
- CVE-2015-7942 Another variation of overflow in Conditional sections
- CVE-2015-7942 Fix an error in previous Conditional section patch
- Fix parsing short unclosed comment uninitialized access
- CVE-2015-7498 Avoid processing entities after encoding conversion failures
- CVE-2015-7497 Avoid an heap buffer overflow in xmlDictComputeFastQKey
- CVE-2015-5312 Another entity expansion issue
- CVE-2015-7499 Add xmlHaltParser() to stop the parser
- CVE-2015-7499 Detect incoherency on GROW
- CVE-2015-7500 Fix memory access error due to incorrect entities boundaries
- CVE-2015-8242 Buffer overead with HTML parser in push mode
- Libxml violates the zlib interface and crashes

* Wed May  6 2015 Daniel Veillard <veillard@redhat.com> - libxml2-2.7.6-20.el6
- CVE-2015-1819 Enforce the reader to run in constant memory(rhbz#1214163)

* Mon Mar 23 2015 Daniel Veillard <veillard@redhat.com> - libxml2-2.7.6-19.el6
- Stop parsing on entities boundaries errors
- Fix missing entities after CVE-2014-3660 fix (rhbz#1149086)

* Mon Mar 16 2015 Daniel Veillard <veillard@redhat.com> - libxml2-2.7.6-18.el6
- CVE-2014-3660 denial of service via recursive entity expansion (rhbz#1149086)
- Fix html serialization error and htmlSetMetaEncoding (rhbz#1004513)

* Wed Jun 11 2014 Daniel Veillard <veillard@redhat.com> - libxml2-2.7.6-17.el6
- Fix a set of regressions introduced in CVE-2014-0191 (rhbz#1105011)

* Tue May  6 2014 Daniel Veillard <veillard@redhat.com> - libxml2-2.7.6-16.el6
- Improve handling of xmlStopParser(CVE-2013-2877)

* Tue May  6 2014 Daniel Veillard <veillard@redhat.com> - libxml2-2.7.6-15.el6
- Do not fetch external parameter entities (CVE-2014-0191)

* Wed Jun  5 2013 Daniel Veillard <veillard@redhat.com> - libxml2-2.7.6-14.el6
- Fix a regression in 2.9.0 breaking validation while streaming (rhbz#863166)

* Tue Feb 19 2013 Daniel Veillard <veillard@redhat.com> - 2.7.6-13.el6
- detect and stop excessive entities expansion upon replacement (rhbz#912575)

* Thu Nov 29 2012 Daniel Veillard <veillard@redhat.com> - 2.7.6-12.el6
- fix out of range heap access (CVE-2012-5134)

* Wed Sep  5 2012 Daniel Veillard <veillard@redhat.com> - 2.7.6-11.el6
- Change the XPath code to percolate allocation error (CVE-2011-1944)

* Wed Aug 22 2012 Daniel Veillard <veillard@redhat.com> - 2.7.6-10.el6
- Fix an off by one pointer access (CVE-2011-3102)

* Tue Aug 21 2012 Daniel Veillard <veillard@redhat.com> - 2.7.6-9.el6
- Fix a failure to report xmlreader parsing failures
- Fix parser local buffers size problems (rhbz#843742)
- Fix entities local buffers size problems (rhbz#843742)
- Fix an error in previous commit (rhbz#843742)
- Do not fetch external parsed entities
- Impose a reasonable limit on attribute size (rhbz#843742)
- Impose a reasonable limit on comment size (rhbz#843742)
- Impose a reasonable limit on PI size (rhbz#843742)
- Cleanups and new limit APIs for dictionaries (rhbz#843742)
- Introduce some default parser limits (rhbz#843742)
- Implement some default limits in the XPath module
- Fixup limits parser (rhbz#843742)
- Enforce XML_PARSER_EOF state handling through the parser
- Avoid quadratic behaviour in some push parsing cases (rhbz#843742)
- More avoid quadratic behaviour (rhbz#843742)
- Strengthen behaviour of the push parser in problematic situations (rhbz#843742)
- More fixups on the push parser behaviour (rhbz#843742)
- Fix a segfault on XSD validation on pattern error
- Fix an unimplemented part in RNG value validation

* Wed Feb 15 2012 Daniel Veillard <veillard@redhat.com> - 2.7.6-8.el6
- remove chunk in patch related to configure.in as it breaks rebuild
- Resolves: rhbz#788846

* Mon Feb 13 2012 Daniel Veillard <veillard@redhat.com> - 2.7.6-7.el6
- fix previous build to force compilation of randomization code
- Resolves: rhbz#788846

* Fri Feb 10 2012 Daniel Veillard <veillard@redhat.com> - 2.7.6-6.el6
- adds randomization to hash and dict structures CVE-2012-0841
- Resolves: rhbz#788846

* Fri Jan 06 2012 Daniel Veillard <veillard@redhat.com> - 2.7.6-5.el6
- Make sure the parser returns when getting a Stop order CVE-2011-3905
- Fix an allocation error when copying entities CVE-2011-3919
- Resolves: rhbz#771910

* Tue Oct 11 2011 Daniel Veillard <veillard@redhat.com> - 2.7.6-4
- Fixes another XPath problem CVE-2011-2834
- Resolves: rhbz#732335

* Mon Aug 22 2011 Daniel Veillard <veillard@redhat.com> - 2.7.6-3
- Fixes various other issues in 2.7.6 XPath evaluation
- Resolves: rhbz#732335

* Tue Jun 28 2011 Daniel Veillard <veillard@redhat.com> - 2.7.6-2
- Fix a potential crasher in XPath or XSLT, CVE-2011-1944
- Resolves: rhbz#710397

* Tue Oct  6 2009 Daniel Veillard <veillard@redhat.com> - 2.7.6-1
- Upstream release of 2.7.6
- restore thread support off by default in 2.7.5

* Thu Sep 24 2009 Daniel Veillard <veillard@redhat.com> - 2.7.5-1
- Upstream release of 2.7.5
- fix a couple of Relax-NG validation problems
- couple more fixes

* Tue Sep 15 2009 Daniel Veillard <veillard@redhat.com> - 2.7.4-2
- fix a problem with little data at startup affecting inkscape #523002

* Thu Sep 10 2009 Daniel Veillard <veillard@redhat.com> - 2.7.4-1
- upstream release 2.7.4
- symbol versioning of libxml2 shared libs
- very large number of bug fixes

* Mon Aug 10 2009 Daniel Veillard <veillard@redhat.com> - 2.7.3-4
- two patches for parsing problems CVE-2009-2414 and CVE-2009-2416

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Jan 18 2009 Daniel Veillard <veillard@redhat.com> - 2.7.3-1
- new release 2.7.3
- limit default max size of text nodes
- special parser mode for PHP
- bug fixes and more compiler checks

* Wed Dec  3 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.7.2-7
- Pull back into Python 2.6

* Wed Dec  3 2008 Caolán McNamara <caolanm@redhat.com> - 2.7.2-6
- AutoProvides requires BuildRequires pkgconfig

* Wed Dec  3 2008 Caolán McNamara <caolanm@redhat.com> - 2.7.2-5
- rebuild to get provides(libxml-2.0) into HEAD rawhide

* Mon Dec  1 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.7.2-4
- Rebuild for pkgconfig logic

* Fri Nov 28 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.7.2-3
- Rebuild for Python 2.6

* Wed Nov 12 2008 Daniel Veillard <veillard@redhat.com> - 2.7.2-2.fc11
- two patches for size overflows problems CVE-2008-4225 and CVE-2008-4226

* Fri Oct  3 2008 Daniel Veillard <veillard@redhat.com> 2.7.2-1.fc10
- new release 2.7.2
- Fixes the known problems in 2.7.1
- increase the set of options when saving documents

* Thu Oct  2 2008 Daniel Veillard <veillard@redhat.com> 2.7.1-2.fc10
- fix a nasty bug in 2.7.x, http://bugzilla.gnome.org/show_bug.cgi?id=554660

* Mon Sep  1 2008 Daniel Veillard <veillard@redhat.com> 2.7.1-1.fc10
- fix python serialization which was broken in 2.7.0
- Resolve: rhbz#460774

* Sat Aug 30 2008 Daniel Veillard <veillard@redhat.com> 2.7.0-1.fc10
- upstream release of 2.7.0
- switch to XML 1.0 5th edition
- switch to RFC 3986 for URI parsing
- better entity handling
- option to remove hardcoded limitations in the parser
- more testing
- a new API to allocate entity nodes
- and lot of fixes and clanups

* Mon Aug 25 2008 Daniel Veillard <veillard@redhat.com> 2.6.32-4.fc10
- fix for entities recursion problem
- Resolve: rhbz#459714

* Fri May 30 2008 Daniel Veillard <veillard@redhat.com> 2.6.32-3.fc10
- cleanup based on Fedora packaging guidelines, should fix #226079
- separate a -static package

* Thu May 15 2008 Daniel Veillard <veillard@redhat.com> 2.6.32-2.fc10
- try to fix multiarch problems like #440206

* Tue Apr  8 2008 Daniel Veillard <veillard@redhat.com> 2.6.32-1.fc9
- upstream release 2.6.32 see http://xmlsoft.org/news.html
- many bug fixed upstream

* Wed Feb 20 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 2.6.31-2
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Daniel Veillard <veillard@redhat.com> 2.6.31-1.fc9
- upstream release 2.6.31 see http://xmlsoft.org/news.html
- many bug fixed upstream

* Thu Aug 23 2007 Daniel Veillard <veillard@redhat.com> 2.6.30-1
- upstream release 2.6.30 see http://xmlsoft.org/news.html
- many bug fixed upstream

* Tue Jun 12 2007 Daniel Veillard <veillard@redhat.com> 2.6.29-1
- upstream release 2.6.29 see http://xmlsoft.org/news.html
- many bug fixed upstream

* Wed May 16 2007 Matthias Clasen <mclasen@redhat.com> 2.6.28-2
- Bump revision to fix N-V-R problem

* Tue Apr 17 2007 Daniel Veillard <veillard@redhat.com> 2.6.28-1
- upstream release 2.6.28 see http://xmlsoft.org/news.html
- many bug fixed upstream

* Thu Dec  7 2006 Jeremy Katz <katzj@redhat.com> - 2.6.27-2
- rebuild against python 2.5

* Wed Oct 25 2006 Daniel Veillard <veillard@redhat.com> 2.6.27-1
- upstream release 2.6.27 see http://xmlsoft.org/news.html
- very large amount of bug fixes reported upstream

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.6.26-2.1.1
- rebuild

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 2.6.26-2.1
- rebuild

* Wed Jun  7 2006 Daniel Veillard <veillard@redhat.com> 2.6.26-2
- fix bug #192873
* Tue Jun  6 2006 Daniel Veillard <veillard@redhat.com> 2.6.26-1
- upstream release 2.6.26 see http://xmlsoft.org/news.html

* Tue Jun  6 2006 Daniel Veillard <veillard@redhat.com>
- upstream release 2.6.25 broken, do not ship !

