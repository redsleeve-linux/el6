# Conditional for release and snapshot builds. Uncomment for release-builds.
#global rel_build 1

# Setup _pkgdocdir if not defined already.
%{!?_pkgdocdir:%global _pkgdocdir	%{_docdir}/%{name}-%{version}}

# Settings used for build from snapshots.
%{!?rel_build:%global commit		723738c7069e83cd2d4fe1a0593e635839e42b22}
%{!?rel_build:%global commit_date	20141214}
%{!?rel_build:%global shortcommit	%(c=%{commit};echo ${c:0:7})}
%{!?rel_build:%global gitver		git%{commit_date}-%{shortcommit}}
%{!?rel_build:%global gitrel		.git%{commit_date}.%{shortcommit}}

# Proper naming for the tarball from github.
%global gittar %{name}-%{version}%{!?rel_build:-%{gitver}}.tar.gz

Name:			2048-cli
Version:		0.9
Release:		4%{?gitrel}%{?dist}
Summary:		The game 2048 for your Linux terminal
%{?el5:Group:		Amusements/Games}

License:		MIT
URL:			https://github.com/Tiehuis/%{name}
# Sources for release-builds.
%{?rel_build:Source0:	%{url}/archive/v%{version}.tar.gz#/%{gittar}}
# Sources for snapshot-builds.
%{!?rel_build:Source0:	%{url}/archive/%{commit}.tar.gz#/%{gittar}}

%{?el5:BuildRoot:	%(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)}
BuildRequires:		asciidoc
BuildRequires:		docbook-style-xsl
BuildRequires:		libxslt
BuildRequires:		ncurses-devel
BuildRequires:		util-linux-ng

%description
A cli version of the game 2048 for your Linux terminal.


%package nocurses
Summary:		The game 2048 for your Linux terminal (non-ncurses)
%{?el5:Group:		Amusements/Games}

%description nocurses
A non-ncurses cli version of the game 2048 for your Linux terminal.


%prep
%setup -q%{!?rel_build:n %{name}-%{commit}}


%build
%{__make} %{?_smp_mflags} 2048 2048nc man			\
	CFLAGS='%{optflags}' LDFLAGS='%{?__global_ldflags}'


%install
%{?el5:%{__rm} -rf %{buildroot}}

# There is no install-target in Makefile.
%{__mkdir} -p %{buildroot}%{_bindir}				\
		%{buildroot}%{_mandir}/man1			\
		%{buildroot}%{_pkgdocdir}
%{__install} -pm 0755 2048 2048nc %{buildroot}%{_bindir}
%{__install} -pm 0644 man/*.1 %{buildroot}%{_mandir}/man1
%{__install} -pm 0644 man/2048*.1.txt LICENSE README.md		\
		%{buildroot}%{_pkgdocdir}


%{?el5:%clean}
%{?el5:%{__rm} -rf %{buildroot}}


%files
%doc %{_pkgdocdir}
%{_bindir}/2048
%{_mandir}/man1/2048.1*

%files nocurses
%doc %{_pkgdocdir}
%{_bindir}/2048nc
%{_mandir}/man1/2048nc.1*


%changelog
* Sun Dec 14 2014 Björn Esser <bjoern.esser@gmail.com> - 0.9-4.git20141214.723738c
- update to new snapshot git20141214.723738c, obsoletes Patch0

* Sat Dec 13 2014 Björn Esser <bjoern.esser@gmail.com> - 0.9-3
- updated Patch0

* Sat Dec 13 2014 Björn Esser <bjoern.esser@gmail.com> - 0.9-2
- added Patch0 to fix malformated manpages

* Fri Dec 05 2014 Björn Esser <bjoern.esser@gmail.com> - 0.9-1
- new upstream release v0.9
- obsoleted Patch0

* Fri Dec 05 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8-3.git20141205.a9505d9
- updated to new snapshot git20141205.a9505d9
- added Patch0 to have manpages

* Thu Dec 04 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8-2
- dropped Patch0 (#1170231)
- some minor readability clean-up

* Wed Dec 03 2014 Björn Esser <bjoern.esser@gmail.com> - 0.8-1
- initial rpm-release (#1170231)
