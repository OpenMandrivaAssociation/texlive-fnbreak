Name:		texlive-fnbreak
Version:	25003
Release:	2
Summary:	Warn for split footnotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fnbreak
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnbreak.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnbreak.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnbreak.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package detects footnotes that are split over several
pages, and writes a warning to the log file.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fnbreak/fnbreak.sty
%doc %{_texmfdistdir}/doc/latex/fnbreak/ChangeLog
%doc %{_texmfdistdir}/doc/latex/fnbreak/Makefile
%doc %{_texmfdistdir}/doc/latex/fnbreak/README
%doc %{_texmfdistdir}/doc/latex/fnbreak/fnbreak-v.tex
%doc %{_texmfdistdir}/doc/latex/fnbreak/fnbreak.pdf
%doc %{_texmfdistdir}/doc/latex/fnbreak/fnbreak.xml
%doc %{_texmfdistdir}/doc/latex/fnbreak/fnbreaktest.tex
#- source
%doc %{_texmfdistdir}/source/latex/fnbreak/fnbreak.dtx
%doc %{_texmfdistdir}/source/latex/fnbreak/fnbreak.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
