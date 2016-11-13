package		= TurboGears

sources:
	if [ -f ~/.wgetrc ] ; \
	then \
		cp ~/.wgetrc ~/.wgetrc.bak ; \
	fi
	echo "content_disposition = on" > ~/.wgetrc
	echo "check_certificate = off" >> ~/.wgetrc
	spectool -g $(package).spec
	rm -rf ~/.wgetrc
	if [ -f ~/.wgetrc.bak ] ; \
	then \
		cp ~/.wgetrc.bak ~/.wgetrc ; \
		rm -rf ~/.wgetrc.bak ; \
	fi


