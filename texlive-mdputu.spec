%global tl_name mdputu
%global tl_revision 20298

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Upright digits in Adobe Utopia Italic
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/mdputu
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mdputu.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mdputu.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The Annals of Mathematics uses italics for theorems. However, slanted
digits and parentheses look disturbing when surrounded by (upright)
mathematics. This package provides virtual fonts with italics and
upright digits and punctuation, as an extension to Mathdesign's Utopia
bundle.

