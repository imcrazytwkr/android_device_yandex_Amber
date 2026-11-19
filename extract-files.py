#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.fixups_lib import (
    lib_fixups,
    lib_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    "device/yandex/Amber",
    "hardware/qcom-caf/common/libqti-perfd-client",
    "hardware/qcom-caf/msm8998",
    "hardware/qcom-caf/wlan",
    "vendor/qcom/opensource/dataservices",
    "vendor/qcom/opensource/data-ipa-cfg-mgr-legacy-um",
]


def lib_fixup_vendor_suffix(lib: str, partition: str, *args, **kwargs):
    return f"{lib}_{partition}" if partition == "vendor" else None


lib_fixups: lib_fixups_user_type = {
    **lib_fixups,
    (
        "com.qualcomm.qti.ant@1.0",
        "com.qualcomm.qti.dpm.api@1.0",
        "com.qualcomm.qti.imscmservice@1.0",
        "com.qualcomm.qti.imscmservice@2.0",
        "com.qualcomm.qti.imscmservice@2.1",
        "com.qualcomm.qti.imscmservice@2.2",
        "com.qualcomm.qti.uceservice@2.0",
        "com.qualcomm.qti.uceservice@2.1",
        "vendor.qti.gnss@1.0",
        "vendor.qti.gnss@1.1",
        "vendor.qti.gnss@1.2",
        "vendor.qti.gnss@2.0",
        "vendor.qti.hardware.fm@1.0",
        "vendor.qti.hardware.radio.ims@1.0",
        "vendor.qti.hardware.radio.ims@1.1",
        "vendor.qti.hardware.radio.ims@1.2",
        "vendor.qti.hardware.radio.ims@1.3",
        "vendor.qti.hardware.radio.ims@1.4",
        "vendor.qti.ims.callinfo@1.0",
        "vendor.qti.ims.rcsconfig@1.0",
        "vendor.qti.imsrtpservice@2.0",
        "vendor.qti.imsrtpservice@2.1",
    ): lib_fixup_vendor_suffix,
}

blob_fixups: blob_fixups_user_type = {
    (
        "system_ext/etc/init/dpmd.rc",
        "system_ext/etc/permissions/com.qti.dpmframework.xml",
        "system_ext/etc/permissions/dpmapi.xml",
    ): blob_fixup()
        .regex_replace("/system/product/", "/system/system_ext/"),
    "system_ext/lib64/lib-imscamera.so": blob_fixup()
        .add_needed("libgui_shim.so")
        .remove_needed("libhidltransport.so")
        .remove_needed("libhwbinder.so"),
    (
        "system_ext/lib/lib-imsvideocodec.so",
        "system_ext/lib64/lib-imsvideocodec.so",
    ): blob_fixup()
        .add_needed("libgui_shim.so")
        .replace_needed("libqdMetaData.so", "libqdMetaData.system.so")
        .remove_needed("libhidltransport.so")
        .remove_needed("libhwbinder.so"),
    (
        "product/lib/com.qualcomm.qti.imscmservice@1.0.so",
        "product/lib/com.qualcomm.qti.imscmservice@2.0.so",
        "product/lib/com.qualcomm.qti.imscmservice@2.1.so",
        "product/lib/com.qualcomm.qti.imscmservice@2.2.so",
        "product/lib/com.qualcomm.qti.uceservice@2.0.so",
        "product/lib/com.qualcomm.qti.uceservice@2.1.so",
        "product/lib/vendor.qti.hardware.radio.ims@1.0.so",
        "product/lib/vendor.qti.hardware.radio.ims@1.1.so",
        "product/lib/vendor.qti.hardware.radio.ims@1.2.so",
        "product/lib/vendor.qti.hardware.radio.ims@1.3.so",
        "product/lib/vendor.qti.hardware.radio.ims@1.4.so",
        "product/lib/vendor.qti.ims.callinfo@1.0.so",
        "product/lib/vendor.qti.ims.rcsconfig@1.0.so",
        "product/lib64/com.qualcomm.qti.imscmservice@1.0.so",
        "product/lib64/com.qualcomm.qti.imscmservice@2.0.so",
        "product/lib64/com.qualcomm.qti.imscmservice@2.1.so",
        "product/lib64/com.qualcomm.qti.imscmservice@2.2.so",
        "product/lib64/com.qualcomm.qti.uceservice@2.0.so",
        "product/lib64/com.qualcomm.qti.uceservice@2.1.so",
        "product/lib64/vendor.qti.hardware.radio.ims@1.0.so",
        "product/lib64/vendor.qti.hardware.radio.ims@1.1.so",
        "product/lib64/vendor.qti.hardware.radio.ims@1.2.so",
        "product/lib64/vendor.qti.hardware.radio.ims@1.3.so",
        "product/lib64/vendor.qti.hardware.radio.ims@1.4.so",
        "product/lib64/vendor.qti.ims.callinfo@1.0.so",
        "product/lib64/vendor.qti.ims.rcsconfig@1.0.so",
        "system_ext/lib/com.qualcomm.qti.dpm.api@1.0.so",
        "system_ext/lib/libdpmframework.so",
        "system_ext/lib/vendor.qti.imsrtpservice@2.0.so",
        "system_ext/lib/vendor.qti.imsrtpservice@2.1.so",
        "system_ext/lib64/com.qualcomm.qti.dpm.api@1.0.so",
        "system_ext/lib64/lib-imsvt.so",
        "system_ext/lib64/vendor.qti.imsrtpservice@2.0.so",
        "system_ext/lib64/vendor.qti.imsrtpservice@2.1.so",
    ): blob_fixup()
        .remove_needed("libhidltransport.so")
        .remove_needed("libhwbinder.so"),
    (
        'vendor/lib/libdualcameraddm.so',
        'vendor/lib/libvideobokeh.so',
    ): blob_fixup()
        .remove_needed('libstdc++.so'),
    (
        'vendor/lib/vendor.qti.hardware.factory@1.0.so',
        'vendor/lib/vendor.qti.hardware.fm@1.0.so',
        'vendor/lib64/com.qualcomm.qti.ant@1.0.so',
        'vendor/lib64/vendor.display.color@1.0.so',
        'vendor/lib64/vendor.display.postproc@1.0.so',
        'vendor/lib64/vendor.qti.gnss@1.0.so',
        'vendor/lib64/vendor.qti.gnss@1.1.so',
        'vendor/lib64/vendor.qti.gnss@2.0.so',
        'vendor/lib64/vendor.qti.gnss@1.2.so',
        'vendor/lib64/vendor.qti.hardware.factory@1.0.so',
        'vendor/lib64/vendor.qti.hardware.fm@1.0.so',
        'vendor/lib64/vendor.qti.hardware.tui_comm@1.0.so',
    ): blob_fixup()
        .add_needed('libhidlbase_shim.so'),
    (
        'system/lib/vendor.qti.hardware.fm@1.0.so',
        'system/lib64/com.qualcomm.qti.ant@1.0.so',
        'system/lib64/vendor.qti.gnss@1.0.so',
        'system/lib64/vendor.qti.gnss@1.1.so',
        'system/lib64/vendor.qti.gnss@1.2.so',
        'system/lib64/vendor.qti.gnss@2.0.so',
        'system/lib64/vendor.qti.gnss@2.1.so',
        'system/lib64/vendor.qti.hardware.fm@1.0.so',
    ): blob_fixup()
        .add_needed('libhidlbase_shim_sys.so'),
    'system_ext/lib/libdpmframework.so': blob_fixup()
        .add_needed('libcutils_shim.so'),
    (
        'vendor/lib/libllvm-glnext.so',
        'vendor/lib/libllvm-qcom.so',
        'vendor/lib64/libllvm-glnext.so',
        'vendor/lib64/libllvm-qcom.so',
        'vendor/lib64/libril-qc-hal-qmi.so',
    ): blob_fixup()
        .add_needed('libgnu_strerror_shim.so'),
}  # fmt: skip

module = ExtractUtilsModule(
    "Amber",
    "yandex",
    blob_fixups=blob_fixups,
    lib_fixups=lib_fixups,
    namespace_imports=namespace_imports,
    skip_main_proprietary_file=True,
)
module.add_proprietary_file("proprietary-files-qc.txt")
module.add_proprietary_file("proprietary-files-yandex.txt")

if __name__ == "__main__":
    utils = ExtractUtils.device(module)
    utils.run()
