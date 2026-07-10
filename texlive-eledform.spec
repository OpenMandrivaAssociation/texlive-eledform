%global tl_name eledform
%global tl_revision 38114

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1a
Release:	%{tl_revision}.1
Summary:	Define textual variants
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eledform
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eledform.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eledform.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eledform.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides commands to formalize textual variants in critical
editions typeset using eledmac.

