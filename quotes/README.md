# Scrapy Framework TroubleShoot in macOS

If scrapy framework doesn't install in MacOS do the FOLLOWING THINGS:

First Install Update OpenSSL: (One Time) 
1. brew install openssl [ Mac / Linux ] 
2. brew upgrade openssl 

Apple has deprecated use of OpenSSL in favor of its own TLS and crypto libraries https://github.com/pyca/cryptography/issues/2692 

export LDFLAGS="-L/usr/local/opt/openssl/lib" 

export CPPFLAGS="-I/usr/local/opt/openssl/include" 

export PKG_CONFIG_PATH="/usr/local/opt/openssl/lib/pkgconfig" 

