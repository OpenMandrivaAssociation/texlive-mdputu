# revision 20298
# category Package
# catalog-ctan /fonts/mdputu
# catalog-date 2010-11-03 15:55:25 +0100
# catalog-license other-free
# catalog-version 1.2
Name:		texlive-mdputu
Version:	1.2
Release:	1
Summary:	Upright digits in Adobe Utopia Italic
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/fonts/mdputu
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdputu.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mdputu.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The Annals of Mathematics uses italics for theorems. However,
slanted digits and parentheses look disturbing when surrounded
by (upright) mathematics. This package provides virtual fonts
with italics and upright digits and punctuation, as an
extension to Mathdesign Utopia.

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
%{_texmfdistdir}/fonts/tfm/public/mdputu/mdputubi7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mdputu/mdputubi8t.tfm
%{_texmfdistdir}/fonts/tfm/public/mdputu/mdputuri7t.tfm
%{_texmfdistdir}/fonts/tfm/public/mdputu/mdputuri8t.tfm
%{_texmfdistdir}/fonts/vf/public/mdputu/mdputubi7t.vf
%{_texmfdistdir}/fonts/vf/public/mdputu/mdputubi8t.vf
%{_texmfdistdir}/fonts/vf/public/mdputu/mdputuri7t.vf
%{_texmfdistdir}/fonts/vf/public/mdputu/mdputuri8t.vf
%{_texmfdistdir}/tex/latex/mdputu/mdputu.sty
%{_texmfdistdir}/tex/latex/mdputu/ot1mdputu.fd
%{_texmfdistdir}/tex/latex/mdputu/t1mdputu.fd
%doc %{_texmfdistdir}/doc/latex/mdputu/README
%doc %{_texmfdistdir}/doc/latex/mdputu/mdputu.dtx
%doc %{_texmfdistdir}/doc/latex/mdputu/mdputu.ins
%doc %{_texmfdistdir}/doc/latex/mdputu/mdputu.pdf
%doc %{_texmfdistdir}/doc/latex/mdputu/sample.pdf
%doc %{_texmfdistdir}/doc/latex/mdputu/sample.tex
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}