#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

# Inherit from those products. Most specific first.
$(call inherit-product, $(SRC_TARGET_DIR)/product/core_64_bit.mk)
$(call inherit-product, vendor/lineage/config/common_full_phone.mk)
$(call inherit-product, $(SRC_TARGET_DIR)/product/full_base_telephony.mk)

# Device
$(call inherit-product, device/yandex/Amber/device.mk)

PRODUCT_BRAND := Yandex
PRODUCT_DEVICE := Amber
PRODUCT_MANUFACTURER := Yandex
PRODUCT_MODEL := YNDX-000SB
PRODUCT_NAME := lineage_Amber

PRODUCT_GMS_CLIENTID_BASE := android-uniscope

PRODUCT_BUILD_PROP_OVERRIDES += \
    BuildDesc="yphone-user 9 8710.2.A.0037.20201023 10232034 release-keys" \
    BuildFingerprint=Yandex/Amber/Amber:9/8710.2.A.0037.20201023/10232034:user/release-keys \
    DeviceProduct=Amber
