# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/fnbreak
# catalog-date 2007-01-04 00:44:01 +0100
# catalog-license lppl
# catalog-version 1.10
Name:		texlive-fnbreak
Version:	1.10
Release:	1
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
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This package detects footnotes that are split over several
pages, and writes a warning to the log file.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fnbreak/fnbreak.sty
%doc %{_texmfdistdir}/doc/latex/fnbreak/ChangeLog
%doc %{_texmfdistdir}/doc/latex/fnbreak/README
%doc %{_texmfdistdir}/doc/latex/fnbreak/fnbreak-v.tex
%doc %{_texmfdistdir}/doc/latex/fnbreak/fnbreak.pdf
%doc %{_texmfdistdir}/doc/latex/fnbreak/fnbreak.xml
%doc %{_texmfdistdir}/doc/latex/fnbreak/fnbreaktest.tex
#- source
%doc %{_texmfdistdir}/source/latex/fnbreak/Makefile
%doc %{_texmfdistdir}/source/latex/fnbreak/fnbreak.dtx
%doc %{_texmfdistdir}/source/latex/fnbreak/fnbreak.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
