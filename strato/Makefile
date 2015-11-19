STRATO_BUILD_DIR = build/strato
STRATO_RPM_DIR = build/rpm

all: build rpm

.PHONY: submit
submit:
	solvent submitproduct rpm $(STRATO_RPM_DIR)

.PHONY: approve
approve:
	solvent approve --product=rpm

.PHONY: prepareForCleanBuild
prepareForCleanBuild:
	@echo "Not doing anything here, as this target is executed as root. Change the makefile if cleanbuild.sh was fixed."

.PHONY: build
build:
	rm -rf $(STRATO_BUILD_DIR)
	mkdir -p $(STRATO_BUILD_DIR)
	cd $(STRATO_BUILD_DIR) && cmake -G "Unix Makefiles" ../..
	$(MAKE) -C $(STRATO_BUILD_DIR)

.PHONY: rpm
rpm: build clean_rpm
	mkdir -p $(STRATO_RPM_DIR)
	rpmbuild -ba -vv --define "TOP `pwd`" strato/flatbuffers.spec
	cp $(HOME)/rpmbuild/$*/RPMS/x86_64/*.rpm  build/rpm
	cp $(HOME)/rpmbuild/$*/SRPMS/*.rpm  build/rpm
	rm -rf $(HOME)/rpmbuild/$*

.PHONY: clean
clean: clean_rpm
	rm -rf $(STRATO_BUILD_DIR)

.PHONY: clean_rpm
clean_rpm:
	rm -rf $(STRATO_RPM_DIR)

