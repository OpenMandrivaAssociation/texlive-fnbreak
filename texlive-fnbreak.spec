%global tl_name fnbreak
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.40
Release:	%{tl_revision}.1
Summary:	Warn for split footnotes
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/fnbreak
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fnbreak.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fnbreak.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/fnbreak.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package detects footnotes that are split over several pages, and
writes a warning to the log file.

