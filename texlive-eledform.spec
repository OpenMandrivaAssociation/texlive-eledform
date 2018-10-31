Name:		texlive-eledform
Version:	1.1a
Release:	2
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
%{_texmfdistdir}/tex/latex/eledform
%doc %{_texmfdistdir}/doc/latex/eledform
#- source
%doc %{_texmfdistdir}/source/latex/eledform

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
