%define		plugin	methods
Summary:	Extra functionality to base JS objects (e.g. Array, String, Date etc)
Name:		jquery-%{plugin}
# no versioning, use date
Version:	20111004
Release:	1
License:	MIT / GPL
Group:		Applications/WWW
Source0:	https://github.com/vitch/jquery-methods/tarball/master/%{name}-%{version}.tgz
# Source0-md5:	c94e98d4464dd17885aa6096a9e6c33e
URL:		https://github.com/vitch/jquery-methods
BuildRequires:	js
BuildRequires:	rpmbuild(macros) >= 1.565
BuildRequires:	yuicompressor
Requires:	jquery
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/jquery/%{plugin}

%description
A set of files to provide additional functionality to built in
JavaScript objects (e.g. Array, Date and String) for use with jQuery.

These methods were previously hosted in the main jQuery repository but
that is now reserved for core jQuery code so I've imported their
history to github for future hosting and development.

%prep
%setup -qc
mv *-jquery-methods-*/* .

%build
install -d build

# compress .js
for js in *.js; do
	out=build/${js#*/jquery.}
%if 0%{!?debug:1}
	yuicompressor --charset UTF-8 $js -o $out
	js -C -f $out
	touch -r $js $out
%else
	cp -p $js $out
%endif
done

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appdir}
cp -p build/* $RPM_BUILD_ROOT%{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.markdown
%dir %{_appdir}
%{_appdir}/array.js
%{_appdir}/date.js
%{_appdir}/string.js

# localized
%lang(bg) %{_appdir}/date_be_utf8.js
%lang(cs) %{_appdir}/date_cz.js
%lang(da) %{_appdir}/date_da.js
%lang(de) %{_appdir}/date_de.js
%lang(el) %{_appdir}/date_el.js
%lang(es) %{_appdir}/date_es.js
%lang(fr) %{_appdir}/date_fr.js
%lang(hu) %{_appdir}/date_hu.js
%lang(it) %{_appdir}/date_it.js
%lang(ja) %{_appdir}/date_jp.js
%lang(nl) %{_appdir}/date_nl.js
%lang(nb) %{_appdir}/date_no.js
%lang(pl) %{_appdir}/date_pl.js
%lang(pt_BR) %{_appdir}/date_pt-br.js
%lang(ru) %{_appdir}/date_ru_utf8.js
%lang(ru) %{_appdir}/date_ru_win1251.js
%lang(sv) %{_appdir}/date_se.js
%lang(si) %{_appdir}/date_si.js
%lang(tr) %{_appdir}/date_tr.js
%lang(ua) %{_appdir}/date_ua_utf8.js
