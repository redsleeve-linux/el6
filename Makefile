package		= 2048-cli

sources:
	if [ -f ~/.wgetrc ] ; \
	then \
		cp ~/.wgetrc ~/.wgetrc.bak ; \
	fi
	echo "content_disposition = on" > ~/.wgetrc
	echo "check_certificate = off" >> ~/.wgetrc
	spectool -g $(package).spec
	# fix
	mv 2048-cli-723738c7069e83cd2d4fe1a0593e635839e42b22.tar.gz 2048-cli-0.9-git20141214-723738c.tar.gz
	rm -rf ~/.wgetrc
	if [ -f ~/.wgetrc.bak ] ; \
	then \
		cp ~/.wgetrc.bak ~/.wgetrc ; \
		rm -rf ~/.wgetrc.bak ; \
	fi


