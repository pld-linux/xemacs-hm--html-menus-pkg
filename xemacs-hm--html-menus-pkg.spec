Summary:	HTML editing
Summary(pl):	Edycja HTML
Name:		xemacs-hm--html-menus-pkg
%define		srcname	hm--html-menus
Version:	1.18
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	ftp://ftp.xemacs.org/xemacs/packages/%{srcname}-%{version}-pkg.tar.gz
URL:		http://www.xemacs.org/
Patch0:		%{name}-info.patch
BuildArch:	noarch
Conflicts:	xemacs-sumo
Requires:	xemacs
Requires:	xemacs-dired-pkg
Requires:	xemacs-base-pkg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
HTML editing.

%description -l pl
Edycja HTML.

%prep
%setup -q -c
#%patch0 -p1

%build
(cd man/hm--html-menus; awk '/^\\input texinfo/ {print FILENAME}' * | xargs makeinfo)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/xemacs-packages,%{_infodir}}

cp -a * $RPM_BUILD_ROOT%{_datadir}/xemacs-packages
mv -f $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info/*.info* $RPM_BUILD_ROOT%{_infodir}
rm -fr $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/info

# remove .el file if corresponding .elc file exists
find $RPM_BUILD_ROOT -type f -name "*.el" | while read i; do test ! -f ${i}c || rm -f $i; done

%clean
rm -fr $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%files
%defattr(644,root,root,755)
%doc lisp/hm--html-menus/ChangeLog
%{_datadir}/xemacs-packages%{_sysconfdir}/*
%{_infodir}/*
%dir %{_datadir}/xemacs-packages/lisp/*
%{_datadir}/xemacs-packages/lisp/*/*.el*
