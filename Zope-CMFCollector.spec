%define		zope_subname	CMFCollector
Summary:	An issue collector for Zopei
Summary(pl.UTF-8):   Dodatek do Zope umożliwiający zbieranie wyników
Name:		Zope-%{zope_subname}
Version:	0.93
Release:	3
License:	GPL
Group:		Development/Tools
Source0:	http://zope.org/Members/bowerymarc/%{zope_subname}-update/%{version}/%{zope_subname}.%{version}.tgz
# Source0-md5:	742fc8c28c073311b00b5104ff75c26f
URL:		http://zope.org/Members/bowerymarc/CMFCollector-update/
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.268
%pyrequires_eq	python-modules
Requires(post,postun):	/usr/sbin/installzopeproduct
Requires:	Zope >= 2.4
Requires:	Zope-CMF >= 1:1.4
Conflicts:	CMF
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CMFCollector is an issue collector for Zope.

%description -l pl.UTF-8
CMFCollector jest dodatkiem do Zope umożliwiającym zbieranie wyników.

%prep
%setup -q -n %{zope_subname}
find . -type f -name .DS_Store | xargs rm -rf

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

cp -af {Extensions,dtml,help,image_sources,skins,tests,*.py,*.zexp,version.txt} $RPM_BUILD_ROOT%{_datadir}/%{name}

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

# find $RPM_BUILD_ROOT -type f -name "*.py" -exec rm -rf {} \;;

%clean
rm -rf $RPM_BUILD_ROOT

%post
/usr/sbin/installzopeproduct %{_datadir}/%{name} %{zope_subname}
%service -q zope restart

%postun
if [ "$1" = "0" ]; then
	/usr/sbin/installzopeproduct -d %{zope_subname}
	%service -q zope restart
fi

%files
%defattr(644,root,root,755)
%doc CHANGELOG.txt INSTALL.txt KNOWN_PROBLEMS.txt README.txt TODO.txt RELEASE_NOTES.txt
%{_datadir}/%{name}
