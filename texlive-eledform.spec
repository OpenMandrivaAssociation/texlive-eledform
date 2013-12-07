# revision 27922
# category Package
# catalog-ctan /macros/latex/contrib/eledform
# catalog-date 2012-10-08 11:45:11 +0200
# catalog-license lppl1.3
# catalog-version 1.0
Name:		texlive-eledform
Version:	1.0
Release:	5
Summary:	Define textual variants
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eledform
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eledform.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eledform.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eledform.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides commands to formalize textual variants in
critical editions typeset using eledmac.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/eledform/eledform.sty
%doc %{_texmfdistdir}/doc/latex/eledform/README.md
%doc %{_texmfdistdir}/doc/latex/eledform/eledform.pdf
%doc %{_texmfdistdir}/doc/latex/eledform/example.pdf
%doc %{_texmfdistdir}/doc/latex/eledform/example.tex
%doc %{_texmfdistdir}/doc/latex/eledform/include/stemma.tex
%doc %{_texmfdistdir}/doc/latex/eledform/makefile
#- source
%doc %{_texmfdistdir}/source/latex/eledform/eledform.dtx
%doc %{_texmfdistdir}/source/latex/eledform/eledform.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
