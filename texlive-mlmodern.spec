Name:		texlive-mlmodern
Version:	57458
Release:	1
Summary:	A blacker Type 1 version of Computer Modern, with multilingual support
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mlmodern
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlmodern.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlmodern.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
MLModern is a text and math font family with (La)TeX support,
based on the design of Donald Knuth's Computer Modern and the
Latin Modern project. It avoids the spindliness of most other
Type 1 versions of Computer Modern.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/mlmodern
%{_texmfdistdir}/fonts/type1/public/mlmodern
%{_texmfdistdir}/fonts/tfm/public/mlmodern
%{_texmfdistdir}/fonts/map/dvips/mlmodern
%doc %{_texmfdistdir}/doc/fonts/mlmodern

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
