SUMMARY = "Dasharo Tools Suite scripts"
LICENSE = "GPL-2.0-only"
LIC_FILES_CHKSUM = "file://LICENSE;md5=b234ee4d69f5fce4486a80fdaf4a4263"

SRC_URI = "git://github.com/Dasharo/dts-scripts.git;protocol=https;branch=develop"
SRCREV = "${AUTOREV}"

S = "${WORKDIR}/git"

# Set default DTS_CONFIG_REF based on the branch being built
DTS_CONFIG_REF ?= "refs/heads/main"
DTS_CONFIG_REF:nightly = "refs/heads/develop"

do_install() {
    install -d ${D}/usr/sbin
    install -m 0755 ${S}/include/dts-environment.sh ${D}/usr/sbin/dts-environment.sh
    # Inject the configured DTS_CONFIG_REF value
    sed -i "s|export DTS_CONFIG_REF=.*|export DTS_CONFIG_REF=${DTS_CONFIG_REF}|" ${D}/usr/sbin/dts-environment.sh
}

FILES:${PN} = "/usr/sbin/dts-environment.sh"
