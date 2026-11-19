/*
 * Copyright (C) 2023 The LineageOS Project
 * SPDX-License-Identifier: Apache-2.0
 */

#include <hidl/Static.h>

namespace android {
namespace hardware {
namespace details {

// Pie HIDL libraries import this global. libhidlbase now exposes
// getBnConstructorMap() instead.
DoNotDestruct<BnConstructorMap> gBnConstructorMap{};

}  // namespace details
}  // namespace hardware
}  // namespace android
