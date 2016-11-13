SPECFILE = $(firstword $(wildcard *.spec))

ifdef DIST 
DIST_DEFINES := --define "dist $(DIST)" 
endif 

ifndef NAME
NAME := $(shell rpm $(RPM_DEFINES) $(DIST_DEFINES) -q --qf "%{NAME}\n" --specfile $(SPECFILE)| head -1)
endif

ifndef VERSION 
VERSION := $(shell rpm $(RPM_DEFINES) $(DIST_DEFINES) -q --qf "%{VERSION}\n" --specfile $(SPECFILE)| head -1 | tr -d " ")
endif 
# the release of the package 
ifndef RELEASE 
RELEASE := $(shell rpm $(RPM_DEFINES) $(DIST_DEFINES) -q --qf "%{RELEASE}\n" --specfile $(SPECFILE)| head -1 | tr -d " ")
endif 

ifndef WORKDIR 
WORKDIR := $(shell pwd) 
endif 

sources:
	@if [ -f ~/.wgetrc ] ; \
	then \
		cp ~/.wgetrc ~/.wgetrc.bak ; \
	fi
	@echo "content_disposition = on" > ~/.wgetrc
	@echo "check_certificate = off" >> ~/.wgetrc
	@echo "ftp_user = you" >> ~/.wgetrc
	@echo "ftp_password=wish" >> ~/.wgetrc

	#spectool -g $(SPECFILE)
	wget ftp://192.168.1.2/gitstorage/$(NAME)/$(VERSION)/*

	@rm -rf ~/.wgetrc
	@if [ -f ~/.wgetrc.bak ] ; \
	then \
		cp ~/.wgetrc.bak ~/.wgetrc ; \
		rm -rf ~/.wgetrc.bak ; \
	fi
	@rm -rf $(NAME)-$(VERSION)
