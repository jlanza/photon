%{!?python_sitelib: %define python_sitelib %(python -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}
%{!?python3_sitelib: %define python3_sitelib %(python3 -c "from distutils.sysconfig import get_python_lib;print(get_python_lib())")}

Summary:        The Python Cryptography Toolkit.
Name:           pycrypto
Version:        2.6.1
Release:        5%{?dist}
License:        Public Domain and Python
URL:            http://www.pycrypto.org/
Source0:        https://ftp.dlitz.net/pub/dlitz/crypto/pycrypto/%{name}-%{version}.tar.gz
%define         sha1 pycrypto=aeda3ed41caf1766409d4efc689b9ca30ad6aeb2
Patch0:         pycrypto-2.6.1-CVE-2013-7459.patch
Patch1:         pycrypto-2.6.1-CVE-2018-6594.patch
Group:          Development/Tools
Vendor:         VMware, Inc.
Distribution:   Photon

BuildRequires:  python-setuptools
BuildRequires:  python2-devel
Requires:       python2
%description
This is a collection of both secure hash functions (such as SHA256 and RIPEMD160), and various encryption algorithms (AES, DES, RSA, ElGamal, etc.). 

%package -n     python3-pycrypto
Summary:        python3-pycrypto
BuildRequires:  python3-devel

Requires:       python3
%description -n python3-pycrypto

Python 3 version.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
python setup.py build
python3 setup.py build

%install
python setup.py install -O1 --root=%{buildroot} --prefix=/usr
python3 setup.py install -O1 --root=%{buildroot} --prefix=/usr

%files
%defattr(-,root,root)
%{python_sitelib}/*

%files -n python3-pycrypto
%defattr(-, root, root)
%{python3_sitelib}/*

%changelog
*   Tue Apr 17 2018 Xiaolin Li <xiaolinl@vmware.com> 2.6.1-5
-   Apply patch for CVE-2018-6594
*   Mon Dec 04 2017 Kumar Kaushik <kaushikk@vmware.com> 2.6.1-4
-   Release bump to use python 3.5.4.
*   Thu Jul 20 2017 Anish Swaminathan <anishs@vmware.com> 2.6.1-3
-   Apply patch for CVE-2013-7459
*   Thu Jul 13 2017 Divya Thaluru <dthaluru@vmware.com> 2.6.1-2
-   Downgraded to stable version 2.6.1
*   Mon Feb 27 2017 Xiaolin Li <xiaolinl@vmware.com> 2.7a1-3
-   Added python3 site-packages.
*	Tue May 24 2016 Priyesh Padmavilasom <ppadmavilasom@vmware.com> 2.7a1-2
-	GA - Bump release of all rpms
*   Tue Feb 23 2016 Xiaolin Li <xiaolinl@vmware.com> 2.7a1-1
-   Updated to version 2.7a1
*	Tue Dec 15 2015 Xiaolin Li <xiaolinl@vmware.com> 2.6.1-1
-   Initial build.  First version
