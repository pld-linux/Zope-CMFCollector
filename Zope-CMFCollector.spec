
%include	/usr/lib/rpm/macros.python

%define		zope_subname	CMFCollector

Summary:	CMFCollector is an issue collector for Zope.
Summary(pl):	CMFCollector jest dodatkiem do Zope umo¿liwiaj±cy zbieranie wyników
Name:		Zope-%{zope_subname}
Version:	0.9b
Release:	1
License:	GNU
Group:		Development/Tools
Source0:	http://cvs.zope.org/CMF/%{zope_subname}/%{zope_subname}.tar.gz?tarball=1
# Source0-md5:	151c906d1058115f3f98155ec042f8fe
URL:		http://cvs.zope.org/CMF/%{zope_subname}/
%pyrequires_eq	python-modules
Requires:	Zope
Requires:	CMF
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		zope_lib	/usr/lib/zope/Addons
%define 	product_dir	/usr/lib/zope/Products

%description
CMFCollector is an issue collector for Zope.

%description -l pl
CMFCollector jest dodatkiem do Zope umo¿liwiaj±cy zbieranie wyników

%prep
%setup -q -c %{zope_subname}.tar.gz?tarball=1

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{zope_lib}
install -d $RPM_BUILD_ROOT%{product_dir}
cp -af * $RPM_BUILD_ROOT%{zope_lib}/%{zope_subname}
rm -rf $RPM_BUILD_ROOT%{zope_lib}/%{zope_subname}/*.txt
ln -s %{zope_lib}/%{zope_subname}/ $RPM_BUILD_ROOT%{product_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%preun

%postun
if [ -f /var/lock/subsys/zope ]; then
	/etc/rc.d/init.d/zope restart >&2
fi

%files
%defattr(644,root,root,755)
%doc %{zope_subname}/*.txt
%{zope_lib}
%{product_dir}
