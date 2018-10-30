# revision 25003
# category Package
# catalog-ctan /macros/latex/contrib/fnbreak
# catalog-date 2012-01-02 14:24:13 +0100
# catalog-license lppl
# catalog-version 1.30
Name:		texlive-fnbreak
Version:	1.30
Release:	10
Summary:	Warn for split footnotes
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fnbreak
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnbreak.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnbreak.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fnbreak.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.30-1
+ Revision: 758880
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.10-2
+ Revision: 752000
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.10-1
+ Revision: 718470
- texlive-fnbreak
- texlive-fnbreak
- texlive-fnbreak
- texlive-fnbreak

